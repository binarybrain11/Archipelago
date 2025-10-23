cd_name_location = 0x9304
cd_name = "SCUS_942.21"

world_bin_start = 0x0BD00408

rom_name_location = 0x0BD6A136
seed_hash_location = 0x0BD6A134

rom_name_location_in_ram = 0x13C2AE
rom_name_length = 20
seed_hash_location_in_ram = 0x13C2AC
seed_hash_length = 2

seed_hash_in_memory_card = 0x0578CC

items_received_low = 0x578CE
items_received_high = 0x578CF
items_obtained_size = 2

world_loaded_address = 0x0E0228
world_loaded_length = 4
world_loaded_value = [0x27, 0xBD, 0xFF, 0xE8]

inventory_start_address = 0x0596E0
shop_progression_address = 0x0578D8

war_funds_address = 0x0577CC
war_funds_length = 4

zodiac_stones_1_address = 0x057974
zodiac_stones_2_address = 0x057975

stones_lookup = {
    "Aries": (zodiac_stones_1_address, 3),
    "Taurus": (zodiac_stones_1_address, 4),
    "Gemini": (zodiac_stones_1_address, 5),
    "Cancer": (zodiac_stones_1_address, 6),
    "Leo": (zodiac_stones_1_address, 7),
    "Virgo": (zodiac_stones_2_address, 0),
    "Libra": (zodiac_stones_2_address, 1),
    "Scorpio": (zodiac_stones_2_address, 2),
    "Sagittarius": (zodiac_stones_2_address, 3),
    "Capricorn": (zodiac_stones_2_address, 4),
    "Aquarius": (zodiac_stones_2_address, 5),
    "Pisces": (zodiac_stones_2_address, 6),
    "Serpentarius": (zodiac_stones_2_address, 7),
}

unit_stats_address = 0x057F74
unit_stat_size = 0x100
unit_count = 16
unit_stats_length = unit_stat_size * unit_count
party_id_offset = 0x01
jp_offset = 0x6E
job_amount = 20

event_flags_location = 0x05791C
event_flags_length = 0x224



story_addresses = {
    "Gariland Magic City Story Battle": 0x94,
    "Mandalia Plains Story Battle": 0x95,
    "Igros Castle Story Battle": 0x96,
    "Sweegy Woods Story Battle": 0x97,
    "Dorter Slums Story Battle": 0x98,
    "Dorter City Story Battle": 0x99,
    "Thieves' Fort Story Battle": 0x9A,
    "Lenalia Plateau Story Battle": 0x9B,
    "Fort Zeakden Story Battle": 0x9C,
    "Grog Hill Story Battle": 0x9D,
    "Yardow Fort City Story Battle": 0x9E,
    "Yuguo Woods Story Battle": 0x9F,
    "Gate of Riovanes Story Battle": 0xA0,
    "Inside Riovanes Castle Story Battle": 0xA1,
    "Roof of Riovanes Castle Story Battle": 0xA2,
    "Fovoham Plains Story Battle": 0xA3,
    "Araguay Woods Story Battle": 0xA4,
    "Zirekile Falls Story Battle": 0xA5,
    "Zeklaus Desert Story Battle": 0xA6,
    "Back Gate of Lesalia Castle Story Battle": 0xA7,
    "Goland Coal City Story Battle": 0xA8,
    "Doguola Pass Story Battle": 0xA9,
    "Zaland Fort City Story Battle": 0xAA,
    "Bariaus Hill Story Battle": 0xAB,
    "Gate of Lionel Castle Story Battle": 0xAC,
    "Inside of Lionel Castle Story Battle": 0xAD,
    "Zigolis Swamp Story Battle": 0xAE,
    "Golgorand Execution Site Story Battle": 0xAF,
    "Bariaus Valley Story Battle": 0xB0,
    "Bervenia Free City Story Battle": 0xB1,
    "Finath River Story Battle": 0xB2,
    "Zeltennia Castle Story Battle": 0xB3,
    "Germinas Peak Story Battle": 0xB4,
    "Bethla Garrison North Wall Story Battle": 0xB6,
    "Bethla Garrison South Wall Story Battle": 0xB6,
    "Bethla Garrison Sluice Story Battle": 0xB7,
    "Bed Desert Story Battle": 0xB8,
    "Limberry Castle Gates Story Battle": 0xB9,
    "Inside Limberry Castle Story Battle": 0xBa,
    "Limberry Castle Cemetary Story Battle": 0xBB,
    "Poeskas Lake Story Battle": 0xBC,
    "St. Murond Temple Story Battle": 0xBD,
    "St. Murond Temple Hall Story Battle": 0xBE,
    "Chapel of St. Murond Temple Story Battle": 0xBF,
    "Underground Book Storage 1 Story Battle": 0xC0,
    "Underground Book Storage 2 Story Battle": 0xC1,
    "Underground Book Storage 3 Story Battle": 0xC2,
    "Underground Book Storage 4 Story Battle": 0xC3,
    "Underground Book Storage 5 Story Battle": 0xC4,
    "Slums of Goug Story Battle": 0xC5,
    "Murond Death City Story Battle": 0xC6,
    "Lost Sacred Precincts Story Battle": 0xC7,
    "Graveyard of Airships 1 Story Battle": 0xC8,
    "Graveyard of Airships 2 Story Battle": 0xC9
}

sidequest_addresses = {
    "Goland Colliery Third Floor Sidequest Battle": 0xDC,
    "Goland Colliery Second Floor Sidequest Battle": 0xDD,
    "Goland Colliery First Floor Sidequest Battle": 0xDE,
    "Goland Underground Passage Sidequest Battle": 0xDF,
    "Nelveska Temple Sidequest Battle": 0xE0,
    "Zarghidas Trade City Sidequest Battle": 0xE1,
    "NOGIAS Sidequest Battle": 0xE2,
    "TERMINATE Sidequest Battle": 0xE3,
    "DELTA Sidequest Battle": 0xE4,
    "VALKYRIES Sidequest Battle": 0xE5,
    "MLAPAN Sidequest Battle": 0xE6,
    "TIGER Sidequest Battle": 0xE7,
    "BRIDGE Sidequest Battle": 0xE8,
    "VOYAGE Sidequest Battle": 0xE9,
    "HORROR Sidequest Battle": 0xEA,
    "END Sidequest Battle": 0xEB,
}

rare_battle_addresses = {
    "Manalia Plains Rare Battle": 0x11C,
    "Sweegy Woods Rare Battle": 0xCA,
    "Lenalia Plateau Rare Battle": 0xCB,
    "Grog Hill Rare Battle": 0xCC,
    "Yuguo Woods Rare Battle": 0xCD,
    "Fovoham Plains Rare Battle": 0xCe,
    "Araguay Woods Rare Battle": 0xCF,
    "Zirekile Falls Rare Battle": 0xD0,
    "Zeklaus Desert Rare Battle": 0xD1,
    "Bervenia Volvano Rare Battle": 0xD2,
    "Doguola Pass Rare Battle": 0xD3,
    "Bariaus Hill Rare Battle": 0xD4,
    "Zigolis Swamp Rare Battle": 0xD5,
    "Bariaus Valley Rare Battle": 0xD6,
    "Finath River Rare Battle": 0xD7,
    "Germinas Peak Rare Battle": 0xD8,
    "Bed Desert Rare Battle": 0xD9,
    "Dolbodar Swamp Rare Battle": 0xDA,
    "Poeskas Lake Rare Battle": 0xDB
}
# shouldn't need these but noting just in case
shop_unlock_addresses = {
    "Mandalia Plains Shop Unlock": 0xEC,
    "Lenalia Plateau Shop Unlock": 0xED,
    "Fort Zeakden Shop Unlock": 0xEE,
    "Yardow Fort City Shop Unlock": 0xEF,
    "Riovanes Castle Shop Unlock": 0xF0,
    "Zirekile Falls Shop Unlock": 0xF1,
    "Zeklaus Desert Shop Unlock": 0xF2,
    "Lesalia Imperial Capital Shop Unlock": 0xF3,
    "Bariaus Hill Shop Unlock": 0xF4,
    "Lionel Castle Shop Unlock": 0xF5,
    "Bariaus Valley Shop Unlock": 0xF6,
    "Bethla Garrison Shop Unlock": 0xF7,
    "Limberry Castle Shop Unlock": 0xF8,
    "Orbonne Monastery Shop Unlock": 0xF9
}

# These are set when the character is received
character_recruit_addresses = {
    "Rafa": 0xFA,
    "Malak": 0xFB,
    "Boco": 0xFC,
    "Beowulf": 0xFD,
    "Worker 8": 0xFE,
    "Agrias": 0xFF,
    "Reis (Dragon)": 0x100,
    "Reis (Human)": 0x101,
    "Cloud": 0x102,
    "Orlandu": 0x103,
    "Meliadoul": 0x104,
    "Mustadio": 0x105,
    "Byblos": 0x106,
    "Rad": 0x107,
    "Lavian": 0x108,
    "Alicia": 0x109
}

# These are set when the unlock is received.
ramza_job_unlock_addresses = {
    "Chapter 2 Ramza Squire Job Unlock": 0x11A,
    "Chapter 4 Ramza Squire Job Unlock": 0x11B
}

# These are set on client connect.
yaml_options = {
    "Sidequests": 0x18F
}

# This is written to be the client to unlock jobs
available_jobs_addresses = {
    "Time Mage": 0x190,
    "Wizard": 0x191,
    "Priest": 0x192,
    "Monk": 0x193,
    "Archer": 0x194,
    "Knight": 0x195,
    "Chemist": 0x196,
    "Squire": 0x197,
    "Ninja": 0x198,
    "Samurai": 0x199,
    "Lancer": 0x19A,
    "Geomancer": 0x19B,
    "Oracle": 0x19C,
    "Mediator": 0x19D,
    "Thief": 0x19E,
    "Summoner": 0x19F,
    "Mime": 0x1A4,
    "Dancer": 0x1A5,
    "Bard": 0x1A6
}

locations_to_read = {
    **story_addresses, **sidequest_addresses, **rare_battle_addresses
}

for location, flag in locations_to_read.items():
    locations_to_read[location] = flag - 0x80


for location, flag in available_jobs_addresses.items():
    available_jobs_addresses[location] = flag - 0x80

for location, flag in character_recruit_addresses.items():
    character_recruit_addresses[location] = flag - 0x80

for location, flag in ramza_job_unlock_addresses.items():
    ramza_job_unlock_addresses[location] = flag - 0x80

all_main_bits = {
    **story_addresses, **sidequest_addresses, **shop_unlock_addresses, **character_recruit_addresses,
    **ramza_job_unlock_addresses, **yaml_options, **available_jobs_addresses
}

for location, flag in all_main_bits.items():
    all_main_bits[location] = flag - 0x80

poaching_flags_location = 0x0578C4
poaching_flags_length = 8

poaching_addresses = {
    "Poach Yellow Chocobo": 0x00,
    "Poach Black Chocobo": 0x01,
    "Poach Red Chocobo": 0x02,
    "Poach Goblin": 0x03,
    "Poach Black Goblin": 0x04,
    "Poach Gobbledeguck": 0x05,
    "Poach Bomb": 0x06,
    "Poach Grenade": 0x07,
    "Poach Explosive": 0x08,
    "Poach Red Panther": 0x09,
    "Poach Cuar": 0x0A,
    "Poach Vampire": 0x0B,
    "Poach Pisco Demon": 0x0C,
    "Poach Squidlarkin": 0x0D,
    "Poach Mindflare": 0x0E,
    "Poach Skeleton": 0x0F,
    "Poach Bone Snatch": 0x10,
    "Poach Living Bone": 0x11,
    "Poach Ghoul": 0x12,
    "Poach Gust": 0x13,
    "Poach Revnant": 0x14,
    "Poach Floatiball": 0x15,
    "Poach Ahriman": 0x16,
    "Poach Plague": 0x17,
    "Poach Juravis": 0x18,
    "Poach Steel Hawk": 0x19,
    "Poach Cocatoris": 0x1A,
    "Poach Uribo": 0x1B,
    "Poach Porky": 0x1C,
    "Poach Wildbow": 0x1D,
    "Poach Woodman": 0x1E,
    "Poach Trent": 0x1F,
    "Poach Taiju": 0x20,
    "Poach Bull Demon": 0x21,
    "Poach Minitaurus": 0x22,
    "Poach Sacred": 0x23,
    "Poach Morbol": 0x24,
    "Poach Ochu": 0x25,
    "Poach Great Morbul": 0x26,
    "Poach Behemoth": 0x27,
    "Poach King Behemoth": 0x28,
    "Poach Dark Behemoth": 0x29,
    "Poach Dragon": 0x2A,
    "Poach Blue Dragon": 0x2B,
    "Poach Red Dragon": 0x2C,
    "Poach Hyudra": 0x2D,
    "Poach Hydra": 0x2E,
    "Poach Tiamat": 0x2F,
}
job_level_offset = 0x64
job_level_order = [
    "Squire",
    "Chemist",
    "Knight",
    "Archer",
    "Monk",
    "Priest",
    "Wizard",
    "Time Mage",
    "Summoner",
    "Thief",
    "Mediator",
    "Oracle",
    "Geomancer",
    "Lancer",
    "Samurai",
    "Ninja",
    "Calculator",
    "Bard",
    "Dancer",
    "Mime"
]