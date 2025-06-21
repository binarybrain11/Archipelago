import json
import os
from copy import deepcopy

import Utils
import settings
import typing

from typing import Dict, Any
from BaseClasses import MultiWorld, ItemClassification, Tutorial, Item, Region
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule
from .Hints import create_hints, HintedPair

from .Items import item_table, default_item_quantities, ap_name_to_mars_name
from .Locations import all_locations, MetroidFusionLocation, get_location_data_by_name, build_item_message, \
    location_groups, build_shiny_item_message
from .Logic import create_logic_rule, create_logic_rule_for_list, LogicObject
from .Options import MetroidFusionOptions
from .Rom import MetroidFusionProcedurePatch
from .data import memory
from .data.locations import fusion_regions
from .data.offworld_sprites import offworld_sprites, SpriteNames
from .data.room_names import room_names
from .Client import MetroidFusionClient


class MetroidFusionSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the Metroid Fusion ROM"""
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
    options_dataclass = MetroidFusionOptions
    options: MetroidFusionOptions
    topology_present = False
    base_id = 0
    web = MetroidFusionWeb()
    hint_pairs: list[HintedPair] | None

    item_name_to_id = {item: item_data.mars_id for item, item_data in item_table.items()}
    location_name_to_id = {location.name: location.ap_id for location in all_locations}
    location_name_groups = location_groups

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.filler_items = None
        self.hint_pairs = None

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
        item_quantities = deepcopy(default_item_quantities)
        infant_metroids_in_pool = self.options.InfantMetroidsInPool.value
        item_quantities["Infant Metroid"] = infant_metroids_in_pool
        item_quantities["Power Bomb Tank"] -= infant_metroids_in_pool
        for item in item_table:
            if item == preplaced_item:
                self.get_location(preplaced_location).place_locked_item(self.create_item(preplaced_item))
            elif item in item_quantities.keys():
                for i in range(item_quantities[item]):
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
        infant_metroids_required = self.options.InfantMetroidsRequired.value
        if infant_metroids_required > self.options.InfantMetroidsInPool.value:
            infant_metroids_required = self.options.InfantMetroidsInPool.value
        add_rule(
            self.get_location("Victory"),
            lambda state: state.has("Infant Metroid", self.player, infant_metroids_required)
                          and state.has("Energy Tank", self.player, 0))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def generate_basic(self):
        pass

    @staticmethod
    def create_palette_rando(seed: int):
        return {
            "Seed": seed % 2**32,
            "Randomize": {
                "Samus": {
                    "HueMin": 0,
                    "HueMax": 360
                },
                "Beams": {
                    "HueMin": 0,
                    "HueMax": 360
                },
                "Enemies": {
                    "HueMin": 0,
                    "HueMax": 360
                },
                "Tilesets": {
                    "HueMin": 0,
                    "HueMax": 360
                }
            },
            "ColorSpace": "Oklab"
        }


    def create_navigation_text(self, hint_text: list[str], required_metroids: int):
        beginning_text_addition = ""
        if self.options.EnableHints:
            beginning_text_addition = (f"Uplink at [COLOR=2]Navigation Rooms[/COLOR] along the way. "
                                       f"I can scan the station for useful equipment from there.")
        navigation_text = {
            "English": {
                "ShipText": {
                    "InitialText": f"Your objective is as follows: Find enough [COLOR=3]Infant Metroids[/COLOR] "
                                   f"({required_metroids}) to lure out the SA-X. "
                                   f"Then initiate the station's self-destruct sequence. "
                                   f"{beginning_text_addition}"
                                   f"[OBJECTIVE]Good. Move out.",
                    "ConfirmText": "Any Objections, Lady?"
                }
            }
        }
        if self.options.EnableHints:
            nav_room_text = {
                    "MainDeckEast": hint_text[0],
                    "MainDeckWest": hint_text[1],
                    "OperationsDeck": hint_text[2],
                    "AuxiliaryPower": hint_text[3],
                    "RestrictedLabs": hint_text[4],
                    "Sector1Entrance": hint_text[5],
                    "Sector2Entrance": hint_text[6],
                    "Sector3Entrance": hint_text[7],
                    "Sector4Entrance": hint_text[8],
                    "Sector5Entrance": hint_text[9],
                    "Sector6Entrance": hint_text[10]
                }
        else:
            nav_room_text = {
                    "MainDeckEast": "No hint data available.",
                    "MainDeckWest": "No hint data available.",
                    "OperationsDeck": "No hint data available.",
                    "AuxiliaryPower": "No hint data available.",
                    "RestrictedLabs": "No hint data available.",
                    "Sector1Entrance": "No hint data available.",
                    "Sector2Entrance": "No hint data available.",
                    "Sector3Entrance": "No hint data available.",
                    "Sector4Entrance": "No hint data available.",
                    "Sector5Entrance": "No hint data available.",
                    "Sector6Entrance": "No hint data available."
                }
        navigation_text["English"]["NavigationTerminals"] = nav_room_text
        return navigation_text

    def generate_output(self, output_directory: str):
        patch_dict = dict()
        patch_dict["SeedHash"] = str(self.multiworld.seed)[:8]
        patch_dict["Locations"] = {"MajorLocations": [], "MinorLocations": []}

        for location in self.get_locations():
            # Victory location isn't real and can't hurt you.
            if location.name == "Victory":
                continue
            location_data = get_location_data_by_name(location.name)
            item_sprite = None
            if location.item.player == self.player:
                item_name = ap_name_to_mars_name[location.item.name]
                if item_name == "None":   # Empty items, when we implement them,
                    item_sprite = "Empty" # have a different sprite name than item name
                else:
                    item_sprite = item_name
                message = None # A None message leaves the default Fusion message.
            else:
                item_name = "None" # Remote items shouldn't give anything ingame.
                message = build_item_message(location.item.name, self.multiworld.player_name[location.item.player])
                #Check if the item is in the list of eligible offworld items we can use a Fusion sprite for.
                game = self.multiworld.worlds[location.item.player].game
                if game in offworld_sprites.keys():
                    if location.item.name in offworld_sprites[game].keys():
                        item_sprite = offworld_sprites[game][location.item.name].value
            if item_sprite is None: # If we don't have a sprite yet, we use the question mark icon.
                item_sprite = SpriteNames.Anonymous.value
            # For fun, local visible missile and power bomb tanks have a 1/1024 chance to be shiny.
            if location.item.player == self.player and not location_data.major:
                if item_sprite == SpriteNames.MissileTank.value:
                    chance = self.random.randint(1, 1024)
                    if chance == 1:
                        item_sprite = SpriteNames.ShinyMissileTank.value
                        message = build_shiny_item_message(item_name)
                if item_sprite == SpriteNames.PowerBombTank.value:
                    chance = self.random.randint(1, 1024)
                    if chance == 1:
                        item_sprite = SpriteNames.ShinyPowerBombTank.value
                        message = build_shiny_item_message(item_name)
            json_data = location_data.to_json(item_name, item_sprite)
            if message is not None:
                json_data["ItemMessages"] = message
            if location_data.major:
                patch_dict["Locations"]["MajorLocations"].append(json_data)
            else:
                patch_dict["Locations"]["MinorLocations"].append(json_data)

        infant_metroids_required = self.options.InfantMetroidsRequired.value
        if infant_metroids_required > self.options.InfantMetroidsInPool.value:
            infant_metroids_required = self.options.InfantMetroidsInPool.value
        patch_dict["RequiredMetroidCount"] = infant_metroids_required
        patch_dict["PowerBombsWithoutBombs"] = True
        patch_dict["AntiSoftlockRoomEdits"] = True
        patch_dict["RevealHiddenTiles"] = True
        patch_dict["DisableDemos"] = True
        patch_dict["SkipDoorTransitions"] = True
        patch_dict["UnexploredMap"] = True
        patch_dict["RoomNames"] = room_names
        if self.options.PaletteRandomization:
            patch_dict["Palettes"] = self.create_palette_rando(self.multiworld.seed)
        if self.options.EnableHints:
            hint_text, self.hint_pairs = create_hints(self)
            patch_dict["NavigationText"] = self.create_navigation_text(
                hint_text,
                infant_metroids_required)
        else:
            patch_dict["NavigationText"] = self.create_navigation_text([], infant_metroids_required)

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
        hint_data = {}
        if self.options.EnableHints:
            hint_data = {
                "MainDeckEast": self.get_hint(self.hint_pairs[0]),
                "MainDeckWest": self.get_hint(self.hint_pairs[1]),
                "OperationsDeck": self.get_hint(self.hint_pairs[2]),
                "AuxiliaryPower": self.get_hint(self.hint_pairs[3]),
                "RestrictedLabs": self.get_hint(self.hint_pairs[4]),
                "Sector1Entrance": self.get_hint(self.hint_pairs[5]),
                "Sector2Entrance": self.get_hint(self.hint_pairs[6]),
                "Sector3Entrance": self.get_hint(self.hint_pairs[7]),
                "Sector4Entrance": self.get_hint(self.hint_pairs[8]),
                "Sector5Entrance": self.get_hint(self.hint_pairs[9]),
                "Sector6Entrance": self.get_hint(self.hint_pairs[10])
            }
        return {
            "Hints": hint_data
        }

    def get_hint(self, pair: HintedPair):
        return {
            "Location": pair.location.address,
            "Player": pair.location.player
        }

class MetroidFusionItem(Item):
    game = "Metroid Fusion"