from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EnvironmentReasonEnumeration(Enum):
    """
    Values for Environment incident reason types TPEG Pti18_4/TPEG Pti_22.

    :cvar PTI22_0:
    :cvar UNKNOWN: TPEG Pti22_0 unknown.
    :cvar PTI22_1:
    :cvar FOG: TPEG Pti22_1 fog.
    :cvar PTI22_2:
    :cvar ROUGH_SEA: TPEG Pti22_2 rough sea.
    :cvar PTI22_3:
    :cvar HEAVY_SNOW_FALL: TPEG Pti22_3 heavy snow fall.
    :cvar PTI22_3_ALIAS_1:
    :cvar DRIFTING_SNOW: drifting snow - Alias to TPEG Pti22_3
        heavySnowFall.
    :cvar PTI22_3_ALIAS_2:
    :cvar BLIZZARD_CONDITIONS: Blizzard Conditions - Alias to TPEG
        Pti22_3 heavySnowFall.
    :cvar PTI22_4:
    :cvar HEAVY_RAIN: TPEG Pti22_4 heavy rain.
    :cvar PTI22_5:
    :cvar STRONG_WINDS: TPEG Pti22_5 strong winds.
    :cvar PTI22_5_ALIAS_1:
    :cvar STORM_CONDITIONS: stormConditions alias to TPEG Pti22_5 strong
        winds.
    :cvar PTI22_5_ALIAS_2:
    :cvar STORM_DAMAGE: storm damage alias to TPEG Pti22_5 strong winds.
    :cvar PTI22_6:
    :cvar TIDAL_RESTRICTIONS: TPEG Pti22_6 tidal restrictions.
    :cvar PTI22_7:
    :cvar HIGH_TIDE: TPEG Pti22_7 high tide.
    :cvar PTI22_8:
    :cvar LOW_TIDE: TPEG Pti22_8 low tide.
    :cvar PTI22_9:
    :cvar ICE: TPEG Pti22_9 ice.
    :cvar PTI22_10:
    :cvar FROZEN: TPEG Pti22_10 frozen.
    :cvar PTI22_11:
    :cvar HAIL: TPEG Pti22_11 hail.
    :cvar PTI22_11_ALIAS_1:
    :cvar SLEET: Sleet Alias to TPEG Pti22_11 hail.
    :cvar PTI22_12:
    :cvar HIGH_TEMPERATURES: TPEG Pti22_12 high temperatures.
    :cvar PTI22_13:
    :cvar FLOODING: TPEG Pti22_13 flooding.
    :cvar PTI22_14:
    :cvar WATERLOGGED: TPEG Pti22_14 waterlogged.
    :cvar PTI22_15:
    :cvar LOW_WATER_LEVEL: TPEG Pti22_15 low water level.
    :cvar PTI22_16:
    :cvar HIGH_WATER_LEVEL: TPEG Pti22_16 high water level.
    :cvar PTI22_17:
    :cvar FALLEN_LEAVES: TPEG Pti22_17 fallen leaves.
    :cvar PTI22_18:
    :cvar FALLEN_TREE: TPEG Pti22_18 fallen tree.
    :cvar PTI22_19:
    :cvar LANDSLIDE: TPEG Pti22_19 landslide.
    :cvar PTI22_255:
    :cvar UNDEFINED_ENVIRONMENTAL_PROBLEM: TPEG Pti22_255 undefined
        environmental problem.
    :cvar PTI22_255_ALIAS_1:
    :cvar LIGHTNING_STRIKE: lightningStrike alias to TPEG Pti22_255
        undefined environmental problem.
    :cvar PTI22_255_ALIAS_2:
    :cvar SEWER_OVERFLOW:
    :cvar PTI22_255_ALIAS_3:
    :cvar GRASS_FIRE:
    """

    PTI22_0 = "pti22_0"
    UNKNOWN = "unknown"
    PTI22_1 = "pti22_1"
    FOG = "fog"
    PTI22_2 = "pti22_2"
    ROUGH_SEA = "roughSea"
    PTI22_3 = "pti22_3"
    HEAVY_SNOW_FALL = "heavySnowFall"
    PTI22_3_ALIAS_1 = "pti22_3_Alias_1"
    DRIFTING_SNOW = "driftingSnow"
    PTI22_3_ALIAS_2 = "pti22_3_Alias_2"
    BLIZZARD_CONDITIONS = "blizzardConditions"
    PTI22_4 = "pti22_4"
    HEAVY_RAIN = "heavyRain"
    PTI22_5 = "pti22_5"
    STRONG_WINDS = "strongWinds"
    PTI22_5_ALIAS_1 = "pti22_5_Alias_1"
    STORM_CONDITIONS = "stormConditions"
    PTI22_5_ALIAS_2 = "pti22_5_Alias_2"
    STORM_DAMAGE = "stormDamage"
    PTI22_6 = "pti22_6"
    TIDAL_RESTRICTIONS = "tidalRestrictions"
    PTI22_7 = "pti22_7"
    HIGH_TIDE = "highTide"
    PTI22_8 = "pti22_8"
    LOW_TIDE = "lowTide"
    PTI22_9 = "pti22_9"
    ICE = "ice"
    PTI22_10 = "pti22_10"
    FROZEN = "frozen"
    PTI22_11 = "pti22_11"
    HAIL = "hail"
    PTI22_11_ALIAS_1 = "pti22_11_Alias_1"
    SLEET = "sleet"
    PTI22_12 = "pti22_12"
    HIGH_TEMPERATURES = "highTemperatures"
    PTI22_13 = "pti22_13"
    FLOODING = "flooding"
    PTI22_14 = "pti22_14"
    WATERLOGGED = "waterlogged"
    PTI22_15 = "pti22_15"
    LOW_WATER_LEVEL = "lowWaterLevel"
    PTI22_16 = "pti22_16"
    HIGH_WATER_LEVEL = "highWaterLevel"
    PTI22_17 = "pti22_17"
    FALLEN_LEAVES = "fallenLeaves"
    PTI22_18 = "pti22_18"
    FALLEN_TREE = "fallenTree"
    PTI22_19 = "pti22_19"
    LANDSLIDE = "landslide"
    PTI22_255 = "pti22_255"
    UNDEFINED_ENVIRONMENTAL_PROBLEM = "undefinedEnvironmentalProblem"
    PTI22_255_ALIAS_1 = "pti22_255_Alias_1"
    LIGHTNING_STRIKE = "lightningStrike"
    PTI22_255_ALIAS_2 = "pti22_255_Alias_2"
    SEWER_OVERFLOW = "sewerOverflow"
    PTI22_255_ALIAS_3 = "pti22_255_Alias_3"
    GRASS_FIRE = "grassFire"


class EnvironmentSubReasonEnumeration(Enum):
    """
    Values for Environment incident subreason types.
    """

    HEAVY_SNOW_FALL = "heavySnowFall"
    STRONG_WINDS = "strongWinds"
    STORM_CONDITIONS = "stormConditions"
    STORM_DAMAGE = "stormDamage"
    HAIL = "hail"
    LIGHTENING_STRIKE = "lighteningStrike"
    AVALANCHES = "avalanches"
    FLASH_FLOODS = "flashFloods"
    MUDSLIP = "mudslip"
    ROCKFALLS = "rockfalls"
    SUBSIDENCE = "subsidence"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
    SEWER_OVERFLOW = "sewerOverflow"
    GRASS_FIRE = "grassFire"


class EquipmentReasonEnumeration(Enum):
    """
    Values for Equipment incident reason types TPEG Pti18_3/TPEG Pti_21.

    :cvar PTI21_0:
    :cvar UNKNOWN: TPEG Pti21_0 unknown.
    :cvar PTI21_1:
    :cvar POINTS_PROBLEM: TPEG Pti21_1 points problem.
    :cvar PTI21_2:
    :cvar POINTS_FAILURE: TPEG Pti21_2 points failure.
    :cvar PTI21_3:
    :cvar SIGNAL_PROBLEM: TPEG Pti21_3 signal problem.
    :cvar PTI21_3_ALIAS_1:
    :cvar TRAIN_WARNING_SYSTEM_PROBLEM: Train warning system eg
        TPWSAlias to TPEG Pti21_3 signal problem.
    :cvar PTI21_3_ALIAS_2:
    :cvar TRACK_CIRCUIT_PROBLEM: Track circuit alias to TPEG Pti21_3
        signal problem.
    :cvar PTI21_4:
    :cvar SIGNAL_FAILURE: TPEG Pti21_4 signal failure.
    :cvar PTI21_5:
    :cvar DERAILMENT: TPEG Pti21_5 derailment.
    :cvar PTI21_6:
    :cvar ENGINE_FAILURE: TPEG Pti21_6 engine failure.
    :cvar PTI21_6_ALIAS_1:
    :cvar TRACTION_FAILURE: traction failure alais to TPEG Pti21_6
        engine failure.
    :cvar PTI21_7:
    :cvar BREAK_DOWN: TPEG Pti21_7 break down.
    :cvar PTI21_8:
    :cvar TECHNICAL_PROBLEM: TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_1:
    :cvar BROKEN_RAIL: Broken rail - alias to TPEG Pti21_8 technical
        problem.
    :cvar PTI21_8_ALIAS_2:
    :cvar POOR_RAIL_CONDITIONS: poor rail conditions - alias to TPEG
        Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_3:
    :cvar WHEEL_IMPACT_LOAD: Wheel Impact Load detectedi by trackside
        equipment alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_4:
    :cvar LACK_OF_OPERATIONAL_STOCK: late lack of operational stock -
        alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_5:
    :cvar DEFECTIVE_FIRE_ALARM_EQUIPMENT: defective fire alarm equipment
        - alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_6:
    :cvar DEFECTIVE_PLATFORM_EDGE_DOORS: defective PEDs (platform edge
        doors) - alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_7:
    :cvar DEFECTIVE_CCTV: defective CCTV - alias to TPEG Pti21_8
        technical problem.
    :cvar PTI21_8_ALIAS_8:
    :cvar DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM: defective PA - alias to
        TPEG Pti21_8 technical problem.
    :cvar PTI21_8_ALIAS_9:
    :cvar TICKETING_SYSTEM_NOT_AVAILABLE: ticketing facility unavailable
        - alias to TPEG Pti21_8 technical problem.
    :cvar PTI21_9:
    :cvar REPAIR_WORK: TPEG Pti21_9 repair work.
    :cvar PTI21_10:
    :cvar CONSTRUCTION_WORK: TPEG Pti21_10 construction work.
    :cvar PTI21_11:
    :cvar MAINTENANCE_WORK: TPEG Pti21_11 maintenance work.
    :cvar PTI21_11_ALIAS_1:
    :cvar EMERGENCY_ENGINEERING_WORK: emergency engineering work - alias
        to TPEG Pti21_11 maintenance work.
    :cvar PTI21_11_ALIAS_2:
    :cvar LATE_FINISH_TO_ENGINEERING_WORK: late finish to engineering
        work - alias to TPEG Pti21_11 maintenance work.
    :cvar PTI21_12:
    :cvar POWER_PROBLEM: TPEG Pti21_12 power problem.
    :cvar PTI21_13:
    :cvar FUEL_PROBLEM: TPEG Pti21_13 fuel problem.
    :cvar PTI21_14:
    :cvar SWING_BRIDGE_FAILURE: TPEG Pti21_14 swing bridge failure.
    :cvar PTI21_15:
    :cvar ESCALATOR_FAILURE: TPEG Pti21_15 escalator failure.
    :cvar PTI21_16:
    :cvar LIFT_FAILURE: TPEG Pti21_16 lift failure.
    :cvar PTI21_17:
    :cvar GANGWAY_PROBLEM: TPEG Pti21_17 gangway problem.
    :cvar PTI21_18:
    :cvar CLOSED_FOR_MAINTENANCE: TPEG Pti21_18 closed for maintenance.
    :cvar PTI21_19:
    :cvar FUEL_SHORTAGE: TPEG Pti21_19 fuel shortage.
    :cvar PTI21_20:
    :cvar DEICING_WORK: TPEG Pti21_20 de-icing work.
    :cvar PTI21_21:
    :cvar WHEEL_PROBLEM: TPEG Pti21_21 wheel problem.
    :cvar PTI21_22:
    :cvar LUGGAGE_CAROUSEL_PROBLEM: TPEG Pti21_22 luggage carousel
        problem.
    :cvar PTI21_255:
    :cvar UNDEFINED_EQUIPMENT_PROBLEM: TPEG Pti21_255 undefined
        equipment problem.
    """

    PTI21_0 = "pti21_0"
    UNKNOWN = "unknown"
    PTI21_1 = "pti21_1"
    POINTS_PROBLEM = "pointsProblem"
    PTI21_2 = "pti21_2"
    POINTS_FAILURE = "pointsFailure"
    PTI21_3 = "pti21_3"
    SIGNAL_PROBLEM = "signalProblem"
    PTI21_3_ALIAS_1 = "pti21_3_Alias_1"
    TRAIN_WARNING_SYSTEM_PROBLEM = "trainWarningSystemProblem"
    PTI21_3_ALIAS_2 = "pti21_3_Alias_2"
    TRACK_CIRCUIT_PROBLEM = "trackCircuitProblem"
    PTI21_4 = "pti21_4"
    SIGNAL_FAILURE = "signalFailure"
    PTI21_5 = "pti21_5"
    DERAILMENT = "derailment"
    PTI21_6 = "pti21_6"
    ENGINE_FAILURE = "engineFailure"
    PTI21_6_ALIAS_1 = "pti21_6_Alias_1"
    TRACTION_FAILURE = "tractionFailure"
    PTI21_7 = "pti21_7"
    BREAK_DOWN = "breakDown"
    PTI21_8 = "pti21_8"
    TECHNICAL_PROBLEM = "technicalProblem"
    PTI21_8_ALIAS_1 = "pti21_8_Alias_1"
    BROKEN_RAIL = "brokenRail"
    PTI21_8_ALIAS_2 = "pti21_8_Alias_2"
    POOR_RAIL_CONDITIONS = "poorRailConditions"
    PTI21_8_ALIAS_3 = "pti21_8_Alias_3"
    WHEEL_IMPACT_LOAD = "wheelImpactLoad"
    PTI21_8_ALIAS_4 = "pti21_8_Alias_4"
    LACK_OF_OPERATIONAL_STOCK = "lackOfOperationalStock"
    PTI21_8_ALIAS_5 = "pti21_8_Alias_5"
    DEFECTIVE_FIRE_ALARM_EQUIPMENT = "defectiveFireAlarmEquipment"
    PTI21_8_ALIAS_6 = "pti21_8_Alias_6"
    DEFECTIVE_PLATFORM_EDGE_DOORS = "defectivePlatformEdgeDoors"
    PTI21_8_ALIAS_7 = "pti21_8_Alias_7"
    DEFECTIVE_CCTV = "defectiveCctv"
    PTI21_8_ALIAS_8 = "pti21_8_Alias_8"
    DEFECTIVE_PUBLIC_ANNOUNCEMENT_SYSTEM = "defectivePublicAnnouncementSystem"
    PTI21_8_ALIAS_9 = "pti21_8_Alias_9"
    TICKETING_SYSTEM_NOT_AVAILABLE = "ticketingSystemNotAvailable"
    PTI21_9 = "pti21_9"
    REPAIR_WORK = "repairWork"
    PTI21_10 = "pti21_10"
    CONSTRUCTION_WORK = "constructionWork"
    PTI21_11 = "pti21_11"
    MAINTENANCE_WORK = "maintenanceWork"
    PTI21_11_ALIAS_1 = "pti21_11_Alias_1"
    EMERGENCY_ENGINEERING_WORK = "emergencyEngineeringWork"
    PTI21_11_ALIAS_2 = "pti21_11_Alias_2"
    LATE_FINISH_TO_ENGINEERING_WORK = "lateFinishToEngineeringWork"
    PTI21_12 = "pti21_12"
    POWER_PROBLEM = "powerProblem"
    PTI21_13 = "pti21_13"
    FUEL_PROBLEM = "fuelProblem"
    PTI21_14 = "pti21_14"
    SWING_BRIDGE_FAILURE = "swingBridgeFailure"
    PTI21_15 = "pti21_15"
    ESCALATOR_FAILURE = "escalatorFailure"
    PTI21_16 = "pti21_16"
    LIFT_FAILURE = "liftFailure"
    PTI21_17 = "pti21_17"
    GANGWAY_PROBLEM = "gangwayProblem"
    PTI21_18 = "pti21_18"
    CLOSED_FOR_MAINTENANCE = "closedForMaintenance"
    PTI21_19 = "pti21_19"
    FUEL_SHORTAGE = "fuelShortage"
    PTI21_20 = "pti21_20"
    DEICING_WORK = "deicingWork"
    PTI21_21 = "pti21_21"
    WHEEL_PROBLEM = "wheelProblem"
    PTI21_22 = "pti21_22"
    LUGGAGE_CAROUSEL_PROBLEM = "luggageCarouselProblem"
    PTI21_255 = "pti21_255"
    UNDEFINED_EQUIPMENT_PROBLEM = "undefinedEquipmentProblem"


class EquipmentSubReasonEnumeration(Enum):
    """
    Values for Equipment incident sub reason types.

    :cvar STAFF_SICKNESS: TPEG Pti_19_25 bridge strike.
    :cvar STAFF_INJURY:
    :cvar UNOFFICIAL_INDUSTRIAL_ACTION: TPEG Pti_19_26 overhead
        obstruction.
    """

    STAFF_SICKNESS = "staffSickness"
    STAFF_INJURY = "staffInjury"
    UNOFFICIAL_INDUSTRIAL_ACTION = "unofficialIndustrialAction"


class MiscellaneousReasonEnumeration(Enum):
    """
    Values for Miscellaneous incident reason types TPEG Pti18_1/TPEG Pti_19.

    :cvar PTI19_0:
    :cvar UNKNOWN: TPEG Pti_19_0 unknown.
    :cvar PTI19_1:
    :cvar INCIDENT: TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_1:
    :cvar NEAR_MISS: Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_2:
    :cvar SAFETY_VIOLATION: Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_3:
    :cvar SIGNAL_PASSED_AT_DANGER: Signal passed at danger - alias to
        TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_4:
    :cvar STATION_OVERRUN: Station overrun - alias to TPEG Pti_19_1
        incident.
    :cvar PTI19_1_ALIAS_5:
    :cvar TRAIN_DOOR: trainDoor- alias to TPEG Pti_19_1 incident.
    :cvar PTI19_1_ALIAS_6:
    :cvar EMERGENCY_SERVICES_CALL: Unspecified emergency service visit.
        Alias to pti19
    :cvar PTI19_2:
    :cvar BOMB_EXPLOSION: TPEG Pti_19_2 bomb explosion.
    :cvar PTI19_3:
    :cvar SECURITY_ALERT: TPEG Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_1:
    :cvar POLICE_REQUEST: request of the police Alias to TPEG Pti_19_3
        security alert.
    :cvar PTI19_3_ALIAS_2:
    :cvar FIRE_BRIGADE_SAFETY_CHECKS: fire brigade safety checksAlias to
        TPEG Pti_19_3 security alert.
    :cvar PTI19_3_ALIAS_3:
    :cvar UNATTENDED_BAG: an unattended bag TPEG Pti_19_3 security
        alert.
    :cvar PTI19_3_ALIAS_4:
    :cvar TELEPHONED_THREAT: telephoned threat TPEG Pti_19_3 security
        alert.
    :cvar PTI19_3_ALIAS_5:
    :cvar SUSPECT_VEHICLE: telephoned threat TPEG Pti_19_3 security
        alert.
    :cvar PTI19_3_ALIAS_6:
    :cvar CIVIL_EMERGENCY:
    :cvar PTI19_3_ALIAS_7:
    :cvar AIR_RAID:
    :cvar PTI19_3_ALIAS_8:
    :cvar SABOTAGE:
    :cvar PTI19_3_ALIAS_9:
    :cvar BOMB_ALERT:
    :cvar PTI19_3_ALIAS_10:
    :cvar ATTACH:
    :cvar PTI19_3_ALIAS_11:
    :cvar EVACUATION:
    :cvar PTI19_3_ALIAS_12:
    :cvar TERRORIST_INCIDENT:
    :cvar PTI19_3_ALIAS_13:
    :cvar GUNFIRE_ON_ROADWAY:
    :cvar PTI19_3_ALIAS_14:
    :cvar EXPLOSION:
    :cvar PTI19_3_ALIAS_15:
    :cvar EXPLOSION_HAZARD:
    :cvar PTI19_3_ALIAS_16:
    :cvar SECURITY_INCIDENT:
    :cvar PTI19_4:
    :cvar FIRE: TPEG Pti_19_4 fire.
    :cvar PTI19_4_ALIAS_1:
    :cvar LINESIDE_FIRE: linesideFire alias to TPEG Pti_19_4 fire.
    :cvar PTI19_5:
    :cvar VANDALISM: TPEG Pti_19_5 vandalism.
    :cvar PTI19_5_ALIAS_1:
    :cvar PASSENGER_ACTION: passengerActionAlias to pti19
    :cvar PTI19_5_ALIAS_2:
    :cvar STAFF_ASSAULT: Assault on stafft.Alias to pti19
    :cvar PTI19_5_ALIAS_3:
    :cvar RAILWAY_CRIME: Railway Crime Alias to pti19
    :cvar PTI19_6:
    :cvar ACCIDENT: TPEG Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_1:
    :cvar FATALITY: fatality alias to TPEG Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_2:
    :cvar PERSON_UNDER_TRAIN: a person under a train - alias to TPEG
        Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_3:
    :cvar PERSON_HIT_BY_TRAIN: a person hit by a train - alias to TPEG
        Pti_19_6 accident.
    :cvar PTI19_6_ALIAS_4:
    :cvar PERSON_ILL_ON_VEHICLE: person ill On Vehicle -Alias to pti19_6
    :cvar PTI19_6_ALIAS_5:
    :cvar EMERGENCY_SERVICES: emergencyServices - alias to TPEG Pti_19_6
        accident.
    :cvar PTI19_6_ALIAS_6:
    :cvar COLLISION: Collision - Alias to pti19_6
    :cvar PTI19_7:
    :cvar OVERCROWDED: TPEG Pti_19_7 overcrowded.
    :cvar PTI19_8:
    :cvar INSUFFICIENT_DEMAND: TPEG Pti_19_8 insufficient demand.
    :cvar PTI19_9:
    :cvar LIGHTING_FAILURE: TPEG Pti_19_9 lighting failure.
    :cvar PTI19_10:
    :cvar LEADER_BOARD_FAILURE: TPEG Pti_19_10 leader board failure.
    :cvar PTI19_11:
    :cvar SERVICE_INDICATOR_FAILURE: TPEG Pti_19_11 service indicator
        failure.
    :cvar PTI19_12:
    :cvar SERVICE_FAILURE: TPEG Pti_19_12 service failure.
    :cvar PTI19_13:
    :cvar OPERATOR_CEASED_TRADING: TPEG Pti_19_13 OPERATOR ceased
        trading.
    :cvar PTI19_14:
    :cvar OPERATOR_SUSPENDED: TPEG Pti_19_14 OPERATOR suspended.
    :cvar PTI19_15:
    :cvar CONGESTION: TPEG Pti_19_15 congestion.
    :cvar PTI19_16:
    :cvar ROUTE_BLOCKAGE: TPEG Pti_19_16 route blockage.
    :cvar PTI19_17:
    :cvar PERSON_ON_THE_LINE: TPEG Pti_19_17 person on the line.
    :cvar PTI19_18:
    :cvar VEHICLE_ON_THE_LINE: TPEG Pti_19_18 VEHICLE on the line.
    :cvar PTI19_18_ALIAS_1:
    :cvar LEVEL_CROSSING_INCIDENT: Level Crossing Incident - alias to
        TPEG Pti_19_18 VEHICLE on the line.
    :cvar PTI19_19:
    :cvar OBJECT_ON_THE_LINE: TPEG Pti_19_19 object on the line.
    :cvar PTI19_19_ALIAS_1:
    :cvar FALLEN_TREE_ON_THE_LINE: fallen tree on line- alias to TPEG
        Pti_19_19 object on the line.
    :cvar PTI19_19_ALIAS_2:
    :cvar VEGETATION: vegetation - alias to TPEG Pti_19_19 object on the
        line.
    :cvar PTI19_19_ALIAS_3:
    :cvar TRAIN_STRUCK_ANIMAL: Train struck animal alias to TPEG
        Pti_19_19 object on the line.
    :cvar PTI19_19_ALIAS_4:
    :cvar TRAIN_STRUCK_OBJECT: Train struck object alias to TPEG
        Pti_19_19 object on the line.
    :cvar PTI19_20:
    :cvar ANIMAL_ON_THE_LINE: TPEG Pti_19_20 animal on the line.
    :cvar PTI19_21:
    :cvar ROUTE_DIVERSION: TPEG Pti_19_21 route diversion.
    :cvar PTI19_22:
    :cvar ROAD_CLOSED: TPEG Pti_19_22 road closed.
    :cvar PTI19_23:
    :cvar ROADWORKS: TPEG Pti_19_23 roadworks.
    :cvar PTI19_24:
    :cvar SPECIAL_EVENT: TPEG Pti_19_24 special event.
    :cvar PTI19_24_ALIAS_1:
    :cvar MARCH:
    :cvar PTI19_24_ALIAS_2:
    :cvar PROCESSION:
    :cvar PTI19_24_ALIAS_3:
    :cvar DEMONSTRATION:
    :cvar PTI19_24_ALIAS_4:
    :cvar PUBLIC_DISTURBANCE:
    :cvar PTI19_24_ALIAS_5:
    :cvar FILTER_BLOCKADE:
    :cvar PTI19_24_ALIAS_6:
    :cvar SIGHTSEERS_OBSTRUCTING_ACCESS:
    :cvar PTI19_25:
    :cvar BRIDGE_STRIKE: TPEG Pti_19_25 bridge strike.
    :cvar PTI19_26:
    :cvar OVERHEAD_OBSTRUCTION: TPEG Pti_19_26 overhead obstruction.
    :cvar PTI19_27:
    :cvar UNDEFINED_PROBLEM: TPEG Pti_19_255 undefined problem.
    :cvar PTI19_255_ALIAS_1:
    :cvar PROBLEMS_AT_BORDER_POST:
    :cvar PTI19_255_ALIAS_2:
    :cvar PROBLEMS_AT_CUSTOMS_POST:
    :cvar PTI19_255_ALIAS_3:
    :cvar PROBLEMS_ON_LOCAL_ROAD:
    """

    PTI19_0 = "pti19_0"
    UNKNOWN = "unknown"
    PTI19_1 = "pti19_1"
    INCIDENT = "incident"
    PTI19_1_ALIAS_1 = "pti19_1_Alias_1"
    NEAR_MISS = "nearMiss"
    PTI19_1_ALIAS_2 = "pti19_1_Alias_2"
    SAFETY_VIOLATION = "safetyViolation"
    PTI19_1_ALIAS_3 = "pti19_1_Alias_3"
    SIGNAL_PASSED_AT_DANGER = "signalPassedAtDanger"
    PTI19_1_ALIAS_4 = "pti19_1_Alias_4"
    STATION_OVERRUN = "stationOverrun"
    PTI19_1_ALIAS_5 = "pti19_1_Alias_5"
    TRAIN_DOOR = "trainDoor"
    PTI19_1_ALIAS_6 = "pti19_1_Alias_6"
    EMERGENCY_SERVICES_CALL = "emergencyServicesCall"
    PTI19_2 = "pti19_2"
    BOMB_EXPLOSION = "bombExplosion"
    PTI19_3 = "pti19_3"
    SECURITY_ALERT = "securityAlert"
    PTI19_3_ALIAS_1 = "pti19_3_Alias_1"
    POLICE_REQUEST = "policeRequest"
    PTI19_3_ALIAS_2 = "pti19_3_Alias_2"
    FIRE_BRIGADE_SAFETY_CHECKS = "fireBrigadeSafetyChecks"
    PTI19_3_ALIAS_3 = "pti19_3_Alias_3"
    UNATTENDED_BAG = "unattendedBag"
    PTI19_3_ALIAS_4 = "pti19_3_Alias_4"
    TELEPHONED_THREAT = "telephonedThreat"
    PTI19_3_ALIAS_5 = "pti19_3_Alias_5"
    SUSPECT_VEHICLE = "suspectVehicle"
    PTI19_3_ALIAS_6 = "pti19_3_Alias_6"
    CIVIL_EMERGENCY = "civilEmergency"
    PTI19_3_ALIAS_7 = "pti19_3_Alias_7"
    AIR_RAID = "airRaid"
    PTI19_3_ALIAS_8 = "pti19_3_Alias_8"
    SABOTAGE = "sabotage"
    PTI19_3_ALIAS_9 = "pti19_3_Alias_9"
    BOMB_ALERT = "bombAlert"
    PTI19_3_ALIAS_10 = "pti19_3_Alias_10"
    ATTACH = "attach"
    PTI19_3_ALIAS_11 = "pti19_3_Alias_11"
    EVACUATION = "evacuation"
    PTI19_3_ALIAS_12 = "pti19_3_Alias_12"
    TERRORIST_INCIDENT = "terroristIncident"
    PTI19_3_ALIAS_13 = "pti19_3_Alias_13"
    GUNFIRE_ON_ROADWAY = "gunfireOnRoadway"
    PTI19_3_ALIAS_14 = "pti19_3_Alias_14"
    EXPLOSION = "explosion"
    PTI19_3_ALIAS_15 = "pti19_3_Alias_15"
    EXPLOSION_HAZARD = "explosionHazard"
    PTI19_3_ALIAS_16 = "pti19_3_Alias_16"
    SECURITY_INCIDENT = "securityIncident"
    PTI19_4 = "pti19_4"
    FIRE = "fire"
    PTI19_4_ALIAS_1 = "pti19_4_Alias_1"
    LINESIDE_FIRE = "linesideFire"
    PTI19_5 = "pti19_5"
    VANDALISM = "vandalism"
    PTI19_5_ALIAS_1 = "pti19_5_Alias_1"
    PASSENGER_ACTION = "passengerAction"
    PTI19_5_ALIAS_2 = "pti19_5_Alias_2"
    STAFF_ASSAULT = "staffAssault"
    PTI19_5_ALIAS_3 = "pti19_5_Alias_3"
    RAILWAY_CRIME = "railwayCrime"
    PTI19_6 = "pti19_6"
    ACCIDENT = "accident"
    PTI19_6_ALIAS_1 = "pti19_6_Alias_1"
    FATALITY = "fatality"
    PTI19_6_ALIAS_2 = "pti19_6_Alias_2"
    PERSON_UNDER_TRAIN = "personUnderTrain"
    PTI19_6_ALIAS_3 = "pti19_6_Alias_3"
    PERSON_HIT_BY_TRAIN = "personHitByTrain"
    PTI19_6_ALIAS_4 = "pti19_6_Alias_4"
    PERSON_ILL_ON_VEHICLE = "personIllOnVehicle"
    PTI19_6_ALIAS_5 = "pti19_6_Alias_5"
    EMERGENCY_SERVICES = "emergencyServices"
    PTI19_6_ALIAS_6 = "pti19_6_Alias_6"
    COLLISION = "collision"
    PTI19_7 = "pti19_7"
    OVERCROWDED = "overcrowded"
    PTI19_8 = "pti19_8"
    INSUFFICIENT_DEMAND = "insufficientDemand"
    PTI19_9 = "pti19_9"
    LIGHTING_FAILURE = "lightingFailure"
    PTI19_10 = "pti19_10"
    LEADER_BOARD_FAILURE = "leaderBoardFailure"
    PTI19_11 = "pti19_11"
    SERVICE_INDICATOR_FAILURE = "serviceIndicatorFailure"
    PTI19_12 = "pti19_12"
    SERVICE_FAILURE = "serviceFailure"
    PTI19_13 = "pti19_13"
    OPERATOR_CEASED_TRADING = "operatorCeasedTrading"
    PTI19_14 = "pti19_14"
    OPERATOR_SUSPENDED = "operatorSuspended"
    PTI19_15 = "pti19_15"
    CONGESTION = "congestion"
    PTI19_16 = "pti19_16"
    ROUTE_BLOCKAGE = "routeBlockage"
    PTI19_17 = "pti19_17"
    PERSON_ON_THE_LINE = "personOnTheLine"
    PTI19_18 = "pti19_18"
    VEHICLE_ON_THE_LINE = "vehicleOnTheLine"
    PTI19_18_ALIAS_1 = "pti19_18_Alias_1"
    LEVEL_CROSSING_INCIDENT = "levelCrossingIncident"
    PTI19_19 = "pti19_19"
    OBJECT_ON_THE_LINE = "objectOnTheLine"
    PTI19_19_ALIAS_1 = "pti19_19_Alias_1"
    FALLEN_TREE_ON_THE_LINE = "fallenTreeOnTheLine"
    PTI19_19_ALIAS_2 = "pti19_19_Alias_2"
    VEGETATION = "vegetation"
    PTI19_19_ALIAS_3 = "pti19_19_Alias_3"
    TRAIN_STRUCK_ANIMAL = "trainStruckAnimal"
    PTI19_19_ALIAS_4 = "pti19_19_Alias_4"
    TRAIN_STRUCK_OBJECT = "trainStruckObject"
    PTI19_20 = "pti19_20"
    ANIMAL_ON_THE_LINE = "animalOnTheLine"
    PTI19_21 = "pti19_21"
    ROUTE_DIVERSION = "routeDiversion"
    PTI19_22 = "pti19_22"
    ROAD_CLOSED = "roadClosed"
    PTI19_23 = "pti19_23"
    ROADWORKS = "roadworks"
    PTI19_24 = "pti19_24"
    SPECIAL_EVENT = "specialEvent"
    PTI19_24_ALIAS_1 = "pti19_24_Alias_1"
    MARCH = "march"
    PTI19_24_ALIAS_2 = "pti19_24_Alias_2"
    PROCESSION = "procession"
    PTI19_24_ALIAS_3 = "pti19_24_Alias_3"
    DEMONSTRATION = "demonstration"
    PTI19_24_ALIAS_4 = "pti19_24_Alias_4"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    PTI19_24_ALIAS_5 = "pti19_24_Alias_5"
    FILTER_BLOCKADE = "filterBlockade"
    PTI19_24_ALIAS_6 = "pti19_24_Alias_6"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    PTI19_25 = "pti19_25"
    BRIDGE_STRIKE = "bridgeStrike"
    PTI19_26 = "pti19_26"
    OVERHEAD_OBSTRUCTION = "overheadObstruction"
    PTI19_27 = "pti19_27"
    UNDEFINED_PROBLEM = "undefinedProblem"
    PTI19_255_ALIAS_1 = "pti19_255_Alias_1"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PTI19_255_ALIAS_2 = "pti19_255_Alias_2"
    PROBLEMS_AT_CUSTOMS_POST = "problemsAtCustomsPost"
    PTI19_255_ALIAS_3 = "pti19_255_Alias_3"
    PROBLEMS_ON_LOCAL_ROAD = "problemsOnLocalRoad"


class MiscellaneousSubReasonEnumeration(Enum):
    """
    Values for Miscellaneous incident sub reason types.

    :cvar NEAR_MISS: Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar SAFETY_VIOLATION: Near Miss - alias to TPEG Pti_19_1 incident.
    :cvar SIGNAL_PASSED_AT_DANGER: Signal passed at danger - alias to
        TPEG Pti_19_1 incident.
    :cvar STATION_OVERRUN: Station overrun - alias to TPEG Pti_19_1
        incident.
    :cvar TRAIN_DOOR: trainDoor- alias to TPEG Pti_19_1 incident.
    :cvar EMERGENCY_SERVICES_CALL: Unspecified emergency service visit.
        Alias to pti19
    :cvar POLICE_REQUEST: request of the police Alias to TPEG Pti_19_3
        security alert.
    :cvar FIRE_BRIGADE_SAFETY_CHECKS: fire brigade safety checksAlias to
        TPEG Pti_19_3 security alert.
    :cvar UNATTENDED_BAG: an unattended bag TPEG Pti_19_3 security
        alert.
    :cvar TELEPHONED_THREAT: telephoned threat TPEG Pti_19_3 security
        alert.
    :cvar SUSPECT_VEHICLE: telephoned threat TPEG Pti_19_3 security
        alert.
    :cvar VANDALISM: TPEG Pti_19_5 vandalism.
    :cvar PASSENGER_ACTION: passengerActionAlias to pti19
    :cvar STAFF_ASSAULT: Assault on stafft.Alias to pti19
    :cvar RAILWAY_CRIME: Railway Crime Alias to pti19
    :cvar ALTERCATION:
    :cvar THEFT:
    :cvar FATALITY: fatality alias to TPEG Pti_19_6 accident.
    :cvar ILL_VEHICLE_OCCUPANTS:
    :cvar PERSON_UNDER_TRAIN: a person under a train - alias to TPEG
        Pti_19_6 accident.
    :cvar PERSON_HIT_BY_TRAIN: a person hit by a train - alias to TPEG
        Pti_19_6 accident.
    :cvar PERSON_ILL_ON_VEHICLE: person ill On Vehicle -Alias to pti19_6
    :cvar EMERGENCY_SERVICES: emergencyServices - alias to TPEG Pti_19_6
        accident.
    :cvar COLLISION: Collision - Alias to pti19_6
    :cvar LINESIDE_FIRE:
    :cvar LEVEL_CROSSING_INCIDENT: Level Crossing Incident - alias to
        TPEG Pti_19_18 VEHICLE on the line.
    :cvar FALLEN_TREE_ON_THE_LINE: fallen tree on line- alias to TPEG
        Pti_19_19 object on the line.
    :cvar VEGETATION: vegetation - alias to TPEG Pti_19_19 object on the
        line.
    :cvar TRAIN_STRUCK_ANIMAL: Train struck animal alias to TPEG
        Pti_19_19 object on the line.
    :cvar TRAIN_STRUCK_OBJECT: Train struck object alias to TPEG
        Pti_19_19 object on the line.
    :cvar ANIMAL_ON_THE_LINE: TPEG Pti_19_20 animal on the line.
    :cvar ROUTE_DIVERSION: TPEG Pti_19_21 route diversion.
    :cvar ROAD_CLOSED: TPEG Pti_19_22 road closed.
    :cvar ROADWORKS: TPEG Pti_19_23 roadworks.
    :cvar SPECIAL_EVENT: TPEG Pti_19_24 special event.
    :cvar BRIDGE_STRIKE: TPEG Pti_19_25 bridge strike.
    :cvar OVERHEAD_OBSTRUCTION: TPEG Pti_19_26 overhead obstruction.
    :cvar UNDEFINED_PROBLEM: TPEG Pti_19_255 undefined problem.
    :cvar MARCH:
    :cvar PROCESSION:
    :cvar DEMONSTRATION:
    :cvar PUBLIC_DISTURBANCE:
    :cvar FILTER_BLOCKADE:
    :cvar SIGHTSEERS_OBSTRUCTING_ACCESS:
    :cvar PROBLEMS_AT_BORDER_POST:
    :cvar PROBLEMS_AT_CUSTOME_POST:
    :cvar PROBLEMS_ON_LOCAL_ROAD:
    """

    NEAR_MISS = "nearMiss"
    SAFETY_VIOLATION = "safetyViolation"
    SIGNAL_PASSED_AT_DANGER = "signalPassedAtDanger"
    STATION_OVERRUN = "stationOverrun"
    TRAIN_DOOR = "trainDoor"
    EMERGENCY_SERVICES_CALL = "emergencyServicesCall"
    POLICE_REQUEST = "policeRequest"
    FIRE_BRIGADE_SAFETY_CHECKS = "fireBrigadeSafetyChecks"
    UNATTENDED_BAG = "unattendedBag"
    TELEPHONED_THREAT = "telephonedThreat"
    SUSPECT_VEHICLE = "suspectVehicle"
    VANDALISM = "vandalism"
    PASSENGER_ACTION = "passengerAction"
    STAFF_ASSAULT = "staffAssault"
    RAILWAY_CRIME = "railwayCrime"
    ALTERCATION = "altercation"
    THEFT = "theft"
    FATALITY = "fatality"
    ILL_VEHICLE_OCCUPANTS = "illVehicleOccupants"
    PERSON_UNDER_TRAIN = "personUnderTrain"
    PERSON_HIT_BY_TRAIN = "personHitByTrain"
    PERSON_ILL_ON_VEHICLE = "personIllOnVehicle"
    EMERGENCY_SERVICES = "emergencyServices"
    COLLISION = "collision"
    LINESIDE_FIRE = "linesideFire"
    LEVEL_CROSSING_INCIDENT = "levelCrossingIncident"
    FALLEN_TREE_ON_THE_LINE = "fallenTreeOnTheLine"
    VEGETATION = "vegetation"
    TRAIN_STRUCK_ANIMAL = "trainStruckAnimal"
    TRAIN_STRUCK_OBJECT = "trainStruckObject"
    ANIMAL_ON_THE_LINE = "animalOnTheLine"
    ROUTE_DIVERSION = "routeDiversion"
    ROAD_CLOSED = "roadClosed"
    ROADWORKS = "roadworks"
    SPECIAL_EVENT = "specialEvent"
    BRIDGE_STRIKE = "bridgeStrike"
    OVERHEAD_OBSTRUCTION = "overheadObstruction"
    UNDEFINED_PROBLEM = "undefinedProblem"
    MARCH = "march"
    PROCESSION = "procession"
    DEMONSTRATION = "demonstration"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    FILTER_BLOCKADE = "filterBlockade"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOME_POST = "problemsAtCustomePost"
    PROBLEMS_ON_LOCAL_ROAD = "problemsOnLocalRoad"


class PersonnelReasonEnumeration(Enum):
    """
    Values for Personnel incident reason types TPEG Pti18_2/TPEG Pti_20.

    :cvar PTI20_0:
    :cvar UNKNOWN: TPEG Pti20_0 unknown.
    :cvar PTI20_1:
    :cvar STAFF_SICKNESS: TPEG Pti20_1 staff sickness.
    :cvar PTI20_1_ALIAS_1:
    :cvar STAFF_INJURY: staff injury alias to TPEG Pti20_1 staff
        sickness.
    :cvar PTI20_1_ALIAS_2:
    :cvar CONTRACTOR_STAFF_INJURY: contractor staff injury alias to TPEG
        Pti20_1 staff sickness.
    :cvar PTI20_2:
    :cvar STAFF_ABSENCE: TPEG Pti20_2 staff absence.
    :cvar PTI20_3:
    :cvar STAFF_IN_WRONG_PLACE: TPEG Pti20_3 staff in wrong place.
    :cvar PTI20_4:
    :cvar STAFF_SHORTAGE: TPEG Pti20_4 staff shortage.
    :cvar PTI20_5:
    :cvar INDUSTRIAL_ACTION: TPEG Pti20_5 industrial action.
    :cvar PTI20_5_ALIAS_1:
    :cvar UNOFFICIAL_INDUSTRIAL_ACTION: Unofffical action - alias to
        TPEG Pti20_5 industrial action.
    :cvar PTI20_6:
    :cvar WORK_TO_RULE: TPEG Pti20_6 work to rule.
    :cvar PTI20_255:
    :cvar UNDEFINED_PERSONNEL_PROBLEM: TPEG Pti20_255 undefined
        personnel problem.
    """

    PTI20_0 = "pti20_0"
    UNKNOWN = "unknown"
    PTI20_1 = "pti20_1"
    STAFF_SICKNESS = "staffSickness"
    PTI20_1_ALIAS_1 = "pti20_1_Alias_1"
    STAFF_INJURY = "staffInjury"
    PTI20_1_ALIAS_2 = "pti20_1_Alias_2"
    CONTRACTOR_STAFF_INJURY = "contractorStaffInjury"
    PTI20_2 = "pti20_2"
    STAFF_ABSENCE = "staffAbsence"
    PTI20_3 = "pti20_3"
    STAFF_IN_WRONG_PLACE = "staffInWrongPlace"
    PTI20_4 = "pti20_4"
    STAFF_SHORTAGE = "staffShortage"
    PTI20_5 = "pti20_5"
    INDUSTRIAL_ACTION = "industrialAction"
    PTI20_5_ALIAS_1 = "pti20_5_Alias_1"
    UNOFFICIAL_INDUSTRIAL_ACTION = "unofficialIndustrialAction"
    PTI20_6 = "pti20_6"
    WORK_TO_RULE = "workToRule"
    PTI20_255 = "pti20_255"
    UNDEFINED_PERSONNEL_PROBLEM = "undefinedPersonnelProblem"


class PersonnelSubReasonEnumeration(Enum):
    """
    Values for Personnel incident sub reason types.
    """

    STAFF_SICKNESS = "staffSickness"
    STAFF_INJURY = "staffInjury"
    UNOFFICIAL_INDUSTRIAL_ACTION = "unofficialIndustrialAction"


@dataclass
class UndefinedReason:
    """
    TPEG Pti18_255/TPEG Pti_22 undefined event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class UnknownReason:
    """
    TPEG Pti18_0/TPEG unknown event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class EnvironmentReason:
    """
    TPEG Pti18_4/TPEG Pti_22 environment event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EnvironmentReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class EnvironmentSubReason:
    """
    Additional refinements TPEG Environmentevent reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EnvironmentSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class EquipmentReason:
    """
    TPEG Pti18_3/TPEG Pti_21 equipment event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EquipmentReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class EquipmentSubReason:
    """
    Additional refinements TPEG Equipment event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[EquipmentSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MiscellaneousReason:
    """
    TPEG Pti18_1/TPEG Pti_19 miscellaneous event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[MiscellaneousReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class MiscellaneousSubReason:
    """
    Additional refinements TPEG miscellaneous event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[MiscellaneousSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class PersonnelReason:
    """
    TPEG Pti18_2/TPEG Pti_20 personnel event reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[PersonnelReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class PersonnelSubReason:
    """
    Additional refinements TPEG Personnelevent reason.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[PersonnelSubReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
