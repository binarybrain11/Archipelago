from dataclasses import dataclass

from Options import Range, PerGameCommonOptions, OptionGroup, StartInventoryPool, DefaultOnToggle, Toggle, Choice


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

class ZodiacStoneLocations(Choice):
    """Where can Zodiac Stones appear?
    Vanilla limits their possible locations to those events which had one in the vanilla game. Note that this limits
    the number of stones in the pool to 11, with sidequests on, and 8 without.
    Anywhere Local means stones can be at any location in your world.
    Anywhere means stones can be anywhere in the multiworld."""
    display_name = "Zodiac Stone Locations"
    option_vanilla_stones = 0
    option_anywhere_local = 1
    option_anywhere = 2
    default = 0

class FinalBattles(Choice):
    """What the final goal is.
    Vanilla requires the completion of all six final battles in sequence at Murond Death City.
    Altima Only requires only Altima at Murond Death City, and the other endgame battles will be located at Orbonne."""
    display_name = "Final Battles"
    option_vanilla = 0
    option_altima_only = 1
    default = 0

class SidequestBattles(DefaultOnToggle):
    """Are sidequest battles (Colliery, Nelveska, Zarghidas, Deep Dungeon) in the pool of locations?"""
    display_name = "Sidequest Battles"

class JobUnlocks(DefaultOnToggle):
    """Are job unlocks in the item and location pools?"""
    display_name = "Job Unlocks"

class RareBattles(Toggle):
    """Are the rare battles for each battleground in the location pool?"""
    display_name = "Rare Battles"

class PoachLocations(Toggle):
    """Are poaches in the location pool? WARNING: Can be grindy and RNG-heavy."""
    display_name = "Poach Locations"

class NormalItemWeight(Range):
    """Weight of items normally sold in shops in the filler pool."""
    display_name = "Normal Item Weight"
    range_start = 0
    range_end = 10
    default = 3

class RareItemWeight(Range):
    """Weight of items not normally sold in shops in the filler pool."""
    display_name = "Rare Item Weight"
    range_start = 0
    range_end = 10
    default = 1

class BonusGilItemWeight(Range):
    """Weight of bonus items in the filler pool."""
    display_name = "Bonus Gil Item Weight"
    range_start = 0
    range_end = 10
    default = 2

class JPBoonItemWeight(Range):
    """Weight of JP Boon items that award JP to the team in the filler pool"""
    display_name = "JP Boon Item Weight"
    range_start = 0
    range_end = 10
    default = 1

class BonusGilItemSize(Choice):
    """Adjusts the value of bonus gil items in the pool.
    Normal is 1000/5000/10000. Frugal halves that, Expensive doubles."""
    display_name = "Bonus Gil Item Size"
    option_frugal = 0
    option_normal = 1
    option_valuable = 2
    default = 1

class JPBoonSize(Choice):
    """Adjusts the value of JP Boon items. Normal is 100/200/500 JP. Frugal halves that, Expensive doubles."""
    display_name = "JP Boon Item Size"
    option_frugal = 0
    option_normal = 1
    option_valuable = 2
    default = 1

class StartingRegion(Choice):
    """What region to start in. Gallione is easiest, followed by Lesalia and Lionel. Fovoham, Zeltennia, and Limberry
    should only be chosen if you're looking for a challenge."""
    display_name = "Starting Region"
    option_gallione = 0
    option_lesalia = 1
    option_lionel = 2
    option_fovoham = 3
    option_zeltennia = 4
    option_limberry = 5
    default = 0

class CharactersJoinWithEquipment(Toggle):
    """Do characters come with their vanilla equipment?"""
    display_name = "Characters Join with Equipment"

class JPGainMultiplier(Choice):
    """Multiplier to in-battle JP gains."""
    option_normal = 0
    option_double = 1
    option_triple = 2
    default = 1

@dataclass
class FinalFantasyTacticsIIOptions(PerGameCommonOptions):
    zodiac_stones_in_pool: ZodiacStonesInPool
    zodiac_stones_required: ZodiacStonesRequired
    zodiac_stone_locations: ZodiacStoneLocations
    final_battles: FinalBattles
    sidequest_battles: SidequestBattles
    job_unlocks: JobUnlocks
    rare_battles: RareBattles
    poach_locations: PoachLocations
    normal_item_weight: NormalItemWeight
    rare_item_weight: RareItemWeight
    bonus_gil_item_weight: BonusGilItemWeight
    jp_boon_item_weight: JPBoonItemWeight
    bonus_gil_item_size: BonusGilItemSize
    jp_boon_size: JPBoonSize
    characters_join_with_equipment: CharactersJoinWithEquipment
    jp_gain_multiplier: JPGainMultiplier
    start_inventory_from_pool: StartInventoryPool

fftii_option_groups = [
    OptionGroup("Main Options", [
        ZodiacStonesInPool,
        ZodiacStonesRequired,
        ZodiacStoneLocations,
        FinalBattles,
        SidequestBattles,
        JobUnlocks,
        PoachLocations,
        RareBattles,
    ]),
    OptionGroup("Filler Options", [
        NormalItemWeight,
        RareItemWeight,
        BonusGilItemWeight,
        JPBoonItemWeight,
        BonusGilItemSize,
        JPBoonSize
    ]),
    OptionGroup("QOL Options", [
        CharactersJoinWithEquipment,
        JPGainMultiplier
    ])
]