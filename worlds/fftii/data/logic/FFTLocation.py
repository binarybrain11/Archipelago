from .Requirement import Requirement


class FFTLocation:
    name: str
    requirements: list[Requirement]
    battle_level: int

    def __init__(self, name, requirements: list[Requirement] = None, battle_level: int = 0):
        if requirements is None:
            requirements = list()
        self.name = name
        self.requirements = requirements
        self.battle_level = battle_level
