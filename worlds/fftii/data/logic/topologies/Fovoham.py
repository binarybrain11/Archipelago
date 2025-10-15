from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Fovoham import *
from ..regions.Gallione import Zeakden, Lenalia
from ..regions.Lesalia import Lesalia, Doguola, BerveniaVolcano

Grog.connections = [
    Connection(Yardow),
    Connection(Lesalia, [HasLesaliaPass]),
    Connection(Doguola, [HasLesaliaPass])
]

Grog.locations = [
    FFTLocation("Grog Hill Story Battle"),
    FFTLocation("Grog Hill Rare Battle")
]

Yardow.connections = [
    Connection(Grog),
    Connection(Yuguo)
]

Yardow.locations = [
    FFTLocation("Yardow Fort City Story Battle"),
    FFTLocation("Yardow Fort City Shop Unlock")
]

Yuguo.connections = [
    Connection(Yardow),
    Connection(Riovanes)
]

Yuguo.locations = [
    FFTLocation("Yuguo Woods Story Battle"),
    FFTLocation("Yuguo Woods Rare Battle")
]

Riovanes.connections = [
    Connection(Fovoham),
    Connection(Yuguo),
    Connection(BerveniaVolcano, [HasLesaliaPass]),
]

Riovanes.locations = [
    FFTLocation("Gate of Riovanes Story Battle"),
    FFTLocation("Inside Riovanes Castle Story Battle"),
    FFTLocation("Roof of Riovanes Castle Story Battle"),
    FFTLocation("Recruit Rafa"),
    FFTLocation("Recruit Malak"),
    FFTLocation("Riovanes Castle Shop Unlock")
]

Fovoham.connections = [
    Connection(Riovanes),
    Connection(Zeakden, [HasGallionePass]),
    Connection(Lenalia, [HasGallionePass])
]

Fovoham.locations = [
    FFTLocation("Fovoham Plains Story Battle"),
    FFTLocation("Fovoham Plains Rare Battle")
]