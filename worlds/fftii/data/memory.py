cd_name_location = 0x9304
cd_name = "SCUS_942.21"

rom_name_location = 0x0BDD0F30
seed_hash_location = 0x0BDD0F60

items_received_low = 0x57B18
items_received_high = 0x57B19
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