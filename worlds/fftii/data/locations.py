from .logic.FFTRegion import FFTRegion
from .logic.Monsters import monster_locations
from .logic.regions.Fovoham import fovoham_regions
from .logic.regions.Gallione import gallione_regions
from .logic.regions.Jobs import jobs_regions
from .logic.regions.Lesalia import lesalia_regions
from .logic.regions.Limberry import limberry_regions
from .logic.regions.Lionel import lionel_regions
from .logic.regions.Murond import murond_regions
from .logic.regions.Zeltennia import zeltennia_regions

world_map_regions: list[FFTRegion] = [
    *gallione_regions,
    *fovoham_regions,
    *lesalia_regions,
    *lionel_regions,
    *zeltennia_regions,
    *limberry_regions,
    *murond_regions
]

menu_regions: list[FFTRegion] = [
    *jobs_regions
]

all_regions: list[FFTRegion] = [
    *world_map_regions, *menu_regions
]

story_battle_locations = [
    "Garliand Magic City Story Battle",
    "Mandalia Plains Story Battle",
    "Igros Castle Story Battle",
    "Sweegy Woods Story Battle",
    "Dorter Slums Story Battle",
    "Dorter City Story Battle",
    "Thieves' Fort Story Battle",
    "Lenalia Plateau Story Battle",
    "Fort Zeakden Story Battle",
    "Grog Hill Story Battle",
    "Yardow Fort City Story Battle",
    "Yuguo Woods Story Battle",
    "Gate of Riovanes Story Battle",
    "Inside Riovanes Castle Story Battle",
    "Roof of Riovanes Castle Story Battle",
    "Fovoham Plains Story Battle",
    "Araguay Woods Story Battle",
    "Zirekile Falls Story Battle",
    "Zeklaus Desert Story Battle",
    "Back Gate of Lesalia Castle Story Battle",
    "Goland Coal City Story Battle",
    "Doguola Pass Story Battle",
    "Zaland Fort City Story Battle",
    "Bariaus Hill Story Battle",
    "Gate of Lionel Castle Story Battle",
    "Inside of Lionel Castle Story Battle",
    "Zigolis Swamp Story Battle",
    "Golgorand Execution Site Story Battle",
    "Bariaus Valley Story Battle",
    "Bervenia Free City Story Battle",
    "Finath River Story Battle",
    "Zeltennia Castle Story Battle",
    "Germinas Peak Story Battle",
    "Bethla Garrison North Wall Story Battle",
    "Bethla Garrison South Wall Story Battle",
    "Bethla Garrison Sluice Story Battle",
    "Bed Desert Story Battle",
    "Limberry Castle Gates Story Battle",
    "Inside Limberry Castle Story Battle",
    "Limberry Castle Cemetary Story Battle",
    "Poeskas Lake Story Battle",
    "St. Murond Temple Story Battle",
    "St. Murond Temple Hall Story Battle",
    "Chapel of St. Murond Temple Story Battle",
    "Underground Book Storage 1 Story Battle",
    "Underground Book Storage 2 Story Battle",
    "Underground Book Storage 3 Story Battle",
    "Underground Book Storage 4 Story Battle",
    "Underground Book Storage 5 Story Battle",
    "Slums of Goug Story Battle",
    "Murond Death City Story Battle",
    "Lost Sacred Precincts Story Battle",
    "Graveyard of Airships 1 Story Battle",
    "Graveyard of Airships 2 Story Battle"
]

character_recruit_locations = [
    "Recruit Rafa",
    "Recruit Malak",
    "Recruit Boco",
    "Recruit Beowulf",
    "Recruit Worker 8",
    "Recruit Agrias",
    "Recruit Reis (Dragon)",
    "Recruit Reis (Human)",
    "Recruit Cloud",
    "Recruit Orlandu",
    "Recruit Meliadoul",
    "Recruit Mustadio",
    "Recruit Byblos"
]

sidequest_battle_locations = [
    "Goland Colliery Third Floor Sidequest Battle",
    "Goland Colliery Second Floor Sidequest Battle",
    "Goland Colliery First Floor Sidequest Battle",
    "Goland Underground Passage Sidequest Battle",
    "Nelveska Temple Sidequest Battle",
    "Zarghidas Trade City Sidequest Battle",
    "NOGIAS Sidequest Battle",
    "TERMINATE Sidequest Battle",
    "DELTA Sidequest Battle",
    "VALKYRIES Sidequest Battle",
    "MLAPAN Sidequest Battle",
    "TIGER Sidequest Battle",
    "BRIDGE Sidequest Battle",
    "VOYAGE Sidequest Battle",
    "HORROR Sidequest Battle",
    "END Sidequest Battle",
    "Recruit Beowulf",
    "Recruit Worker 8",
    "Recruit Reis (Dragon)",
    "Recruit Reis (Human)",
    "Recruit Cloud",
    "Recruit Byblos"
]

rare_battle_locations = [
    "Manalia Plains Rare Battle",
    "Sweegy Woods Rare Battle",
    "Lenalia Plateau Rare Battle",
    "Grog Hill Rare Battle",
    "Yuguo Woods Rare Battle",
    "Fovoham Plains Rare Battle",
    "Araguay Woods Rare Battle",
    "Zirekile Falls Rare Battle",
    "Zeklaus Desert Rare Battle",
    "Bervenia Volvano Rare Battle",
    "Doguola Pass Rare Battle",
    "Bariaus Hill Rare Battle",
    "Zigolis Swamp Rare Battle",
    "Bariaus Valley Rare Battle",
    "Finath River Rare Battle",
    "Germinas Peak Rare Battle",
    "Bed Desert Rare Battle",
    "Dolbodar Swamp Rare Battle",
    "Poeskas Lake Rare Battle",
    "Deep Dungeon Rare Battle"
]

job_unlock_locations = [
    "Squire Unlock",
    "Chemist Unlock",
    "Knight Unlock",
    "Archer Unlock",
    "Thief Unlock",
    "Monk Unlock",
    "Priest Unlock",
    "Wizard Unlock",
    "Time Mage Unlock",
    "Summoner Unlock",
    "Oracle Unlock",
    "Mediator Unlock",
    "Geomancer Unlock",
    "Lancer Unlock",
    "Samurai Unlock",
    "Ninja Unlock",
    "Calculator Unlock",
    "Bard Unlock",
    "Dancer Unlock",
    "Mime Unlock"
]

shop_unlock_locations = [
    "Mandalia Plains Shop Unlock",
    "Lenalia Plateau Shop Unlock",
    "Fort Zeakden Shop Unlock",
    "Yardow Fort City Shop Unlock",
    "Riovanes Castle Shop Unlock",
    "Zirekile Falls Shop Unlock",
    "Zeklaus Desert Shop Unlock",
    "Lesalia Imperial Capital Shop Unlock",
    "Bariaus Hill Shop Unlock",
    "Lionel Castle Shop Unlock",
    "Bariaus Valley Shop Unlock",
    "Bethla Garrison Shop Unlock",
    "Limberry Castle Shop Unlock",
    "Orbonne Monastery Shop Unlock"
]

default_murond_fights = [
    "Murond Death City Story Battle",
    "Lost Sacred Precincts Story Battle",
    "Graveyard of Airships 1 Story Battle"
]

monster_location_names = [f"Poach {monster.monster_name.value}" for monster in monster_locations]