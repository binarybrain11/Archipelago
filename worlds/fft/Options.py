from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, OptionGroup


# Main Options
class ZodiacStonesInPool(Range):
    """How many Zodiac Stones will be in the item pool."""
    display_name = "Zodiac Stones in Pool"
    range_start = 1
    range_end = 13
    default = 6

class ZodiacStonesRequired(Range):
    """How many Zodiac Stones will be required to beat the game.
    If set to more than the number in the pool, will instead become however many are present."""
    display_name = "Zodiac Stones Required"
    range_start = 1
    range_end = 13
    default = 6

@dataclass
class FinalFantasyTacticsOptions(PerGameCommonOptions):
    ZodiacStonesInPool: ZodiacStonesInPool
    ZodiacStonesRequired: ZodiacStonesRequired

fft_option_groups = [
    OptionGroup("Main Options", [
        ZodiacStonesInPool,
        ZodiacStonesRequired
    ])
]