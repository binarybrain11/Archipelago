from ..Connection import Connection
from ..Monsters import MonsterNames
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
    FFTLocation("Bed Desert Story Battle", battle_level=4),
    FFTLocation("Bed Desert Rare Battle")
]

Bethla.connections = [
    Connection(Bed),
    Connection(Dolbodar),
    Connection(Zirekile, [HasLesaliaPass])
]

Bethla.locations = [
    FFTLocation("Bethla Garrison North Wall Story Battle", battle_level=4),
    FFTLocation("Bethla Garrison South Wall Story Battle", battle_level=4),
    FFTLocation("Bethla Garrison Sluice Story Battle", battle_level=4),
    FFTLocation("Recruit Orlandu", battle_level=4),
    FFTLocation("Bethla Garrison Shop Unlock", battle_level=4)
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
    FFTLocation("Limberry Castle Gates Story Battle", battle_level=5),
    FFTLocation("Inside Limberry Castle Story Battle", battle_level=5),
    FFTLocation("Limberry Castle Cemetary Story Battle", battle_level=5),
    FFTLocation("Recruit Meliadoul", battle_level=5),
    FFTLocation("Limberry Castle Shop Unlock", battle_level=5)
]

Poeskas.connections = [
    Connection(Germinas, [HasZeltenniaPass]),
    Connection(Limberry)
]

Poeskas.locations = [
    FFTLocation("Poeskas Lake Story Battle", battle_level=5),
    FFTLocation("Poeskas Lake Rare Battle")
]