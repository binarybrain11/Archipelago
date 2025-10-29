from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation, RareBattleLocation, LocationNames

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
    FFTLocation(LocationNames.GARILAND_STORY)
]

Mandalia.connections = [
    Connection(Gariland),
    Connection(ThievesFort),
    Connection(Igros)
]

Mandalia.locations = [
    FFTLocation(LocationNames.MANDALIA_STORY),
    FFTLocation(LocationNames.MANDALIA_SHOP),
    RareBattleLocation(LocationNames.MANDALIA_RARE, battle_level=5)
]

Igros.connections = [
    Connection(Mandalia),
    Connection(Zeakden)
]

Igros.locations = [
    FFTLocation(LocationNames.IGROS_STORY, battle_level=5)
]

Sweegy.connections = [
    Connection(Gariland),
    Connection(Dorter)
]

Sweegy.locations = [
    FFTLocation(LocationNames.SWEEGY_STORY),
    RareBattleLocation(LocationNames.SWEEGY_RARE, battle_level=5)
]

Dorter.connections = [
    Connection(Sweegy),
    Connection(Zeklaus, [HasLesaliaPass]),
    Connection(Araguay, [HasLesaliaPass]),
    Connection(Orbonne, [HasMurondPass])
]

Dorter.locations = [
    FFTLocation(LocationNames.DORTER_1_STORY),
    FFTLocation(LocationNames.DORTER_2_STORY, battle_level=2)
]

ThievesFort.connections = [
    Connection(Mandalia)
]

ThievesFort.locations = [
    FFTLocation(LocationNames.THIEVES_FORT_STORY)
]

Lenalia.connections = [
    Connection(Gariland),
    Connection(Fovoham, [HasFovohamPass])
]

Lenalia.locations = [
    FFTLocation(LocationNames.LENALIA_STORY),
    FFTLocation(LocationNames.LENALIA_SHOP),
    RareBattleLocation(LocationNames.LENALIA_RARE, battle_level=5)

]

Zeakden.connections = [
    Connection(Igros),
    Connection(Fovoham, [HasFovohamPass])
]

Zeakden.locations = [
    FFTLocation(LocationNames.ZEAKDEN_STORY),
    FFTLocation(LocationNames.ZEAKDEN_SHOP),
    FFTLocation(LocationNames.RAMZA_CHAPTER_2_UNLOCK),
    FFTLocation(LocationNames.RAD_RECRUIT),
    FFTLocation(LocationNames.ALICIA_RECRUIT),
    FFTLocation(LocationNames.LAVIAN_RECRUIT)
]