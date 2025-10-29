from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation, LocationNames, RareBattleLocation

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
    FFTLocation(LocationNames.GROG_STORY, battle_level=3),
    RareBattleLocation(LocationNames.GROG_RARE, battle_level=5)
]

Yardow.connections = [
    Connection(Grog),
    Connection(Yuguo)
]

Yardow.locations = [
    FFTLocation(LocationNames.YARDOW_STORY, battle_level=3),
    FFTLocation(LocationNames.YARDOW_SHOP)
]

Yuguo.connections = [
    Connection(Yardow),
    Connection(Riovanes)
]

Yuguo.locations = [
    FFTLocation(LocationNames.YUGUO_STORY, battle_level=3),
    RareBattleLocation(LocationNames.YUGUO_RARE, battle_level=5)
]

Riovanes.connections = [
    Connection(Fovoham),
    Connection(Yuguo),
    Connection(BerveniaVolcano, [HasLesaliaPass]),
]

Riovanes.locations = [
    FFTLocation(LocationNames.RIOVANES_1_STORY, battle_level=3),
    FFTLocation(LocationNames.RIOVANES_2_STORY, battle_level=3),
    FFTLocation(LocationNames.RIOVANES_3_STORY, battle_level=3),
    FFTLocation(LocationNames.RIOVANES_SHOP, battle_level=3),
    FFTLocation(LocationNames.RAMZA_CHAPTER_4_UNLOCK, battle_level=3),
    FFTLocation(LocationNames.RAFA_RECRUIT, battle_level=3),
    FFTLocation(LocationNames.MALAK_RECRUIT, battle_level=3)
]

Fovoham.connections = [
    Connection(Riovanes),
    Connection(Zeakden, [HasGallionePass]),
    Connection(Lenalia, [HasGallionePass])
]

Fovoham.locations = [
    FFTLocation(LocationNames.FOVOHAM_STORY),
    RareBattleLocation(LocationNames.FOVOHAM_RARE, battle_level=5)
]