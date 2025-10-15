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
    FFTLocation("Zaland Fort City Story Battle")
]

BariausHill.connections = [
    Connection(Zaland),
    Connection(Lionel)
]

BariausHill.locations = [
    FFTLocation("Bariaus Hill Story Battle")
]

Lionel.connections = [
    Connection(Zigolis),
    Connection(BariausValley)
]

Lionel.locations = [
    FFTLocation("Gate of Lionel Castle Story Battle"),
    FFTLocation("Inside of Lionel Castle Story Battle")
]

BariausValley.connections = [
    Connection(Lionel),
    Connection(Golgorand),
    Connection(Warjilis)
]

BariausValley.locations = [
    FFTLocation("Bariaus Valley Story Battle")
]

Golgorand.connections = [
    Connection(BariausValley)
]

Golgorand.locations = [
    FFTLocation("Golgorand Execution Site Story Battle")
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
    FFTLocation("Zigolis Swamp Story Battle")
]
