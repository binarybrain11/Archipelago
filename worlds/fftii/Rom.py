import json
import logging
import os
import tempfile
import typing
import Utils
from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin, APPatchExtension

def get_base_rom_as_bytes() -> bytes:
    with open(get_settings().metroidfusion_options.rom_file, "rb") as infile:
        base_rom_bytes = bytes(Utils.read_snes_rom(infile))
    return base_rom_bytes


class FinalFantasyTacticsIIPatchExtension(APPatchExtension):
    game = "Final Fantasy Tactics Ivalice Island"

    @staticmethod
    def patch_iso(caller, iso, placement_file):
        pass


class FinalFantasyTacticsIIProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Final Fantasy Tactics Ivalice Island"
    hash = "27D02A4F03E172E029C9B82AC3DB79F7"
    patch_file_ending = ".apfftii"
    result_file_ending = ".iso"

    procedure = [
        ("patch_iso", ["patch_file.json"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_as_bytes()

