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
    FFTLocation("Araguay Woods Story Battle", battle_level=2),
    FFTLocation("Recruit Boco", battle_level=2),
    FFTLocation("Araguay Woods Rare Battle")
]

Zeklaus.connections = [
    Connection(Dorter, [HasGallionePass]),
    Connection(Goland),
    Connection(BerveniaVolcano)
]

Zeklaus.locations = [
    FFTLocation("Zeklaus Desert Story Battle"),
    FFTLocation("Zeklaus Desert Rare Battle"),
    FFTLocation("Zeklaus Desert Shop Unlock")
]

BerveniaVolcano.connections = [
    Connection(Zeklaus),
    Connection(Riovanes, [HasFovohamPass])
]

BerveniaVolcano.locations = [
    FFTLocation("Bervenia Volvano Rare Battle")
]

Zirekile.connections = [
    Connection(Araguay),
    Connection(Zaland, [HasLionelPass]),
    Connection(Bethla, [HasLimberryPass])
]

Zirekile.locations = [
    FFTLocation("Zirekile Falls Story Battle", battle_level=2),
    FFTLocation("Zirekile Falls Rare Battle"),
    FFTLocation("Zirekile Falls Shop Unlock", battle_level=2)
]

Goland.connections = [
    Connection(Zeklaus),
    Connection(Lesalia)
]

Goland.locations = [
    FFTLocation("Goland Coal City Story Battle", battle_level=2),
    FFTLocation("Goland Colliery Third Floor Sidequest Battle", battle_level=4),
    FFTLocation("Goland Colliery Second Floor Sidequest Battle", battle_level=4),
    FFTLocation("Goland Colliery First Floor Sidequest Battle", battle_level=4),
    FFTLocation("Goland Underground Passage Sidequest Battle", battle_level=4),
    FFTLocation("Recruit Beowulf", battle_level=4),
    FFTLocation("Recruit Reis (Dragon)", battle_level=4),
    FFTLocation("Recruit Worker 8", battle_level=4)
]

Lesalia.connections = [
    Connection(Goland),
    Connection(Grog, [HasFovohamPass])
]

Lesalia.locations = [
    FFTLocation("Back Gate of Lesalia Castle Story Battle", battle_level=2),
    FFTLocation("Lesalia Imperial Capital Shop Unlock", battle_level=2)
]
