import pkgutil
from typing import Callable

from BaseClasses import Location
from .data.locations import fusion_regions, Requirement
import json

class MetroidFusionLocation(Location):
    game = "Metroid Fusion"
    logic_rule: list[list[str]]

class LocationData():
    name: str
    mars_id: tuple[int, int]
    major: bool
    requirements: list[Requirement]
    ap_id: int
    source_name: str
    room_location: tuple[int, int]

    def __init__(self, name: str, major: bool, ap_id: int):
        self.name = name
        self.major = major
        self.ap_id = ap_id

    def to_json(self, item: str, item_sprite: str):
        if self.major:
            return {
                "Source": self.source_name,
                "Item": item
            }
        else:
            return {
                "Area": self.mars_id[0],
                "Room": self.mars_id[1],
                "BlockX": self.room_location[0],
                "BlockY": self.room_location[1],
                "Item": item,
                "ItemSprite": item_sprite
            }

    def __repr__(self):
        return self.name

def build_item_message(item_name: str, player_name: str):
    return {
        "Languages": {
            "English": f"Found {player_name}'s\n{item_name}",
        },
        "Kind": "CustomMessage"
    }


def populate_json_data(location_data: LocationData):
    file = pkgutil.get_data(__name__, "data/new_locations.json").decode()
    json_data = json.loads(file)
    locations = json_data["MajorLocations"]
    for location in locations:
        if location["room_name"] == location_data.name:
            location_data.source_name = location["Source"]
    locations = json_data["MinorLocations"]
    for location in locations:
        if location["room_name"] == location_data.name:
            location_data.mars_id = location["Area"], location["Room"]
            location_data.room_location = location["BlockX"], location["BlockY"]

file = pkgutil.get_data(__name__, "data/new_locations.json").decode()
json_data = json.loads(file)
locations = json_data["MinorLocations"]

all_locations: list[LocationData] = []
location_ids: dict[str, int] = dict()

ap_id = 1
for region in fusion_regions:
    for location in region.locations:
        location_data = LocationData(location.name, location.major, ap_id)
        location_data.requirements = location.requirements
        populate_json_data(location_data)
        all_locations.append(location_data)
        ap_id += 1



def get_location_data_by_name(name: str):
    return [location for location in all_locations if location.name == name].pop()