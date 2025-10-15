from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Limberry import *
from ..regions.Zeltennia import BerveniaCity, Germinas
from ..regions.Lesalia import Zirekile

Bed.connections = [
    Connection(BerveniaCity, [HasZeltenniaPass]),
    Connection(Bethla)
]

Bed.locations = [
    FFTLocation("Bed Desert Story Battle"),
    FFTLocation("Bed Desert Rare Battle")
]

Bethla.connections = [
    Connection(Bed),
    Connection(Dolbodar),
    Connection(Zirekile, [HasLesaliaPass])
]

Bethla.locations = [
    FFTLocation("Bethla Garrison North Wall Story Battle"),
    FFTLocation("Bethla Garrison South Wall Story Battle"),
    FFTLocation("Bethla Garrison Sluice Story Battle"),
    FFTLocation("Recruit Orlandu"),
    FFTLocation("Bethla Garrison Shop Unlock")
]

Dolbodar.connections = [
    Connection(Bethla),
    Connection(Limberry)
]

Dolbodar.locations = [
    FFTLocation("Dolbodar Swamp Rare Battle")
]

Limberry.connections = [
    Connection(Dolbodar),
    Connection(Poeskas)
]

Limberry.locations = [
    FFTLocation("Limberry Castle Gates Story Battle"),
    FFTLocation("Inside Limberry Castle Story Battle"),
    FFTLocation("Limberry Castle Cemetary Story Battle"),
    FFTLocation("Recruit Meliadoul"),
    FFTLocation("Limberry Castle Shop Unlock")
]

Poeskas.connections = [
    Connection(Germinas, [HasZeltenniaPass]),
    Connection(Limberry)
]

Poeskas.locations = [
    FFTLocation("Poeskas Lake Story Battle"),
    FFTLocation("Poeskas Lake Rare Battle")
]