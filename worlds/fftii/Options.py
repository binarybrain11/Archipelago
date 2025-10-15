from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, OptionGroup, StartInventoryPool, DefaultOnToggle, Toggle


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

class SidequestBattlesInLocationPool(DefaultOnToggle):
    """Are sidequest battles (Colliery, Nelveska, Zarghidas, Deep Dungeon) in the pool of locations?"""
    display_name = "Sidequest Battle in Location Pool"

class JobUnlocksInLocationPool(DefaultOnToggle):
    """Are job unlocks part of the pool of locations?"""
    display_name = "Job Unlocks in Location Pool"

class RareBattlesInLocationPool(Toggle):
    """Are the rare battles for each battleground in the location pool?"""
    display_name = "Rare Battles in Location Pool"

class JobUnlocksInItemPool(DefaultOnToggle):
    """Are job unlocks part of the pool of items? If disabled, jobs are unlocked normally."""
    display_name = "Job Unlocks in Item Pool"

@dataclass
class FinalFantasyTacticsIIOptions(PerGameCommonOptions):
    zodiac_stones_in_pool: ZodiacStonesInPool
    zodiac_stones_required: ZodiacStonesRequired
    sidequest_battles_in_location_pool: SidequestBattlesInLocationPool
    job_unlocks_in_location_pool: JobUnlocksInLocationPool
    rare_battles_in_location_pool: RareBattlesInLocationPool
    job_unlocks_in_item_pool: JobUnlocksInItemPool
    start_inventory_from_pool: StartInventoryPool

fftii_option_groups = [
    OptionGroup("Main Options", [
        ZodiacStonesInPool,
        ZodiacStonesRequired,
        SidequestBattlesInLocationPool,
        JobUnlocksInLocationPool,
        RareBattlesInLocationPool,
        JobUnlocksInItemPool
    ])
]