from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Zeltennia import *
from ..regions.Lesalia import Doguola
from ..regions.Limberry import Bed, Poeskas

BerveniaCity.connections = [
    Connection(Doguola, [HasLesaliaPass]),
    Connection(Bed, [HasLimberryPass]),
    Connection(Finath)
]

BerveniaCity.locations = [
    FFTLocation("Bervenia Free City Story Battle")
]

Finath.connections = [
    Connection(BerveniaCity),
    Connection(Zeltennia)
]

Finath.locations = [
    FFTLocation("Finath River Story Battle"),
    FFTLocation("Finath River Rare Battle")
]

Zeltennia.connections = [
    Connection(Finath),
    Connection(Zarghidas),
    Connection(Nelveska)
]

Zeltennia.locations = [
    FFTLocation("Zeltennia Castle Story Battle")
]

Zarghidas.connections = [
    Connection(Zeltennia),
    Connection(Germinas)
]

Zarghidas.locations = [
    FFTLocation("Zarghidas Trade City Sidequest Battle"),
    FFTLocation("Recruit Cloud")
]

Germinas.connections = [
    Connection(Zarghidas),
    Connection(Poeskas, [HasLimberryPass])
]

Germinas.locations = [
    FFTLocation("Germinas Peak Story Battle"),
    FFTLocation("Germinas Peak Rare Battle")
]

Nelveska.connections = [
    Connection(Zeltennia)
]

Nelveska.locations = [
    FFTLocation("Nelveska Temple Sidequest Battle"),
    FFTLocation("Recruit Reis (Human)")
]