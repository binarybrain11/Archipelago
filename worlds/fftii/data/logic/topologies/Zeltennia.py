from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation


from ..regions.Zeltennia import *
from ..regions.Fovoham import Grog
from ..regions.Limberry import Bed, Poeskas

BerveniaCity.connections = [
    Connection(Doguola, [HasLesaliaPass]),
    Connection(Bed, [HasLimberryPass]),
    Connection(Finath)
]

BerveniaCity.locations = [
    FFTLocation("Bervenia Free City Story Battle", battle_level=4)
]

Finath.connections = [
    Connection(BerveniaCity),
    Connection(Zeltennia)
]

Finath.locations = [
    FFTLocation("Finath River Story Battle", battle_level=4),
    FFTLocation("Finath River Rare Battle", battle_level=4)
]

Zeltennia.connections = [
    Connection(Finath),
    Connection(Zarghidas),
    Connection(Nelveska)
]

Zeltennia.locations = [
    FFTLocation("Zeltennia Castle Story Battle", battle_level=4)
]

Zarghidas.connections = [
    Connection(Zeltennia),
    Connection(Germinas)
]

Zarghidas.locations = [
    FFTLocation("Zarghidas Trade City Sidequest Battle", battle_level=4),
    FFTLocation("Recruit Cloud", battle_level=4)
]

Germinas.connections = [
    Connection(Zarghidas),
    Connection(Poeskas, [HasLimberryPass])
]

Germinas.locations = [
    FFTLocation("Germinas Peak Story Battle", battle_level=5),
    FFTLocation("Germinas Peak Rare Battle", battle_level=5)
]

Nelveska.connections = [
    Connection(Zeltennia)
]

Nelveska.locations = [
    FFTLocation("Nelveska Temple Sidequest Battle", battle_level=5),
    FFTLocation("Recruit Reis (Human)", battle_level=5)
]

Doguola.connections = [
    Connection(Grog),
    Connection(BerveniaCity)
]

Doguola.locations = [
    FFTLocation("Doguola Pass Story Battle", battle_level=3),
    FFTLocation("Doguola Pass Rare Battle")
]