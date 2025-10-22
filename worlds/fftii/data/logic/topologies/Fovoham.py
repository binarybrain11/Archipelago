from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Fovoham import *
from ..regions.Gallione import Zeakden, Lenalia
from ..regions.Lesalia import Lesalia, BerveniaVolcano
from ..regions.Zeltennia import Doguola

Grog.connections = [
    Connection(Yardow),
    Connection(Lesalia, [HasLesaliaPass]),
    Connection(Doguola, [HasZeltenniaPass])
]

Grog.locations = [
    FFTLocation("Grog Hill Story Battle", battle_level=3),
    FFTLocation("Grog Hill Rare Battle")
]

Yardow.connections = [
    Connection(Grog),
    Connection(Yuguo)
]

Yardow.locations = [
    FFTLocation("Yardow Fort City Story Battle", battle_level=3),
    FFTLocation("Yardow Fort City Shop Unlock")
]

Yuguo.connections = [
    Connection(Yardow),
    Connection(Riovanes)
]

Yuguo.locations = [
    FFTLocation("Yuguo Woods Story Battle", battle_level=3),
    FFTLocation("Yuguo Woods Rare Battle")
]

Riovanes.connections = [
    Connection(Fovoham),
    Connection(Yuguo),
    Connection(BerveniaVolcano, [HasLesaliaPass]),
]

Riovanes.locations = [
    FFTLocation("Gate of Riovanes Story Battle", battle_level=3),
    FFTLocation("Inside Riovanes Castle Story Battle", battle_level=3),
    FFTLocation("Roof of Riovanes Castle Story Battle", battle_level=3),
    FFTLocation("Recruit Rafa", battle_level=3),
    FFTLocation("Recruit Malak", battle_level=3),
    FFTLocation("Riovanes Castle Shop Unlock", battle_level=3),
    FFTLocation("Chapter 4 Ramza Squire Job Unlock", battle_level=3)
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