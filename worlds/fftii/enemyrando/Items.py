from enum import Enum, unique


@unique
class Items(Enum):
    NONE = 0xFF
    RANDOM = 0xFE

    EXCALIBUR = 0x23