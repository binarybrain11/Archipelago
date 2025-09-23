import typing
from collections.abc import Callable

from worlds.metroidfusion import MetroidFusionOptions

starting_location_starting_items_map = {
    "Main Deck Hub": {
        "Main Deck -- Quarantine Bay": {
            "Sphere 0": [],
            "Sphere 1": [],
            "PONR Sphere 0": [],
            "PONR Sphere 1": []
        }

    },
    "Sector Hub Elevator Bottom": {
        "Sector 2 -- Security Room": {
            "Sphere 0": [],
            "Sphere 1": ["Morph Ball", "Speed Booster"],
            "PONR Sphere 0": ["Hi-Jump", "Space Jump", "Level 1 Keycard"],
            "PONR Sphere 1": ["Morph Ball", "Speed Booster"]
        }
    }
}

class StartingLocation:
    vanilla_opening_locations: list[str] = []
    elevator_shuffle_opening_locations: list[str] = []
    sphere_0: list[str] = []
    sphere_1: list[str] = []
    ponr_sphere_0: list[str] = []
    ponr_sphere_1: list[str] = []
    get_additional_items: Callable[[typing.Self, MetroidFusionOptions], list[str]] = lambda x, y: []

    def get_sphere_0(self, ponr = False):
        if not ponr:
            return self.sphere_0 if len(self.ponr_sphere_0) == 0 else self.ponr_sphere_0
        else:
            return self.sphere_0

    def get_sphere_1(self, ponr = False):
        if not ponr:
            return self.sphere_1 if len(self.ponr_sphere_1) == 0 else self.ponr_sphere_1
        else:
            return self.sphere_1


main_deck_hub = StartingLocation()
main_deck_hub.vanilla_opening_locations = ["Main Deck -- Quarantine Bay", "Main Deck -- Operations Deck Data Room"]
main_deck_hub.elevator_shuffle_opening_locations = ["Main Deck -- Quarantine Bay"]
main_deck_hub.sphere_1 = ["Morph Ball", "Missile Data"]

def get_main_deck_additional_items(_self: StartingLocation, options: MetroidFusionOptions):
    additional_items = []
    if options.EarlyProgression >= options.EarlyProgression.option_advanced:
        additional_items.append("Screw Attack")
        if options.ShinesparkTrickDifficulty >= options.ShinesparkTrickDifficulty.option_advanced:
            additional_items.append("Speed Booster")
    return additional_items

main_deck_hub.get_additional_items = get_main_deck_additional_items

sector_hub = StartingLocation()
sector_hub.vanilla_opening_locations = ["Sector 2 (TRO) -- Level 1 Security Room"]
sector_hub.elevator_shuffle_opening_locations = ["Sector 2 (TRO) -- Level 1 Security Room"]
sector_hub.sphere_0 = []
sector_hub.sphere_1 = ["Morph Ball", "Missile Data", "Screw Attack", "Speed Booster"]
sector_hub.ponr_sphere_0 = ["Hi-Jump", "Space Jump", "Level 1 Keycard"]
sector_hub.ponr_sphere_1 = ["Morph Ball", "Missile Data", "Screw Attack"]


starting_location_data = {
    "Docking Bay": {
        "Area": 0,
        "Room": 0,
        "BlockX": 25,
        "BlockY": 10
    },
    "Sector Hub": {
        "Area": 0,
        "Room": 24,
        "BlockX": 24,
        "BlockY": 18
    },
    "Concourse Save Station": {
        "Area": 0,
        "Room": 33,
        "BlockX": 9,
        "BlockY": 10
    }
}