from ..Requirements import *
from ..FFTLocation import FFTLocation, LocationNames

from ..regions.Jobs import *

Squire.locations = [
    FFTLocation(LocationNames.SQUIRE_UNLOCK, [])
]

Chemist.locations = [
    FFTLocation(LocationNames.CHEMIST_UNLOCK, [])
]

Knight.locations = [
    FFTLocation(LocationNames.KNIGHT_UNLOCK, [Requirement(["Squire"])])
]

Archer.locations = [
    FFTLocation(LocationNames.ARCHER_UNLOCK, [Requirement(["Squire"])])
]

Monk.locations = [
    FFTLocation(LocationNames.MONK_UNLOCK, [Requirement(["Knight"])])
]

Thief.locations = [
    FFTLocation(LocationNames.THIEF_UNLOCK, [Requirement(["Archer"])])
]

Lancer.locations = [
    FFTLocation(LocationNames.LANCER_UNLOCK, [Requirement(["Thief"])])
]

Geomancer.locations = [
    FFTLocation(LocationNames.GEOMANCER_UNLOCK, [Requirement(["Monk"])])
]

Samurai.locations = [
    FFTLocation(LocationNames.SAMURAI_UNLOCK, [Requirement(["Knight", "Monk", "Lancer"])])
]

Ninja.locations = [
    FFTLocation(LocationNames.NINJA_UNLOCK, [Requirement(["Archer", "Thief", "Geomancer"])])
]

Dancer.locations = [
    FFTLocation(LocationNames.DANCER_UNLOCK, [Requirement(["Lancer", "Geomancer"])])
]

Priest.locations = [
    FFTLocation(LocationNames.PRIEST_UNLOCK, [Requirement(["Chemist"])])
]

Wizard.locations = [
    FFTLocation(LocationNames.WIZARD_UNLOCK, [Requirement(["Chemist"])])
]

Oracle.locations = [
    FFTLocation(LocationNames.ORACLE_UNLOCK, [Requirement(["Priest"])])
]

TimeMage.locations = [
    FFTLocation(LocationNames.TIME_MAGE_UNLOCK, [Requirement(["Wizard"])])
]

Mediator.locations = [
    FFTLocation(LocationNames.MEDIATOR_UNLOCK, [Requirement(["Oracle"])])
]

Summoner.locations = [
    FFTLocation(LocationNames.SUMMONER_UNLOCK, [Requirement(["Time Mage"])])
]

Calculator.locations = [
    FFTLocation(LocationNames.CALCULATOR_UNLOCK, [Requirement(["Priest", "Wizard", "Oracle", "Time Mage"])])
]

Bard.locations = [
    FFTLocation(LocationNames.BARD_UNLOCK, [Requirement(["Mediator", "Summoner"])])
]

Mime.locations = [
    FFTLocation(LocationNames.MIME_UNLOCK, [
        Requirement(["Squire", "Chemist", "Lancer", "Geomancer", "Mediator", "Summoner"])
    ])
]