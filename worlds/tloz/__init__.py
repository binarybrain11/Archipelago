import json
import os
import threading
from pkgutil import get_data

import bsdiff4
from docutils.parsers.rst.directives import encoding

import Utils
import settings
import typing

from typing import NamedTuple, Union, Dict, Any
from BaseClasses import Item, Location, Region, Entrance, MultiWorld, ItemClassification, Tutorial
from .ItemPool import generate_itempool, starting_weapons, dangerous_weapon_locations
from .Items import item_table, item_prices, item_game_ids
from .Locations import location_table, level_locations, major_locations, shop_locations, all_level_locations, \
    standard_level_locations, shop_price_location_ids, secret_money_ids, location_ids, food_locations, \
    take_any_locations, sword_cave_locations, shop_categories, cave_data_location_start
from .Options import TlozOptions
from .Rom import get_base_rom_path, first_quest_dungeon_items_early, first_quest_dungeon_items_late, \
    cave_type_flags, warp_cave_offset, starting_sword_cave_location_byte, white_sword_pond_location_byte, \
    magical_sword_grave_location_byte, letter_cave_location_byte, TLOZProcedurePatch
from .Rules import set_rules
from .Client import TLOZClient
from .EntranceRandoRules import create_entrance_randomizer_set
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule


class TLoZSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Zelda 1"""
        description = "The Legend of Zelda (U) ROM File"
        copy_to = "Legend of Zelda, The (U) (PRG0) [!].nes"

    class RomStart(str):
        """
        Set this to false to never autostart a rom (such as after patching)
                    true  for operating system default program
        Alternatively, a path to a program to open the .nes file with
        """

    class DisplayMsgs(settings.Bool):
        """Display message inside of Bizhawk"""

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: typing.Union[RomStart, bool] = True
    display_msgs: typing.Union[DisplayMsgs, bool] = True


class TLoZWeb(WebWorld):
    theme = "stone"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up The Legend of Zelda for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Rosalie and Figment"]
    )

    tutorials = [setup]


class TLoZWorld(World):
    """
    The Legend of Zelda needs almost no introduction. Gather the eight fragments of the
    Triforce of Wisdom, enter Death Mountain, defeat Ganon, and rescue Princess Zelda.
    This randomizer shuffles all the items in the game around, leading to a new adventure
    every time.
    """
    options_dataclass = TlozOptions
    options: TlozOptions
    settings: typing.ClassVar[TLoZSettings]
    game = "The Legend of Zelda"
    topology_present = True
    base_id = 7000
    web = TLoZWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    q1_item_name_groups = {
        # 'weapons': starting_weapons,
        'swords': {
            "Sword", "White Sword", "Magical Sword"
        },
        "candles": {
            "Candle", "Red Candle"
        },
        "arrows": {
            "Arrow", "Silver Arrow"
        }
    }
    q2_item_name_groups = {"Q2 " + group: { "Q2 " + i for i in items } for group, items in item_name_groups.items()}
    item_name_groups = {**q1_item_name_groups,**q2_item_name_groups}

    location_name_groups = {
        "Shops": set(shop_locations),
        "Take Any": set(take_any_locations),
        "Sword Caves": set(sword_cave_locations),
        "Level 1": set(level_locations[0]),
        "Level 2": set(level_locations[1]),
        "Level 3": set(level_locations[2]),
        "Level 4": set(level_locations[3]),
        "Level 5": set(level_locations[4]),
        "Level 6": set(level_locations[5]),
        "Level 7": set(level_locations[6]),
        "Level 8": set(level_locations[7]),
        "Level 9": set(level_locations[8]),
        "Q2 Level 1": set(q2_level_locations[0]),
        "Q2 Level 2": set(q2_level_locations[1]),
        "Q2 Level 3": set(q2_level_locations[2]),
        "Q2 Level 4": set(q2_level_locations[3]),
        "Q2 Level 5": set(q2_level_locations[4]),
        "Q2 Level 6": set(q2_level_locations[5]),
        "Q2 Level 7": set(q2_level_locations[6]),
        "Q2 Level 8": set(q2_level_locations[7]),
        "Q2 Level 9": set(q2_level_locations[8])
    }

    for k, v in item_name_to_id.items():
        item_name_to_id[k] = v + base_id

    for k, v in location_name_to_id.items():
        if v is not None:
            location_name_to_id[k] = v + base_id

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.generator_in_use = threading.Event()
        self.rom_name_available_event = threading.Event()
        self.overworlds = None
        self.levels = None
        self.filler_items = None
        self.entrance_randomizer_set = None

    def create_item(self, name: str):
        if name == "Power Bracelet":
            return TLoZItem(
                name,
                    ItemClassification.progression
                    if (self.options.EntranceShuffle.value > 1 and self.options.RandomizeWarpCaves)
                    else item_table[name].classification,
                self.item_name_to_id[name],
                self.player)
        return TLoZItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str):
        return TLoZItem(event, ItemClassification.progression, None, self.player)

    def create_location(self, name, id, parent, event=False):
        return_location = TLoZLocation(self.player, name, id, parent)
        return return_location

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.overworlds = [ Region("Overworld", self.player, self.multiworld) ]
        if self.options.SecondQuestShuffle:
            self.overworlds.append(
                Region("Q2 Overworld", self.player, self.multiworld))

        self.entrance_randomizer_set = create_entrance_randomizer_set(self)

        self.levels = [[None]*10, [None]*10] # Yes I'm making one-indexed arrays in a zero-indexed language. I hate me too.
        shared_regions = {}
        shared_locations = {
            "Take Any Item": take_any_locations,
            **shop_categories
        }
        for screen, entrance in self.entrance_randomizer_set.items():
            for quest in range(2):
                if quest == 1 and not self.options.SecondQuestShuffle:
                    continue
                if entrance[quest] == None:
                    continue

                location = entrance[quest][1] 
                location_name = location if quest == 0 else "Q2 " + location
                overworld_name = "Overworld" if quest == 0 else "Q2 Overworld"

                if location[:5] == "Level":
                    self.create_level_region(screen, entrance[quest], quest)
                    continue

                if "Take Any Item" == location and not self.options.ExpandedPool:
                    continue

                # These locations have a simple region with one entrance
                if location in sword_cave_locations or location == "Letter Cave":
                    region = Region(location_name, self.player, self.multiworld)
                else:
                    # These caves have more than one entrance. Initialize the region once
                    if location_name not in shared_regions:
                        shared_regions[location_name] = Region(location_name, self.player, self.multiworld)
                        # Attach all of the locations to the region
                        for shared_location in shared_locations[location]:
                            shared_location_name = shared_location if quest == 0 else "Q2 " + shared_location
                            shared_regions[location_name].locations.append(
                                self.create_location(shared_location_name, 
                                    # These locations only have one spot in the ROM for the first and second quest, 
                                    # so we use the same id for different shared_location_names. The Client can 
                                    # distinguish these locations at runtime
                                    self.location_name_to_id[location], region))
                    region = shared_regions[location_name]

                entrando_rule = entrance[quest][0]
                self.overworlds[quest].connect(region, 
                    f"{overworld_name} to {screen}", 
                    lambda state, rule=entrando_rule: rule(state, self.player))
                region.locations.append(
                    self.create_location(location, self.location_name_to_id[location], region))

        # Tidy up some locations not included in entrando
        for location in overworld_locations:
            if location not in sword_cave_locations and location != "Letter Cave":
                self.overworlds[0].locations.append(
                    self.create_location(location, self.location_name_to_id[location], self.overworlds[0]))
                if SecondQuestShuffle:
                    self.overworlds[1].locations.append(
                        self.create_location("Q2 " + location, self.location_name_to_id[location], self.overworlds[1]))


        ganon = self.create_location("Ganon", None, self.multiworld.get_region("Level 9", self.player))
        zelda = self.create_location("Zelda", None, self.multiworld.get_region("Level 9", self.player))
        ganon.show_in_spoiler = False
        zelda.show_in_spoiler = False
        self.levels[0][9].locations.append(ganon)
        self.levels[0][9].locations.append(zelda)
        menu.connect(self.overworlds[0], "Begin Game")

        if self.options.SecondQuestShuffle:
            q2_ganon = self.create_location("Q2 Ganon", None, self.multiworld.get_region("Q2 Level 9", self.player))
            q2_zelda = self.create_location("Q2 Zelda", None, self.multiworld.get_region("Q2 Level 9", self.player))
            q2_ganon.show_in_spoiler = False
            q2_zelda.show_in_spoiler = False
            self.levels[1][9].locations.append(q2_ganon)
            self.levels[1][9].locations.append(q2_zelda)
            menu.connect(self.overworlds[1], "Q2 Begin Game",
                lambda state: state.has("Rescued Zelda!", player))

        self.multiworld.regions.append(menu)
        self.multiworld.regions.append(self.overworlds[0])


    def create_level_region(self, screen, entrance_data, quest):
        if quest == 0:
            level_name = entrance_data[1]
        else:
            level_name = "Q2 " + entrance_data[1]
        # Here we expect level_name to match regex /^(Q2 )?Level \d$/
        level_num = int(level_name[-1:])
        level = Region(level_name, self.player, self.multiworld)
        self.levels[quest][level_num]
        new_entrance = Entrance(self.player, level_name, self.overworlds[quest])
        entrando_rule = entrance_data[0]
        new_entrance.connect(level)
        overworld.connect(
            level,
            f"{level_name} Entrance at {screen}",
            lambda state, rule=entrando_rule: rule(state, self.player))

        location_list = level_locations if quest == 0 else q2_level_locations
        for location in location_list[level_num - 1]:
            if self.options.ExpandedPool or "Drop" not in location:
                level.locations.append(
                    self.create_location(location, self.location_name_to_id[location], level))

        boss_event = self.create_location(f"{level_name} Boss Status", None,
                                            level, True)
        boss_event.show_in_spoiler = False
        level.locations.append(boss_event)

        self.multiworld.regions.append(level)



    def create_items(self):
        # refer to ItemPool.py
        generate_itempool(self)

    # refer to Rules.py
    set_rules = set_rules

    def generate_output(self, output_directory: str):
        try:
            outfilebase = 'AP_' + self.multiworld.seed_name
            outfilepname = f'_P{self.player}'
            outfilepname += f"_{self.multiworld.get_file_safe_player_name(self.player).replace(' ', '_')}"
            output_filename = os.path.join(output_directory, f'{outfilebase}{outfilepname}.nes')
            self.rom_name_text = f'LOZ{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
            self.rom_name = self.rom_name_text[:0x20]
            self.rom_name.ljust(0x20, "0")
            self.rom_name = str(self.rom_name)
            placement_dict = self.create_placement_file()
            placement_dict["meta"] = {}
            placement_dict["meta"]["rom_name"] = self.rom_name
            placement_dict["meta"]["player_name"] = self.player_name
            placement_dict["meta"]["output_filename"] = output_filename
            placement_dict["meta"]["death_link"] = self.options.DeathLink.value

            # We shuffle the tiers of rupee caves. Caves that shared a value before still will.
            # Easiest to do it here so we have the multiworld's random object
            secret_caves = self.random.sample(sorted(secret_money_ids), 3)
            secret_cave_money_amounts = [20, 50, 100]
            for i, amount in enumerate(secret_cave_money_amounts):
                # Giving approximately double the money to keep grinding down
                amount = amount * self.random.triangular(1.5, 2.5)
                secret_cave_money_amounts[i] = int(amount)
            for i, cave in enumerate(secret_caves):
                placement_dict[cave] = secret_cave_money_amounts[i]

            patch = TLOZProcedurePatch(player=self.player, player_name=self.multiworld.player_name[self.player])
            patch.write_file("placement_file.json", json.dumps(placement_dict).encode("UTF-8"))
            rom_path = os.path.join(
                output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}" f"{patch.patch_file_ending}"
            )
            patch.write(rom_path)
        finally:
            self.rom_name_available_event.set()

    def create_placement_file(self):
        placement_dict = {}
        for location in self.multiworld.get_filled_locations(self.player):
            if location.item.player == self.player:
                placement_dict[location.name] = location.item.name
            else:
                if location.item.classification in [ItemClassification.progression, ItemClassification.trap]:
                    placement_dict[location.name] = "Archipelago-progression"
                else:
                    placement_dict[location.name] = "Archipelago-filler"
                placement_dict[location.name + " Classification"] = location.item.classification
        entrance_randomizer_set = {}
        for screen, data in self.entrance_randomizer_set.items():
            entrance_randomizer_set[screen] = data[1]
        placement_dict["entrance_randomizer_set"] = entrance_randomizer_set
        return placement_dict

    def modify_multidata(self, multidata: dict):
        import base64
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name, encoding="utf-8")).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = [item for item in item_table if item_table[item].classification == ItemClassification.filler]
        return self.random.choice(self.filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        if self.options.ExpandedPool:
            take_any_left = self.multiworld.get_location("Take Any Item Left", self.player).item
            take_any_middle = self.multiworld.get_location("Take Any Item Middle", self.player).item
            take_any_right = self.multiworld.get_location("Take Any Item Right", self.player).item
            if take_any_left.player == self.player:
                take_any_left = take_any_left.code
            else:
                take_any_left = -1
            if take_any_middle.player == self.player:
                take_any_middle = take_any_middle.code
            else:
                take_any_middle = -1
            if take_any_right.player == self.player:
                take_any_right = take_any_right.code
            else:
                take_any_right = -1

            slot_data = {
                "TakeAnyLeft": take_any_left,
                "TakeAnyMiddle": take_any_middle,
                "TakeAnyRight": take_any_right
            }
        else:
            slot_data = {
                "TakeAnyLeft": -1,
                "TakeAnyMiddle": -1,
                "TakeAnyRight": -1
            }
        return slot_data

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        """
        Fill in additional entrance information text into locations, which is displayed when hinted.
        structure is {player_id: {location_id: text}} You will need to insert your own player_id.
        """
        if self.options.EntranceShuffle > 0:
            hint_data.update({self.player: {}})
            for location in self.multiworld.get_locations(self.player):
                if not location.address: # Skip events
                    continue
                if location.name == "Armos Knights": # Armos are always in the same spot.
                    continue
                if location.name == "Ocean Heart Container": # Same for the ocean HC
                    continue
                current_region = location.parent_region
                entrances = [entrance for entrance in current_region.entrances
                                 if entrance.parent_region.name == "Overworld"]
                if len(entrances) > 0: # Dungeon location
                    entrance = [entrance for entrance in current_region.entrances if "Screen" in entrance.name].pop()
                    hint_data[self.player][location.address] = entrance.name[-9:]
                else: # Cave location
                    screens = [entrance.name[:9] for entrance in current_region.entrances]
                    hint_data[self.player][location.address] = ", ".join(screens)


class TLoZItem(Item):
    game = 'The Legend of Zelda'


class TLoZLocation(Location):
    game = 'The Legend of Zelda'
