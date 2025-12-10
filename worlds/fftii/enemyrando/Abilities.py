from enum import Enum, unique


@unique
class ActionAbility(Enum):
    JOB = 0xFF
    RANDOM = 0xFE

    GUTS_C4 = 0x1B
    IZLUDE_JUMP = 0x34
    SWORD_SPIRIT = 0x3E
    BLOOD_SUCK = 0x3F
    HOLY_MAGIC = 0x4C
    VELIUS_FEAR = 0x67
    WARLOCK_SUMMON = 0x68
    ZALERA_FEAR = 0x6B
    JA_MAGIC = 0x6C
    HASHMALUM_FEAR = 0x6F
    DIMENSION_MAGIC = 0x70
    QUEKLAIN_FEAR = 0x73
    IMPURE = 0x74
    ADRAMELK_FEAR = 0x77
    ALL_MAGIC = 0x78
    ULTIMATE_MAGIC = 0x7B
    CHAOS = 0x7C
    COMPLETE_MAGIC = 0x7D
    SATURATION = 0x7E

@unique
class ReactionAbility(Enum):
    RANDOM = 0x01FE
    COUNTER = 0x01BA
    BLADE_GRASP = 0x01C3

@unique
class SupportAbility(Enum):
    RANDOM = 0x01FE
    MAINTENANCE = 0x01DB

@unique
class MovementAbility(Enum):
    RANDOM = 0x01FE