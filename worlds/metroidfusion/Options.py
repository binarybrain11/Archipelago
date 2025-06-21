from dataclasses import dataclass

from Options import (Toggle, Range, Choice, PerGameCommonOptions, DefaultOnToggle, StartInventoryPool, OptionGroup,
                     OptionSet, Visibility)

class InfantMetroidsInPool(Range):
    """How many Infant Metroids will be in the item pool."""
    display_name = "Infant Metroids in Pool"
    range_start = 1
    range_end = 20
    default = 5

class InfantMetroidsRequired(Range):
    """How many Infant Metroids will be required to beat the game.
    If set to more than the number in the pool, will instead become however many are present."""
    display_name = "Infant Metroids Required"
    range_start = 1
    range_end = 20
    default = 5

class PaletteRandomization(Toggle):
    """Randomize the ingame palettes."""
    display_name = "Palette Randomization"

class EnableHints(DefaultOnToggle):
    """Enable ingame hints at Navigation Stations."""
    display_name = "Enable Hints"


@dataclass
class MetroidFusionOptions(PerGameCommonOptions):
    InfantMetroidsInPool: InfantMetroidsInPool
    InfantMetroidsRequired: InfantMetroidsRequired
    PaletteRandomization: PaletteRandomization
    EnableHints: EnableHints
