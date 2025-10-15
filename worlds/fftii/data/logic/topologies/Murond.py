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
    FFTLocation("St. Murond Temple Story Battle"),
    FFTLocation("St. Murond Temple Hall Story Battle"),
    FFTLocation("Chapel of St. Murond Temple Story Battle")
]

Goug.connections = [
    Connection(Murond),
    Connection(Zigolis, [HasLionelPass])
]

Goug.locations = [
    FFTLocation("Slums of Goug Story Battle"),
    FFTLocation("Recruit Mustadio")
]

Orbonne.connections = [
    Connection(Dorter, [HasGallionePass]),
    Connection(MurondDeathCity, [HasZodiacStones])
]

Orbonne.locations = [
    FFTLocation("Underground Book Storage 1 Story Battle"),
    FFTLocation("Underground Book Storage 2 Story Battle"),
    FFTLocation("Underground Book Storage 3 Story Battle"),
    FFTLocation("Underground Book Storage 4 Story Battle"),
    FFTLocation("Underground Book Storage 5 Story Battle")
]

DeepDungeon.connections = [
    Connection(Warjilis,  [HasLionelPass])
]

DeepDungeon.locations = [
    FFTLocation("NOGIAS Sidequest Battle"),
    FFTLocation("TERMINATE Sidequest Battle"),
    FFTLocation("DELTA Sidequest Battle"),
    FFTLocation("VALKYRIES Sidequest Battle"),
    FFTLocation("MLAPAN Sidequest Battle"),
    FFTLocation("TIGER Sidequest Battle"),
    FFTLocation("BRIDGE Sidequest Battle"),
    FFTLocation("VOYAGE Sidequest Battle"),
    FFTLocation("HORROR Sidequest Battle"),
    FFTLocation("END Sidequest Battle"),
    FFTLocation("Recruit Byblos"),
    FFTLocation("Deep Dungeon Rare Battle")
]

MurondDeathCity.connections = [
    Connection(Orbonne) # This should never be relevant, but I like completionism
]

MurondDeathCity.locations = [
    FFTLocation("Murond Death City Story Battle"),
    FFTLocation("Lost Sacred Precincts Story Battle"),
    FFTLocation("Graveyard of Airships 1 Story Battle"),
    FFTLocation("Graveyard of Airships 2 Story Battle")
]