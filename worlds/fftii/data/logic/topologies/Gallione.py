from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Gallione import *
from ..regions.Fovoham import Fovoham
from ..regions.Lesalia import Zeklaus, Araguay
from ..regions.Murond import Murond, Orbonne

Gariland.connections = [
    Connection(Mandalia),
    Connection(Sweegy),
    Connection(Lenalia),
    Connection(Murond, [HasMurondPass])
]

Gariland.locations = [
    FFTLocation("Garliand Magic City Story Battle")
]

Mandalia.connections = [
    Connection(Gariland),
    Connection(ThievesFort),
    Connection(Igros)
]

Mandalia.locations = [
    FFTLocation("Mandalia Plains Story Battle"),
    FFTLocation("Mandalia Plains Rare Battle"),
    FFTLocation("Mandalia Plains Shop Unlock")
]

Igros.connections = [
    Connection(Mandalia),
    Connection(Zeakden)
]

Igros.locations = [
    FFTLocation("Igros Castle Story Battle")
]

Sweegy.connections = [
    Connection(Gariland),
    Connection(Dorter)
]

Sweegy.locations = [
    FFTLocation("Sweegy Woods Story Battle"),
    FFTLocation("Sweegy Woods Rare Battle")
]

Dorter.connections = [
    Connection(Sweegy),
    Connection(Zeklaus, [HasLesaliaPass]),
    Connection(Araguay, [HasLesaliaPass]),
    Connection(Orbonne, [HasMurondPass])
]

Dorter.locations = [
    FFTLocation("Dorter Slums Story Battle"),
    FFTLocation("Dorter City Story Battle")
]

ThievesFort.connections = [
    Connection(Mandalia)
]

ThievesFort.locations = [
    FFTLocation("Thieves' Fort Story Battle"),
    FFTLocation("Thieves' Fort Shop Unlock")
]

Lenalia.connections = [
    Connection(Gariland),
    Connection(Fovoham, [HasFovohamPass])
]

Lenalia.locations = [
    FFTLocation("Lenalia Plateau Story Battle"),
    FFTLocation("Lenalia Plateau Rare Battle")
]

Zeakden.connections = [
    Connection(Igros),
    Connection(Fovoham, [HasFovohamPass])
]

Zeakden.locations = [
    FFTLocation("Fort Zeakden Story Battle"),
    FFTLocation("Fort Zeakden Shop Unlock"),
    FFTLocation("Recruit Rad"),
    FFTLocation("Recruit Alicia"),
    FFTLocation("Recruit Lavian")
]