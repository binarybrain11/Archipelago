from ..Connection import Connection
from ..Requirements import *
from ..FFTLocation import FFTLocation

from ..regions.Jobs import *

Squire.locations = [
    FFTLocation("Squire Unlock", [])
]

Chemist.locations = [
    FFTLocation("Chemist Unlock", [])
]

Knight.locations = [
    FFTLocation("Knight Unlock", [Requirement(["Squire"])])
]

Archer.locations = [
    FFTLocation("Archer Unlock", [Requirement(["Squire"])])
]

Monk.locations = [
    FFTLocation("Monk Unlock", [Requirement(["Knight"])])
]

Thief.locations = [
    FFTLocation("Thief Unlock", [Requirement(["Archer"])])
]

Lancer.locations = [
    FFTLocation("Lancer Unlock", [Requirement(["Thief"])])
]

Geomancer.locations = [
    FFTLocation("Geomancer Unlock", [Requirement(["Monk"])])
]

Samurai.locations = [
    FFTLocation("Samurai Unlock", [Requirement(["Knight", "Monk", "Lancer"])])
]

Ninja.locations = [
    FFTLocation("Ninja Unlock", [Requirement(["Archer", "Thief", "Geomancer"])])
]

Dancer.locations = [
    FFTLocation("Dancer Unlock", [Requirement(["Lancer", "Geomancer"])])
]

Priest.locations = [
    FFTLocation("Priest Unlock", [Requirement(["Chemist"])])
]

Wizard.locations = [
    FFTLocation("Wizard Unlock", [Requirement(["Chemist"])])
]

Oracle.locations = [
    FFTLocation("Oracle Unlock", [Requirement(["Priest"])])
]

TimeMage.locations = [
    FFTLocation("Time Mage Unlock", [Requirement(["Wizard"])])
]

Mediator.locations = [
    FFTLocation("Mediator Unlock", [Requirement(["Oracle"])])
]

Summoner.locations = [
    FFTLocation("Summoner Unlock", [Requirement(["Time Mage"])])
]

Calculator.locations = [
    FFTLocation("Calculator Unlock", [Requirement(["Priest", "Wizard", "Oracle", "Time Mage"])])
]

Bard.locations = [
    FFTLocation("Bard Unlock", [Requirement(["Mediator", "Summoner"])])
]

Mime.locations = [
    FFTLocation("Mime Unlock", [
        Requirement(["Squire", "Chemist", "Lancer", "Geomancer", "Mediator", "Summoner"])
    ])
]