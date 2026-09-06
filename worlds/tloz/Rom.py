import hashlib
import json
import zlib
import os
from pkgutil import get_data
import warnings

import bsdiff4

import Utils
from BaseClasses import ItemClassification
from worlds.Files import APDeltaPatch, APProcedurePatch, APTokenMixin, APPatchExtension

NA10CHECKSUM = '337bd6f1a1163df31bf2633665589ab0'
rom_name_location = 0x00
rom_name_length = 0x20
header_length = 0x10
player_name_location = 0x20
player_name_length = 0x40
major_offsets_location = 0x60
deathlink_options = 0x80
bit_positions = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
candle_shop = bit_positions[4]
arrow_shop = bit_positions[3]
potion_shop = bit_positions[2]
shield_shop = bit_positions[5]
ring_shop = bit_positions[6]
take_any = bit_positions[1]
left_shop_slots = 0x0628
middle_shop_slots = 0x0629
right_shop_slots = 0x062A
take_any_caves_checked = 0x0678
first_quest_dungeon_items_early = 0x18910
first_quest_dungeon_items_late = 0x18C10
game_mode = 0x12
fill_hearts = 0x63
death_mode_counter = 0xE5
items_obtained_low = 0x0677
items_obtained_high = 0x067B
sword = 0x0657
bombs = 0x0658
max_bombs = 0x067C
arrow = 0x0659
bow = 0x065A
candle = 0x065B
recorder = 0x065C
food = 0x065D
potion = 0x065E
magical_rod = 0x065F
raft = 0x0660
book_of_magic = 0x0661
ring = 0x0662
stepladder = 0x0663
magical_key = 0x0664
power_bracelet = 0x0665
letter = 0x0666
clock = 0x066C
keys = 0x066E
heart_containers = 0x066F
partial_hearts = 0x0670
triforce_fragments = 0x0671
triforce_count = 0x0679
boomerang = 0x0674
magical_boomerang = 0x0675
magical_shield = 0x0676
rupees_to_add = 0x067D

item_to_lift = 0x0505
item_lift_timer = 0x0506
sound_effect_queue = 0x0602


overworld_status_block = 0x067F
underworld_early_status_block = 0x06FF
underworld_late_status_block = 0x077F

cave_type_flags = {
    "Starting Sword Cave": 0b01000000,
    "Take Any Item": 0b01000100,
    "Door Repair": 0b01011100,
    "Potion Shop": 0b01101000,
    "Level 9": 0b00100100,
    "White Sword Pond": 0b01001000,
    "Level 5": 0b00010100,
    "Candle Shop": 0b01111000,
    "Letter Cave": 0b01100000,
    "Secret Money Large": 0b10001000,
    "Money Making Game": 0b01011000,
    "Shield Shop": 0b01111100,
    "Secret Money Medium": 0b10000100,
    "Go Up The Mountain Hint": 0b01101100,
    "Secret Is In Tree Hint": 0b01010100,
    "Warp Cave": 0b01010000,
    "Magical Sword Grave": 0b01001100,
    "Level 6": 0b00011000,
    "Arrow Shop": 0b01110100,
    "Blue Ring Shop": 0b10000000,
    "Level 2": 0b00001000,
    "Level 7": 0b00011100,
    "Level 4": 0b00010000,
    "Secret Money Small": 0b10001100,
    "Level 8": 0b00100000,
    "Lost Woods Hint": 0b01110000,
    "Level 3": 0b00001100,
    "Old Man Grave Hint": 0b01100100,
    "Level 1": 0b00000100
}

warp_cave_offset = 0x19344
starting_sword_cave_location_byte = 0x70
white_sword_pond_location_byte = 0x71
magical_sword_grave_location_byte = 0x72
letter_cave_location_byte = 0x73

shop_correspondance = {
    "Arrow Shop": arrow_shop,
    "Candle Shop": candle_shop,
    "Blue Ring Shop": ring_shop,
    "Shield Shop": shield_shop,
    "Potion Shop": potion_shop
}

item_frame_table_offset = 0x71A7
item_palette_table_offset = 0x6BD7
map_item_slot = 0x11
item_tiles_offset = 0x808F
compass_tile_offset = 0x6A0
archipelago_sprite = [ 0x03, 0x07, 0x3f, 0x7f, 0xff, 0xff, 0xc6, 0x00, 0x00, 0x00, 0x38, 0x7c, 0xfe, 0xfe, 0xfe, 0x7c, 0x00, 0x03, 0x07, 0x0f, 0x0f, 0x0f, 0x07, 0x03, 0xfe, 0xfc, 0xf8, 0x70, 0x30, 0x00, 0x00, 0x00 ]

string_table_index_offset = 0x4010
string_table_end = 0x45B2 
hint_offsets = (
    0x00,  # __IT'S DANGEROUS TO GO____ALONE! TAKE THIS.
    0x02,  # __MASTER USING IT AND___YOU CAN HAVE THIS.
    0x04,  # _TAKE ANY ROAD YOU WANT.
    0x06,  # _SECRET IS IN THE TREE____AT THE DEAD-END.
    0x08,  # ___LET'S PLAY MONEY___MAKING GAME.
    0x0A,  # __PAY ME FOR THE DOOR_____REPAIR CHARGE.
    0x0C,  # ____SHOW THIS TO THE_______OLD WOMAN.
    0x0E,  # ____MEET THE OLD MAN______AT THE GRAVE.
    0x10,  # __BUY MEDICINE BEFORE__YOU GO.
    0x12,  # __PAY ME AND I'LL TALK.
    0x14,  # ___THIS AIN'T ENOUGH________TO TALK.
    0x16,  # _______GO UP,UP,___THE MOUNTAIN AHEAD.
    0x18,  # __GO NORTH,WEST,SOUTH,__WEST TO THE FOREST  OF MAZE.
    0x1A,  # ____BOY, YOU'RE RICH!
    0x1C,  # _BUY SOMETHIN' WILL YA!
    0x1E,  # _____BOY, THIS IS___REALLY EXPENSIVE!
    0x20,  # _TAKE ANY ONE YOU WANT.
    0x22,  # _____IT'S A SECRET_____TO EVERYBODY.
    0x24,  # ___GRUMBLE,GRUMBLE...
    0x26,  # __EASTMOST PENNINSULA_____IS THE SECRET.
    0x28,  # _DODONGO DISLIKES SMOKE.
    0x2A,  # _DID YOU GET THE SWORD_FROM THE OLD MAN ON_TOP OF THE WATERFALL?
    0x2C,  # _____WALK INTO THE_______WATERFALL.
    0x2E,  # __SECRET POWER IS SAID___TO BE IN THE ARROW.
    0x30,  # ____DIGDOGGER HATES_CERTAIN KIND OF SOUND.
    0x32,  # ____I BET YOU'D LIKE___TO HAVE MORE BOMBS.
    0x34,  # ____IF YOU GO IN THE_DIRECTION OF THE ARROW.
    0x36,  # ____LEAVE YOUR LIFE_______OR MONEY.
    0x38,  # _THERE ARE SECRETS WHERE___FAIRIES DON'T LIVE.
    0x3A,  # ____AIM AT THE EYES_______OF GOHMA.
    0x3C,  # __SOUTH OF ARROW MARK____HIDES A SECRET.
    0x3E,  # __THERE'S A SECRET IN__THE TIP OF THE NOSE.
    0x40,  # ___SPECTACLE ROCK IS__AN ENTRANCE TO DEATH.
    0x42,  # 10TH ENEMY HAS THE BOMB.
    0x44,  # _ONES WHO DOES NOT HAVE_TRIFORCE CAN'T GO IN.
    0x46,  # ___PATRA HAS THE MAP.
    0x48,  # __GO TO THE NEXT ROOM.
    0x4A   # _____EYES OF SKULL_____HAS A SECRET.
)


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path()
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if NA10CHECKSUM != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for NA (1.0) release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    from worlds.tloz import TLoZWorld
    return TLoZWorld.settings.rom_file

class TLOZPatchExtension(APPatchExtension):
    game = "The Legend of Zelda"

    @staticmethod
    def apply_base_patch(rom):
        # The base patch source is on a different repo, so here's the summary of changes:
        # Remove Triforce check for recorder, so you can always warp.
        # Remove level check for Triforce Fragments (and maps and compasses, but this won't matter)
        # Replace some code with a jump to free space
        # Check if we're picking up a Triforce Fragment. If so, increment the local count
        # In either case, we do the instructions we overwrote with the jump and then return to normal flow
        # Remove map/compass check so they're always on
        # Removing a bit from the boss roars flags, so we can have more dungeon items. This allows us to
        # go past 0x1F items for dungeon items.
        base_patch = get_data(__name__, "z1_base_patch.bsdiff4")
        rom_data = bsdiff4.patch(rom.read(), base_patch)
        rom_data = bytearray(rom_data)
        # Set every item to the new nothing value, but keep room flags. Type 2 boss roars should
        # become type 1 boss roars, so we at least keep the sound of roaring where it should be.
        for i in range(0, 0x7F):
            item = rom_data[first_quest_dungeon_items_early + i]
            if item & 0b00100000:
                item = item & 0b11011111
                item = item | 0b01000000
                rom_data[first_quest_dungeon_items_early + i] = item
            if item & 0b00011111 == 0b00000011:  # Change all Item 03s to Item 3F, the proper "nothing"
                rom_data[first_quest_dungeon_items_early + i] = item | 0b00111111

            item = rom_data[first_quest_dungeon_items_late + i]
            if item & 0b00100000:
                item = item & 0b11011111
                item = item | 0b01000000
                rom_data[first_quest_dungeon_items_late + i] = item
            if item & 0b00011111 == 0b00000011:
                rom_data[first_quest_dungeon_items_late + i] = item | 0b00111111

        # Make the map item use the same sprite as the compass 
        rom_data[item_frame_table_offset + map_item_slot] = 0x18 
        # Change the palette to blue for non-progression items
        rom_data[item_palette_table_offset + map_item_slot] = 0x01
        for i in range(len(archipelago_sprite)):
            rom_data[item_tiles_offset + compass_tile_offset + i] = archipelago_sprite[i]

        return rom_data

    @staticmethod
    def write_entrances(rom_data, entrance_randomizer_set):
        from worlds.tloz import cave_data_location_start
        warp_caves = []
        for entrance, data in entrance_randomizer_set.items():
            entrance_offset = int(entrance[7:], 16)
            entrance_name = data
            entrance_flag = cave_type_flags[entrance_name]
            original_data = rom_data[cave_data_location_start + entrance_offset]
            original_data = original_data & 0b00000011
            new_data = entrance_flag | original_data
            rom_data[cave_data_location_start + entrance_offset] = new_data
            if entrance_name == "Warp Cave":
                warp_caves.append(entrance_offset)
            if entrance_name == "Starting Sword Cave":
                rom_data[starting_sword_cave_location_byte] = entrance_offset
            if entrance_name == "White Sword Pond":
                rom_data[white_sword_pond_location_byte] = entrance_offset
            if entrance_name == "Magical Sword Grave":
                rom_data[magical_sword_grave_location_byte] = entrance_offset
            if entrance_name == "Letter Cave":
                rom_data[letter_cave_location_byte] = entrance_offset
        for i, cave in enumerate(warp_caves):
            rom_data[warp_cave_offset + i] = cave
            print(hex(cave))
        return rom_data

    @staticmethod
    def apply_randomizer(caller, rom, placement_file):
        from worlds.tloz import (shop_price_location_ids, shop_locations, item_game_ids, location_ids,
                                 item_prices, secret_money_ids)
        placements: dict[str, any] = json.loads(caller.get_file(placement_file))
        with open(get_base_rom_path(), 'rb') as rom:
            rom_data = TLOZPatchExtension.apply_base_patch(rom)
            rom_data = TLOZPatchExtension.write_entrances(rom_data, placements["entrance_randomizer_set"])
        rom_name = bytearray(placements["meta"]["rom_name"][:rom_name_length], "utf8")[:rom_name_length]
        rom_name.extend([0] * (rom_name_length - len(rom_name)))
        rom_data[rom_name_location + header_length:rom_name_location + header_length + rom_name_length] = rom_name
        player_name = bytearray(placements["meta"]["player_name"], 'utf8')[:player_name_length]
        player_name.extend([0] * (player_name_length - len(player_name)))
        rom_data[player_name_location + header_length:player_name_location + header_length + player_name_length] = player_name
        rom_data[deathlink_options + header_length] = placements["meta"]["death_link"]

        # Write each location's new data in
        for location, item in placements.items():
            # Zelda and Ganon aren't real locations. Neither is the metadata.
            if location == "Ganon" or location == "Zelda" or location == "entrance_randomizer_set" or location == "meta":
                continue

            if "Secret Money" in location:
                rom_data[secret_money_ids[location]] = item
                continue

            if "Classification" in location:
                continue

            # Neither are boss defeat events
            if "Status" in location:
                continue
            item_id = item_game_ids[item]
            location_id = location_ids[location]

            # Shop prices need to be set
            if location in shop_locations:
                if location[-5:] == "Right":
                    # Final item in stores has bit 6 and 7 set. It's what marks the cave a shop.
                    item_id = item_id | 0b11000000
                price_location = shop_price_location_ids[location]
                rom_data[price_location] = item_prices[item]
            if location == "Take Any Item Right":
                # Same story as above: bit 6 is what makes this a Take Any cave
                item_id = item_id | 0b01000000
            rom_data[location_id] = item_id

        # string_table = TLOZPatchExtension.read_string_table(rom_data)
        # string_table[0] = TLOZPatchExtension.string_to_bytes("Hello World")
        # TLOZPatchExtension.write_string_table(rom_data, string_table)

        return rom_data

    # Converts a Python string to a ROM-encoded string
    @staticmethod
    def string_to_bytes(string):
        res = []
        char_byte_table = {
            '0': 0x00, '1': 0x01, '2': 0x02, '3': 0x03, '4': 0x04, '5': 0x05, '6': 0x06, '7': 0x07, '8': 0x08, '9': 0x09,
            'a': 0x0A, 'b': 0x0B, 'c': 0x0C, 'd': 0x0D, 'e': 0x0E, 'f': 0x0F, 'g': 0x10, 'h': 0x11, 'i': 0x12, 'j': 0x13, 'k': 0x14, 'l': 0x15, 'm': 0x16, 'n': 0x17, 'o': 0x18, 'p': 0x19, 'q': 0x1A, 'r': 0x1B, 's': 0x1C, 't': 0x1D, 'u': 0x1E, 'v': 0x1F, 'w': 0x20, 'x': 0x21, 'y': 0x22, 'z': 0x23,
            ' ': 0x24,
            # '~': 0x25, # This is actually a spacing character, not a tilde
            ',': 0x28, '!': 0x29, '\'': 0x2A, '&': 0x2B,
            '.': 0x2C, '"': 0x2D, '?': 0x2E, '-': 0x2F
        }
        for char in string.lower():
            byte = char_byte_table.get(char)
            if None != byte:
                res.append(byte)
        return res

        #byte += 0x80 # Next character should appear on the second line
        #byte += 0x40 # Next character should appear on the third line
        #byte += 0xC0 # End of string
        # lines of text are 24 characters wide before they careen into the background

    # Returns a list of ROM-encoded strings from the string table
    @staticmethod
    def read_string_table(rom_data):
        string_table_offset = string_table_index_offset + 0x4C
        res = []
        cur_str = []
        for offset in range(string_table_end - string_table_offset):
            cur_str.append(rom_data[string_table_offset + offset])
            if (cur_str[-1] & 0xC0 == 0xC0):
                res.append(cur_str)
                print(cur_str)
                cur_str = []
        return res

    # Writes a list of ROM-encoded strings to the string table
    @staticmethod
    def write_string_table(rom_data, string_table):
        string_table_offset = string_table_index_offset + 0x4C
        # Ensure there are fewer strings than entries in the table
        assert len(string_table) <= ( 0x4C >> 1 ), "Attempting to write too many strings to the string table! {} <= {}".format(len(string_table), 0x4C >> 1)
        # Ensure the string table we're trying to write can fit
        assert sum(len(s) for s in string_table) < (string_table_end - string_table_offset), "Attempting to write a string table that's too large! {} <= {}".format(sum(len(s) for s in string_table), (string_table_end - string_table_offset))

        string_write_offset = string_table_offset
        for string_num, string in enumerate(string_table):
            # The ROM pointer needs to be translated to the in-memory pointer. This bank starts at 0x4010 and is translated to 0x8000 (it's a
            # coincidence here that the string table is at the beginning of the bank, therefore the 0x4010 literal)
            memory_string_offset = string_write_offset - 0x4010 + 0x8000
            rom_data[string_table_index_offset + string_num * 2] = memory_string_offset & 0xFF
            rom_data[string_table_index_offset + string_num * 2 + 1] = (memory_string_offset >> 8) & 0xFF
            for char in string:
                rom_data[string_write_offset] = char
                string_write_offset += 1

                # If we ever try to write past the string table, STOP
                # immediately and warn. Stopping here prevents us from
                # corrupting the rest of the game, just the text will be funky
                if string_write_offset >= string_table_end:
                    # Ensure the string is terminated
                    rom_data[string_write_offset - 1] |= 0xC0
                    warnings.warn("Attempted to write past the string table!")
                    return

            # Ensure the string is terminated
            rom_data[string_write_offset - 1] |= 0xC0

class TLOZProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "The Legend of Zelda"
    hash = NA10CHECKSUM
    patch_file_ending = ".aptloz"
    result_file_ending = ".nes"

    procedure = [
        ("apply_randomizer", ["placement_file.json"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
