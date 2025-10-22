import json
import logging
import os

import Utils
import settings
import typing

from typing import Dict, Any, TextIO
from BaseClasses import MultiWorld, ItemClassification, Tutorial, Item, Region, Entrance

from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule

from .Items import item_table
from .Locations import all_locations, FinalFantasyTacticsIILocation
from .Logic import create_logic_rule, create_logic_rule_for_list, LogicObject, PoachLogicObject
from .Options import FinalFantasyTacticsIIOptions, fftii_option_groups
from .Rom import FinalFantasyTacticsIIProcedurePatch
from .Client import FinalFantasyTacticsIvaliceIslandClient

from .data.items import zodiac_stone_names, world_map_pass_names, job_names, shop_levels, \
    special_character_names, ramza_job_levels, rare_item_names, shop_item_names, \
    gil_item_names_weighted, earned_job_names, filler_item_names, jp_item_names_weighted
from .data.locations import all_regions, world_map_regions, story_battle_locations, character_recruit_locations, \
    sidequest_battle_locations, job_unlock_locations, rare_battle_locations, default_murond_fights, \
    shop_unlock_locations, monster_location_names, story_zodiac_stone_locations, sidequest_zodiac_stone_locations, \
    ramza_job_unlock_locations
from .data.logic.Monsters import monster_locations_lookup, monster_family_lookup, monster_families
from .data.logic.regions.Fovoham import fovoham_regions
from .data.logic.regions.Gallione import gallione_regions
from .data.logic.regions.Jobs import jobs_regions
from .data.logic.regions.Lesalia import lesalia_regions
from .data.logic.regions.Limberry import limberry_regions
from .data.logic.regions.Lionel import lionel_regions
from .data.logic.regions.Murond import murond_regions
from .data.logic.regions.Zeltennia import zeltennia_regions


class FinalFantasyTacticsIISettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Final Fantasy Tactics ISO"""
        description = "Final Fantasy Tactics ISO File"
        copy_to = "Final Fantasy Tactics (USA).bin"
        md5s = ["b156ba386436d20fd5ed8d37bab6b624"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = True


class FinalFantasyTacticsIIWeb(WebWorld):
    theme = "ocean"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Final Fantasy Tactics for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Rosalie"]
    )

    tutorials = [setup]

    rich_text_options_doc = True
    option_groups = fftii_option_groups


class FinalFantasyTacticsIvaliceIslandWorld(World):
    """
    An open world mod for Final Fantasy Tactics for Archipelago.
    Find all the Zodiac Stones and make your way to Murond Death City to confront Altima!
    """
    settings: typing.ClassVar[FinalFantasyTacticsIISettings]
    game = "Final Fantasy Tactics Ivalice Island"
    options_dataclass = FinalFantasyTacticsIIOptions
    options: FinalFantasyTacticsIIOptions

    base_id = 0
    web = FinalFantasyTacticsIIWeb()

    item_name_to_id = {item: item_data.id for item, item_data in item_table.items()}
    location_name_to_id = {location.name: location.id for location in all_locations}
    item_name_groups = {
        "Zodiac Stones": zodiac_stone_names
    }

    filler_items: list[str] | None
    included_locations: list[str]
    murond_fights: list[str]
    starting_pass: str
    zodiac_stones_required: int

    version = 1
    debug = False
    topology_present = debug

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.filler_items = None
        self.included_locations = list()
        self.murond_fights = list()
        self.starting_pass = "Gallione Pass"
        self.zodiac_stones_required = 0

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld) -> None:
        logging.info(f"Final Fantasy Tactics Ivalice Island APWorld v{cls.version} used for generation.")

    @classmethod
    def stage_write_spoiler_header(cls, _multiworld: MultiWorld, spoiler_handle: TextIO):
        spoiler_handle.write(f"\nFinal Fantasy Tactics Ivalice Island APWorld version: v{cls.version}\n")

    def create_item(self, name: str) -> "FinalFantasyTacticsIIItem":
        return FinalFantasyTacticsIIItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    def create_event(self, name: str) -> "FinalFantasyTacticsIIItem":
        return FinalFantasyTacticsIIItem(name, ItemClassification.progression, None, self.player)

    def generate_early(self) -> None:
        # Story battles are always in
        self.included_locations.extend(story_battle_locations)

        # Character recruitment locations are always in if not tied to a sidequest
        if self.options.sidequest_battles:
            character_recruitments = character_recruit_locations
        else:
            character_recruitments = [
                character for character in character_recruit_locations if character not in sidequest_battle_locations
            ]
        self.included_locations.extend(character_recruitments)

        # Shop unlocks are always in
        self.included_locations.extend(shop_unlock_locations)

        # Ramza form unlocks are always in
        self.included_locations.extend(ramza_job_unlock_locations)

        # Optional locations
        if self.options.sidequest_battles:
            self.included_locations.extend(sidequest_battle_locations)
        if self.options.job_unlocks:
            self.included_locations.extend(job_unlock_locations)
        if self.options.rare_battles:
            self.included_locations.extend(rare_battle_locations)
        if self.options.poach_locations:
            self.included_locations.extend(monster_location_names)

        # Right now, the final series can't unlock anything since we don't return to the world map, so pull those out.
        self.murond_fights.extend(default_murond_fights)
        for fight in self.murond_fights:
            self.included_locations.remove(fight)

        # Make Zodiac Stones local if option is set
        if self.options.zodiac_stone_locations == self.options.zodiac_stone_locations.option_anywhere_local:
            self.options.local_items.value.add("Zodiac Stones")

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for region_data in all_regions:
            region = Region(region_data.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Will be adjusted for different starting regions.
        starting_region = self.get_region("Gariland")
        menu.connect(starting_region)
        self.options.start_inventory.value[self.starting_pass] = 1

        # Debug lists
        gallione_locations = []
        fovoham_locations = []
        lesalia_locations = []
        lionel_locations = []
        zeltennia_locations = []
        limberry_locations = []
        murond_locations = []

        # Define connections
        for origin_region_data in all_regions:
            origin_region = self.get_region(origin_region_data.name)
            for connection in origin_region_data.connections:
                connecting_region = self.get_region(connection.destination.name)
                logic_object = LogicObject(self.player, self.options, 0)
                if self.debug:
                    print(f"Connection: {origin_region.name} to {connecting_region.name}")
                logic_object.requirements = create_logic_rule_for_list(
                    connection.requirements,
                    self.options,
                    self.debug)
                connection_name = f"{origin_region.name} to {connecting_region.name}"
                new_entrance = Entrance(self.player, connection_name, origin_region)
                new_entrance.access_rule = logic_object.logic_rule
                origin_region.exits.append(new_entrance)
                new_entrance.connect(connecting_region)
            for location in origin_region_data.locations:
                if origin_region_data in gallione_regions:
                    gallione_locations.append(location)
                if origin_region_data in fovoham_regions:
                    fovoham_locations.append(location)
                if origin_region_data in lesalia_regions:
                    lesalia_locations.append(location)
                if origin_region_data in lionel_regions:
                    lionel_locations.append(location)
                if origin_region_data in zeltennia_regions:
                    zeltennia_locations.append(location)
                if origin_region_data in limberry_regions:
                    limberry_locations.append(location)
                if origin_region_data in murond_regions:
                    murond_locations.append(location)
                if location.name not in self.included_locations:
                    if self.debug:
                        print(f"Excluding {location.name}")
                    continue
                new_location = FinalFantasyTacticsIILocation(
                    self.player,
                    location.name,
                    self.location_name_to_id[location.name],
                    origin_region
                )
                origin_region.locations.append(new_location)
        for region in jobs_regions:
            menu.connect(self.get_region(region.name))

        poach_region = Region("Poaching", self.player, self.multiworld)
        self.multiworld.regions.append(poach_region)
        menu.connect(poach_region)
        if self.options.poach_locations:
            for poach_location in monster_location_names:
                new_location = FinalFantasyTacticsIILocation(
                    self.player, poach_location, self.location_name_to_id[poach_location], poach_region
                )
                poach_region.locations.append(new_location)

        victory_location = self.get_location("Graveyard of Airships 2 Story Battle")
        victory_location.place_locked_item(self.create_item("Farlem"))

        # Debug print list and number of locations for analysis purposes
        if self.debug:
            all_region_locations = {
                "Gallione": gallione_locations,
                "Fovoham": fovoham_locations,
                "Lesalia": lesalia_locations,
                "Lionel": lionel_locations,
                "Zeltennia": zeltennia_locations,
                "Limberry": limberry_locations,
                "Murond": murond_locations
            }
            with open("fftlocations.txt", "w") as file:
                for key, value in all_region_locations.items():
                    locations = [location.name for location in value if location.name in self.included_locations]
                    file.write(f"{key} Locations ({len(locations)}):\n")
                    for location in locations:
                        file.write(f"{location}\n")
                    file.write("\n")

        #for fight in self.murond_fights:
        #    self.get_location(fight).place_locked_item(self.create_item(self.random.choice(rare_item_names)))

        if self.debug:
            from Utils import visualize_regions
            visualize_regions(self.get_region("Menu"), f"fftdiagram{self.player}.puml")

    def create_items(self):
        # Determine number of zodiac stones based on options
        self.zodiac_stones_required = self.options.zodiac_stones_required.value
        zodiac_stones_in_pool = self.options.zodiac_stones_in_pool.value
        if self.options.zodiac_stone_locations == self.options.zodiac_stone_locations.option_vanilla_stones:
            if self.options.sidequest_battles:
                self.zodiac_stones_required = min(
                    self.zodiac_stones_required,
                    len(story_zodiac_stone_locations) + len(sidequest_zodiac_stone_locations))
                zodiac_stones_in_pool = min(
                    zodiac_stones_in_pool,
                    len(story_zodiac_stone_locations) + len(sidequest_zodiac_stone_locations))
            else:
                self.zodiac_stones_required = min(self.zodiac_stones_required, len(story_zodiac_stone_locations))
                zodiac_stones_in_pool = min(zodiac_stones_in_pool, len(story_zodiac_stone_locations))
        if zodiac_stones_in_pool < self.zodiac_stones_required:
            zodiac_stones_in_pool = self.zodiac_stones_required

        # Get all world map passes we don't start with
        world_map_passes = [item for item in world_map_pass_names if item != self.starting_pass]
        self.push_precollected(self.create_item(self.starting_pass))

        # Squire is always unlocked
        self.options.start_inventory.value["Squire"] = 1
        self.push_precollected(self.create_item("Squire"))

        # If we don't have jobs in the pool, we "start" with them all
        if not self.options.job_unlocks:
            for job_name in earned_job_names:
                self.options.start_inventory.value[job_name] = 1
                self.push_precollected(self.create_item(job_name))

        # Pick Zodiac Stones to place ingame
        zodiac_stones_in_game = self.random.sample(zodiac_stone_names, k=zodiac_stones_in_pool)

        # Handle major items
        major_items = [
           *world_map_passes, *shop_levels, *special_character_names, *ramza_job_levels
        ]

        # Place Zodiac Stones if stones are in vanilla spots. Otherwise, add them to itempool.
        if self.options.zodiac_stone_locations == self.options.zodiac_stone_locations.option_vanilla_stones:
            stone_locations = story_zodiac_stone_locations
            if self.options.sidequest_battles:
                stone_locations.extend(sidequest_zodiac_stone_locations)
            stone_locations = self.random.sample(stone_locations, k=zodiac_stones_in_pool)
            self.random.shuffle(stone_locations)
            for stone in zodiac_stones_in_game:
                self.get_location(stone_locations.pop()).place_locked_item(self.create_item(stone))
        else:
            major_items.extend(zodiac_stones_in_game)

        # Add jobs if they're items
        if self.options.job_unlocks:
            major_items.extend(earned_job_names)

        # Get unfilled location count.
        world_locations = self.multiworld.get_unfilled_locations(self.player)
        location_count = len(world_locations)

        # Get filler item count and determine filler pool
        filler_item_count = location_count - len(major_items)
        filler_items = self.determine_filler_item_pool(filler_item_count)

        # Create items
        itempool = [*major_items, *filler_items]
        for item in map(self.create_item, itempool):
            self.multiworld.itempool.append(item)

    def determine_filler_item_pool(self, filler_item_count: int) -> list[str]:

        filler_lists = []
        normal_weight = self.options.normal_item_weight.value
        rare_weight = self.options.rare_item_weight.value
        gil_weight = self.options.gil_item_weight.value
        jp_weight = self.options.jp_boon_item_weight.value

        # Shortcut if everything's the same weight (or if someone gets funny and sets them all to zero)
        if normal_weight == rare_weight == gil_weight == jp_weight:
            filler_lists = [shop_item_names, rare_item_names, gil_item_names_weighted, jp_item_names_weighted]
        else:
            # One instance of a list per weight value
            for i in range(normal_weight):
                filler_lists.append(shop_item_names)
            for i in range(rare_weight):
                filler_lists.append(rare_item_names)
            for i in range(gil_weight):
                filler_lists.append(gil_item_names_weighted)
            for i in range(jp_weight):
                filler_lists.append(jp_item_names_weighted)
        return_list = []

        # For every itempool slot, just pull a random item from each pool in order based on weight
        # Could change this if we want the weights to be random and not static
        for i in range(filler_item_count):
            chosen_list = filler_lists[i % len(filler_lists)]
            chosen_item = self.random.choice(chosen_list)
            return_list.append(chosen_item)
        return return_list

    def set_rules(self):
        # Locations that aren't real don't get rules set, of course
        for location in all_locations:
            if location.name not in self.included_locations:
                continue

            ap_location = self.get_location(location.name)
            if location.name in monster_location_names:
                # Poach locations rules
                monster_object = monster_locations_lookup[location.name[6:]]
                monster_family_name = monster_family_lookup[monster_object.monster_name]
                monster_family = [
                    monster_locations_lookup[monster_name.value] for monster_name in
                    monster_families[monster_family_name]
                ]
                poach_logic_object = PoachLogicObject(self.player, self.options)
                poach_logic_object.requirements = monster_object.compiled_requirements
                breed_logic_object = PoachLogicObject(self.player, self.options)
                breed_logic_object.requirements = []
                for monster in monster_family:
                    breed_logic_object.requirements.extend(monster.compiled_requirements)
                add_rule(
                    ap_location,
                    lambda state: poach_logic_object.poach_logic_rule(state) or
                                  (breed_logic_object.poach_logic_rule(state) and state.has("Mediator", self.player)))
            else:
                # Regular location rules
                logic_object = LogicObject(self.player, self.options, location.battle_level)
                if self.debug:
                    print(f"\n{location.name} requirements:")
                logic_object.requirements = create_logic_rule_for_list(
                    location.requirements, self.options, self.debug)
                add_rule(ap_location, logic_object.logic_rule)

        # Victory condition
        add_rule(
            self.get_location("Graveyard of Airships 2 Story Battle"),
            lambda state: state.has_group("Zodiac Stones", self.player, self.zodiac_stones_required)
                          and state.can_reach_region("Murond Death City", self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Farlem", self.player)

    def pre_fill(self) -> None:
        pass

    def generate_basic(self):
        pass

    def generate_output(self, output_directory: str) -> None:
        patch_dict: dict[str, Any] = dict()
        # Hash of the MW seed to associate with save file
        patch_dict["SeedHash"] = self.multiworld.seed % 0x7FFF

        rom_name_text = f'FFTII{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:9}'
        rom_name_text = rom_name_text[:20]
        rom_name = bytearray(rom_name_text, 'utf-8')
        rom_name.extend([0] * (20 - len(rom_name)))
        patch_dict["RomName"] = f'FFTII{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:9}'

        patch_dict["OutputFile"] = f'{self.multiworld.get_out_file_name_base(self.player)}'

        patch = FinalFantasyTacticsIIProcedurePatch(player=self.player, player_name=self.player_name)
        patch.write_file("patch_file.json", json.dumps(patch_dict).encode("UTF-8"))
        rom_path = os.path.join(
            output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}" f"{patch.patch_file_ending}"
        )
        patch.write(rom_path)

    def modify_multidata(self, multidata: dict):
        import base64
        rom_name_text = f'FFTII{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:9}'
        rom_name_text = rom_name_text[:20]
        rom_name = bytearray(rom_name_text, 'utf-8')
        rom_name.extend([0] * (20 - len(rom_name)))
        new_name = base64.b64encode(bytes(rom_name)).decode()
        multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = [item for item in item_table if item in filler_item_names]
        return self.random.choice(self.filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict("gil_item_size", "jp_boon_size")


class FinalFantasyTacticsIIItem(Item):
    game = "Final Fantasy Tactics Ivalice Island"
