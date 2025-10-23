import json
import logging
import os
import pkgutil
import tempfile
import typing
from pathlib import Path

import bsdiff4

import Utils
from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APPatchExtension
from worlds.fftii.ErrorRecalc import ErrorRecalculator
from worlds.fftii.data import memory


def get_base_rom_as_bytes() -> bytes:
    with open(get_settings().fftii_options.rom_file, "rb") as infile:
        base_rom_bytes = bytes(Utils.read_snes_rom(infile))
    return base_rom_bytes


class FinalFantasyTacticsIIPatchExtension(APPatchExtension):
    game = "Final Fantasy Tactics Ivalice Island"

    @staticmethod
    def patch_bin(caller, iso, placement_file):
        patch_dict = json.loads(caller.get_file(placement_file))
        base_patch = pkgutil.get_data(__name__, "fftii.bsdiff4")
        rom_data = bsdiff4.patch(iso, base_patch)
        rom_data = bytearray(rom_data)
        rom_name_text = patch_dict["RomName"]
        rom_name = bytearray(rom_name_text, 'utf-8')
        rom_name.extend([0] * (20 - len(rom_name)))
        rom_data[memory.rom_name_location:memory.rom_name_location + 20] = bytes(rom_name[:20])
        seed_hash = int(patch_dict["SeedHash"])
        print(hex(seed_hash))
        seed_hash_bytes = seed_hash.to_bytes(2)
        rom_data[memory.seed_hash_location:memory.seed_hash_location + 2] = bytes(seed_hash_bytes)

        return rom_data


class FinalFantasyTacticsIIProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Final Fantasy Tactics Ivalice Island"
    hash = "b156ba386436d20fd5ed8d37bab6b624"
    patch_file_ending = ".apfftii"
    result_file_ending = ".cue"

    procedure = [
        ("patch_bin", ["patch_file.json"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_as_bytes()

    def patch(self, target: str) -> None:
        file_name = target[:-4]
        if os.path.exists(file_name + ".cue"):
            os.unlink(file_name + ".cue")
        if os.path.exists(file_name + ".bin"):
            os.unlink(file_name + ".bin")

        super().patch(target)
        os.rename(target, file_name + ".bin")
        error_recalculator = ErrorRecalculator(calculate_form_2_edc=False)
        stats = error_recalculator.recalc(target_file=Path(file_name + ".bin"),
                                          base_file=get_settings().fftii_options.rom_file)
        print(
            f"{stats.identical_sectors} identical sectors out of {stats.total_sectors()}, {stats.recalc_sectors} sectors recalculated")
        print(f"{stats.edc_blocks_computed} EDC blocks computed, {stats.ecc_blocks_generated} ECC blocks generated")

        cue_text = f'FILE "{file_name}.bin" BINARY\n  TRACK 01 MODE2/2352\n    INDEX 01 00:00:00'
        with open(file_name + ".cue", "w") as cue_file:
            cue_file.write(cue_text)