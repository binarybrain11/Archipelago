import json
import logging
import os
from copy import deepcopy, copy

import Utils
import settings
import typing

from typing import Dict, Any, TextIO
from BaseClasses import MultiWorld, ItemClassification, Tutorial, Item, Region, EntranceType, CollectionState, Entrance
from entrance_rando import disconnect_entrance_for_randomization, randomize_entrances
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule

from .Items import item_table
from .Locations import all_locations, FinalFantasyTacticsLocation
from .Logic import create_logic_rule, create_logic_rule_for_list, LogicObject
from .Options import FinalFantasyTacticsOptions, fft_option_groups
from .Rom import FinalFantasyTacticsProcedurePatch

from .data.items import zodiac_stone_names, world_map_pass_names, job_names, filler_item_names, shop_levels, \
    special_character_names
from .data.locations import all_regions, world_map_regions
from .data.logic.regions.Jobs import jobs_regions


class FinalFantasyTacticsSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Metroid Fusion ROM"""
        description = "Metroid Fusion (USA) ROM File"
        copy_to = "Metroid Fusion (USA).gba"
        md5s = ["af5040fc0f579800151ee2a683e2e5b5"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = True
    display_location_found_messages: bool = True


class FinalFantasyTacticsWeb(WebWorld):
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
    option_groups = fft_option_groups


class FinalFantasyTacticsWorld(World):
    """
    FFT description here.
    """
    settings: typing.ClassVar[FinalFantasyTacticsSettings]
    game = "Final Fantasy Tactics"
    options_dataclass = FinalFantasyTacticsOptions
    options: FinalFantasyTacticsOptions

    topology_present = True
    base_id = 0
    web = FinalFantasyTacticsWeb()

    item_name_to_id = {item: item_data.id for item, item_data in item_table.items()}
    location_name_to_id = {location.name: location.id for location in all_locations}
    item_name_groups = {
        "Zodiac Stones": zodiac_stone_names
    }

    version = 1
    debug = False



    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.filler_items = None

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld) -> None:
        logging.info(f"Final Fantasy Tactics APWorld v{cls.version} used for generation.")

    @classmethod
    def stage_write_spoiler_header(cls, _multiworld: MultiWorld, spoiler_handle: TextIO):
        spoiler_handle.write(f"\nFinal Fantasy Tactics APWorld version: v{cls.version}\n")

    def create_item(self, name: str) -> "FinalFantasyTacticsItem":
        return FinalFantasyTacticsItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    def create_event(self, name: str) -> "FinalFantasyTacticsItem":
        return FinalFantasyTacticsItem(name, ItemClassification.progression, None, self.player)

    def generate_early(self) -> None:
        pass

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for region_data in all_regions:
            region = Region(region_data.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        starting_region = self.get_region("Gariland")
        menu.connect(starting_region)

        # Define connections
        for origin_region_data in all_regions:
            origin_region = self.get_region(origin_region_data.name)
            for connection in origin_region_data.connections:
                connecting_region = self.get_region(connection.destination.name)
                logic_object = LogicObject(self.player, self.options)
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
                new_location = FinalFantasyTacticsLocation(
                    self.player,
                    location.name,
                    self.location_name_to_id[location.name],
                    origin_region
                )
                origin_region.locations.append(new_location)
        for region in jobs_regions:
            menu.connect(self.get_region(region.name))
        murond_death_city = self.get_region("Murond Death City")
        victory_location = FinalFantasyTacticsLocation(self.player, "Victory", None, murond_death_city)
        victory_location.place_locked_item(self.create_event("Victory"))
        murond_death_city.locations.append(victory_location)
        from Utils import visualize_regions
        visualize_regions(self.get_region("Menu"), f"fftdiagram{self.player}.puml")

    def create_items(self):
        world_locations = self.get_locations()
        location_count = 0
        for location in world_locations:
            if location.item is None:
                location_count += 1

        zodiac_stones_required = self.options.ZodiacStonesRequired.value
        zodiac_stones_in_pool = self.options.ZodiacStonesInPool.value
        if zodiac_stones_in_pool < zodiac_stones_required:
            zodiac_stones_in_pool = zodiac_stones_required

        zodiac_stones_in_game = self.random.sample(zodiac_stone_names, k=zodiac_stones_in_pool)
        major_items = [
            *zodiac_stones_in_game, *world_map_pass_names, *job_names, *shop_levels, *special_character_names
        ]

        filler_item_count = location_count - len(major_items)
        filler_items = []
        for i in range(filler_item_count):
            filler_items.append(self.random.choice(filler_item_names))

        itempool = [*major_items, *filler_items]
        for item in map(self.create_item, itempool):
            if item.name == "Squire":
                self.get_location("Squire Unlock").place_locked_item(item)
            else:
                self.multiworld.itempool.append(item)

    def set_rules(self):
        for location in all_locations:
            ap_location = self.get_location(location.name)
            logic_object = LogicObject(self.player, self.options)
            if self.debug:
                print(f"\n{location.name} requirements:")
            logic_object.requirements = create_logic_rule_for_list(
                location.requirements, self.options, self.debug)
            add_rule(ap_location, logic_object.logic_rule)

        zodiac_stones_required = self.options.ZodiacStonesRequired.value
        zodiac_stones_in_pool = self.options.ZodiacStonesInPool.value
        if zodiac_stones_in_pool < zodiac_stones_required:
            zodiac_stones_in_pool = zodiac_stones_required


        add_rule(
            self.get_location("Victory"),
            lambda state: state.has_group("Zodiac Stones", self.player, zodiac_stones_required))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def pre_fill(self) -> None:
        pass

    def generate_basic(self):
        pass

    def generate_output(self, output_directory: str) -> None:
        pass
        # patch_dict = dict()
        # patch_dict["SeedHash"] = str(self.multiworld.seed)[:8]
        # patch_dict["Locations"] = {"MajorLocations": [], "MinorLocations": []}
        #
        # for location in self.get_locations():
        #     pass
        #
        #
        # patch_dict["RequiredMetroidCount"] = infant_metroids_required
        #
        # patch_dict["StartingLocation"] = self.build_starting_location_dict()
        #
        # patch_dict["NavStationLocks"] = self.build_nav_locks_dict()
        #
        # patch_dict["GenerationVersion"] = MetroidFusionWorld.version
        #
        # patch_dict["SectorShortcuts"] = self.build_sector_connections()
        # patch_dict["ElevatorConnections"] = self.build_elevator_connections()
        #
        # rom_name_text = f'MFU{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        # rom_name_text = rom_name_text[:20]
        # rom_name = bytearray(rom_name_text, 'utf-8')
        # rom_name.extend([0] * (20 - len(rom_name)))
        # patch_dict["RomName"] = f'MFU{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        # patch_dict["OutputFile"] = f'{self.multiworld.get_out_file_name_base(self.player)}' + '.gba'
        #
        # # Our actual patch is just a set of instructions and data for MARS to use.
        # patch = MetroidFusionProcedurePatch(player=self.player, player_name=self.player_name)
        # patch.write_file("patch_file.json", json.dumps(patch_dict).encode("UTF-8"))
        # rom_path = os.path.join(
        #     output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}" f"{patch.patch_file_ending}"
        # )
        # patch.write(rom_path)

    def modify_multidata(self, multidata: dict):
        import base64
        rom_name_text = f'MFU{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        rom_name_text = rom_name_text[:20]
        rom_name = bytearray(rom_name_text, 'utf-8')
        rom_name.extend([0] * (20 - len(rom_name)))
        new_name = base64.b64encode(bytes(rom_name)).decode()
        multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = [item for item in item_table if
                                 item_table[item].classification == ItemClassification.filler]
        return self.random.choice(self.filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        pass


class FinalFantasyTacticsItem(Item):
    game = "Final Fantasy Tactics"

