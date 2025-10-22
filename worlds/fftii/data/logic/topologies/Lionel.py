from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation


from ..regions.Lionel import *
from ..regions.Lesalia import Zirekile
from ..regions.Murond import Goug, DeepDungeon

Zaland.connections = [
    Connection(Zirekile),
    Connection(BariausHill)
]

Zaland.locations = [
    FFTLocation("Zaland Fort City Story Battle", battle_level=2)
]

BariausHill.connections = [
    Connection(Zaland),
    Connection(Lionel)
]

BariausHill.locations = [
    FFTLocation("Bariaus Hill Story Battle", battle_level=2),
    FFTLocation("Bariaus Hill Rare Battle"),
    FFTLocation("Bariaus Hill Shop Unlock", battle_level=2)
]

Lionel.connections = [
    Connection(Zigolis),
    Connection(BariausValley)
]

Lionel.locations = [
    FFTLocation("Gate of Lionel Castle Story Battle", battle_level=2),
    FFTLocation("Inside of Lionel Castle Story Battle", battle_level=2),
    FFTLocation("Lionel Castle Shop Unlock", battle_level=2)
]

BariausValley.connections = [
    Connection(Lionel),
    Connection(Golgorand),
    Connection(Warjilis)
]

BariausValley.locations = [
    FFTLocation("Bariaus Valley Story Battle", battle_level=2),
    FFTLocation("Recruit Agrias", battle_level=2),
    FFTLocation("Bariaus Valley Rare Battle"),
    FFTLocation("Bariaus Valley Shop Unlock", battle_level=2)
]

Golgorand.connections = [
    Connection(BariausValley)
]

Golgorand.locations = [
    FFTLocation("Golgorand Execution Site Story Battle", battle_level=2)
]

Warjilis.connections = [
    Connection(BariausValley),
    Connection(DeepDungeon, [HasMurondPass])
]

Zigolis.connections = [
    Connection(Lionel),
    Connection(Goug, [HasMurondPass])
]

Zigolis.locations = [
    FFTLocation("Zigolis Swamp Story Battle", battle_level=2),
    FFTLocation("Zigolis Swamp Rare Battle")
]
