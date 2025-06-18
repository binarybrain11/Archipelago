import json
import os
import Utils
import settings
import typing

from typing import Dict, Any
from BaseClasses import MultiWorld, ItemClassification, Tutorial, Item, Region
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule

from .Items import item_table, default_item_quantities, ap_name_to_mars_name
from .Locations import all_locations, MetroidFusionLocation, get_location_data_by_name, build_item_message
from .Logic import create_logic_rule, create_logic_rule_for_list, LogicObject
from .Rom import MetroidFusionProcedurePatch
from .data import memory
from .data.locations import fusion_regions
from .data.room_names import room_names
from .Client import MetroidFusionClient


class MetroidFusionSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Zelda 1"""
        description = "Metroid Fusion (USA) ROM File"
        copy_to = "Metroid Fusion (USA).gba"
        md5s = ["af5040fc0f579800151ee2a683e2e5b5"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = True


class MetroidFusionWeb(WebWorld):
    theme = "ocean"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Metroid Fusion for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Rosalie"]
    )

    tutorials = [setup]


class MetroidFusionWorld(World):
    """
    The Legend of Zelda needs almost no introduction. Gather the eight fragments of the
    Triforce of Wisdom, enter Death Mountain, defeat Ganon, and rescue Princess Zelda.
    This randomizer shuffles all the items in the game around, leading to a new adventure
    every time.
    """
    #options_dataclass = TlozOptions
    #options: TlozOptions
    settings: typing.ClassVar[MetroidFusionSettings]
    game = "Metroid Fusion"
    topology_present = False
    base_id = 0
    web = MetroidFusionWeb()

    item_name_to_id = {item: item_data.mars_id for item, item_data in item_table.items()}
    location_name_to_id = {location.name: location.ap_id for location in all_locations}

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def create_item(self, name: str):
        return MetroidFusionItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    def create_event(self, name: str):
        return MetroidFusionItem(name, ItemClassification.progression, None, self.player)

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for region_data in fusion_regions:
            region = Region(region_data.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        main_deck = self.get_region("Main Deck Hub")
        menu.connect(main_deck)

        # Define connections
        for origin_region_data in fusion_regions:
            origin_region = self.get_region(origin_region_data.name)
            for connection in origin_region_data.connections:
                connecting_region = self.get_region(connection.destination.name)
                logic_object = LogicObject(self.player)
                logic_object.requirements, logic_object.energy_tanks = create_logic_rule_for_list(connection.requirements)
                origin_region.connect(
                    connecting_region,
                    f"{origin_region.name} to {connecting_region.name}",
                    logic_object.logic_rule
                )
            for location in origin_region_data.locations:
                new_location = MetroidFusionLocation(
                    self.player,
                    location.name,
                    self.location_name_to_id[location.name],
                    origin_region
                )
                origin_region.locations.append(new_location)
        operations_deck = self.get_region("Operations Deck")
        victory_event = MetroidFusionLocation(self.player, "Victory", None, operations_deck)
        operations_deck.locations.append(victory_event)
        victory_event.place_locked_item(self.create_event("Victory"))

    def create_items(self):
        itempool = []
        sphere_1_locations = ["Main Deck -- Quarantine Bay", "Main Deck -- Operations Deck Data Room"]
        sphere_1_item_names = ["Morph Ball", "Missile Data"]
        preplaced_location = self.random.choice(sphere_1_locations)
        preplaced_item = self.random.choice(sphere_1_item_names)
        for item in item_table:
            if item == preplaced_item:
                self.get_location(preplaced_location).place_locked_item(self.create_item(preplaced_item))
            elif item in default_item_quantities.keys():
                for i in range(default_item_quantities[item]):
                    itempool.append(item)
            else:
                itempool.append(item)
        for item in map(self.create_item, itempool):
            self.multiworld.itempool.append(item)

    def set_rules(self):
        for location in all_locations:
            ap_location = self.get_location(location.name)
            location_data = get_location_data_by_name(location.name)
            logic_object = LogicObject(self.player)
            logic_object.requirements, logic_object.energy_tanks = create_logic_rule_for_list(location_data.requirements)
            add_rule(ap_location, logic_object.logic_rule)
        add_rule(self.get_location("Victory"), lambda state: state.has("Infant Metroid", self.player, 5) and state.has("Energy Tank", self.player, 0))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def generate_basic(self):
        pass

    def generate_output(self, output_directory: str):
        patch_dict = dict()
        patch_dict["SeedHash"] = str(self.multiworld.seed)[:8]
        patch_dict["Locations"] = {"MajorLocations": [], "MinorLocations": []}
        for location in self.get_locations():
            if location.name == "Victory":
                continue
            location_data = get_location_data_by_name(location.name)
            if location.item.player == self.player:
                item_name = ap_name_to_mars_name[location.item.name]
                message = None
            else:
                item_name = "None"
                message = build_item_message(location.item.name, self.multiworld.player_name[location.item.player])
            json_data = location_data.to_json(item_name)
            if message is not None:
                json_data["ItemMessages"] = message
            if location_data.major:
                patch_dict["Locations"]["MajorLocations"].append(json_data)
            else:
                patch_dict["Locations"]["MinorLocations"].append(json_data)
        patch_dict["RequiredMetroidCount"] = 5
        patch_dict["PowerBombsWithoutBombs"] = True
        patch_dict["AntiSoftlockRoomEdits"] = True
        patch_dict["RevealHiddenTiles"] = True
        patch_dict["DisableDemos"] = True
        patch_dict["SkipDoorTransitions"] = True
        patch_dict["UnexploredMap"] = True
        patch_dict["RoomNames"] = room_names[0]
        rom_name_text = f'MFU{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        rom_name_text = rom_name_text[:20]
        rom_name = bytearray(rom_name_text, 'utf-8')
        rom_name.extend([0] * (20 - len(rom_name)))
        patch_dict["RomName"] = f'MFU{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        patch_dict["OutputFile"] = f'{self.multiworld.get_out_file_name_base(self.player)}' + '.gba'

        # Our actual patch is just a set of instructions and data for MARS to use.
        patch = MetroidFusionProcedurePatch(player=self.player, player_name=self.player_name)
        patch.write_file("patch_file.json", json.dumps(patch_dict).encode("UTF-8"))
        rom_path = os.path.join(
            output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}" f"{patch.patch_file_ending}"
        )
        patch.write(rom_path)

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

class MetroidFusionItem(Item):
    game = "Metroid Fusion"