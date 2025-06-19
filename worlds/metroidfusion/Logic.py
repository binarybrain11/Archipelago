from copy import copy
from typing import Callable

from BaseClasses import CollectionState
from .data.locations import Requirement


class LogicObject():
    requirements: list[list[str]] = []
    energy_tanks: int = 0
    player: int

    def __init__(self, player: int):
        self.player = player

    def logic_rule(self, state: CollectionState) -> bool:
        if len(self.requirements) == 0:
            return True
        expression = None
        for requirement_list in self.requirements:
            if expression is None:
                expression = state.has_all(requirement_list, self.player)
            else:
                expression = expression or state.has_all(requirement_list, self.player)
        if self.energy_tanks > 0:
            expression = bool(expression) and state.has("Energy Tank", self.player, self.energy_tanks)
        return expression



def create_logic_rule_for_list(requirements: list[Requirement]) -> tuple[list, int]:
    expression = None
    energy_tanks = 0
    requirements_list = []
    for requirement in requirements:
        new_rule = create_logic_rule(requirement)
        energy_tanks += new_rule[1]
        for requirement2 in new_rule[0]:
            requirements_list.append(requirement2)
        continue
    return requirements_list, energy_tanks

def create_logic_rule(requirement: Requirement) -> tuple[list, int]:
    requirements_list = []
    energy_tanks_needed = unpack_requirement(requirement, requirements_list, [])
    return requirements_list, energy_tanks_needed

def create_logic_rule_for_list2(requirements: list[Requirement], player: int) -> Callable:
    expression = None
    energy_tanks = 0
    for requirement in requirements:
        new_rule = create_logic_rule2(requirement, player)
        energy_tanks += new_rule[1]
        if expression is None:
            expression = new_rule[0]
        else:
            expression = expression or new_rule[0]
    if expression is None:
        expression = lambda state: True
    if energy_tanks > 0:
        expression = lambda state: expression# and state.has("Energy Tank", player, energy_tanks)
    return expression

def create_logic_rule2(requirement: Requirement, player: int) -> tuple[Callable, int, list]:
    requirements_list = []
    energy_tanks_needed = unpack_requirement(requirement, requirements_list, [])
    expression = None
    for option in requirements_list:
        new_rule = lambda state: state.has_all(option, player)
        if expression is None:
            expression = new_rule
        else:
            expression = expression or new_rule
    if expression is None:
        expression = lambda state: True
    return expression, energy_tanks_needed, requirements_list

item_names = [
    "Level 0 Keycard",
    "Missile Data",
    "Morph Ball",
    "Charge Beam",
    "Level 1 Keycard",
    "Bomb Data",
    "Hi-Jump",
    "Speed Booster",
    "Level 2 Keycard",
    "Super Missile",
    "Varia Suit",
    "Level 3 Keycard",
    "Ice Missile",
    "Wide Beam",
    "Power Bomb Data",
    "Space Jump",
    "Plasma Beam",
    "Gravity Suit",
    "Level 4 Keycard",
    "Diffusion Missile",
    "Wave Beam",
    "Screw Attack",
    "Ice Beam",
    "Missile Tank",
    "Energy Tank",
    "Power Bomb Tank",
    "Ice Trap",
    "Infant Metroid",
    "Nothing"
]

def unpack_requirement(requirement: Requirement, possibilities: list[list[str]], parent_items: list[str]) -> int:
    energy_tanks = 0
    if len(requirement.other_requirements) > 0:
        for nested_requirement in requirement.other_requirements:
            current_parent_items = copy(parent_items)
            parent_items.extend(requirement.items_needed)
            energy_tanks += unpack_requirement(nested_requirement, possibilities, parent_items)
            parent_items = copy(current_parent_items)
    elif len(requirement.items_needed) > 0:
        items_needed = copy(requirement.items_needed)
        for item_needed in items_needed:
            assert item_needed in item_names
        items_needed.extend(parent_items)
        possibilities.append(items_needed)
    energy_tanks += requirement.energy_tanks_needed
    return energy_tanks