from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Murond import *
from ..regions.Gallione import Gariland, Dorter
from ..regions.Lionel import Zigolis, Warjilis

Murond.connections = [
    Connection(Gariland, [HasGallionePass]),
    Connection(Goug)
]

Murond.locations = [
    FFTLocation("St. Murond Temple Story Battle", battle_level=5),
    FFTLocation("St. Murond Temple Hall Story Battle", battle_level=5),
    FFTLocation("Chapel of St. Murond Temple Story Battle", battle_level=5)
]

Goug.connections = [
    Connection(Murond),
    Connection(Zigolis, [HasLionelPass])
]

Goug.locations = [
    FFTLocation("Slums of Goug Story Battle", battle_level=2),
    FFTLocation("Recruit Mustadio", battle_level=2)
]

Orbonne.connections = [
    Connection(Dorter, [HasGallionePass]),
    Connection(MurondDeathCity, [HasZodiacStones])
]

Orbonne.locations = [
    FFTLocation("Underground Book Storage 1 Story Battle", battle_level=3),
    FFTLocation("Underground Book Storage 2 Story Battle", battle_level=3),
    FFTLocation("Underground Book Storage 3 Story Battle", battle_level=3),
    FFTLocation("Underground Book Storage 4 Story Battle", battle_level=5),
    FFTLocation("Underground Book Storage 5 Story Battle", battle_level=5),
    FFTLocation("Orbonne Monastery Shop Unlock", battle_level=3)
]

DeepDungeon.connections = [
    Connection(Warjilis,  [HasLionelPass])
]

DeepDungeon.locations = [
    FFTLocation("NOGIAS Sidequest Battle", battle_level=5),
    FFTLocation("TERMINATE Sidequest Battle", battle_level=5),
    FFTLocation("DELTA Sidequest Battle", battle_level=5),
    FFTLocation("VALKYRIES Sidequest Battle", battle_level=5),
    FFTLocation("MLAPAN Sidequest Battle", battle_level=5),
    FFTLocation("TIGER Sidequest Battle", battle_level=5),
    FFTLocation("BRIDGE Sidequest Battle", battle_level=5),
    FFTLocation("VOYAGE Sidequest Battle", battle_level=5),
    FFTLocation("HORROR Sidequest Battle", battle_level=5),
    FFTLocation("END Sidequest Battle", battle_level=5),
    FFTLocation("Recruit Byblos", battle_level=5),
]

MurondDeathCity.connections = [
    Connection(Orbonne) # This should never be relevant, but I like completionism
]

MurondDeathCity.locations = [
    FFTLocation("Murond Death City Story Battle", battle_level=5),
    FFTLocation("Lost Sacred Precincts Story Battle", battle_level=5),
    FFTLocation("Graveyard of Airships 1 Story Battle", battle_level=5),
    FFTLocation("Graveyard of Airships 2 Story Battle", battle_level=5)
]