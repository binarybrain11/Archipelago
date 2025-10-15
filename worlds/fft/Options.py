from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, OptionGroup, StartInventoryPool


# Main Options
class ZodiacStonesInPool(Range):
    """How many Zodiac Stones will be in the item pool.
    If set to less than the number required, will instead become however many are required."""
    display_name = "Zodiac Stones in Pool"
    range_start = 1
    range_end = 13
    default = 6

class ZodiacStonesRequired(Range):
    """How many Zodiac Stones will be required to beat the game."""
    display_name = "Zodiac Stones Required"
    range_start = 1
    range_end = 13
    default = 6

@dataclass
class FinalFantasyTacticsOptions(PerGameCommonOptions):
    ZodiacStonesInPool: ZodiacStonesInPool
    ZodiacStonesRequired: ZodiacStonesRequired
    start_inventory_from_pool: StartInventoryPool

fft_option_groups = [
    OptionGroup("Main Options", [
        ZodiacStonesInPool,
        ZodiacStonesRequired
    ])
]