class Requirement():
    items_needed: list[str] = []
    other_requirements: list["Requirement"] = []
    energy_tanks_needed: int = 0

    def __init__(self, items_needed, other_requirements):
        self.items_needed = items_needed
        self.other_requirements = other_requirements

    def __repr__(self):
        return self.__class__.__name__

class MissileRequirement(Requirement):
    power: int

    def __init__(self, items_needed, other_requirements, power):
        super().__init__(items_needed, other_requirements)
        self.power = power

class FusionLocation():
    name: str
    major: bool
    requirements: list[Requirement]

    def __init__(self, name, major, requirements):
        self.name = name
        self.major = major
        self.requirements = requirements

class Connection():
    destination: "FusionRegion"
    requirements: list[Requirement]
    one_way: bool

    def __init__(self, destination, requirements, one_way=False):
        self.destination = destination
        self.requirements = requirements
        self.one_way = one_way

class FusionRegion():
    name: str
    connections: list[Connection] = []
    locations: list[FusionLocation] = []

# Requirements
class HasMorph(Requirement):
    items_needed = ["Morph Ball"]

class HasVaria(Requirement):
    items_needed = ["Varia Suit"]

class HasGravity(Requirement):
    items_needed = ["Gravity Suit"]

class HasHiJump(Requirement):
    items_needed = ["Hi-Jump"]

class HasSpaceJump(Requirement):
    items_needed = ["Space Jump"]

class HasSpeedBooster(Requirement):
    items_needed = ["Speed Booster"]

class HasScrewAttack(Requirement):
    items_needed = ["Screw Attack"]

class HasMissile(Requirement):
    items_needed = ["Missile Data"]

class HasChargeBeam(Requirement):
    items_needed = ["Charge Beam"]

class HasWaveBeam(Requirement):
    items_needed = ["Wave Beam"]

class HasKeycard1(Requirement):
    energy_tanks_needed = 3
    items_needed = ["Level 1 Keycard"]

class HasKeycard2(Requirement):
    energy_tanks_needed = 5
    items_needed = ["Level 2 Keycard"]

class HasKeycard1And2(Requirement):
    energy_tanks_needed = 5
    items_needed = ["Level 1 Keycard", "Level 2 Keycard"]

class HasKeycard3(Requirement):
    energy_tanks_needed = 7
    items_needed = ["Level 3 Keycard"]

class HasKeycard4(Requirement):
    energy_tanks_needed = 10
    items_needed = ["Level 4 Keycard"]


class CanJumpHigh(Requirement):
    other_requirements = [
        Requirement(["Hi-Jump"], []),
        Requirement(["Space Jump"], [])
    ]

class CanLavaDive(Requirement):
    items_needed = ["Varia Suit", "Gravity Suit"]

class CanWallJump(Requirement):
    items_needed = ["Space Jump"]

class CanBomb(Requirement):
    items_needed = ["Morph Ball"]
    other_requirements = [
        Requirement(["Bomb Data"], []),
        Requirement(["Power Bomb Data"], [])
    ]

class CanPowerBomb(Requirement):
    items_needed = ["Morph Ball", "Power Bomb Data"]

class CanPowerBombAndJumpHigh(Requirement):
    items_needed = ["Morph Ball", "Power Bomb Data"]
    other_requirements = [CanJumpHigh]

class CanBallJump(Requirement):
    items_needed = ["Morph Ball"]
    other_requirements = [
        Requirement(["Bomb Data"], []),
        Requirement(["Hi-Jump"], [])
    ]

class CanBallJumpAndBomb(Requirement):
    other_requirements = [CanBomb, Requirement(["Hi-Jump"], [CanPowerBomb])]

class CanScrewAttackAndSpaceJump(Requirement):
    items_needed = ["Screw Attack", "Space Jump"]

class CanJumpHighUnderwater(Requirement):
    items_needed = ["Gravity Suit"]
    other_requirements = [CanJumpHigh]

class CanSpeedBoosterUnderwater(Requirement):
    items_needed = ["Gravity Suit", "Speed Booster"]

class CanPlasmaBossws(Requirement):
    items_needed = ["Charge Beam", "Plasma Beam"]

class CanFreezeEnemies(Requirement):
    other_requirements = [
        Requirement(["Ice Missile"], [HasMissile]),
        Requirement(["Diffusion Missile"], [HasMissile]),
        Requirement(["Ice Beam"], [])
    ]

class CanBeatToughEnemy(Requirement):
    other_requirements = [HasChargeBeam, HasMissile]

class CanBeatToughEnemyAndJumpHigh(Requirement):
    other_requirements = [
        Requirement(["Hi-Jump"], [CanBeatToughEnemy]),
        Requirement(["Space Jump"], [CanBeatToughEnemy])
    ]

class CanActivatePillar(Requirement):
    other_requirements = [CanBomb, HasWaveBeam]

class CanDiffusionMissile(Requirement):
    items_needed = ["Missile Data", "Diffusion Missile"]

class CanDefeatSmallGeron(Requirement):
    other_requirements = [
        Requirement(["Missile Data"], []),
        CanPowerBomb,
        Requirement(["Screw Attack"], [])
    ]

class CanDefeatMediumGeron(Requirement):
    other_requirements = [
        Requirement(["Missile Data", "Super Missile"], []),
        CanPowerBomb,
        Requirement(["Screw Attack"], [])
    ]

class CanDefeatLargeGeron(Requirement):
    other_requirements = [
        CanPowerBomb,
        Requirement(["Screw Attack"], [])
    ]

class CanFightBeginnerBoss(Requirement):
    items_needed = ["Missile Data"]

class CanFightBoss(Requirement):
    energy_tanks_needed = 2
    items_needed = ["Missile Data", "Charge Beam"]

class CanFightMidgameBoss(Requirement):
    items_needed = ["Super Missile"]
    other_requirements = [CanFightBoss]

class CanFightLateGameBoss(Requirement):
    items_needed = ["Plasma Beam", "Space Jump"]
    other_requirements = [CanFightMidgameBoss]

class CanEscapeZazabi(Requirement):
    items_needed = ["Charge Beam", "Missile Data"]
    other_requirements = [CanJumpHigh]

class CanReachAnimals(Requirement):
    items_needed = ["Speed Booster"]
    other_requirements = [CanFreezeEnemies, HasSpaceJump]

class CanReachGenesisSpeedway(Requirement):
    items_needed = ["Morph Ball", "Power Bomb Data"]
    other_requirements = [CanBallJump]

class CanCrossFromReactorToSector2(Requirement):
    items_needed = ["Space Jump", "Missile Data"]
    other_requirements = [CanBomb]

class CanReachAnimorphs(Requirement):
    items_needed = ["Space Jump", "Charge Beam", "Wave Beam", "Missile Data", "Super Missile"]

class CanReachOasisStorage(Requirement):
    other_requirements = [
        CanPowerBomb,
        Requirement(["Hi-Jump"], [CanBomb])
    ]

class CanAscendBOXRoom(Requirement):
    items_needed = ["Charge Beam", "Missile Data"]
    other_requirements = [CanJumpHigh]

class CanNavigateLavaMaze(Requirement):
    items_needed = ["Morph Ball", "Power Bomb Data"]
    other_requirements = [CanLavaDive]

class CanAccessL2SecurityRoom(Requirement):
    items_needed = ["Speed Booster"]
    other_requirements = [CanBallJumpAndBomb]

class CanAccessDrainPipe(Requirement):
    items_needed = ["Morph Ball"]
    other_requirements = [
        HasWaveBeam,
        CanPowerBomb,
        Requirement(["Missile Data", "Super Missile"], []),
        Requirement(["Screw Attack", "Gravity Suit"], [])
    ]

class CanAscendCheddarBay(Requirement):
    items_needed = ["Missile Data"]
    other_requirements = [CanBomb]

class CanAccessReservoirVault(Requirement):
    other_requirements = [
        Requirement(["Hi-Jump"], [CanBomb])
    ]

class CanAccessSanctuaryCache(Requirement):
    other_requirements = [
        Requirement(["Wave Beam", "Charge Beam"], []),
        Requirement(["Wave Beam", "Missile Data", "Morph Ball"], []),
        Requirement(["Power Bomb Data", "Missile Data", "Morph Ball"], []),
        Requirement(["Power Bomb Data", "Charge Beam", "Morph Ball"], []),
    ]

class CanEscapeNightmareRoom(Requirement):
    items_needed = ["Gravity Suit", "Speed Booster"]
    other_requirements = [CanFightLateGameBoss]

class CanAccessRipperRoad(Requirement):
    items_needed = ["Morph Ball", "Hi-Jump"]
    other_requirements = [CanFreezeEnemies]

class CanAccessRipperTreasure(Requirement):
    items_needed = ["Power Bomb Data"]
    other_requirements = [
        HasSpaceJump,
        Requirement(["Hi-Jump"], [CanFreezeEnemies])
    ]

#region Region Definitions

# Main Deck Regions

class MainDeckHub(FusionRegion):
    name = "Main Deck Hub"

class ArachnusZone(FusionRegion):
    name = "Arachnus Zone"

class OperationsDeck(FusionRegion):
    name = "Operations Deck"

class HabitationDeck(FusionRegion):
    name = "Habitation Deck"

class SectorHub(FusionRegion):
    name = "Sector Hub"

class ReactorZone(FusionRegion):
    name = "Reactor Zone"

class YakuzaZone(FusionRegion):
    name = "Yakuza Zone"

class AuxiliaryReactor(FusionRegion):
    name = "Auxiliary Reactor"

class NexusStorage(FusionRegion):
    name = "Nexus Storage"

# Sector 1 Regions

class Sector1Hub(FusionRegion):
    name = "Sector 1 Hub"

class Sector1ToSector2(FusionRegion):
    name = "Sector 1 to Sector 2"

class Sector1ToSector3(FusionRegion):
    name = "Sector 1 to Sector 3"

class Sector1FirstStabilizerZone(FusionRegion):
    name = "Sector 1 First Stabilizer Zone"

class Sector1SecondStabilizerZone(FusionRegion):
    name = "Sector 1 Second Stabilizer Zone"

class Sector1ChargeCoreZone(FusionRegion):
    name = "Sector 1 Charge Core Zone"

class Sector1AfterChargeCoreZone(FusionRegion):
    name = "Sector 1 After Charge Core Zone"

class Sector1TourianExit(FusionRegion):
    name = "Sector 1 Tourian Exit"

class Sector1TourianHub(FusionRegion):
    name = "Sector 1 Tourian Hub"

# Sector 2 Regions

class Sector2Hub(FusionRegion):
    name = "Sector 2 Hub"

class Sector2ToSector4(FusionRegion):
    name = "Sector 2 to Sector 4"

class Sector2LeftSide(FusionRegion):
    name = "Sector 2 Left Side"

class Sector2ZazabiZone(FusionRegion):
    name = "Sector 2 Zazabi Zone"

class Sector2ZazabiZoneUpper(FusionRegion):
    name = "Sector 2 Zazabi Zone Upper"

class Sector2NettoriZone(FusionRegion):
    name = "Sector 2 Nettori Zone"

# Sector 3 Regions

class Sector3Hub(FusionRegion):
    name = "Sector 3 Hub"

class Sector3ToSector5(FusionRegion):
    name = "Sector 3 to Sector 5"

class Sector3SecurityZone(FusionRegion):
    name = "Sector 3 Security Zone"

class Sector3MainShaft(FusionRegion):
    name = "Sector 3 Main Shaft"

class Sector3BoilerZone(FusionRegion):
    name = "Sector 3 Boiler Zone"

class Sector3BOXZone(FusionRegion):
    name = "Sector 3 BOX Zone"

class Sector3Attic(FusionRegion):
    name = "Sector 3 Attic"

class Sector3RightShaft(FusionRegion):
    name = "Sector 3 Right Shaft"

# Sector 4 Regions

class Sector4Hub(FusionRegion):
    name = "Sector 4 Hub"

class Sector4UpperZone(FusionRegion):
    name = "Sector 4 Upper Zone"

class Sector4SerrisZone(FusionRegion):
    name = "Sector 4 Serris Zone"

class Sector4ToSector6(FusionRegion):
    name = "Sector 4 to Sector 6"

class Sector4PumpControl(FusionRegion):
    name = "Sector 4 Pump Control"

class Sector4UpperWaterZone(FusionRegion):
    name = "Sector 4 Upper Water Zone"

class Sector4SecurityZone(FusionRegion):
    name = "Sector 4 Security Zone"

class Sector4LowerSecurityZone(FusionRegion):
    name = "Sector 4 Lower Security Zone"

class Sector4SecurityRoom(FusionRegion):
    name = "Sector 4 Security Room"

class Sector4RightWaterZone(FusionRegion):
    name = "Sector 4 Right Water Zone"

class Sector4DataZone(FusionRegion):
    name = "Sector 4 Data Zone"

# Sector 5 Regions

class Sector5Hub(FusionRegion):
    name = "Sector 5 Hub"

class Sector5ToSector6(FusionRegion):
    name = "Sector 5 to Sector 6"

class Sector5BigRoom(FusionRegion):
    name = "Sector 5 Big Room"

class Sector5FrozenHub(FusionRegion):
    name = "Sector 5 Frozen Hub"

class Sector5SecurityZone(FusionRegion):
    name = "Sector 5 Security Zone"

class Sector5DataRoom(FusionRegion):
    name = "Sector 5 Data Room"

class Sector5BeforeNightmareHub(FusionRegion):
    name = "Sector 5 Before Nightmare Hub"

class Sector5NightmareHub(FusionRegion):
    name = "Sector 5 Nightmare Hub"

class Sector5NightmareZone(FusionRegion):
    name = "Sector 5 Nightmare Zone"

# Sector 6 Regions

class Sector6Hub(FusionRegion):
    name = "Sector 6 Hub"

class Sector6Crossroads(FusionRegion):
    name = "Sector 6 Crossroads"

class Sector6BeforeXBOXZone(FusionRegion):
    name = "Sector 6 Before X-BOX Zone"

class Sector6XBOXZone(FusionRegion):
    name = "Sector 6 X-BOX Zone"

class Sector6AfterXBOXZone(FusionRegion):
    name = "Sector 6 After X-BOX Zone"

class Sector6RestrictedZone(FusionRegion):
    name = "Sector 6 RestrictedZone"

class Sector6BeforeVariaCoreXZone(FusionRegion):
    name = "Sector 6 Before Varia Core-X Zone"

class Sector6VariaCoreXZone(FusionRegion):
    name = "Sector 6 Varia Core-X Zone"

class Sector6AfterVariaCoreXZone(FusionRegion):
    name = "Sector 6 After Varia Core-X Zone"

#endregion

#region Main Deck Topology
MainDeckHub.connections = [
    Connection(OperationsDeck, []),
    Connection(ArachnusZone, [CanDefeatSmallGeron, Requirement(["Morph Ball", "Screw Attack", "Space Jump"], [])]),
    Connection(HabitationDeck, [HasKeycard2]),
    Connection(SectorHub, [HasMorph]),
    Connection(ReactorZone, [HasKeycard4, CanPowerBomb]),
    Connection(NexusStorage, [Requirement(["Level 2 Keycard"], [CanDefeatLargeGeron])])
]

OperationsDeck.connections = [
    Connection(ArachnusZone, [HasMissile], one_way=True)
]

ReactorZone.connections = [
    Connection(YakuzaZone, [CanFightBoss]),
    Connection(AuxiliaryReactor, [HasWaveBeam], one_way=True),
    Connection(Sector2NettoriZone, [CanCrossFromReactorToSector2], one_way=True)
]

AuxiliaryReactor.connections = [
    Connection(ReactorZone, [], one_way=True)
]

YakuzaZone.connections = [
    Connection(AuxiliaryReactor, [HasSpaceJump])
]

SectorHub.connections = [
    Connection(Sector1Hub, []),
    Connection(Sector2Hub, []),
    Connection(Sector3Hub, [HasKeycard1]),
    Connection(Sector4Hub, [HasKeycard1]),
    Connection(Sector5Hub, [HasKeycard1And2]),
    Connection(Sector6Hub, [HasKeycard1And2])
]

MainDeckHub.locations = [
    FusionLocation("Main Deck -- Cubby Hole", False, [HasMorph]),
    FusionLocation("Main Deck -- Genesis Speedway", False, [CanReachGenesisSpeedway]),
    FusionLocation("Main Deck -- Quarantine Bay", False, []),
    FusionLocation("Main Deck -- Station Entrance", False, [CanPowerBomb]),
    FusionLocation("Main Deck -- Sub-Zero Containment", False, [Requirement(["Level 3 Keycard"], [HasVaria])])
]

OperationsDeck.locations = [
    FusionLocation("Main Deck -- Operations Deck Data Room", True, [])
]

ArachnusZone.locations = [
    FusionLocation("Main Deck -- Arachnus Arena -- Core X", True, [CanFightBeginnerBoss]),
    FusionLocation("Main Deck -- Arachnus Arena -- Upper Item", False, [HasMissile, HasChargeBeam]),
    FusionLocation("Main Deck -- Attic", False, [HasMissile]),
    FusionLocation("Main Deck -- Operations Ventilation", False, []),
    FusionLocation("Main Deck -- Operations Ventilation Storage", False, []),
]

HabitationDeck.locations = [
    FusionLocation("Main Deck -- Habitation Deck -- Animals", True, [CanReachAnimals]),
    FusionLocation("Main Deck -- Habitation Deck -- Lower Item", False, [CanReachAnimals, HasWaveBeam])
]

ReactorZone.locations = [
    FusionLocation("Main Deck -- Silo Catwalk", False, []),
    FusionLocation("Main Deck -- Silo Scaffolding", False, [HasMorph])
]

YakuzaZone.locations = [
    FusionLocation("Main Deck -- Yakuza Arena", True, [CanFightBoss])
]

AuxiliaryReactor.locations = [
    FusionLocation("Main Deck -- Auxiliary Power Station", True, [])
]

SectorHub.locations = [
    FusionLocation("Main Deck -- Main Elevator Cache", False, [HasSpeedBooster])
]

NexusStorage.locations = [
    FusionLocation("Main Deck -- Nexus Storage", False, [CanBallJumpAndBomb])
]

#endregion

#region Sector 1 Topology
Sector1Hub.connections = [
    Connection(Sector1ToSector2, [Requirement(["Level 2 Keycard", "Space Jump", "Screw Attack"], [])]),
    Connection(Sector1ToSector3, [Requirement(["Level 1 Keycard", "Morph Ball", "Screw Attack"], [])]),
    Connection(Sector1FirstStabilizerZone, [CanDefeatSmallGeron, Requirement(["Level 1 Keycard", "Level 2 Keycard"], [CanLavaDive])]),
]

Sector1ToSector2.connections = [
    Connection(Sector1Hub, [HasScrewAttack], one_way=True),
    Connection(Sector2Hub, [HasScrewAttack])
]

Sector1ToSector3.connections = [
    Connection(Sector3Attic, [HasScrewAttack], one_way=True)
]

Sector1FirstStabilizerZone.connections = [
    Connection(Sector1SecondStabilizerZone, [], one_way=True),
    Connection(Sector1AfterChargeCoreZone, [HasWaveBeam]),
]

Sector1SecondStabilizerZone.connections = [
    Connection(Sector1ChargeCoreZone, [HasMorph], one_way=True),
    Connection(Sector1TourianHub, [Requirement(["Screw Attack", "Space Jump"], [])])
]

Sector1ChargeCoreZone.connections = [
    Connection(Sector1AfterChargeCoreZone, [CanFightBeginnerBoss])
]

Sector1AfterChargeCoreZone.connections = [
    Connection(Sector1FirstStabilizerZone, [])
]

Sector1TourianExit.connections = [
    Connection(Sector1TourianHub, [Requirement(["Screw Attack", "Wave Beam", "Morph Ball"], [])])
]

Sector1ToSector2.locations = [
    FusionLocation("Sector 1 (SRX) -- Antechamber", False, [])
]

Sector1FirstStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Atmospheric Stabilizer Northeast", False, []),
    FusionLocation("Sector 1 (SRX) -- Hornoad Hole", False, [HasMorph]),
    FusionLocation("Sector 1 (SRX) -- Wall Jump Tutorial", False, [CanWallJump])
]

Sector1SecondStabilizerZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Lower Item", False, [CanLavaDive]),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Left Item", False, [HasSpaceJump, HasSpeedBooster]),
    FusionLocation("Sector 1 (SRX) -- Lava Lake -- Upper Right Item", False, []),
    FusionLocation("Sector 1 (SRX) -- Stabilizer Storage", False, []),
]

Sector1ChargeCoreZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Core X", True, [CanFightBeginnerBoss]),
    FusionLocation("Sector 1 (SRX) -- Charge Core Arena -- Upper Item", False, [Requirement(["Speed Booster"], [CanFightBeginnerBoss])]),
    FusionLocation("Sector 1 (SRX) -- Watering Hole", False, [Requirement(["Speed Booster", "Gravity Suit", "Charge Beam"], [CanBomb])])
]

Sector1AfterChargeCoreZone.locations = [
    FusionLocation("Sector 1 (SRX) -- Crab Rave", False, [Requirement(["Morph Ball", "Missile Data"], [])])
]

Sector1TourianHub.locations = [
    FusionLocation("Sector 1 (SRX) -- Animorphs Cache", False, [CanReachAnimorphs]),
    FusionLocation("Sector 1 (SRX) -- Ridley Arena", True, [CanFightLateGameBoss]),
    FusionLocation("Sector 1 (SRX) -- Ripper Maze", False, [HasMissile])
]

#endregion

#region Sector 2 Topology
Sector2Hub.connections = [
    Connection(Sector2ToSector4, [HasScrewAttack]),
    Connection(Sector2LeftSide, [CanBomb]),
    Connection(Sector2ZazabiZoneUpper, [CanBomb]),
    Connection(Sector2NettoriZone, [CanPowerBombAndJumpHigh])
]

Sector2ToSector4.connections = [
    Connection(Sector4RightWaterZone, [Requirement(["Gravity Suit"], [CanScrewAttackAndSpaceJump])])
]

Sector2LeftSide.connections = [
    Connection(Sector2ZazabiZone, [CanBomb], one_way=True)
]

Sector2ZazabiZone.connections = [
    Connection(Sector2LeftSide, [Requirement(["Space Jump"], [CanBomb])]),
    Connection(Sector2NettoriZone, [HasSpaceJump]),
    Connection(Sector2ZazabiZoneUpper, [CanEscapeZazabi, HasSpaceJump])
]

Sector2ZazabiZoneUpper.connections = [
    Connection(Sector2ZazabiZone, [], one_way=True)
]

Sector2Hub.locations = [
    FusionLocation("Sector 2 (TRO) -- Crumble City -- Lower Item", False, [CanScrewAttackAndSpaceJump]),
    FusionLocation("Sector 2 (TRO) -- Crumble City -- Upper Item", False, [CanScrewAttackAndSpaceJump]),
    FusionLocation("Sector 2 (TRO) -- Data Courtyard", False, [CanBomb]),
    FusionLocation("Sector 2 (TRO) -- Data Room", True, [HasKeycard1]),
    FusionLocation("Sector 2 (TRO) -- Kago Room", False, [CanJumpHigh, HasScrewAttack]),
    FusionLocation("Sector 2 (TRO) -- Level 1 Security Room", True, []),
    FusionLocation("Sector 2 (TRO) -- Lobby Cache", False, [Requirement(["Level 1 Keycard"], [CanBomb])]),
]

Sector2LeftSide.locations = [
    FusionLocation("Sector 2 (TRO) -- Zoro Zig-Zag", False, [Requirement(["Morph Ball"], [CanActivatePillar, CanJumpHigh])])
]

Sector2ZazabiZone.locations = [
    FusionLocation("Sector 2 (TRO) -- Cultivation Station", False, [CanBomb]),
    FusionLocation("Sector 2 (TRO) -- Oasis", False, [CanJumpHigh]),
    FusionLocation("Sector 2 (TRO) -- Oasis Storage", False, [CanReachOasisStorage]),
    FusionLocation("Sector 2 (TRO) -- Ripper Tower -- Lower Item", False, [Requirement(["Morph Ball"], [CanFreezeEnemies])]),
    FusionLocation("Sector 2 (TRO) -- Ripper Tower -- Upper Item", False, [Requirement(["Morph Ball"], [CanFreezeEnemies])]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Arena", True, [CanEscapeZazabi]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Arena Access", False, []),
    FusionLocation("Sector 2 (TRO) -- Zazabi Speedway -- Lower Item", False, [Requirement(["Speed Booster"], [CanEscapeZazabi])]),
    FusionLocation("Sector 2 (TRO) -- Zazabi Speedway -- Upper Item", False, [Requirement(["Speed Booster"], [CanEscapeZazabi])])
]

Sector2ZazabiZoneUpper.locations = [
    FusionLocation("Sector 2 (TRO) -- Dessgeega Dorm", False, [CanBomb])
]

Sector2NettoriZone.locations = [
    FusionLocation("Sector 2 (TRO) -- Nettori Arena", True, [CanFightMidgameBoss]),
    FusionLocation("Sector 2 (TRO) -- Overgrown Cache", False, [HasMorph]),
    FusionLocation("Sector 2 (TRO) -- Puyo Palace", False, [])
]


#endregion

#region Sector 3 Topology
Sector3Hub.connections = [
    Connection(Sector3ToSector5, [Requirement(["Screw Attack", "Varia Suit"], [])], one_way=True),
    Connection(Sector3SecurityZone, [HasSpeedBooster]),
    Connection(Sector3MainShaft, [Requirement(["Morph Ball", "Speed Booster"], [])]),
    Connection(Sector3BOXZone, [CanDefeatMediumGeron]),
    Connection(Sector3Attic, [Requirement(["Screw Attack", "Space Jump"], [HasMorph, HasMissile])])
]

Sector3ToSector5.connections = [
    Connection(Sector5BeforeNightmareHub, [], one_way=True),
    Connection(Sector3Hub, [Requirement(["Screw Attack"], [CanJumpHigh])], one_way=True)
]

Sector3MainShaft.connections = [
    Connection(Sector3Hub, [HasMorph], one_way=True),
    Connection(Sector3BoilerZone, [HasVaria]),
    Connection(Sector3BOXZone, [CanBallJumpAndBomb]),
    Connection(Sector3RightShaft, [Requirement(["Screw Attack"], [CanLavaDive])])
]

Sector3BOXZone.connections = [
    Connection(Sector3Attic, [CanAscendBOXRoom])
]

Sector3Attic.connections = [
    Connection(Sector3Hub, [CanBomb], one_way=True),
    Connection(Sector3BOXZone, [], one_way=True)
]

Sector3RightShaft.connections = [
    Connection(Sector3Attic, [HasSpeedBooster], one_way=True)
]

Sector3Hub.locations = [
    FusionLocation("Sector 3 (PYR) -- Fiery Storage -- Lower Item", False, [HasVaria]),
    FusionLocation("Sector 3 (PYR) -- Fiery Storage -- Upper Item", False, [Requirement(["Varia Suit", "Speed Booster"], [CanActivatePillar])])
]

Sector3ToSector5.locations = [
    FusionLocation("Sector 3 (PYR) -- Glass Tube to Sector 5 (ARC)", False, [])
]

Sector3SecurityZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Level 2 Security Room", True, [HasKeycard2, CanAccessL2SecurityRoom]),
    FusionLocation("Sector 3 (PYR) -- Security Access", False, [CanBeatToughEnemyAndJumpHigh])
]

Sector3MainShaft.locations = [
    FusionLocation("Sector 3 (PYR) -- Namihe's Lair", False, [CanPowerBombAndJumpHigh]),
    FusionLocation("Sector 3 (PYR) -- Processing Access", False, []),
    FusionLocation("Sector 3 (PYR) -- Sova Processing -- Left Item", False, [Requirement(["Morph Ball"], [HasSpaceJump, CanFreezeEnemies])]),
    FusionLocation("Sector 3 (PYR) -- Sova Processing -- Right Item", False, [Requirement(["Morph Ball"], [HasSpaceJump, CanFreezeEnemies])]),
]

Sector3BoilerZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Lava Maze", False, [Requirement([], [CanNavigateLavaMaze])]),
    FusionLocation("Sector 3 (PYR) -- Main Boiler Control Room -- Boiler", True, [CanFightBoss]),
    FusionLocation("Sector 3 (PYR) -- Main Boiler Control Room -- Core X", True, [CanFightBoss])
]

Sector3BOXZone.locations = [
    FusionLocation("Sector 3 (PYR) -- Bob's Abode", False, [HasMorph]),
    FusionLocation("Sector 3 (PYR) -- Data Room", True, [CanFightBoss]),
    FusionLocation("Sector 3 (PYR) -- Deserted Runway", False, [HasSpeedBooster]),
    FusionLocation("Sector 3 (PYR) -- Geron's Treasure", False, [CanDefeatMediumGeron])
]

Sector3Attic.locations = [
    FusionLocation("Sector 3 (PYR) -- Alcove -- Lower Item", False, [CanBomb]),
    FusionLocation("Sector 3 (PYR) -- Alcove -- Upper Item", False, [Requirement(["Speed Booster"], [CanPowerBomb])])
]

Sector3RightShaft.locations = [
    FusionLocation("Sector 3 (PYR) -- Garbage Chute -- Lower Item", False, [HasSpeedBooster]),
    FusionLocation("Sector 3 (PYR) -- Garbage Chute -- Upper Item", False, [HasSpeedBooster])
]

#endregion

#region Sector 4 Topology
Sector4Hub.connections = [
    Connection(Sector4UpperZone, [CanBomb], one_way=True),
    Connection(Sector4DataZone, [Requirement(["Morph Ball", "Diffusion Missile"], [])]),
    Connection(Sector4RightWaterZone, [Requirement(["Diffusion Missile", "Gravity Suit"], [])])
]

Sector4ToSector6.connections = [
    Connection(Sector6Hub, [HasScrewAttack])
]

Sector4UpperZone.connections = [
    Connection(Sector4Hub, [HasSpeedBooster], one_way=True),
    Connection(Sector4PumpControl, [HasSpeedBooster], one_way=True),
    Connection(Sector4UpperWaterZone, [Requirement(["Gravity Suit"], [HasKeycard4])]),
    Connection(Sector4SerrisZone, [HasHiJump], one_way=True)
]

Sector4SerrisZone.connections = [
    Connection(Sector4UpperZone, [HasSpeedBooster], one_way=True)
]

Sector4PumpControl.connections = [
    Connection(Sector4UpperZone, [CanBallJump], one_way=True)
]

Sector4UpperWaterZone.connections = [
    Connection(Sector5NightmareHub, [Requirement(["Hi-Jump"], [HasSpeedBooster])]),
    Connection(Sector4SecurityZone, [HasSpeedBooster, HasScrewAttack]),
]

Sector4SecurityZone.connections = [
    Connection(Sector4RightWaterZone, [HasKeycard4]),
    Connection(Sector4LowerSecurityZone, [HasKeycard4]),
    Connection(Sector4SecurityRoom, [CanAscendCheddarBay], one_way=True)
]

Sector4LowerSecurityZone.connections = [
    Connection(Sector4SecurityRoom, [HasKeycard4])
]

Sector4RightWaterZone.connections = [
    Connection(Sector4DataZone, [CanFreezeEnemies, HasSpaceJump]),
    Connection(Sector4ToSector6, [Requirement(["Missile Data"], [CanFreezeEnemies, HasSpaceJump])])
]

Sector4DataZone.connections = [
    Connection(Sector4ToSector6, [CanDiffusionMissile])
]

Sector4Hub.locations = [
    FusionLocation("Sector 4 (AQA) -- Drain Pipe", False, [CanAccessDrainPipe]),
    FusionLocation("Sector 4 (AQA) -- Reservoir East", False, [CanPowerBomb])
]

Sector4PumpControl.locations = [
    FusionLocation("Sector 4 (AQA) -- Pump Control Unit", False, [HasMorph])
]

Sector4UpperZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Aquarium Pirate Tank", False, [Requirement(["Space Jump"], [CanPowerBomb])]),
    FusionLocation("Sector 4 (AQA) -- Broken Bridge", False, []),
    FusionLocation("Sector 4 (AQA) -- C-Cache", False, []),
    FusionLocation("Sector 4 (AQA) -- Reservoir Vault -- Lower Item", False, [CanAccessReservoirVault]),
    FusionLocation("Sector 4 (AQA) -- Reservoir Vault -- Upper Item", False, [Requirement(["Missile Data"], [CanAccessReservoirVault])]),
]

Sector4SerrisZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Serris Arena", True, [Requirement(["Hi-Jump"], [CanFightBoss])])
]

Sector4UpperWaterZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Cargo Hold to Sector 5 (ARC)", False, [HasScrewAttack, HasSpeedBooster]),
    FusionLocation("Sector 4 (AQA) -- Waterway", False, [HasSpeedBooster])
]

Sector4SecurityZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Cheddar Bay", False, [CanAscendCheddarBay]),
    FusionLocation("Sector 4 (AQA) -- Yard Firing Range", False, [])
]

Sector4LowerSecurityZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Sanctuary Cache", False, [CanAccessSanctuaryCache])
]

Sector4SecurityRoom.locations = [
    FusionLocation("Sector 4 (AQA) -- Level 4 Security Room", True, [Requirement(["Space Jump"], [HasKeycard4, CanAscendCheddarBay])]),
]

Sector4RightWaterZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Aquarium Kago Storage -- Left Item", False, [HasSpeedBooster, HasScrewAttack]),
    FusionLocation("Sector 4 (AQA) -- Aquarium Kago Storage -- Right Item", False, [HasSpeedBooster])
]

Sector4DataZone.locations = [
    FusionLocation("Sector 4 (AQA) -- Data Room", True, [Requirement([], [HasKeycard4])])
]

#endregion

#region Sector 5 Topology
Sector5Hub.connections = [
    Connection(Sector5ToSector6, [Requirement(["Level 3 Keycard"], [HasScrewAttack])]),
    Connection(Sector5BigRoom, [HasKeycard3, Requirement(["Morph Ball"], [HasMissile])])
]

Sector5BigRoom.connections = [
    Connection(Sector5FrozenHub, [HasVaria])
]

Sector5FrozenHub.connections = [
    Connection(Sector5DataRoom, [HasKeycard3], one_way=True),
    Connection(Sector5BeforeNightmareHub, [HasKeycard3]),
    Connection(Sector5SecurityZone, [
        Requirement(["Speed Booster"], [CanBomb]),
        Requirement(["Level 3 Keycard"], [HasWaveBeam])
    ], one_way=True),

]

Sector5SecurityZone.connections = [
    Connection(Sector5DataRoom, [Requirement(["Space Jump"], [HasKeycard3])]),
    Connection(Sector5FrozenHub, [HasKeycard3, Requirement(["Space Jump"], [CanBomb])], one_way=True)
]

Sector5DataRoom.connections = [
    Connection(Sector5FrozenHub, [HasWaveBeam]),
    Connection(Sector5SecurityZone, [], one_way=True)
]

Sector5BeforeNightmareHub.connections = [
    Connection(Sector3ToSector5, [CanJumpHigh]),
    Connection(Sector5NightmareHub, [HasHiJump], one_way=True)
]

Sector5NightmareHub.connections = [
    Connection(Sector5BeforeNightmareHub, [Requirement(["Gravity Suit"], [CanScrewAttackAndSpaceJump])]),
    Connection(Sector5NightmareZone, [CanSpeedBoosterUnderwater, HasMorph], one_way=True),
    Connection(Sector4UpperWaterZone, [CanSpeedBoosterUnderwater])
]

Sector5NightmareZone.connections = [
    Connection(Sector5NightmareHub, [CanEscapeNightmareRoom])
]

Sector5Hub.locations = [
    FusionLocation("Sector 5 (ARC) -- Gerubus Gully", False, [
        Requirement(["Level 3 Keycard"], [CanPowerBomb]),
        Requirement(["Level 3 Keycard", "Morph Ball", "Bomb Data"], [HasScrewAttack])
    ]
                   ),
    FusionLocation("Sector 5 (ARC) -- Magic Box", False, [HasKeycard3])
]

Sector5BigRoom.locations = [
    FusionLocation("Sector 5 (ARC) -- Training Aerie -- Left Item", False, [Requirement(["Speed Booster"], [HasSpaceJump, CanFreezeEnemies])]),
    FusionLocation("Sector 5 (ARC) -- Training Aerie -- Right Item", False, [HasSpaceJump, CanFreezeEnemies])
]

Sector5FrozenHub.locations = [
    FusionLocation("Sector 5 (ARC) -- Ripper Road", False, [])
]

Sector5BeforeNightmareHub.locations = [
    FusionLocation("Sector 5 (ARC) -- Crow's Nest", False, [Requirement(["Morph Ball", "Power Bomb Data"], [CanJumpHigh])])
]

Sector5DataRoom.locations = [
    FusionLocation("Sector 5 (ARC) -- Data Room", True, [])
]

Sector5SecurityZone.locations = [
    FusionLocation("Sector 5 (ARC) -- E-Tank Mimic Den", False, [Requirement(["Level 3 Keycard"], [CanFreezeEnemies, HasSpaceJump])]),
    FusionLocation("Sector 5 (ARC) -- Level 3 Security Room", True, []),
    FusionLocation("Sector 5 (ARC) -- Ripper's Treasure", False, [CanAccessRipperTreasure]),
    FusionLocation("Sector 5 (ARC) -- Security Shaft East", False, [CanPowerBomb]),
    FusionLocation("Sector 5 (ARC) -- Transmutation Trial", False, [Requirement(["Hi-Jump", "Level 3 Keycard"], [HasSpaceJump, CanFreezeEnemies])])
]

Sector5NightmareHub.locations = [
    FusionLocation("Sector 5 (ARC) -- Flooded Airlock to Sector 4 (AQA)", False, [CanSpeedBoosterUnderwater]),
    FusionLocation("Sector 5 (ARC) -- Mini-Fridge", False, [Requirement(["Varia Suit", "Gravity Suit"], [CanBallJump])]),
    FusionLocation("Sector 5 (ARC) -- Nightmare Hub", False, [Requirement(["Power Bomb Data"], [CanBallJump])]),
    FusionLocation("Sector 5 (ARC) -- Ruined Break Room", False, [CanPowerBomb])
]

Sector5NightmareZone.locations = [
    FusionLocation("Sector 5 (ARC) -- Nightmare Arena", True, [CanFightLateGameBoss]),
    FusionLocation("Sector 5 (ARC) -- Nightmare Nook", False, [CanBallJumpAndBomb])
]
#endregion

#region Sector6 Topology
Sector6Hub.connections = [
    Connection(Sector6Crossroads, [CanDefeatMediumGeron])
]

Sector6Crossroads.connections = [
    Connection(Sector6BeforeXBOXZone, [Requirement(["Varia Suit", "Level 4 Keycard"], [CanPowerBomb])]),
    Connection(Sector6BeforeVariaCoreXZone, [Requirement(["Speed Booster"], [CanBomb])]),
    Connection(Sector6AfterVariaCoreXZone, [Requirement(["Varia Suit"], [HasScrewAttack])])
]

Sector6BeforeXBOXZone.connections = [
    Connection(Sector6XBOXZone, [], one_way=True)
]

Sector6XBOXZone.connections = [
    Connection(Sector6AfterXBOXZone, [CanFightLateGameBoss])
]

Sector6AfterXBOXZone.connections = [
    Connection(Sector6BeforeXBOXZone, [CanScrewAttackAndSpaceJump], one_way=True),
    Connection(Sector6RestrictedZone, [HasWaveBeam])
]

Sector6RestrictedZone.connections = [
    Connection(Sector1TourianHub, [HasSpeedBooster], one_way=True)
]

Sector6BeforeVariaCoreXZone.connections = [
    Connection(Sector6VariaCoreXZone, [CanFightBoss])
]

Sector6VariaCoreXZone.connections = [
    Connection(Sector6AfterVariaCoreXZone, [Requirement(["Varia Suit"], [CanFightBoss])])
]

Sector6AfterVariaCoreXZone.connections = [
    Connection(Sector6Crossroads, [HasMorph])
]

Sector6Hub.locations = [
    FusionLocation("Sector 6 (NOC) -- Entrance Lobby", False, [HasMorph])
]

Sector6Crossroads.locations = [
    FusionLocation("Sector 6 (NOC) -- Catacombs", False, []),
    FusionLocation("Sector 6 (NOC) -- Missile Mimic Lodge", False, [Requirement(["Varia Suit"], [CanBomb])]),
    FusionLocation("Sector 6 (NOC) -- Pillar Highway", False, [Requirement(["Screw Attack", "Speed Booster", "Varia Suit"], [CanBomb, HasWaveBeam])]),
    FusionLocation("Sector 6 (NOC) -- Vault", False, [CanBomb])
]

Sector6BeforeXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Lower Item", False, [Requirement(["Hi-Jump", "Space Jump"], [HasSpeedBooster])]),
    FusionLocation("Sector 6 (NOC) -- Spaceboost Alley -- Upper Item", False, [Requirement([], [HasSpeedBooster])])
]

Sector6XBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Arena", True, [CanFightLateGameBoss])
]

Sector6AfterXBOXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Lower Item", False, [HasWaveBeam]),
    FusionLocation("Sector 6 (NOC) -- X-B.O.X. Garage -- Upper Item", False, [CanScrewAttackAndSpaceJump])
]

Sector6RestrictedZone.locations = [
    FusionLocation("Main Deck -- Restricted Airlock", False, [HasSpeedBooster])
]

Sector6BeforeVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Zozoro Wine Cellar", False, [
        Requirement(["Morph Ball", "Bomb Data"], [CanJumpHigh]),
        Requirement(["Morph Ball", "Power Bomb Data"], [CanJumpHigh]),
    ])
]

Sector6VariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Varia Core-X Arena", True, [CanFightBoss])
]

Sector6AfterVariaCoreXZone.locations = [
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Lower Item", False, [Requirement(["Morph Ball"], [CanJumpHigh])]),
    FusionLocation("Sector 6 (NOC) -- Twin Caverns West -- Upper Item", False, [])
]

#endregion

fusion_regions: list[FusionRegion] = [
    MainDeckHub,
    ArachnusZone,
    OperationsDeck,
    HabitationDeck,
    SectorHub,
    ReactorZone,
    YakuzaZone,
    AuxiliaryReactor,
    NexusStorage,
    Sector1Hub,
    Sector1ToSector2,
    Sector1ToSector3,
    Sector1FirstStabilizerZone,
    Sector1SecondStabilizerZone,
    Sector1ChargeCoreZone,
    Sector1AfterChargeCoreZone,
    Sector1TourianExit,
    Sector1TourianHub,
    Sector2Hub,
    Sector2ToSector4,
    Sector2LeftSide,
    Sector2ZazabiZone,
    Sector2ZazabiZoneUpper,
    Sector2NettoriZone,
    Sector3Hub,
    Sector3ToSector5,
    Sector3SecurityZone,
    Sector3MainShaft,
    Sector3BoilerZone,
    Sector3BOXZone,
    Sector3Attic,
    Sector3RightShaft,
    Sector4Hub,
    Sector4UpperZone,
    Sector4SerrisZone,
    Sector4ToSector6,
    Sector4PumpControl,
    Sector4UpperWaterZone,
    Sector4SecurityZone,
    Sector4LowerSecurityZone,
    Sector4SecurityRoom,
    Sector4RightWaterZone,
    Sector4DataZone,
    Sector5Hub,
    Sector5ToSector6,
    Sector5BigRoom,
    Sector5FrozenHub,
    Sector5SecurityZone,
    Sector5DataRoom,
    Sector5BeforeNightmareHub,
    Sector5NightmareHub,
    Sector5NightmareZone,
    Sector6Hub,
    Sector6Crossroads,
    Sector6BeforeXBOXZone,
    Sector6XBOXZone,
    Sector6AfterXBOXZone,
    Sector6RestrictedZone,
    Sector6BeforeVariaCoreXZone,
    Sector6VariaCoreXZone,
    Sector6AfterVariaCoreXZone,
]

