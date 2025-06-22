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

class RevealHiddenBlocks(DefaultOnToggle):
    """Enables whether destructible blocks are revealed from the start."""
    display_name = "Reveal Hidden Blocks"

class FastDoorTransitions(DefaultOnToggle):
    """Enables fast door transitions between rooms."""
    display_name = "Fast Door Transitions"

class MissileDataAmmo(Range):
    """The amount of missiles provided by a Missile Data item."""
    display_name = "Missile Data Ammo"
    range_start = 5
    range_end = 100
    default = 10

class PowerBombDataAmmo(Range):
    """The amount of power bombs provided by a Power Bomb Data item."""
    display_name = "Power Bomb Data Ammo"
    range_start = 5
    range_end = 100
    default = 10

class MissileTankAmmo(Range):
    """The amount of missiles provided by a Missile Tank item."""
    display_name = "Missile Tank Ammo"
    range_start = 0
    range_end = 100
    default = 5

class PowerBombTankAmmo(Range):
    """The amount of power bombs provided by a Power Bomb Tank item."""
    display_name = "Power Bomb Tank Ammo"
    range_start = 0
    range_end = 100
    default = 2

@dataclass
class MetroidFusionOptions(PerGameCommonOptions):
    InfantMetroidsInPool: InfantMetroidsInPool
    InfantMetroidsRequired: InfantMetroidsRequired
    PaletteRandomization: PaletteRandomization
    EnableHints: EnableHints
    RevealHiddenBlocks: RevealHiddenBlocks
    FastDoorTransitions: FastDoorTransitions
    MissileDataAmmo: MissileDataAmmo
    MissileTankAmmo: MissileTankAmmo
    PowerBombDataAmmo: PowerBombDataAmmo
    PowerBombTankAmmo: PowerBombTankAmmo
