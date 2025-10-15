from copy import copy
from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from .data.logic.Requirement import Requirement
from .Items import valid_item_names

if TYPE_CHECKING:
    from worlds.fft import FinalFantasyTacticsOptions

class LogicObject:
    requirements: list[list[str]] = []
    energy_tanks: list[int] = []
    calculated_energy_tanks: int = 0
    player: int
    options: "FinalFantasyTacticsOptions"

    def __init__(self, player: int, options: "FinalFantasyTacticsOptions"):
        self.player = player
        self.options = options

    def logic_rule(self, state: CollectionState) -> bool:
        if len(self.requirements) == 0:
            return True
        expression = None
        for requirement_list in self.requirements:
            if "Zodiac Stones" in requirement_list:
                expression = state.has_group("Zodiac Stones", self.player, self.options.ZodiacStonesRequired.value)
            elif expression is None:
                expression = state.has_all(requirement_list, self.player)
            else:
                expression = expression or state.has_all(requirement_list, self.player)
        return expression

def create_logic_rule_for_list(
        requirements: list[Requirement],
        options: "FinalFantasyTacticsOptions",
        debug: bool = False) -> list:
    requirements_list = []
    for requirement in requirements:
        new_rule = create_logic_rule(requirement, options, debug)
        for requirement2 in new_rule:
            requirements_list.append(requirement2)
        continue
    if debug:
        print("Create logic rule for list...")
        for requirement, energy_tanks_amount in zip(requirements_list):
            print("Logic rule:")
            print(f"Requirements: {requirement}")
        print("===\n")
    return requirements_list

def create_logic_rule(
        requirement: Requirement,
        options: "FinalFantasyTacticsOptions",
        debug: bool = False) -> list[str]:
    if requirement.check_option_enabled(options):
        requirements_list = []
        unpack_requirement(
            requirement,
            requirements_list,
            [],
            options,
            debug)
        if debug:
            print("Create logic rule...")
            print(f"Requirement: {requirement}")
            print(f"Requirements List: [")
            for requirement in requirements_list:
                print(f"  {requirement}")
            print(f"]")
        return requirements_list
    else:
        if debug:
            print(f"Requirement {requirement.name} disabled due to options.")
        return []

def unpack_requirement(
        requirement: Requirement,
        possibilities: list[list[str]],
        parent_items: list[str],
        options: "FinalFantasyTacticsOptions",
        debug = False) -> None:
    if requirement.check_option_enabled(options):
        if len(requirement.other_requirements) > 0:
            for nested_requirement in requirement.other_requirements:
                current_parent_items = copy(parent_items)
                for item_needed in requirement.items_needed:
                    assert item_needed in valid_item_names, (item_needed, requirement)
                parent_items.extend(requirement.items_needed)
                unpack_requirement(
                    nested_requirement,
                    possibilities,
                    parent_items,
                    options,
                    debug
                )
                parent_items = copy(current_parent_items)
        elif len(requirement.items_needed) > 0:
            items_needed = copy(requirement.items_needed)
            for item_needed in items_needed:
                assert item_needed in valid_item_names, (item_needed, requirement)
            items_needed.extend(parent_items)
            possibilities.append(items_needed)
    else:
        if debug:
            print(f"Requirement {requirement.name} disabled due to options.")