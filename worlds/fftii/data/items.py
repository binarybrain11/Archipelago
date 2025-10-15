zodiac_stone_names = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo ",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Serpentarius",
]

world_map_pass_names = [
    "Gallione Pass", "Lesalia Pass", "Fovoham Pass", "Lionel Pass", "Zeltennia Pass", "Limberry Pass", "Murond Pass"
]

job_names = [
    "Squire", "Chemist", "Knight", "Archer", "Monk", "Thief", "Lancer", "Geomancer", "Samurai", "Ninja", "Dancer",
    "Priest", "Wizard", "Oracle", "Time Mage", "Mediator", "Summoner", "Calculator", "Bard", "Mime"
]

shop_levels = []

for i in range(14):
    shop_levels.append("Progressive Shop Level")

major_item_names = [
    *zodiac_stone_names, *world_map_pass_names, *job_names, "Progressive Shop Level", "Progressive Ramza Job Form"
]

ramza_job_levels = [
    "Progressive Ramza Job Form", "Progressive Ramza Job Form"
]


special_character_names = [
    "Boco", "Agrias", "Mustadio", "Rafa",
    "Malak", "Beowulf", "Reis", "Orlandu",
    "Worker 8", "Cloud", "Meliadoul", "Byblos"
]

rare_item_names = [
    "Rare Item"
]

useful_item_names = [
    "Useful Item"
]

filler_item_names = [
    "Filler Item"
]

all_item_names = [
    *major_item_names, *special_character_names, *job_names, *rare_item_names, *useful_item_names, *filler_item_names
]
