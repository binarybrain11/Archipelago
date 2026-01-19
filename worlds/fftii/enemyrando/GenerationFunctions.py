from typing import TYPE_CHECKING

from .RandomizedUnitFactory import RandomizedUnitFactory
from .SpriteSet import SpriteSet
from .. import FinalFantasyTacticsIIOptions
from .SourceUnit import SourceUnit
from .RandomizedMapping import RandomizedMapping
from .RandomizedMappings import generic_job_table, special_job_table, generic_monster_table, special_monster_table, \
    lucavi_table
from .Job import generic_jobs, generic_monster_jobs, special_character_jobs, special_monster_jobs, lucavi_jobs, Job

if TYPE_CHECKING:
    from .. import FinalFantasyTacticsIvaliceIslandWorld

battle_levels = [
    [0, 1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10, 11],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [0, 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14]
]

def get_logic_adjusted_fight_level(fight_level: int, logical_difficulty: int):
    return battle_levels[logical_difficulty][fight_level]

def get_eligible_destination_jobs(source_unit: SourceUnit, options: "FinalFantasyTacticsIIOptions") -> dict[Job, list[Job]]:
    eligible_destination_job_table: dict[Job, list[Job]] = {}
    if source_unit.job.value in generic_jobs.keys():
        eligible_destination_job_table.update(generic_job_table)
        if options.cross_enemy_randomizer:  # if cross-class rando
            eligible_destination_job_table.update(special_job_table)
        if options.cross_species_randomizer:  # if cross-monster rando
            eligible_destination_job_table.update(generic_monster_table)
        if options.cross_enemy_randomizer and options.cross_species_randomizer:  # if both
            eligible_destination_job_table.update(special_monster_table)
            if options.lucavi_randomizer:  # if Lucavi
                eligible_destination_job_table.update(lucavi_table)
    if source_unit.job.value in generic_monster_jobs.keys():
        eligible_destination_job_table.update(generic_monster_table)
        if options.cross_enemy_randomizer:  # if cross-class rando
            eligible_destination_job_table.update(special_monster_table)
        if options.cross_species_randomizer:  # if cross-monster rando
            eligible_destination_job_table.update(generic_job_table)
        if options.cross_enemy_randomizer and options.cross_species_randomizer:  # if both
            eligible_destination_job_table.update(special_job_table)
            if options.lucavi_randomizer:  # if Lucavi
                eligible_destination_job_table.update(lucavi_table)
    if source_unit.job.value in special_character_jobs.keys() or source_unit.sprite_set == SpriteSet.ALGUS:
        eligible_destination_job_table.update(special_job_table)
        if options.cross_enemy_randomizer:  # if cross-class rando
            eligible_destination_job_table.update(generic_job_table)
        if options.cross_species_randomizer:  # if cross-monster rando
            eligible_destination_job_table.update(special_monster_table)
            if options.lucavi_randomizer:  # if Lucavi
                eligible_destination_job_table.update(lucavi_table)
        if options.cross_enemy_randomizer and options.cross_species_randomizer:  # if both
            eligible_destination_job_table.update(generic_monster_table)
    if source_unit.job.value in special_monster_jobs.keys():
        eligible_destination_job_table.update(special_monster_table)
        if options.cross_enemy_randomizer:  # if cross-class rando
            eligible_destination_job_table.update(generic_monster_table)
        if options.cross_species_randomizer:  # if cross-monster rando
            eligible_destination_job_table.update(special_job_table)
        if options.cross_enemy_randomizer and options.cross_species_randomizer:  # if both
            eligible_destination_job_table.update(generic_job_table)
        if options.lucavi_randomizer:  # if Lucavi
            eligible_destination_job_table.update(lucavi_table)
    if source_unit.job.value in lucavi_jobs.keys():
        eligible_destination_job_table.update(lucavi_table)
        if options.lucavi_randomizer:  # if Lucavi
            eligible_destination_job_table.update(special_monster_table)
            if options.cross_enemy_randomizer:  # if cross-class rando
                eligible_destination_job_table.update(generic_monster_table)
            if options.cross_species_randomizer:  # if cross-monster rando
                eligible_destination_job_table.update(special_job_table)
            if options.cross_enemy_randomizer and options.cross_species_randomizer:  # if both
                eligible_destination_job_table.update(generic_job_table)
    assert len(eligible_destination_job_table) > 0, source_unit.job.value
    return eligible_destination_job_table


def get_randomized_mapping(
        randomized_factories: dict[Job, RandomizedUnitFactory],
        fight_difficulty: int,
        source_unit: SourceUnit,
        world: "FinalFantasyTacticsIvaliceIslandWorld"):
    eligible_factories = {
        job: factory for job, factory in randomized_factories.items()
        if factory.get_lowest_difficulty() <= fight_difficulty
    }
    eligible_destination_job_table = get_eligible_destination_jobs(source_unit, world.options)
    eligible_destination_job_table = {
        job: options for job, options in eligible_destination_job_table.items()
        if job in eligible_factories.keys()
    }
    destination_job_key = world.random.choice(sorted(list(eligible_destination_job_table.keys())))
    #chosen_destination_job = world.random.choice(eligible_destination_job_table[destination_job_key])
    #chosen_factory = eligible_factories[chosen_destination_job]
    #destination_unit = chosen_factory.get_unit(fight_difficulty)
    new_mapping = RandomizedMapping(source_unit, destination_job_key)
    new_mapping.battle_level = fight_difficulty
    return new_mapping