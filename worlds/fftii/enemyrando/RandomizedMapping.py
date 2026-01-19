from .Abilities import ActionAbility, ReactionAbility, SupportAbility, MovementAbility
from .Birthday import Month
from .Items import Items
from .RandomizedUnits import RandomizedUnit
from .SourceUnit import SourceUnit
from .SpriteSet import SpriteSet
from .Job import Job, UnlockedJob
from worlds.fftii.patchersuite.Unit import UnitGender


class RandomizedMapping:
    source_unit: SourceUnit
    destination_unit: Job
    battle_level: int = 0

    def __init__(self, source_unit: SourceUnit = None, destination_unit: Job = None):
        self.source_unit = source_unit
        self.destination_unit = destination_unit

    def to_json(self):
        return {
            "SourceUnit": self.source_unit.to_json(),
            "DestinationUnit": self.destination_unit,
            "BattleLevel": self.battle_level
        }

    @classmethod
    def from_json(cls, json_data) -> "RandomizedMapping":
        source_unit = SourceUnit(
            SpriteSet(json_data["SourceUnit"]["SpriteSet"]),
            Job(json_data["SourceUnit"]["Job"]),
            UnitGender(json_data["SourceUnit"]["Gender"])
        )
        new_mapping = RandomizedMapping(source_unit, Job(json_data["DestinationUnit"]))
        new_mapping.battle_level = json_data["BattleLevel"]
        return new_mapping

    def __repr__(self):
        return f"{self.source_unit} -- {Job(self.destination_unit).name}"