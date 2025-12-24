from .logic.FFTLocation import LocationNames

cd_name_location = 0x9304
cd_name = "SCUS_942.21"

world_bin_start = 0x0BD00408

rom_name_location = 0x00028CC0
volume_name_location = 0x00009340
seed_hash_location = 0x0BD6A136

rom_name_location_in_ram = 0x027058
rom_name_length = 20
seed_hash_location_in_ram = 0x13C2AE
seed_hash_length = 2

seed_hash_in_memory_card = 0x0578CE

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

# These could have been with the event flags but I wrote them first so here they are in this format.
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

temp_unit_stats_address = 0x1C8638
temp_unit_stat_size = 0x128
temp_unit_count = 16
temp_unit_stats_length = temp_unit_stat_size * temp_unit_count
temp_party_id_offset = 0x01
temp_jp_offset = 0xBE
temp_job_amount = 20

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
    "Bethla Garrison North Wall Story Battle": 0xB5,
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
    "Mandalia Plains Rare Battle": 0x11C,
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

# These are set during patching
yaml_options = {
    "RareBattles": (0x00348931, 0x04),
    "Sidequests": (0x00348931, 0x02),
    "FinalBattles": (0x00348931, 0x01),
    "EXPMultiplier": 0x35565C,
    "JPMultiplier": 0x355670
}

# This is written to the client to unlock jobs
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
    "Bard": 0x1A6,
    "Calculator": 0x1A7
}

locations_to_read = {
    **story_addresses, **sidequest_addresses, **rare_battle_addresses
}

# We offset a bunch of flags by 0x80 because the bitflag offset starts later than the flag bits do
# as the first set of flags correspond to words, not bits...but we want the flag numbers to match our notes

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
    **ramza_job_unlock_addresses, **available_jobs_addresses
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
    "Poach Great Morbol": 0x26,
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

pass_paths = {
    "Gallione Pass": {
        "Fovoham Pass": [
            0x231 - 0x80, # Lenalia <> Fovoham
            0x232 - 0x80  # Fovoham <> Zeakden
        ],
        "Lesalia Pass": [
            0x236 - 0x80, # Dorter <> Zeklaus
            0x240 - 0x80  # Dorter <> Araguay
        ],
        "Murond Pass": [
            0x23F - 0x80, # Dorter <> Orbonne
            0x25A - 0x80  # Gariland <> Murond Temple
        ]
    },
    "Fovoham Pass": {
        "Lesalia Pass": [
            0x234 - 0x80, # Riovanes <> Bervenia Volcano
            0x23C - 0x80  # Grog <> Lesalia
        ],
        "Zeltennia Pass": [
            0x246 - 0x80, # Grog <> Doguola
        ]
    },
    "Lesalia Pass": {
        "Lionel Pass": [
            0x250 - 0x80  # Zirekile <> Zaland
        ],
        "Limberry Pass": [
            0x242 - 0x80  # Zirekile <> Bethla
        ]
    },
    "Lionel Pass": {
        "Murond Pass": [
            0x258 - 0x80, # Goug <> Zigolis
            0x255 - 0x80  # Warjilis <> Deep Dungeon
        ]
    },
    "Zeltennia Pass": {
        "Limberry Pass": [
            0x244 - 0x80, # Bervenia City <> Bed
            0x24C - 0x80  # Germinas <> Poeskas
        ]
    },
}

finale_path = 0x25B - 0x80 # Formerly Goug <> Warjilis, now Deep Dungeon <> Murond Death City
game_started_flag_address = 0x18E - 0x80


victory_text_offsets = {
    LocationNames.GARILAND_STORY.value: 0x86D5A0,
    LocationNames.MANDALIA_STORY.value: [
        0x88439F, 0x886A26
    ],
    LocationNames.IGROS_STORY.value: 0xC44725,
    LocationNames.SWEEGY_STORY.value: 0x89B335,
    LocationNames.DORTER_1_STORY.value: 0x8A45F8,
    LocationNames.DORTER_2_STORY.value: 0x965739,
    LocationNames.THIEVES_FORT_STORY.value: 0x8C48B3,
    LocationNames.LENALIA_STORY.value: 0x8EBADE,
    LocationNames.ZEAKDEN_STORY.value: 0x91BD3A,

    LocationNames.GROG_STORY.value: 0xAA24B9,
    LocationNames.YARDOW_STORY.value: 0xAB95A0,
    LocationNames.YUGUO_STORY.value: 0xAC4BF2,
    LocationNames.RIOVANES_1_STORY.value: 0xAD7348,
    LocationNames.RIOVANES_2_STORY.value: 0xAE7335,
    LocationNames.RIOVANES_3_STORY.value: 0xAF5168,
    LocationNames.FOVOHAM_STORY.value: 0x8FE378,

    LocationNames.ARAGUAY_STORY.value: 0x9757C8,
    LocationNames.ZIREKILE_STORY.value: 0x98A0F8,
    LocationNames.ZEKLAUS_STORY.value: 0x8AFDF8,
    LocationNames.LESALIA_STORY.value: 0xA5FAF0,
    LocationNames.GOLAND_STORY.value: 0xA2D238,

    LocationNames.ZALAND_STORY.value: 0x99EC0A,
    LocationNames.BARIAUS_HILL_STORY.value: 0x9AEE89,
    LocationNames.LIONEL_1_STORY.value: 0xA11976,
    LocationNames.LIONEL_2_STORY.value: 0xA1ADD8,
    LocationNames.ZIGOLIS_STORY.value: 0x9C82E0,
    LocationNames.GOLGORAND_STORY.value: 0xA01828,
    LocationNames.BARIAUS_VALLEY_STORY.value: 0x9ECF1C,

    LocationNames.DOGUOLA_STORY.value: 0xB50D78,
    LocationNames.BERVENIA_CITY_STORY.value: 0xB5EBAA,
    LocationNames.FINATH_STORY.value: 0xB65838,
    LocationNames.ZELTENNIA_STORY.value: 0xB759A8,
    LocationNames.GERMINAS_STORY.value: 0xBB8338,

    LocationNames.BETHLA_NORTH_STORY.value: 0xB95C31,
    LocationNames.BETHLA_SOUTH_STORY.value: 0xB8EDF1,
    LocationNames.BETHLA_SLUICE_STORY.value: [
        0xBA3894, 0xBA8214
    ],
    LocationNames.BED_STORY.value: 0xB8364D,
    LocationNames.LIMBERRY_1_STORY.value: 0xBCAAE3,
    LocationNames.LIMBERRY_2_STORY.value: 0xBDAC70,
    LocationNames.LIMBERRY_3_STORY.value: 0xBE6275,
    LocationNames.POESKAS_STORY.value: 0xBBF178,

    LocationNames.MUROND_TEMPLE_1_STORY.value: 0xC4FCE3,
    LocationNames.MUROND_TEMPLE_2_STORY.value: 0xC5B4C6,
    LocationNames.MUROND_TEMPLE_3_STORY.value: 0xC66E1C,
    LocationNames.UBS_1_STORY.value: 0xA8920B,
    LocationNames.UBS_2_STORY.value: 0xA6FC46,
    LocationNames.UBS_3_STORY.value: 0xA7B599,
    LocationNames.UBS_4_STORY.value: 0xB09C48,
    LocationNames.UBS_5_STORY.value: 0xB12F5E,
    LocationNames.GOUG_STORY.value: 0x9D3922,
    LocationNames.MUROND_DEATH_CITY_STORY.value: 0xB209FB,
    LocationNames.PRECINCTS_STORY.value: 0xB29E56,
    LocationNames.AIRSHIPS_1_STORY.value: 0xB331FD,
    LocationNames.AIRSHIPS_2_STORY.value: 0xB3C2D6,

    LocationNames.GOLAND_1_SIDEQUEST.value: 0xC89378,
    LocationNames.GOLAND_2_SIDEQUEST.value: 0xC901B8,
    LocationNames.GOLAND_3_SIDEQUEST.value: 0xC96FF8,
    LocationNames.GOLAND_4_SIDEQUEST.value: 0xCA27B8,
    LocationNames.NELVESKA_SIDEQUEST.value: 0xCB05DA,
    LocationNames.ZARGHIDAS_SIDEQUEST.value: 0xA4FC25,

    LocationNames.END_SIDEQUEST.value: 0x9553FB,

}

rare_battles_offset = 0x871478
dd_battles_offset = 0x929978

total_jp_boon_gained = 0x057930
total_jp_boon_gained_length = 2

STORY_LOCATIONS = "StoryLocations"
RARE_BATTLE = "RareBattle"
SIDEQUEST_LOCATIONS = "SidequestLocations"
ALTIMA_ONLY_STORY_LOCATIONS = "AltimaOnlyStoryLocations"
ADDRESS = "Address"

location_dot_info = {
    "Gariland": {
        STORY_LOCATIONS: [
            LocationNames.GARILAND_STORY
        ],
        ADDRESS: (0x057959, 0x20)
    },
    "Mandalia": {
        STORY_LOCATIONS: [
            LocationNames.MANDALIA_STORY,
            LocationNames.MANDALIA_SHOP
        ],
        RARE_BATTLE: LocationNames.MANDALIA_RARE,
        ADDRESS: (0x05795B, 0x80)
    },
    "Igros": {
        STORY_LOCATIONS: [
            LocationNames.IGROS_STORY
        ],
        ADDRESS: (0x057959, 0x02)
    },
    "Sweegy": {
        STORY_LOCATIONS: [
            LocationNames.SWEEGY_STORY
        ],
        RARE_BATTLE: LocationNames.SWEEGY_RARE,
        ADDRESS: (0x05795C, 0x02)
    },
    "Dorter": {
        STORY_LOCATIONS: [
            LocationNames.DORTER_1_STORY,
            LocationNames.DORTER_2_STORY
        ],
        ADDRESS: (0x05795A, 0x01)
    },
    "ThievesFort": {
        STORY_LOCATIONS: [
            LocationNames.THIEVES_FORT_STORY
        ],
        ADDRESS: (0x05795B, 0x01)
    },
    "Lenalia": {
        STORY_LOCATIONS: [
            LocationNames.LENALIA_STORY,
            LocationNames.LENALIA_SHOP
        ],
        RARE_BATTLE: LocationNames.LENALIA_RARE,
        ADDRESS: (0x05795C, 0x10)
    },
    "Zeakden": {
        STORY_LOCATIONS: [
            LocationNames.ZEAKDEN_STORY,
            LocationNames.ZEAKDEN_SHOP,
            LocationNames.RAMZA_CHAPTER_2_UNLOCK,
            LocationNames.RAD_RECRUIT,
            LocationNames.ALICIA_RECRUIT,
            LocationNames.LAVIAN_RECRUIT
        ],
        ADDRESS: (0x05795A, 0x40)
    },
    "Fovoham": {
        STORY_LOCATIONS: [
            LocationNames.FOVOHAM_STORY
        ],
        RARE_BATTLE: LocationNames.FOVOHAM_RARE,
        ADDRESS: (0x05795C, 0x01)
    },
    "Riovanes": {
        STORY_LOCATIONS: [
            LocationNames.RIOVANES_1_STORY,
            LocationNames.RIOVANES_2_STORY,
            LocationNames.RIOVANES_3_STORY,
            LocationNames.RIOVANES_SHOP,
            LocationNames.RAMZA_CHAPTER_4_UNLOCK,
            LocationNames.RAFA_RECRUIT,
            LocationNames.MALAK_RECRUIT
        ],
        ADDRESS: (0x057959, 0x01)
    },
    "Yuguo": {
        STORY_LOCATIONS: [
            LocationNames.YUGUO_STORY
        ],
        RARE_BATTLE: LocationNames.YUGUO_RARE,
        ADDRESS: (0x05795C, 0x40)
    },
    "Yardow": {
        STORY_LOCATIONS: [
            LocationNames.YARDOW_STORY,
            LocationNames.YARDOW_SHOP
        ],
        ADDRESS: (0x057959, 0x40)
    },
    "Grog": {
        STORY_LOCATIONS: [
            LocationNames.GROG_STORY
        ],
        RARE_BATTLE: LocationNames.GROG_RARE,
        ADDRESS: (0x05795D, 0x01)
    },
    "Zeklaus": {
        STORY_LOCATIONS: [
            LocationNames.ZEKLAUS_STORY,
            LocationNames.ZEKLAUS_SHOP
        ],
        RARE_BATTLE: LocationNames.ZEKLAUS_RARE,
        ADDRESS: (0x05795C, 0x08)
    },
    "Araguay": {
        STORY_LOCATIONS: [
            LocationNames.ARAGUAY_STORY,
            LocationNames.BOCO_RECRUIT
        ],
        RARE_BATTLE: LocationNames.ARAGUAY_RARE,
        ADDRESS: (0x05795C, 0x80)
    },
    "Zirekile": {
        STORY_LOCATIONS: [
            LocationNames.ZIREKILE_STORY,
            LocationNames.ZIREKILE_SHOP
        ],
        RARE_BATTLE: LocationNames.ZIREKILE_RARE,
        ADDRESS: (0x05795D, 0x04)
    },
    "Goland": {
        STORY_LOCATIONS: [
            LocationNames.GOLAND_STORY
        ],
        SIDEQUEST_LOCATIONS: [
            LocationNames.GOLAND_1_SIDEQUEST,
            LocationNames.GOLAND_2_SIDEQUEST,
            LocationNames.GOLAND_3_SIDEQUEST,
            LocationNames.GOLAND_4_SIDEQUEST,
            LocationNames.BEOWULF_RECRUIT,
            LocationNames.REIS_DRAGON_RECRUIT,
            LocationNames.WORKER_8_RECRUIT
        ],
        ADDRESS: (0x057959, 0x80)
    },
    "Lesalia": {
        STORY_LOCATIONS: [
            LocationNames.LESALIA_STORY,
            LocationNames.LESALIA_SHOP
        ],
        ADDRESS: (0x057958, 0x80)
    },
    "BerveniaVolcano": {
        STORY_LOCATIONS: [],
        RARE_BATTLE: LocationNames.BERVENIA_VOLCANO_RARE,
        ADDRESS: (0x05795C, 0x04)
    },
    "Zaland": {
        STORY_LOCATIONS: [
            LocationNames.ZALAND_STORY
        ],
        ADDRESS: (0x05795A, 0x02)
    },
    "BariausHill": {
        STORY_LOCATIONS: [
            LocationNames.BARIAUS_HILL_STORY,
            LocationNames.BARIAUS_HILL_SHOP
        ],
        RARE_BATTLE: LocationNames.BARIAUS_HILL_RARE,
        ADDRESS: (0x05795D, 0x10)
    },
    "Lionel": {
        STORY_LOCATIONS: [
            LocationNames.LIONEL_1_STORY,
            LocationNames.LIONEL_2_STORY,
            LocationNames.LIONEL_SHOP
        ],
        ADDRESS: (0x057959, 0x04)
    },
    "Zigolis": {
        STORY_LOCATIONS: [
            LocationNames.ZIGOLIS_STORY
        ],
        RARE_BATTLE: LocationNames.ZIGOLIS_RARE,
        ADDRESS: (0x05795C, 0x20)
    },
    "BariausValley": {
        STORY_LOCATIONS: [
            LocationNames.BARIAUS_VALLEY_STORY,
            LocationNames.BARIAUS_VALLEY_SHOP,
            LocationNames.AGRIAS_RECRUIT
        ],
        RARE_BATTLE: LocationNames.BARIAUS_VALLEY_RARE,
        ADDRESS: (0x05795D, 0x40)
    },
    "Golgorand": {
        STORY_LOCATIONS: [
            LocationNames.GOLGORAND_STORY
        ],
        ADDRESS: (0x05795B, 0x04)
    },
    "Doguola": {
        STORY_LOCATIONS: [
            LocationNames.DOGUOLA_STORY
        ],
        RARE_BATTLE: LocationNames.DOGUOLA_RARE,
        ADDRESS: (0x05795D, 0x20)
    },
    "BerveniaCity": {
        STORY_LOCATIONS: [
            LocationNames.BERVENIA_CITY_STORY
        ],
        ADDRESS: (0x05795A, 0x10)
    },
    "Finath": {
        STORY_LOCATIONS: [
            LocationNames.FINATH_STORY
        ],
        RARE_BATTLE: LocationNames.FINATH_RARE,
        ADDRESS: (0x05795D, 0x80)
    },
    "Zeltennia": {
        STORY_LOCATIONS: [
            LocationNames.ZELTENNIA_STORY
        ],
        ADDRESS: (0x057959, 0x10)
    },
    "Nelveska": {
        STORY_LOCATIONS: [],
        SIDEQUEST_LOCATIONS: [
            LocationNames.NELVESKA_SIDEQUEST,
            LocationNames.REIS_HUMAN_RECRUIT
        ],
        ADDRESS: (0x05795B, 0x40)
    },
    "Zarghidas": {
        STORY_LOCATIONS: [],
        SIDEQUEST_LOCATIONS: [
            LocationNames.ZARGHIDAS_SIDEQUEST,
            LocationNames.CLOUD_RECRUIT
        ],
        ADDRESS: (0x05795A, 0x20)
    },
    "Germinas": {
        STORY_LOCATIONS: [
            LocationNames.GERMINAS_STORY
        ],
        RARE_BATTLE: LocationNames.GERMINAS_RARE,
        ADDRESS: (0x05795E, 0x02)
    },
    "Poeskas": {
        STORY_LOCATIONS: [
            LocationNames.POESKAS_STORY
        ],
        RARE_BATTLE: LocationNames.POESKAS_RARE,
        ADDRESS: (0x05795E, 0x01)
    },
    "Limberry": {
        STORY_LOCATIONS: [
            LocationNames.LIMBERRY_1_STORY,
            LocationNames.LIMBERRY_2_STORY,
            LocationNames.LIMBERRY_3_STORY,
            LocationNames.LIMBERRY_SHOP,
            LocationNames.MELIADOUL_RECRUIT
        ],
        ADDRESS: (0x057959, 0x08)
    },
    "Dolbodar": {
        STORY_LOCATIONS: [],
        RARE_BATTLE: LocationNames.DOLBODAR_RARE,
        ADDRESS: (0x05795D, 0x08)
    },
    "Bethla": {
        STORY_LOCATIONS: [
            LocationNames.BETHLA_NORTH_STORY,
            LocationNames.BETHLA_SOUTH_STORY,
            LocationNames.BETHLA_SLUICE_STORY,
            LocationNames.BETHLA_SHOP,
            LocationNames.ORLANDU_RECRUIT
        ],
        ADDRESS: (0x05795B, 0x10)
    },
    "Bed": {
        STORY_LOCATIONS: [
            LocationNames.BED_STORY
        ],
        RARE_BATTLE: LocationNames.BED_RARE,
        ADDRESS: (0x05795D, 0x02)
    },
    "Orbonne": {
        STORY_LOCATIONS: [
            LocationNames.UBS_2_STORY,
            LocationNames.UBS_3_STORY,
            LocationNames.UBS_1_STORY,
            LocationNames.ORBONNE_SHOP
        ],
        ALTIMA_ONLY_STORY_LOCATIONS: [
            LocationNames.UBS_4_STORY,
            LocationNames.UBS_5_STORY,
            LocationNames.MUROND_DEATH_CITY_STORY,
            LocationNames.PRECINCTS_STORY,
            LocationNames.AIRSHIPS_1_STORY
        ],
        ADDRESS: (0x05795B, 0x02)
    },
    "Goug": {
        STORY_LOCATIONS: [
            LocationNames.GOUG_STORY,
            LocationNames.MUSTADIO_RECRUIT
        ],
        ADDRESS: (0x05795A, 0x04)
    },
    "MurondTemple": {
        STORY_LOCATIONS: [
            LocationNames.MUROND_TEMPLE_1_STORY,
            LocationNames.MUROND_TEMPLE_2_STORY,
            LocationNames.MUROND_TEMPLE_3_STORY,
        ],
        ADDRESS: (0x05795A, 0x80)
    },
    "DeepDungeon": {
        STORY_LOCATIONS: [],
        SIDEQUEST_LOCATIONS: [
            LocationNames.NOGIAS_SIDEQUEST,
            LocationNames.TERMINATE_SIDEQUEST,
            LocationNames.DELTA_SIDEQUEST,
            LocationNames.VALKYRIES_SIDEQUEST,
            LocationNames.MLAPAN_SIDEQUEST,
            LocationNames.TIGER_SIDEQUEST,
            LocationNames.BRIDGE_SIDEQUEST,
            LocationNames.VOYAGE_SIDEQUEST,
            LocationNames.HORROR_SIDEQUEST,
            LocationNames.END_SIDEQUEST,
            LocationNames.BYBLOS_RECRUIT
        ],
        ADDRESS: (0x05795B, 0x20)
    },
    "MurondDeathCity": {
        STORY_LOCATIONS: [
            LocationNames.AIRSHIPS_2_STORY
        ],
        ADDRESS: (0x05795B, 0x08)
    }
}