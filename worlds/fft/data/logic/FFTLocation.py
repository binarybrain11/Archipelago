from .Requirement import Requirement


class FFTLocation:
    name: str
    requirements: list[Requirement]

    def __init__(self, name, requirements=None):
        if requirements is None:
            requirements = list()
        self.name = name
        self.requirements = requirements
