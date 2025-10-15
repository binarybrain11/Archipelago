from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Lesalia import *
from ..regions.Gallione import Dorter
from ..regions.Fovoham import Grog, Riovanes
from ..regions.Limberry import Bethla
from ..regions.Lionel import Zaland

Araguay.connections = [
    Connection(Dorter, [HasGallionePass]),
    Connection(Zirekile)
]

Araguay.locations = [
    FFTLocation("Araguay Woods Story Battle")
]

Zeklaus.connections = [
    Connection(Dorter, [HasGallionePass]),
    Connection(Goland),
    Connection(BerveniaVolcano)
]

Zeklaus.locations = [
    FFTLocation("Zeklaus Desert Story Battle")
]

BerveniaVolcano.connections = [
    Connection(Zeklaus),
    Connection(Riovanes, [HasFovohamPass])
]

Zirekile.connections = [
    Connection(Araguay),
    Connection(Zaland, [HasLionelPass]),
    Connection(Bethla, [HasLimberryPass])
]

Zirekile.locations = [
    FFTLocation("Zirekile Falls Story Battle")
]

Goland.connections = [
    Connection(Zeklaus),
    Connection(Lesalia)
]

Goland.locations = [
    FFTLocation("Goland Coal City Story Battle"),
    FFTLocation("Goland Colliery Third Floor Sidequest Battle"),
    FFTLocation("Goland Colliery Second Floor Sidequest Battle"),
    FFTLocation("Goland Colliery First Floor Sidequest Battle"),
    FFTLocation("Goland Underground Passage Sidequest Battle"),
]

Lesalia.connections = [
    Connection(Goland),
    Connection(Grog, [HasFovohamPass])
]

Doguola.connections = [
    Connection(Grog)
]

Doguola.locations = [
    FFTLocation("Doguola Pass Story Battle")
]