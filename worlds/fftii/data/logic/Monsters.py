from enum import Enum

from worlds.fftii.data.logic.FFTRegion import FFTRegion
from worlds.fftii.data.logic.regions import Mandalia, Grog, Zirekile, BariausHill, Finath, Dolbodar, Fovoham, Bethla, \
    Zaland, BerveniaVolcano, Riovanes, Lenalia, Lesalia, Araguay, BariausValley, Sweegy, Yuguo, Bed, BerveniaCity, \
    Germinas, Zeklaus, Doguola, Poeskas, Zigolis, Dorter, Goug, Zeakden, Nelveska


class MonsterNames(Enum):
    YELLOW_CHOCOBO = "Yellow Chocobo"
    BLACK_CHOCOBO = "Black Chocobo"
    RED_CHOCOBO = "Red Chocobo"

    GOBLIN = "Goblin"
    BLACK_GOBLIN = "Black Goblin"
    GOBBLEDEGUCK = "Gobbledeguck"

    RED_PANTHER = "Red Panther"
    CUAR = "Cuar"
    VAMPIRE = "Vampire"

    BOMB = "Bomb"
    GRENADE = "Grenade"
    EXPLOSIVE = "Explosive"

    SKELETON = "Skeleton"
    BONE_SNATCH = "Bone Snatch"
    LIVING_BONE = "Living Bone"

    GHOUL = "Ghoul"
    GUST = "Gust"
    REVNANT = "Revnant"

    FLOATIBALL = "Floatiball"
    AHRIMAN = "Ahriman"
    PLAGUE = "Plague"

    PISCO_DEMON = "Pisco Demon"
    SQUIDLARKIN = "Squidlarkin"
    MINDFLARE = "Mindflare"

    JURAVIS = "Juravis"
    STEEL_HAWK = "Steel Hawk"
    COCATORIS = "Cocatoris"

    BULL_DEMON = "Bull Demon"
    MINITAURUS = "Minitaurus"
    SACRED = "Sacred"

    MORBOL = "Morbol"
    OCHU = "Ochu"
    GREAT_MORBOL = "Great Morbul"

    WOODMAN = "Woodman"
    TRENT = "Trent"
    TAIJU = "Taiju"

    DRAGON = "Dragon"
    BLUE_DRAGON = "Blue Dragon"
    RED_DRAGON = "Red Dragon"

    BEHEMOTH = "Behemoth"
    KING_BEHEMOTH = "King Behemoth"
    DARK_BEHEMOTH = "Dark Behemoth"

    HYUDRA = "Hyudra"
    HYDRA = "Hydra"
    TIAMAT = "Tiamat"

    URIBO = "Uribo"
    PORKY = "Porky"
    WILDBOW = "Wildbow"

class MonsterFamilies(Enum):
    CHOCOBO = "Chocobo"
    GOBLIN = "Goblin"
    PANTHER = "Panther"
    BOMB = "Bomb"
    SKELETON = "Skeleton"
    GHOST = "Ghost"
    AHRIMAN = "Ahriman"
    MINDFLAYER = "Mindflayer"
    BIRD = "Bird"
    MINOTAUR = "Minotaur"
    MALBORO = "Malboro"
    TREANT = "Treant"
    DRAGON = "Dragon"
    BEHEMOTH = "Behemoth"
    HYDRA = "Hydra"
    PIG = "Pig"

monster_families: dict[MonsterFamilies, list[MonsterNames]] = {
    MonsterFamilies.CHOCOBO: [MonsterNames.YELLOW_CHOCOBO, MonsterNames.BLACK_CHOCOBO, MonsterNames.RED_CHOCOBO],
    MonsterFamilies.GOBLIN: [MonsterNames.GOBLIN, MonsterNames.BLACK_GOBLIN, MonsterNames.GOBBLEDEGUCK],
    MonsterFamilies.PANTHER: [MonsterNames.RED_PANTHER, MonsterNames.CUAR, MonsterNames.VAMPIRE],
    MonsterFamilies.BOMB: [MonsterNames.BOMB, MonsterNames.GRENADE, MonsterNames.EXPLOSIVE],
    MonsterFamilies.SKELETON: [MonsterNames.SKELETON, MonsterNames.BONE_SNATCH, MonsterNames.LIVING_BONE],
    MonsterFamilies.GHOST: [MonsterNames.GHOUL, MonsterNames.GUST, MonsterNames.REVNANT],
    MonsterFamilies.AHRIMAN: [MonsterNames.FLOATIBALL, MonsterNames.AHRIMAN, MonsterNames.PLAGUE],
    MonsterFamilies.MINDFLAYER: [MonsterNames.PISCO_DEMON, MonsterNames.SQUIDLARKIN, MonsterNames.MINDFLARE],
    MonsterFamilies.BIRD: [MonsterNames.JURAVIS, MonsterNames.STEEL_HAWK, MonsterNames.COCATORIS],
    MonsterFamilies.MINOTAUR: [MonsterNames.BULL_DEMON, MonsterNames.MINITAURUS, MonsterNames.SACRED],
    MonsterFamilies.MALBORO: [MonsterNames.MORBOL, MonsterNames.OCHU, MonsterNames.GREAT_MORBOL],
    MonsterFamilies.TREANT: [MonsterNames.WOODMAN, MonsterNames.TRENT, MonsterNames.TAIJU],
    MonsterFamilies.DRAGON: [MonsterNames.DRAGON, MonsterNames.BLUE_DRAGON, MonsterNames.RED_DRAGON],
    MonsterFamilies.BEHEMOTH: [MonsterNames.BEHEMOTH, MonsterNames.KING_BEHEMOTH, MonsterNames.DARK_BEHEMOTH],
    MonsterFamilies.HYDRA: [MonsterNames.HYUDRA, MonsterNames.HYDRA, MonsterNames.TIAMAT],
    MonsterFamilies.PIG: [MonsterNames.URIBO, MonsterNames.PORKY, MonsterNames.WILDBOW]
}

monster_family_lookup: dict[MonsterNames, MonsterFamilies] = {}

for family, monsters in monster_families.items():
    for monster in monsters:
        monster_family_lookup[monster] = family


class RegionAccessRequirement:
    access_regions: list[type[FFTRegion]]
    battle_level: int

    def __init__(self, access_regions: list[type[FFTRegion]], battle_level: int):
        self.access_regions = access_regions
        self.battle_level = battle_level

class MonsterRegion:
    monster_name: MonsterNames
    gallione_locations: list[RegionAccessRequirement] = []
    fovoham_locations: list[RegionAccessRequirement] = []
    lesalia_locations: list[RegionAccessRequirement] = []
    lionel_locations: list[RegionAccessRequirement] = []
    zeltennia_locations: list[RegionAccessRequirement] = []
    limberry_locations: list[RegionAccessRequirement] = []
    compiled_requirements: list[RegionAccessRequirement] = []

    def __init__(self, name: MonsterNames):
        self.monster_name = name

yellow_chocobo = MonsterRegion(MonsterNames.YELLOW_CHOCOBO)
yellow_chocobo.gallione_locations = [RegionAccessRequirement([Mandalia], 1)]
yellow_chocobo.fovoham_locations = [RegionAccessRequirement([Grog], 1)]
yellow_chocobo.lesalia_locations = [RegionAccessRequirement([Zirekile], 1)]
yellow_chocobo.lionel_locations = [RegionAccessRequirement([BariausHill], 1)]
yellow_chocobo.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
yellow_chocobo.limberry_locations = [RegionAccessRequirement([Dolbodar], 5)]

black_chocobo = MonsterRegion(MonsterNames.BLACK_CHOCOBO)
black_chocobo.gallione_locations = [RegionAccessRequirement([Mandalia], 3)]
black_chocobo.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
black_chocobo.lesalia_locations = [
    RegionAccessRequirement([Zirekile], 3),
    RegionAccessRequirement([Zirekile, Zaland], 2),
    RegionAccessRequirement([Zirekile, Bethla], 1),
    RegionAccessRequirement([BerveniaVolcano, Riovanes], 5)
]
black_chocobo.lionel_locations = [RegionAccessRequirement([BariausHill], 1)]
black_chocobo.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
black_chocobo.limberry_locations = [RegionAccessRequirement([Dolbodar], 5)]

red_chocobo = MonsterRegion(MonsterNames.RED_CHOCOBO)
red_chocobo.gallione_locations = [RegionAccessRequirement([Lenalia], 3)]
red_chocobo.fovoham_locations = [RegionAccessRequirement([Grog], 2)]
red_chocobo.lesalia_locations = [
    RegionAccessRequirement([Zirekile, Bethla], 3),
    RegionAccessRequirement([Zirekile, Zaland], 3),
    RegionAccessRequirement([BerveniaVolcano, Riovanes], 5)
]
red_chocobo.lionel_locations = [RegionAccessRequirement([BariausHill], 1)]
red_chocobo.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
red_chocobo.limberry_locations = [RegionAccessRequirement([Dolbodar], 5)]

goblin = MonsterRegion(MonsterNames.GOBLIN)
goblin.gallione_locations = [RegionAccessRequirement([Mandalia], 1)]
goblin.fovoham_locations = [
    RegionAccessRequirement([Fovoham, Lenalia], 1),
    RegionAccessRequirement([Grog, Lesalia], 3)
]
goblin.lesalia_locations = [RegionAccessRequirement([Araguay], 1)]
goblin.lionel_locations = [RegionAccessRequirement([BariausValley], 1)]
goblin.zeltennia_locations = [RegionAccessRequirement([Finath], 5)]
goblin.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

black_goblin = MonsterRegion(MonsterNames.BLACK_GOBLIN)
black_goblin.gallione_locations = [RegionAccessRequirement([Sweegy], 1)]
black_goblin.fovoham_locations = [RegionAccessRequirement([Yuguo], 2)]
black_goblin.lesalia_locations = [RegionAccessRequirement([Araguay], 1)]
black_goblin.lionel_locations = [RegionAccessRequirement([BariausValley], 1)]
black_goblin.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

gobbledeguck = MonsterRegion(MonsterNames.GOBBLEDEGUCK)
gobbledeguck.gallione_locations = [RegionAccessRequirement([Mandalia], 3)]
gobbledeguck.fovoham_locations = [RegionAccessRequirement([Yuguo], 3)]
gobbledeguck.lesalia_locations = [RegionAccessRequirement([Araguay], 4)]
gobbledeguck.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
gobbledeguck.limberry_locations = [RegionAccessRequirement([Dolbodar], 3)]

red_panther = MonsterRegion(MonsterNames.RED_PANTHER)
red_panther.gallione_locations = [RegionAccessRequirement([Mandalia], 1)]
red_panther.fovoham_locations = [RegionAccessRequirement([Grog], 1)]
red_panther.lesalia_locations = [RegionAccessRequirement([Araguay], 1)]
red_panther.lionel_locations = [RegionAccessRequirement([BariausValley], 1)]
red_panther.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
red_panther.limberry_locations = [RegionAccessRequirement([Bed], 3)]

cuar = MonsterRegion(MonsterNames.CUAR)
cuar.gallione_locations = [
    RegionAccessRequirement([Sweegy], 3),
    RegionAccessRequirement([Lenalia, Fovoham], 2),
]
cuar.fovoham_locations = [RegionAccessRequirement([Grog], 2)]
cuar.lesalia_locations = [RegionAccessRequirement([Araguay], 1)]
cuar.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
cuar.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
cuar.limberry_locations = [RegionAccessRequirement([Bed, BerveniaCity], 1)]

vampire = MonsterRegion(MonsterNames.VAMPIRE)
vampire.gallione_locations = [RegionAccessRequirement([Sweegy], 3)]
vampire.fovoham_locations = [RegionAccessRequirement([Yuguo], 3)]
vampire.lesalia_locations = [RegionAccessRequirement([Araguay], 3)]
vampire.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
vampire.zeltennia_locations = [RegionAccessRequirement([Germinas], 3)]
vampire.limberry_locations = [RegionAccessRequirement([Bed], 2)]

bomb = MonsterRegion(MonsterNames.BOMB)
bomb.gallione_locations = [RegionAccessRequirement([Sweegy], 1)]
bomb.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
bomb.lesalia_locations = [RegionAccessRequirement([Zeklaus], 1)]
bomb.lionel_locations = [RegionAccessRequirement([BariausHill], 1)]
bomb.zeltennia_locations = [RegionAccessRequirement([Doguola], 3)]
bomb.limberry_locations = [RegionAccessRequirement([Poeskas], 1)]

grenade = MonsterRegion(MonsterNames.GRENADE)
grenade.gallione_locations = [RegionAccessRequirement([Mandalia], 3)]
grenade.fovoham_locations = [RegionAccessRequirement([Grog], 1)]
grenade.lesalia_locations = [RegionAccessRequirement([Zeklaus], 1)]
grenade.lionel_locations = [RegionAccessRequirement([BariausHill], 1)]
grenade.zeltennia_locations = [RegionAccessRequirement([Doguola, Grog], 3)]
grenade.limberry_locations = [RegionAccessRequirement([Poeskas], 1)]

explosive = MonsterRegion(MonsterNames.EXPLOSIVE)
explosive.gallione_locations = [RegionAccessRequirement([Sweegy], 4)]
explosive.fovoham_locations = [RegionAccessRequirement([Grog], 3)]
explosive.lesalia_locations = [
    RegionAccessRequirement([BerveniaVolcano], 3),
    RegionAccessRequirement([BerveniaVolcano, Riovanes], 2)
]
explosive.lionel_locations = [RegionAccessRequirement([BariausHill], 3)]
explosive.zeltennia_locations = [RegionAccessRequirement([Doguola, Grog], 3)]
explosive.limberry_locations = [RegionAccessRequirement([Poeskas], 1)]

skeleton = MonsterRegion(MonsterNames.SKELETON)
skeleton.gallione_locations = [RegionAccessRequirement([Sweegy], 3)]
skeleton.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
skeleton.lesalia_locations = [RegionAccessRequirement([Zeklaus, Dorter], 1)]
skeleton.lionel_locations = [RegionAccessRequirement([Zigolis], 1)]
skeleton.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

bone_snatch = MonsterRegion(MonsterNames.BONE_SNATCH)
bone_snatch.gallione_locations = [RegionAccessRequirement([Sweegy], 3)]
bone_snatch.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
bone_snatch.lesalia_locations = [RegionAccessRequirement([Araguay], 1)]
bone_snatch.lionel_locations = [RegionAccessRequirement([Zigolis], 1)]
bone_snatch.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

living_bone = MonsterRegion(MonsterNames.LIVING_BONE)
living_bone.gallione_locations = [RegionAccessRequirement([Sweegy], 3)]
living_bone.lesalia_locations = [RegionAccessRequirement([BerveniaVolcano], 3)]
living_bone.lionel_locations = [RegionAccessRequirement([Zigolis, Goug], 3)]
living_bone.limberry_locations = [RegionAccessRequirement([Dolbodar], 2)]

ghoul = MonsterRegion(MonsterNames.GHOUL)
ghoul.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
ghoul.lesalia_locations = [RegionAccessRequirement([Araguay, Dorter], 1)]
ghoul.lionel_locations = [RegionAccessRequirement([Zigolis], 1)]
ghoul.limberry_locations = [RegionAccessRequirement([Poeskas], 1)]

gust = MonsterRegion(MonsterNames.GUST)
gust.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
gust.lesalia_locations = [RegionAccessRequirement([Araguay, Dorter], 2)]
gust.lionel_locations = [RegionAccessRequirement([Zigolis], 2)]
gust.limberry_locations = [RegionAccessRequirement([Poeskas], 1)]

revnant = MonsterRegion(MonsterNames.REVNANT)
revnant.fovoham_locations = [RegionAccessRequirement([Yuguo], 3)]
revnant.lesalia_locations = [RegionAccessRequirement([Araguay, Dorter], 3)]
revnant.lionel_locations = [RegionAccessRequirement([Zigolis], 3)]
revnant.limberry_locations = [RegionAccessRequirement([Poeskas], 2)]

floatiball = MonsterRegion(MonsterNames.FLOATIBALL)
floatiball.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
floatiball.lesalia_locations = [RegionAccessRequirement([Zirekile], 1)]
floatiball.lionel_locations = [RegionAccessRequirement([Zigolis], 1)]
floatiball.limberry_locations = [RegionAccessRequirement([Bed], 1)]

ahriman = MonsterRegion(MonsterNames.AHRIMAN)
ahriman.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
ahriman.lesalia_locations = [
    RegionAccessRequirement([Zirekile, Bethla], 2),
    RegionAccessRequirement([BerveniaVolcano, Riovanes], 1)
]
ahriman.lionel_locations = [RegionAccessRequirement([Zigolis], 2)]
ahriman.limberry_locations = [RegionAccessRequirement([Bed], 1)]

plague = MonsterRegion(MonsterNames.PLAGUE)
plague.fovoham_locations = [RegionAccessRequirement([Fovoham], 4)]
plague.lesalia_locations = [RegionAccessRequirement([BerveniaVolcano, Riovanes], 3)]
plague.lionel_locations = [RegionAccessRequirement([BariausValley], 5)]
plague.zeltennia_locations = [RegionAccessRequirement([Germinas], 3)]
plague.limberry_locations = [RegionAccessRequirement([Bed, BerveniaCity], 3)]

pisco_demon = MonsterRegion(MonsterNames.PISCO_DEMON)
pisco_demon.gallione_locations = [
    RegionAccessRequirement([Lenalia], 2),
    RegionAccessRequirement([Lenalia, Fovoham], 1)
]
pisco_demon.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
pisco_demon.lesalia_locations = [RegionAccessRequirement([Zirekile], 1)]
pisco_demon.lionel_locations = [RegionAccessRequirement([BariausValley], 1)]
pisco_demon.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
pisco_demon.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

squidlarkin = MonsterRegion(MonsterNames.SQUIDLARKIN)
squidlarkin.gallione_locations = [RegionAccessRequirement([Lenalia], 2)]
squidlarkin.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
squidlarkin.lesalia_locations = [RegionAccessRequirement([Zirekile], 1)]
squidlarkin.lionel_locations = [RegionAccessRequirement([BariausValley], 1)]
squidlarkin.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
squidlarkin.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

mindflare = MonsterRegion(MonsterNames.MINDFLARE)
mindflare.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
mindflare.lesalia_locations = [RegionAccessRequirement([Zirekile], 1)]
mindflare.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
mindflare.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
mindflare.limberry_locations = [RegionAccessRequirement([Dolbodar], 3)]

juravis = MonsterRegion(MonsterNames.JURAVIS)
juravis.fovoham_locations = [RegionAccessRequirement([Fovoham, Zeakden], 1)]
juravis.lesalia_locations = [RegionAccessRequirement([BerveniaVolcano], 1)]
juravis.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
juravis.zeltennia_locations = [RegionAccessRequirement([Germinas], 1)]

steel_hawk = MonsterRegion(MonsterNames.STEEL_HAWK)
steel_hawk.fovoham_locations = [RegionAccessRequirement([Fovoham, Zeakden], 2)]
steel_hawk.lesalia_locations = [RegionAccessRequirement([Zeklaus], 1)]
steel_hawk.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
steel_hawk.zeltennia_locations = [RegionAccessRequirement([Germinas], 1)]
steel_hawk.limberry_locations = [RegionAccessRequirement([Poeskas], 2)]

cockatoris = MonsterRegion(MonsterNames.COCATORIS)
cockatoris.fovoham_locations = [RegionAccessRequirement([Fovoham], 1)]
cockatoris.lesalia_locations = [RegionAccessRequirement([Zeklaus], 3)]
cockatoris.lionel_locations = [RegionAccessRequirement([BariausValley], 3)]
cockatoris.limberry_locations = [RegionAccessRequirement([Poeskas], 2)]

bull_demon = MonsterRegion(MonsterNames.BULL_DEMON)
bull_demon.gallione_locations = [RegionAccessRequirement([Sweegy], 1)]
bull_demon.fovoham_locations = [
    RegionAccessRequirement([Fovoham], 3),
    RegionAccessRequirement([Fovoham, Zeakden], 1),
]
bull_demon.lesalia_locations = [RegionAccessRequirement([Zeklaus], 1)]
bull_demon.lionel_locations = [RegionAccessRequirement([BariausHill], 1)]
bull_demon.zeltennia_locations = [RegionAccessRequirement([Doguola], 1)]
bull_demon.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

minitaurus = MonsterRegion(MonsterNames.MINITAURUS)
minitaurus.fovoham_locations = [RegionAccessRequirement([Fovoham], 3)]
minitaurus.lesalia_locations = [RegionAccessRequirement([Zeklaus], 3)]
minitaurus.lionel_locations = [RegionAccessRequirement([BariausValley], 2)]
minitaurus.zeltennia_locations = [RegionAccessRequirement([Germinas], 1)]
minitaurus.limberry_locations = [RegionAccessRequirement([Poeskas], 2)]

sacred = MonsterRegion(MonsterNames.SACRED)
sacred.fovoham_locations = [
    RegionAccessRequirement([Fovoham], 4),
    RegionAccessRequirement([Fovoham, Lenalia], 3)
]
sacred.lesalia_locations = [RegionAccessRequirement([Zeklaus], 3)]
sacred.lionel_locations = [RegionAccessRequirement([BariausHill], 3)]
sacred.limberry_locations = [RegionAccessRequirement([Dolbodar], 5)]

morbol = MonsterRegion(MonsterNames.MORBOL)
morbol.gallione_locations = [RegionAccessRequirement([Mandalia], 3)]
morbol.fovoham_locations = [RegionAccessRequirement([Fovoham], 2)]
morbol.lesalia_locations = [RegionAccessRequirement([Araguay], 2)]
morbol.lionel_locations = [RegionAccessRequirement([Zigolis], 1)]
morbol.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]
morbol.limberry_locations = [RegionAccessRequirement([Dolbodar], 1)]

ochu = MonsterRegion(MonsterNames.OCHU)
ochu.gallione_locations = [RegionAccessRequirement([Lenalia], 3)]
ochu.lesalia_locations = [RegionAccessRequirement([Araguay], 3)]
ochu.lionel_locations = [RegionAccessRequirement([Zigolis], 3)]
ochu.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]

great_morbol = MonsterRegion(MonsterNames.GREAT_MORBOL)
great_morbol.zeltennia_locations = [RegionAccessRequirement([Finath], 4)]

woodman = MonsterRegion(MonsterNames.WOODMAN)
woodman.gallione_locations = [RegionAccessRequirement([Sweegy], 3)]
woodman.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
woodman.lesalia_locations = [RegionAccessRequirement([Araguay], 3)]
woodman.zeltennia_locations = [RegionAccessRequirement([Doguola], 2)]

trent = MonsterRegion(MonsterNames.TRENT)
trent.gallione_locations = [RegionAccessRequirement([Sweegy], 3)]
trent.fovoham_locations = [RegionAccessRequirement([Yuguo], 1)]
trent.lesalia_locations = [RegionAccessRequirement([Araguay], 2)]
trent.zeltennia_locations = [RegionAccessRequirement([Finath], 2)]

taiju = MonsterRegion(MonsterNames.TAIJU)
taiju.fovoham_locations = [RegionAccessRequirement([Yuguo], 3)]
taiju.lesalia_locations = [RegionAccessRequirement([Araguay], 3)]
taiju.zeltennia_locations = [RegionAccessRequirement([Finath], 4)]

dragon = MonsterRegion(MonsterNames.DRAGON)
dragon.gallione_locations = [RegionAccessRequirement([Lenalia], 1)]
dragon.lesalia_locations = [RegionAccessRequirement([Zeklaus], 3)]
dragon.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]
dragon.zeltennia_locations = [RegionAccessRequirement([Germinas], 1)]
dragon.limberry_locations = [RegionAccessRequirement([Bed], 2)]

blue_dragon = MonsterRegion(MonsterNames.BLUE_DRAGON)
blue_dragon.gallione_locations = [RegionAccessRequirement([Mandalia], 5)]
blue_dragon.fovoham_locations = [RegionAccessRequirement([Grog], 1)]
blue_dragon.lionel_locations = [RegionAccessRequirement([BariausValley], 3)]
blue_dragon.zeltennia_locations = [RegionAccessRequirement([Finath], 4)]
blue_dragon.limberry_locations = [
    RegionAccessRequirement([Bed], 4),
    RegionAccessRequirement([Bed, BerveniaCity], 3)
]

red_dragon = MonsterRegion(MonsterNames.RED_DRAGON)
red_dragon.gallione_locations = [RegionAccessRequirement([Mandalia], 5)]
red_dragon.lesalia_locations = [RegionAccessRequirement([Zeklaus], 3)]
red_dragon.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]
red_dragon.zeltennia_locations = [RegionAccessRequirement([Finath], 1)]

behemoth = MonsterRegion(MonsterNames.BEHEMOTH)
behemoth.lesalia_locations = [RegionAccessRequirement([BerveniaVolcano], 2)]
behemoth.lionel_locations = [RegionAccessRequirement([BariausValley], 3)]
behemoth.zeltennia_locations = [RegionAccessRequirement([Doguola], 1)]
behemoth.limberry_locations = [RegionAccessRequirement([Poeskas], 1)]

king_behemoth = MonsterRegion(MonsterNames.KING_BEHEMOTH)
king_behemoth.lesalia_locations = [RegionAccessRequirement([BerveniaVolcano, Riovanes], 5)]
king_behemoth.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]
king_behemoth.limberry_locations = [
    RegionAccessRequirement([Poeskas, Germinas], 1),
    RegionAccessRequirement([Bed], 3)
]

dark_behemoth = MonsterRegion(MonsterNames.DARK_BEHEMOTH)
dark_behemoth.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]
dark_behemoth.limberry_locations = [RegionAccessRequirement([Poeskas], 4)]

hyudra = MonsterRegion(MonsterNames.HYUDRA)
hyudra.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]
hyudra.zeltennia_locations = [RegionAccessRequirement([Nelveska], 5)]

hydra = MonsterRegion(MonsterNames.HYDRA)
hydra.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]

tiamat = MonsterRegion(MonsterNames.TIAMAT)
tiamat.lionel_locations = [RegionAccessRequirement([BariausHill], 5)]

uribo = MonsterRegion(MonsterNames.URIBO)
uribo.lionel_locations = [RegionAccessRequirement([Zigolis], 3)]
uribo.zeltennia_locations = [RegionAccessRequirement([Finath], 5)]
uribo.limberry_locations = [RegionAccessRequirement([Dolbodar], 2)]

porky = MonsterRegion(MonsterNames.PORKY)
porky.limberry_locations = [RegionAccessRequirement([Dolbodar], 5)]

wildbow = MonsterRegion(MonsterNames.WILDBOW)

monster_locations = [
    yellow_chocobo, black_chocobo, red_chocobo,
    goblin, black_goblin, gobbledeguck,
    red_panther, cuar, vampire,
    bomb, grenade, explosive,
    skeleton, bone_snatch, living_bone,
    ghoul, gust, revnant,
    floatiball, ahriman, plague,
    pisco_demon, squidlarkin, mindflare,
    juravis, steel_hawk, cockatoris,
    bull_demon, minitaurus, sacred,
    morbol, ochu, great_morbol,
    woodman, trent, taiju,
    dragon, blue_dragon, red_dragon,
    behemoth, king_behemoth, dark_behemoth,
    hyudra, hydra, tiamat,
    uribo, porky, wildbow
]

monster_locations_lookup: dict[str, MonsterRegion] = {
    monster.monster_name.value: monster for monster in monster_locations
}

for monster in monster_locations:
    monster.compiled_requirements = [
        *monster.gallione_locations,
        *monster.fovoham_locations,
        *monster.lesalia_locations,
        *monster.lionel_locations,
        *monster.zeltennia_locations,
        *monster.limberry_locations
    ]