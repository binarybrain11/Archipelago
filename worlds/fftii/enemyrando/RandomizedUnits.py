from worlds.fftii.enemyrando.Abilities import ReactionAbility, SupportAbility, MovementAbility, \
    ActionAbility
from worlds.fftii.enemyrando.Items import Items
from worlds.fftii.enemyrando.Job import UnlockedJob, Job
from worlds.fftii.enemyrando.SpriteSet import SpriteSet
from worlds.fftii.enemyrando.Unit import UnitGender


class RandomizedUnit:
    job: Job
    job_name: str
    sprite_set: SpriteSet
    sprite_set_name: str
    gender: UnitGender
    unlocked_job: UnlockedJob
    unlocked_job_level: int
    primary: ActionAbility = ActionAbility.JOB
    secondary: ActionAbility = ActionAbility.RANDOM
    reaction: ReactionAbility = ReactionAbility.RANDOM
    support: SupportAbility = SupportAbility.RANDOM
    movement: MovementAbility = MovementAbility.RANDOM
    head: Items = Items.RANDOM
    body: Items = Items.RANDOM
    accessory: Items = Items.RANDOM
    right_hand: Items = Items.RANDOM
    left_hand: Items = Items.RANDOM
    difficulty: int = 0

#region Generic humanss
class MaleSquire(RandomizedUnit):
    job = Job.SQUIRE
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleSquire(RandomizedUnit):
    job = Job.SQUIRE
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleChemist(RandomizedUnit):
    job = Job.CHEMIST
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleChemist(RandomizedUnit):
    job = Job.CHEMIST
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleKnight(RandomizedUnit):
    job = Job.KNIGHT
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleKnight(RandomizedUnit):
    job = Job.KNIGHT
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleArcher(RandomizedUnit):
    job = Job.ARCHER
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleArcher(RandomizedUnit):
    job = Job.ARCHER
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleMonk(RandomizedUnit):
    job = Job.MONK
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleMonk(RandomizedUnit):
    job = Job.MONK
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MalePriest(RandomizedUnit):
    job = Job.PRIEST
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemalePriest(RandomizedUnit):
    job = Job.PRIEST
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleWizard(RandomizedUnit):
    job = Job.WIZARD
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleWizard(RandomizedUnit):
    job = Job.WIZARD
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleTimeMage(RandomizedUnit):
    job = Job.TIMEMAGE
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleTimeMage(RandomizedUnit):
    job = Job.TIMEMAGE
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleSummoner(RandomizedUnit):
    job = Job.SUMMONER
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleSummoner(RandomizedUnit):
    job = Job.SUMMONER
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleThief(RandomizedUnit):
    job = Job.THIEF
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleThief(RandomizedUnit):
    job = Job.THIEF
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleMediator(RandomizedUnit):
    job = Job.MEDIATOR
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleMediator(RandomizedUnit):
    job = Job.MEDIATOR
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleOracle(RandomizedUnit):
    job = Job.ORACLE
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleOracle(RandomizedUnit):
    job = Job.ORACLE
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleGeomancer(RandomizedUnit):
    job = Job.GEOMANCER
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleGeomancer(RandomizedUnit):
    job = Job.GEOMANCER
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleLancer(RandomizedUnit):
    job = Job.LANCER
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleLancer(RandomizedUnit):
    job = Job.LANCER
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleSamurai(RandomizedUnit):
    job = Job.SAMURAI
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleSamurai(RandomizedUnit):
    job = Job.SAMURAI
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleNinja(RandomizedUnit):
    job = Job.NINJA
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleNinja(RandomizedUnit):
    job = Job.NINJA
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleCalculator(RandomizedUnit):
    job = Job.CALCULATOR
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleCalculator(RandomizedUnit):
    job = Job.CALCULATOR
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleBard(RandomizedUnit):
    job = Job.BARD
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleDancer(RandomizedUnit):
    job = Job.DANCER
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE


class MaleMime(RandomizedUnit):
    job = Job.MIME
    sprite_set = SpriteSet.GENERIC_MALE
    gender = UnitGender.MALE


class FemaleMime(RandomizedUnit):
    job = Job.MIME
    sprite_set = SpriteSet.GENERIC_FEMALE
    gender = UnitGender.FEMALE
#endregion

#region Special humans
class RamzaC1Squire(RandomizedUnit):
    job = Job.RAMZA_SQUIRE_CHAPTER_1
    sprite_set = SpriteSet.RAMZA_C1
    gender = UnitGender.MALE


class RamzaC23Squire(RandomizedUnit):
    job = Job.RAMZA_SQUIRE_CHAPTER_23
    sprite_set = SpriteSet.RAMZA_C23
    gender = UnitGender.MALE


class RamzaC4Squire(RandomizedUnit):
    job = Job.RAMZA_SQUIRE_CHAPTER_4
    sprite_set = SpriteSet.RAMZA_C4
    gender = UnitGender.MALE


class RamzaC4SquireFullSkillset(RamzaC4Squire):
    primary = ActionAbility.GUTS_C4


class DelitaSquire(RandomizedUnit):
    job = Job.SQUIRE_DELITA
    sprite_set = SpriteSet.DELITA_C1
    gender = UnitGender.MALE


class DelitaHolyKnight(RandomizedUnit):
    job = Job.HOLY_KNIGHT_DELITA
    sprite_set = SpriteSet.DELITA_C2
    gender = UnitGender.MALE
    difficulty = 4

class DelitaArcKnight(RandomizedUnit):
    job = Job.ARC_KNIGHT_DELITA
    sprite_set = SpriteSet.DELITA_C4
    gender = UnitGender.MALE
    difficulty = 8

class Algus(RandomizedUnit):
    job = Job.SQUIRE_ALGUS
    sprite_set = SpriteSet.ALGUS
    gender = UnitGender.MALE


class ZalbagArcKnight(RandomizedUnit):
    job = Job.ARC_KNIGHT_ZALBAG
    sprite_set = SpriteSet.ZALBAG
    gender = UnitGender.MALE
    difficulty = 4

class LuneKnight(RandomizedUnit):
    job = Job.LUNE_KNIGHT
    sprite_set = SpriteSet.DYCEDARG
    gender = UnitGender.MALE
    difficulty = 4

class Princess(RandomizedUnit):
    job = Job.PRINCESS
    sprite_set = SpriteSet.OVELIA
    gender = UnitGender.FEMALE


class HolySwordsman(RandomizedUnit):
    job = Job.HOLY_SWORDSMAN
    sprite_set = SpriteSet.ORLANDU
    gender = UnitGender.MALE
    difficulty = 8

class HolySwordsmanWithExcalibur(HolySwordsman):
    right_hand: Items = Items.EXCALIBUR
    difficulty = 12


class Dragoner(RandomizedUnit):
    job = Job.DRAGONER
    sprite_set = SpriteSet.REIS
    gender = UnitGender.FEMALE
    difficulty = 4

class HolyPriest(RandomizedUnit):
    job = Job.HOLY_PRIEST
    sprite_set = SpriteSet.ZALMO
    gender = UnitGender.MALE


class DarkKnight(RandomizedUnit):
    job = Job.DARK_KNIGHT_GUEST
    sprite_set = SpriteSet.GAFGARION
    gender = UnitGender.MALE


class Astrologist(RandomizedUnit):
    job = Job.ASTROLOGIST
    sprite_set = SpriteSet.OLAN
    gender = UnitGender.MALE
    difficulty = 4


class EngineerMustadio(RandomizedUnit):
    job = Job.ENGINEER_MUSTADIO
    sprite_set = SpriteSet.MUSTADIO
    gender = UnitGender.MALE


class HellKnight(RandomizedUnit):
    job = Job.HELL_KNIGHT
    sprite_set = SpriteSet.MALAK
    gender = UnitGender.MALE


class ArcKnightElmdor(RandomizedUnit):
    job = Job.ARC_KNIGHT_ELMDOR
    sprite_set = SpriteSet.ELMDOR
    gender = UnitGender.MALE
    difficulty = 8

class ArcKnightElmdorWithKit(ArcKnightElmdor):
    primary = ActionAbility.SWORD_SPIRIT
    secondary = ActionAbility.BLOOD_SUCK
    reaction = ReactionAbility.BLADE_GRASP
    difficulty = 12


class HolyKnightAgrias(RandomizedUnit):
    job = Job.HOLY_KNIGHT_AGRIAS
    sprite_set = SpriteSet.AGRIAS
    gender = UnitGender.FEMALE
    difficulty = 4


class TempleKnight(RandomizedUnit):
    job = Job.TEMPLE_KNIGHT
    sprite_set = SpriteSet.BEOWULF
    gender = UnitGender.MALE
    difficulty = 6


class DivineKnightVormav(RandomizedUnit):
    job = Job.DIVINE_KNIGHT_VORMAV
    sprite_set = SpriteSet.VORMAV
    gender = UnitGender.MALE
    difficulty = 6


class DivineKnightRofel(RandomizedUnit):
    job = Job.DIVINE_KNIGHT_ROFEL
    sprite_set = SpriteSet.ROFEL
    gender = UnitGender.MALE
    difficulty = 6


class KnightBlade(RandomizedUnit):
    job = Job.KNIGHT_BLADE
    sprite_set = SpriteSet.IZLUDE
    gender = UnitGender.MALE
    difficulty = 4


class KnightBladeWithKit(KnightBlade):
    secondary = ActionAbility.IZLUDE_JUMP
    support = SupportAbility.MAINTENANCE
    difficulty = 6


class Sorcerer(RandomizedUnit):
    job = Job.SORCERER
    sprite_set = SpriteSet.KLETIAN
    gender = UnitGender.MALE
    difficulty = 8


class WhiteKnight(RandomizedUnit):
    job = Job.WHITE_KNIGHT_C3
    sprite_set = SpriteSet.WIEGRAF2
    gender = UnitGender.MALE
    difficulty = 4


class WhiteKnightWithCounter(WhiteKnight):
    reaction = ReactionAbility.COUNTER


class WhiteKnightChapter1(WhiteKnight):
    job = Job.WHITE_KNIGHT_C1
    sprite_set = SpriteSet.WIEGRAF1


class WhiteKnightChapter1WithCounter(WhiteKnightChapter1):
    reaction = ReactionAbility.COUNTER


class HeavenKnight(RandomizedUnit):
    job = Job.HEAVEN_KNIGHT
    sprite_set = SpriteSet.RAFA
    gender = UnitGender.FEMALE


class DivineKnightMeliadoul(RandomizedUnit):
    job = Job.DIVINE_KNIGHT_MELIADOUL
    sprite_set = SpriteSet.MELIADOUL
    gender = UnitGender.FEMALE
    difficulty = 6


class EngineerBalk(RandomizedUnit):
    job = Job.ENGINEER_BALK
    sprite_set = SpriteSet.BALK
    gender = UnitGender.MALE


class AssassinCelia(RandomizedUnit):
    job = Job.ASSASSIN_CELIA
    sprite_set = SpriteSet.CELIA
    gender = UnitGender.FEMALE
    difficulty = 10


class AssassinLede(RandomizedUnit):
    job = Job.ASSASSIN_LEDE
    sprite_set = SpriteSet.LEDE
    gender = UnitGender.FEMALE
    difficulty = 10


class Cleric(RandomizedUnit):
    job = Job.CLERIC
    sprite_set = SpriteSet.ALMA
    gender = UnitGender.FEMALE


class ClericWithUltima(Cleric):
    primary = ActionAbility.HOLY_MAGIC
    difficulty = 4


class Soldier(RandomizedUnit):
    job = Job.SOLDIER
    sprite_set = SpriteSet.CLOUD
    gender = UnitGender.MALE
    difficulty = 4


class ArcKnightZombie(RandomizedUnit):
    job = Job.ARC_KNIGHT_ZOMBIE
    sprite_set = SpriteSet.ZALBAG_ZOMBIE
    gender = UnitGender.MALE
    difficulty = 8


class ArcKnightZombieWithKit(ArcKnightZombie):
    secondary = ActionAbility.BLOOD_SUCK
    difficulty = 12


class UndeadKnight(RandomizedUnit):
    job = Job.KNIGHT_UNDEAD
    sprite_set = SpriteSet.UNDEAD_KNIGHT
    gender = UnitGender.MONSTER


class UndeadArcher(RandomizedUnit):
    job = Job.ARCHER_UNDEAD
    sprite_set = SpriteSet.UNDEAD_ARCHER
    gender = UnitGender.MALE


class UndeadWizard(RandomizedUnit):
    job = Job.WIZARD_UNDEAD
    sprite_set = SpriteSet.UNDEAD_WIZARD
    gender = UnitGender.MALE


class UndeadTimeMage(RandomizedUnit):
    job = Job.TIME_MAGE_UNDEAD
    sprite_set = SpriteSet.UNDEAD_TIMEMAGE
    gender = UnitGender.FEMALE


class UndeadOracle(RandomizedUnit):
    job = Job.ORACLE_UNDEAD
    sprite_set = SpriteSet.UNDEAD_ORACLE
    gender = UnitGender.MALE


class UndeadSummoner(RandomizedUnit):
    job = Job.SUMMONER_UNDEAD
    sprite_set = SpriteSet.UNDEAD_SUMMONER
    gender = UnitGender.FEMALE


class Altima1(RandomizedUnit):
    job = Job.ALTIMA_1
    sprite_set = SpriteSet.ALTIMA_1
    gender = UnitGender.MONSTER
    primary = ActionAbility.ULTIMATE_MAGIC
    secondary = ActionAbility.CHAOS
    difficulty = 14


class Altima2(RandomizedUnit):
    job = Job.ALTIMA_2
    sprite_set = SpriteSet.ALTIMA_2
    gender = UnitGender.MONSTER
    primary = ActionAbility.COMPLETE_MAGIC
    secondary = ActionAbility.SATURATION
    difficulty = 14
#endregion

#region Generic monsters
class GenericMonster(RandomizedUnit):
    sprite_set = SpriteSet.MONSTER
    gender = UnitGender.MONSTER


class YellowChocobo(GenericMonster):
    job = Job.YELLOW_CHOCOBO


class BlackChocobo(GenericMonster):
    job = Job.BLACK_CHOCOBO
    difficulty = 4


class RedChocobo(GenericMonster):
    job = Job.RED_CHOCOBO
    difficulty = 6


class Goblin(GenericMonster):
    job = Job.GOBLIN


class BlackGoblin(GenericMonster):
    job = Job.BLACK_GOBLIN


class Gobbledeguck(GenericMonster):
    job = Job.GOBBLEDEGUCK


class Bomb(GenericMonster):
    job = Job.BOMB


class Grenade(GenericMonster):
    job = Job.GRENADE


class Explosive(GenericMonster):
    job = Job.EXPLOSIVE


class RedPanther(GenericMonster):
    job = Job.RED_PANTHER


class Cuar(GenericMonster):
    job = Job.CUAR


class Vampire(GenericMonster):
    job = Job.VAMPIRE


class PiscoDemon(GenericMonster):
    job = Job.PISCO_DEMON


class Squidlarkin(GenericMonster):
    job = Job.SQUIDLARKIN


class Mindflare(GenericMonster):
    job = Job.MINDFLARE
    difficulty = 6


class Skeleton(GenericMonster):
    job = Job.SKELETON


class BoneSnatch(GenericMonster):
    job = Job.BONE_SNATCH


class LivingBone(GenericMonster):
    job = Job.LIVING_BONE


class Ghoul(GenericMonster):
    job = Job.GHOUL


class Gust(GenericMonster):
    job = Job.GUST


class Revnant(GenericMonster):
    job = Job.REVNANT


class Flotiball(GenericMonster):
    job = Job.FLOTIBALL


class Ahriman(GenericMonster):
    job = Job.AHRIMAN


class Plague(GenericMonster):
    job = Job.PLAGUE


class Juravis(GenericMonster):
    job = Job.JURAVIS


class SteelHawk(GenericMonster):
    job = Job.STEEL_HAWK


class Cocatoris(GenericMonster):
    job = Job.COCATORIS


class Uribo(GenericMonster):
    job = Job.URIBO


class Porky(GenericMonster):
    job = Job.PORKY


class Wildbow(GenericMonster):
    job = Job.WILDBOW


class Woodman(GenericMonster):
    job = Job.WOODMAN


class Trent(GenericMonster):
    job = Job.TRENT


class Taiju(GenericMonster):
    job = Job.TAIJU


class BullDemon(GenericMonster):
    job = Job.BULL_DEMON


class Minitaurus(GenericMonster):
    job = Job.MINITAURUS


class Sacred(GenericMonster):
    job = Job.SACRED


class Morbol(GenericMonster):
    job = Job.MORBOL


class Ochu(GenericMonster):
    job = Job.OCHU


class GreatMorbol(GenericMonster):
    job = Job.GREAT_MORBOL


class Behemoth(GenericMonster):
    job = Job.BEHEMOTH
    difficulty = 4


class KingBehemoth(GenericMonster):
    job = Job.KING_BEHEMOTH
    difficulty = 6


class DarkBehemoth(GenericMonster):
    job = Job.DARK_BEHEMOTH
    difficulty = 8


class Dragon(GenericMonster):
    job = Job.DRAGON


class BlueDragon(GenericMonster):
    job = Job.BLUE_DRAGON
    difficulty = 4


class RedDragon(GenericMonster):
    job = Job.RED_DRAGON
    difficulty = 4


class Hyudra(GenericMonster):
    job = Job.HYUDRA
    difficulty = 4


class Hydra(GenericMonster):
    job = Job.HYDRA
    difficulty = 6


class Tiamat(GenericMonster):
    job = Job.TIAMAT
    difficulty = 8
#endregion

#region Special monsters
class SpecialMonster(RandomizedUnit):
    sprite_set = SpriteSet.MONSTER
    gender = UnitGender.MONSTER
    difficulty = 6


class HolyDragon(SpecialMonster):
    job = Job.HOLY_DRAGON
    sprite_set = SpriteSet.HOLY_DRAGON


class Byblos(SpecialMonster):
    job = Job.BYBLOS


class SteelGiant(SpecialMonster):
    job = Job.STEEL_GIANT


class Apanda(SpecialMonster):
    job = Job.APANDA


class ArchaicDemon(SpecialMonster):
    job = Job.ARCHAIC_DEMON


class UltimaDemon(SpecialMonster):
    job = Job.ULTIMA_DEMON
#endregion

#region Lucavi
class Velius(RandomizedUnit):
    job = Job.VELIUS
    sprite_set = SpriteSet.VELIUS
    gender = UnitGender.MONSTER
    difficulty = 8


class VeliusWithKit(Velius):
    primary = ActionAbility.VELIUS_FEAR
    secondary = ActionAbility.WARLOCK_SUMMON


class Zalera(RandomizedUnit):
    job = Job.ZALERA
    sprite_set = SpriteSet.ZALERA
    gender = UnitGender.MALE
    difficulty = 8


class ZaleraWithKit(Zalera):
    primary = ActionAbility.ZALERA_FEAR
    secondary = ActionAbility.JA_MAGIC


class Hashmalum(RandomizedUnit):
    job = Job.HASHMALUM
    sprite_set = SpriteSet.HASHMALUM
    gender = UnitGender.MALE
    difficulty = 10


class HashmalumWithKit(Hashmalum):
    primary = ActionAbility.HASHMALUM_FEAR
    secondary = ActionAbility.DIMENSION_MAGIC


class Queklain(RandomizedUnit):
    job = Job.QUEKLAIN
    sprite_set = SpriteSet.QUEKLAIN
    gender = UnitGender.MALE
    difficulty = 6


class QueklainWithKit(Queklain):
    primary = ActionAbility.QUEKLAIN_FEAR
    secondary = ActionAbility.IMPURE


class Adramelk(RandomizedUnit):
    job = Job.ADRAMELK
    sprite_set = SpriteSet.ADRAMELK
    gender = UnitGender.MONSTER
    difficulty = 8


class AdramelkWithKit(Adramelk):
    primary = ActionAbility.ADRAMELK_FEAR
    secondary = ActionAbility.ALL_MAGIC


class Elidibs(RandomizedUnit):
    job = Job.ELIDIBS
    sprite_set = SpriteSet.MONSTER
    gender = UnitGender.MONSTER
    difficulty = 12
#endregion