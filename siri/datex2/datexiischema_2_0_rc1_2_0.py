from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlTime

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class AbnormalTrafficTypeEnum(Enum):
    STATIONARY_TRAFFIC = "stationaryTraffic"
    QUEUING_TRAFFIC = "queuingTraffic"
    SLOW_TRAFFIC = "slowTraffic"
    HEAVY_TRAFFIC = "heavyTraffic"
    UNSPECIFIED_ABNORMAL_TRAFFIC = "unspecifiedAbnormalTraffic"
    OTHER = "other"


class AccidentCauseEnum(Enum):
    AVOIDANCE_OF_OBSTACLES = "avoidanceOfObstacles"
    DRIVER_DISTRACTION = "driverDistraction"
    DRIVER_DRUG_ABUSE = "driverDrugAbuse"
    DRIVER_ILLNESS = "driverIllness"
    EXCEEDING_SPEEDS_LIMITS = "exceedingSpeedsLimits"
    EXCESS_ALCOHOL = "excessAlcohol"
    EXCESSIVE_DRIVER_TIREDNESS = "excessiveDriverTiredness"
    IMPERMISSIBLE_MANOEUVRE = "impermissibleManoeuvre"
    LIMITED_VISIBILITY = "limitedVisibility"
    NOT_KEEPING_ASAFE_DISTANCE = "notKeepingASafeDistance"
    ON_THE_WRONG_SIDE_OF_THE_ROAD = "onTheWrongSideOfTheRoad"
    PEDESTRIAN_IN_ROAD = "pedestrianInRoad"
    POOR_LANE_ADHERENCE = "poorLaneAdherence"
    POOR_MERGE_ENTRY_OR_EXIT_JUDGEMENT = "poorMergeEntryOrExitJudgement"
    POOR_ROAD_SURFACE_CONDITION = "poorRoadSurfaceCondition"
    POOR_SURFACE_ADHERENCE = "poorSurfaceAdherence"
    UNDISCLOSED = "undisclosed"
    UNKNOWN = "unknown"
    VEHICLE_FAILURE = "vehicleFailure"
    OTHER = "other"


class AccidentTypeEnum(Enum):
    ACCIDENT = "accident"
    ACCIDENT_INVOLVING_BICYCLES = "accidentInvolvingBicycles"
    ACCIDENT_INVOLVING_BUSES = "accidentInvolvingBuses"
    ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS = "accidentInvolvingHazardousMaterials"
    ACCIDENT_INVOLVING_HEAVY_LORRIES = "accidentInvolvingHeavyLorries"
    ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE = "accidentInvolvingMassTransitVehicle"
    ACCIDENT_INVOLVING_MOPEDS = "accidentInvolvingMopeds"
    ACCIDENT_INVOLVING_MOTORCYCLES = "accidentInvolvingMotorcycles"
    ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL = "accidentInvolvingRadioactiveMaterial"
    ACCIDENT_INVOLVING_TRAIN = "accidentInvolvingTrain"
    CHEMICAL_SPILLAGE_ACCIDENT = "chemicalSpillageAccident"
    COLLISION = "collision"
    COLLISION_WITH_ANIMAL = "collisionWithAnimal"
    COLLISION_WITH_OBSTRUCTION = "collisionWithObstruction"
    COLLISION_WITH_PERSON = "collisionWithPerson"
    EARLIER_ACCIDENT = "earlierAccident"
    FUEL_SPILLAGE_ACCIDENT = "fuelSpillageAccident"
    HEAD_ON_COLLISION = "headOnCollision"
    HEAD_ON_OR_SIDE_COLLISION = "headOnOrSideCollision"
    JACKKNIFED_ARTICULATED_LORRY = "jackknifedArticulatedLorry"
    JACKKNIFED_CARAVAN = "jackknifedCaravan"
    JACKKNIFED_TRAILER = "jackknifedTrailer"
    MULTIPLE_VEHICLE_COLLISION = "multipleVehicleCollision"
    MULTIVEHICLE_ACCIDENT = "multivehicleAccident"
    OIL_SPILLAGE_ACCIDENT = "oilSpillageAccident"
    OVERTURNED_HEAVY_LORRY = "overturnedHeavyLorry"
    OVERTURNED_TRAILER = "overturnedTrailer"
    OVERTURNED_VEHICLE = "overturnedVehicle"
    REAR_COLLISION = "rearCollision"
    SECONDARY_ACCIDENT = "secondaryAccident"
    SERIOUS_ACCIDENT = "seriousAccident"
    SIDE_COLLISION = "sideCollision"
    VEHICLE_OFF_ROAD = "vehicleOffRoad"
    VEHICLE_SPUN_AROUND = "vehicleSpunAround"
    OTHER = "other"


class AlertCdirectionEnum(Enum):
    BOTH = "both"
    NEGATIVE = "negative"
    POSITIVE = "positive"
    UNKNOWN = "unknown"


class AnimalPresenceTypeEnum(Enum):
    ANIMALS_ON_THE_ROAD = "animalsOnTheRoad"
    HERD_OF_ANIMALS_ON_THE_ROAD = "herdOfAnimalsOnTheRoad"
    LARGE_ANIMALS_ON_THE_ROAD = "largeAnimalsOnTheRoad"


class AreaOfInterestEnum(Enum):
    CONTINENT_WIDE = "continentWide"
    NATIONAL = "national"
    NEIGHBOURING_COUNTRIES = "neighbouringCountries"
    NOT_SPECIFIED = "notSpecified"
    REGIONAL = "regional"


class AuthorityOperationTypeEnum(Enum):
    ACCIDENT_INVESTIGATION_WORK = "accidentInvestigationWork"
    BOMB_SQUAD_IN_ACTION = "bombSquadInAction"
    CIVIL_EMERGENCY = "civilEmergency"
    CUSTOMS_OPERATION = "customsOperation"
    JURIDICAL_RECONSTRUCTION = "juridicalReconstruction"
    POLICE_CHECK_POINT = "policeCheckPoint"
    POLICE_INVESTIGATION = "policeInvestigation"
    ROAD_OPERATOR_CHECK_POINT = "roadOperatorCheckPoint"
    SURVEY = "survey"
    TRANSPORT_OF_VIP = "transportOfVip"
    UNDEFINED_AUTHORITY_ACTIVITY = "undefinedAuthorityActivity"
    VEHICLE_INSPECTION_CHECK_POINT = "vehicleInspectionCheckPoint"
    VEHICLE_WEIGHING = "vehicleWeighing"
    WEIGH_IN_MOTION = "weighInMotion"
    OTHER = "other"


class CarParkConfigurationEnum(Enum):
    MULTI_STOREY = "multiStorey"
    PARK_AND_RIDE = "parkAndRide"
    SINGLE_LEVEL = "singleLevel"
    UNDERGROUND = "underground"


class CarParkStatusEnum(Enum):
    CAR_PARK_CLOSED = "carParkClosed"
    ALL_CAR_PARKS_FULL = "allCarParksFull"
    CAR_PARK_FACILITY_FAULTY = "carParkFacilityFaulty"
    CAR_PARK_FULL = "carParkFull"
    CAR_PARK_STATUS_UNKNOWN = "carParkStatusUnknown"
    ENOUGH_SPACES_AVAILABLE = "enoughSpacesAvailable"
    MULTI_STORY_CAR_PARKS_FULL = "multiStoryCarParksFull"
    NO_MORE_PARKING_SPACES_AVAILABLE = "noMoreParkingSpacesAvailable"
    NO_PARK_AND_RIDE_INFORMATION = "noParkAndRideInformation"
    NO_PARKING_ALLOWED = "noParkingAllowed"
    NO_PARKING_INFORMATION_AVAILABLE = "noParkingInformationAvailable"
    NORMAL_PARKING_RESTRICTIONS_LIFTED = "normalParkingRestrictionsLifted"
    ONLY_AFEW_SPACES_AVAILABLE = "onlyAFewSpacesAvailable"
    PARK_AND_RIDE_SERVICE_NOT_OPERATING = "parkAndRideServiceNotOperating"
    PARK_AND_RIDE_SERVICE_OPERATING = "parkAndRideServiceOperating"
    SPECIAL_PARKING_RESTRICTIONS_IN_FORCE = "specialParkingRestrictionsInForce"


class CarriagewayEnum(Enum):
    CONNECTING_CARRIAGEWAY = "connectingCarriageway"
    ENTRY_SLIP_ROAD = "entrySlipRoad"
    EXIT_SLIP_ROAD = "exitSlipRoad"
    FLYOVER = "flyover"
    LEFT_HAND_FEEDER_ROAD = "leftHandFeederRoad"
    LEFT_HAND_PARALLEL_CARRIAGEWAY = "leftHandParallelCarriageway"
    MAIN_CARRIAGEWAY = "mainCarriageway"
    OPPOSITE_CARRIAGEWAY = "oppositeCarriageway"
    PARALLEL_CARRIAGEWAY = "parallelCarriageway"
    RIGHT_HAND_FEEDER_ROAD = "rightHandFeederRoad"
    RIGHT_HAND_PARALLEL_CARRIAGEWAY = "rightHandParallelCarriageway"
    SERVICE_ROAD = "serviceRoad"
    SLIP_ROADS = "slipRoads"
    UNDERPASS = "underpass"


class CauseTypeEnum(Enum):
    ACCIDENT = "accident"
    CONGESTION = "congestion"
    EARLIER_ACCIDENT = "earlierAccident"
    EARLIER_EVENT = "earlierEvent"
    EARLIER_INCIDENT = "earlierIncident"
    EQUIPMENT_FAILURE = "equipmentFailure"
    EXCESSIVE_HEAT = "excessiveHeat"
    FROST = "frost"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    INFRASTRUCTURE_FAILURE = "infrastructureFailure"
    LARGE_NUMBERS_OF_VISITORS = "largeNumbersOfVisitors"
    OBSTRUCTION = "obstruction"
    POLLUTION_ALERT = "pollutionAlert"
    POOR_WEATHER = "poorWeather"
    PROBLEMS_AT_BORDER_POST = "problemsAtBorderPost"
    PROBLEMS_AT_CUSTOM_POST = "problemsAtCustomPost"
    PROBLEMS_ON_LOCAL_ROADS = "problemsOnLocalRoads"
    RADIOACTIVE_LEAK_ALERT = "radioactiveLeakAlert"
    ROADSIDE_EVENT = "roadsideEvent"
    RUBBER_NECKING = "rubberNecking"
    SECURITY_INCIDENT = "securityIncident"
    SHEAR_WEIGHT_OF_TRAFFIC = "shearWeightOfTraffic"
    TECHNICAL_PROBLEMS = "technicalProblems"
    TERRORISM = "terrorism"
    TOXIC_CLOUD_ALERT = "toxicCloudAlert"
    VANDALISM = "vandalism"
    OTHER = "other"


class ChangedFlagEnum(Enum):
    CATALOGUE = "catalogue"
    FILTER = "filter"


class ComparisonOperatorEnum(Enum):
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATHER_THAN_OR_EQUAL_TO = "greatherThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"


class ComplianceOptionEnum(Enum):
    ADVISORY = "advisory"
    MANDATORY = "mandatory"


class ComputationMethodEnum(Enum):
    ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES = (
        "arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples"
    )
    ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "arithmeticAverageOfSamplesInATimePeriod"
    HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "harmonicAverageOfSamplesInATimePeriod"
    MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD = "medianOfSamplesInATimePeriod"
    MOVING_AVERAGE_OF_SAMPLES = "movingAverageOfSamples"


class ConfidentialityValueEnum(Enum):
    INTERNAL_USE = "internalUse"
    NO_RESTRICTION = "noRestriction"
    RESTRICTED_TO_AUTHORITIES = "restrictedToAuthorities"
    RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS = "restrictedToAuthoritiesAndTrafficOperators"
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_PUBLISHERS = "restrictedToAuthoritiesTrafficOperatorsAndPublishers"
    RESTRICTED_TO_AUTHORITIES_TRAFFIC_OPERATORS_AND_VMS = "restrictedToAuthoritiesTrafficOperatorsAndVms"


class ConstructionWorkTypeEnum(Enum):
    BLASTING_WORK = "blastingWork"
    CONSTRUCTION_WORK = "constructionWork"
    DEMOLITION_WORK = "demolitionWork"
    ROAD_WIDENING_WORK = "roadWideningWork"


class CountryEnum(Enum):
    AT = "at"
    BE = "be"
    BG = "bg"
    CH = "ch"
    CS = "cs"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DK = "dk"
    EE = "ee"
    ES = "es"
    FI = "fi"
    FO = "fo"
    FR = "fr"
    GB = "gb"
    GG = "gg"
    GI = "gi"
    GR = "gr"
    HR = "hr"
    HU = "hu"
    IE = "ie"
    IM = "im"
    IS = "is"
    IT = "it"
    JE = "je"
    LI = "li"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    MA = "ma"
    MC = "mc"
    MK = "mk"
    MT = "mt"
    NL = "nl"
    NO = "no"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    SE = "se"
    SI = "si"
    SK = "sk"
    SM = "sm"
    TR = "tr"
    VA = "va"
    OTHER = "other"


class DangerousGoodsRegulationsEnum(Enum):
    ADR = "adr"
    IATA_ICAO = "iataIcao"
    IMO_IMDG = "imoImdg"
    RAILROAD_DANGEROUS_GOODS_BOOK = "railroadDangerousGoodsBook"


class DatexPictogramEnum(Enum):
    ADVISORY_SPEED = "advisorySpeed"
    BLANK_VOID = "blankVoid"
    CHAINS_OR_SNOW_TYRES_RECOMMENDED = "chainsOrSnowTyresRecommended"
    CROSS_WIND = "crossWind"
    DRIVING_OF_VEHICLES_LESS_THAN_XMETRES_APART_PROHIBITED = "drivingOfVehiclesLessThanXMetresApartProhibited"
    END_OF_ADVISORY_SPEED = "endOfAdvisorySpeed"
    END_OF_PROHIBITION_OF_OVERTAKING = "endOfProhibitionOfOvertaking"
    END_OF_PROHIBITION_OF_OVERTAKING_FOR_GOODS_VEHICLES = "endOfProhibitionOfOvertakingForGoodsVehicles"
    END_OF_SPEED_LIMIT = "endOfSpeedLimit"
    EXIT_CLOSED = "exitClosed"
    FOG = "fog"
    KEEP_ASAFE_DISTANCE = "keepASafeDistance"
    MAXIMUM_SPEED_LIMIT = "maximumSpeedLimit"
    NO_ENTRY = "noEntry"
    NO_ENTRY_FOR_GOODS_VEHICLES = "noEntryForGoodsVehicles"
    NO_ENTRY_FOR_VEHICLES_EXCEEDING_XTONNES_LADEN_MASS = "noEntryForVehiclesExceedingXTonnesLadenMass"
    NO_ENTRY_FOR_VEHICLES_HAVING_AMASS_EXCEEDING_XTONNES_ON_ONE_AXLE = (
        "noEntryForVehiclesHavingAMassExceedingXTonnesOnOneAxle"
    )
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_HEIGHT_EXCEEDING_XMETRES = (
        "noEntryForVehiclesHavingAnOverallHeightExceedingXMetres"
    )
    NO_ENTRY_FOR_VEHICLES_HAVING_AN_OVERALL_LENGTH_EXCEEDING_XMETRES = (
        "noEntryForVehiclesHavingAnOverallLengthExceedingXMetres"
    )
    NO_ENTRY_FOR_VEHICLES_CARRYING_DANGEROUS_GOODS = "noEntryForVehiclesCarryingDangerousGoods"
    OTHER_DANGER = "otherDanger"
    OVERTAKING_BY_GOODS_VEHICLES_PROHIBITED = "overtakingByGoodsVehiclesProhibited"
    OVERTAKING_PROHIBITED = "overtakingProhibited"
    ROAD_CLOSED_AHEAD = "roadClosedAhead"
    ROADWORKS = "roadworks"
    SLIPPERY_ROAD = "slipperyRoad"
    SNOW = "snow"
    SNOW_TYRES_COMPULSORY = "snowTyresCompulsory"
    TRAFFIC_CONGESTION = "trafficCongestion"


class DayEnum(Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class DelayBandEnum(Enum):
    NEGLIGIBLE = "negligible"
    UP_TO_TEN_MINUTES = "upToTenMinutes"
    BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES = "betweenTenMinutesAndThirtyMinutes"
    BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR = "betweenThirtyMinutesAndOneHour"
    BETWEEN_ONE_HOUR_AND_THREE_HOURS = "betweenOneHourAndThreeHours"
    BETWEEN_THREE_HOURS_AND_SIX_HOURS = "betweenThreeHoursAndSixHours"
    LONGER_THAN_SIX_HOURS = "longerThanSixHours"


class DelaysTypeEnum(Enum):
    DELAYS = "delays"
    DELAYS_OF_UNCERTAIN_DURATION = "delaysOfUncertainDuration"
    LONG_DELAYS = "longDelays"
    VERY_LONG_DELAYS = "veryLongDelays"


class DenyReasonEnum(Enum):
    UNKNOWN_REASON = "unknownReason"
    WRONG_CATALOGUE = "wrongCatalogue"
    WRONG_FILTER = "wrongFilter"
    WRONG_ORDER = "wrongOrder"
    WRONG_PARTNER = "wrongPartner"


class DirectionCompassEnum(Enum):
    EAST = "east"
    EAST_NORTH_EAST = "eastNorthEast"
    EAST_SOUTH_EAST = "eastSouthEast"
    NORTH = "north"
    NORTH_EAST = "northEast"
    NORTH_NORTH_EAST = "northNorthEast"
    NORTH_NORTH_WEST = "northNorthWest"
    NORTH_WEST = "northWest"
    SOUTH = "south"
    SOUTH_EAST = "southEast"
    SOUTH_SOUTH_EAST = "southSouthEast"
    SOUTH_SOUTH_WEST = "southSouthWest"
    SOUTH_WEST = "southWest"
    WEST = "west"
    WEST_NORTH_WEST = "westNorthWest"
    WEST_SOUTH_WEST = "westSouthWest"


class DirectionEnum(Enum):
    ANTICLOCKWISE = "anticlockwise"
    CLOCKWISE = "clockwise"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    EAST_BOUND = "eastBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_BOUND = "southBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    NORTH_WEST_BOUND = "northWestBound"
    INBOUND_TOWARDS_TOWN = "inboundTowardsTown"
    OUTBOUND_FROM_TOWN = "outboundFromTown"


class DisturbanceActivityTypeEnum(Enum):
    AIR_RAID = "airRaid"
    ALTERCATION_OF_VEHICLE_OCCUPANTS = "altercationOfVehicleOccupants"
    ASSAULT = "assault"
    ASSET_DESTRUCTION = "assetDestruction"
    ATTACK = "attack"
    ATTACK_ON_VEHICLE = "attackOnVehicle"
    BLOCKADE_OR_BARRIER = "blockadeOrBarrier"
    BOMB_ALERT = "bombAlert"
    CROWD = "crowd"
    DEMONSTRATION = "demonstration"
    EVACUATION = "evacuation"
    FILTER_BLOCKADE = "filterBlockade"
    GO_SLOW_OPERATION = "goSlowOperation"
    GUNFIRE_ON_ROADWAY = "gunfireOnRoadway"
    ILL_VEHICLE_OCCUPANTS = "illVehicleOccupants"
    MARCH = "march"
    PUBLIC_DISTURBANCE = "publicDisturbance"
    RADIOACTIVE_LEAK_ALERT = "radioactiveLeakAlert"
    RIOT = "riot"
    SABOTAGE = "sabotage"
    SECURITY_ALERT = "securityAlert"
    SECURITY_INCIDENT = "securityIncident"
    SIGHTSEERS_OBSTRUCTING_ACCESS = "sightseersObstructingAccess"
    STRIKE = "strike"
    TERRORIST_INCIDENT = "terroristIncident"
    THEFT = "theft"
    TOXIC_CLOUD_ALERT = "toxicCloudAlert"
    UNSPECIFIED_ALERT = "unspecifiedAlert"
    OTHER = "other"


class DrivingConditionTypeEnum(Enum):
    IMPOSSIBLE = "impossible"
    HAZARDOUS = "hazardous"
    NORMAL = "normal"
    PASSABLE_WITH_CARE = "passableWithCare"
    UNKNOWN = "unknown"
    VERY_HAZARDOUS = "veryHazardous"
    WINTER_CONDITIONS = "winterConditions"
    OTHER = "other"


class EnvironmentalObstructionTypeEnum(Enum):
    AVALANCHES = "avalanches"
    EARTHQUAKE_DAMAGE = "earthquakeDamage"
    FALLEN_TREES = "fallenTrees"
    FALLING_ICE = "fallingIce"
    FALLING_LIGHT_ICE_OR_SNOW = "fallingLightIceOrSnow"
    FLASH_FLOODS = "flashFloods"
    FLOODING = "flooding"
    FOREST_FIRE = "forestFire"
    GRASS_FIRE = "grassFire"
    LANDSLIPS = "landslips"
    MUD_SLIDE = "mudSlide"
    SEWER_OVERFLOW = "sewerOverflow"
    ROCKFALLS = "rockfalls"
    SERIOUS_FIRE = "seriousFire"
    SMOKE_OR_FUMES = "smokeOrFumes"
    STORM_DAMAGE = "stormDamage"
    SUBSIDENCE = "subsidence"
    OTHER = "other"


class EquipmentOrSystemFaultTypeEnum(Enum):
    NOT_WORKING = "notWorking"
    OUT_OF_SERVICE = "outOfService"
    WORKING_INCORRECTLY = "workingIncorrectly"
    WORKING_INTERMITTENTLY = "workingIntermittently"


class EquipmentOrSystemTypeEnum(Enum):
    AUTOMATED_TOLL_SYSTEM = "automatedTollSystem"
    EMERGENCY_ROADSIDE_TELEPHONES = "emergencyRoadsideTelephones"
    GALLERY_LIGHTS = "galleryLights"
    LANE_CONTROL_SIGNS = "laneControlSigns"
    LEVEL_CROSSING = "levelCrossing"
    MATRIX_SIGNS = "matrixSigns"
    RAMP_CONTROLS = "rampControls"
    ROADSIDE_COMMUNICATIONS_SYSTEM = "roadsideCommunicationsSystem"
    ROADSIDE_POWER_SYSTEM = "roadsidePowerSystem"
    SPEED_CONTROL_SIGNS = "speedControlSigns"
    STREET_LIGHTING = "streetLighting"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES = "tollGates"
    TRAFFIC_LIGHT_SETS = "trafficLightSets"
    TRAFFIC_SIGNALS = "trafficSignals"
    TUNNEL_LIGHTS = "tunnelLights"
    TUNNEL_VENTILATION = "tunnelVentilation"
    VARIABLE_MESSAGE_SIGNS = "variableMessageSigns"
    OTHER = "other"


@dataclass
class ExtensionType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


class FuelTypeEnum(Enum):
    BATTERY = "battery"
    BIODIESEL = "biodiesel"
    DIESEL = "diesel"
    DIESEL_BATTERY_HYBRID = "dieselBatteryHybrid"
    ETHANOL = "ethanol"
    HYDROGEN = "hydrogen"
    LIQUID_GAS = "liquidGas"
    LPG = "lpg"
    METHANE = "methane"
    PETROL = "petrol"
    PETROL_BATTERY_HYBRID = "petrolBatteryHybrid"


class GeneralInstructionToRoadUsersTypeEnum(Enum):
    ALLOW_EMERGENCY_VEHICLES_TO_PASS = "allowEmergencyVehiclesToPass"
    APPROACH_WITH_CARE = "approachWithCare"
    AVOID_THE_AREA = "avoidTheArea"
    CLOSE_ALL_WINDOWS_TURN_OFF_HEATER_AND_VENTS = "closeAllWindowsTurnOffHeaterAndVents"
    CROSS_JUNCTION_WITH_CARE = "crossJunctionWithCare"
    DO_NOT_ALLOW_UNNECESSARY_GAPS = "doNotAllowUnnecessaryGaps"
    DO_NOT_LEAVE_YOUR_VEHICLE = "doNotLeaveYourVehicle"
    DO_NOT_THROW_OUT_ANY_BURNING_OBJECTS = "doNotThrowOutAnyBurningObjects"
    DO_NOT_USE_NAVIGATION_SYSTEMS = "doNotUseNavigationSystems"
    DRIVE_CAREFULLY = "driveCarefully"
    DRIVE_WITH_EXTREME_CAUTION = "driveWithExtremeCaution"
    FLASH_YOUR_LIGHTS = "flashYourLights"
    FOLLOW_THE_VEHICLE_IN_FRONT_SMOOTHLY = "followTheVehicleInFrontSmoothly"
    INCREASE_NORMAL_FOLLOWING_DISTANCE = "increaseNormalFollowingDistance"
    IN_EMERGENCY_WAIT_FOR_PATROL_SERVICE = "inEmergencyWaitForPatrolService"
    KEEP_YOUR_DISTANCE = "keepYourDistance"
    LEAVE_YOUR_VEHICLE_PROCEED_TO_NEXT_SAFE_PLACE = "leaveYourVehicleProceedToNextSafePlace"
    NO_NAKED_FLAMES = "noNakedFlames"
    NO_OVERTAKING = "noOvertaking"
    NO_SMOKING = "noSmoking"
    NO_STOPPING = "noStopping"
    NO_UTURNS = "noUturns"
    OBSERVE_SIGNALS = "observeSignals"
    OBSERVE_SIGNS = "observeSigns"
    ONLY_TRAVEL_IF_ABSOLUTELY_NECESSARY = "onlyTravelIfAbsolutelyNecessary"
    OVERTAKE_WITH_CARE = "overtakeWithCare"
    PULL_OVER_TO_THE_EDGE_OF_THE_ROADWAY = "pullOverToTheEdgeOfTheRoadway"
    STOP_AT_NEXT_SAFE_PLACE = "stopAtNextSafePlace"
    STOP_AT_NEXT_SERVICE_AREA = "stopAtNextServiceArea"
    SWITCH_OFF_ENGINE = "switchOffEngine"
    SWITCH_OFF_MOBILE_PHONES_AND_TWO_WAY_RADIOS = "switchOffMobilePhonesAndTwoWayRadios"
    TEST_YOUR_BRAKES = "testYourBrakes"
    USE_BUS_SERVICE = "useBusService"
    USE_FOG_LIGHTS = "useFogLights"
    USE_HAZARD_WARNING_LIGHTS = "useHazardWarningLights"
    USE_HEADLIGHTS = "useHeadlights"
    USE_RAIL_SERVICE = "useRailService"
    USE_TRAM_SERVICE = "useTramService"
    USE_UNDERGROUND_SERVICE = "useUndergroundService"
    WAIT_FOR_ESCORT_VEHICLE = "waitForEscortVehicle"
    OTHER = "other"


class GeneralNetworkManagementTypeEnum(Enum):
    BRIDGE_SWING_IN_OPERATION = "bridgeSwingInOperation"
    CONVOY_SERVICE = "convoyService"
    OBSTACLE_SIGNALLING = "obstacleSignalling"
    RAMP_METERING_IN_OPERATION = "rampMeteringInOperation"
    TEMPORARY_TRAFFIC_LIGHTS = "temporaryTrafficLights"
    TOLL_GATES_OPEN = "tollGatesOpen"
    TRAFFIC_BEING_MANUALLY_DIRECTED = "trafficBeingManuallyDirected"
    TRAFFIC_HELD = "trafficHeld"
    OTHER = "other"


class InformationStatusEnum(Enum):
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"


class InfrastructureDamageTypeEnum(Enum):
    BURST_PIPE = "burstPipe"
    BURST_WATER_MAIN = "burstWaterMain"
    COLLAPSED_SEWER = "collapsedSewer"
    DAMAGED_BRIDGE = "damagedBridge"
    DAMAGED_CRASH_BARRIER = "damagedCrashBarrier"
    DAMAGED_FLYOVER = "damagedFlyover"
    DAMAGED_GALLERY = "damagedGallery"
    DAMAGED_GANTRY = "damagedGantry"
    DAMAGED_ROAD_SURFACE = "damagedRoadSurface"
    DAMAGED_TUNNEL = "damagedTunnel"
    DAMAGED_VIADUCT = "damagedViaduct"
    FALLEN_POWER_CABLES = "fallenPowerCables"
    GAS_LEAK = "gasLeak"
    WEAK_BRIDGE = "weakBridge"
    OTHER = "other"


class InjuryStatusTypeEnum(Enum):
    DEAD = "dead"
    INJURED = "injured"
    SERIOUSLY_INJURED = "seriouslyInjured"
    SLIGHTLY_INJURED = "slightlyInjured"
    UNINJURED = "uninjured"
    UNKNOWN = "unknown"


class InvolvementRolesEnum(Enum):
    CYCLIST = "cyclist"
    PEDESTRIAN = "pedestrian"
    UNKNOWN = "unknown"
    VEHICLE_DRIVER = "vehicleDriver"
    VEHICLE_OCCUPANT = "vehicleOccupant"
    VEHICLE_PASSENGER = "vehiclePassenger"
    WITNESS = "witness"


class LaneEnum(Enum):
    ALL_LANES_COMPLETE_CARRIAGEWAY = "allLanesCompleteCarriageway"
    BUS_LANE = "busLane"
    BUS_STOP = "busStop"
    CAR_POOL_LANE = "carPoolLane"
    CENTRAL_RESERVATION = "centralReservation"
    CRAWLER_LANE = "crawlerLane"
    EMERGENCY_LANE = "emergencyLane"
    ESCAPE_LANE = "escapeLane"
    EXPRESS_LANE = "expressLane"
    HARD_SHOULDER = "hardShoulder"
    HEAVY_VEHICLE_LANE = "heavyVehicleLane"
    LANE1 = "lane1"
    LANE2 = "lane2"
    LANE3 = "lane3"
    LANE4 = "lane4"
    LANE5 = "lane5"
    LANE6 = "lane6"
    LANE7 = "lane7"
    LANE8 = "lane8"
    LANE9 = "lane9"
    LAY_BY = "layBy"
    LEFT_HAND_TURNING_LANE = "leftHandTurningLane"
    LEFT_LANE = "leftLane"
    LOCAL_TRAFFIC_LANE = "localTrafficLane"
    MIDDLE_LANE = "middleLane"
    OPPOSING_LANES = "opposingLanes"
    OVERTAKING_LANE = "overtakingLane"
    RIGHT_HAND_TURNING_LANE = "rightHandTurningLane"
    RIGHT_LANE = "rightLane"
    RUSH_HOUR_LANE = "rushHourLane"
    SET_DOWN_AREA = "setDownArea"
    SLOW_VEHICLE_LANE = "slowVehicleLane"
    THROUGH_TRAFFIC_LANE = "throughTrafficLane"
    TIDAL_FLOW_LANE = "tidalFlowLane"
    TURNING_LANE = "turningLane"
    VERGE = "verge"


class LoadTypeEnum(Enum):
    ABNORMAL_LOAD = "abnormalLoad"
    AMMUNITION = "ammunition"
    CHEMICALS = "chemicals"
    COMBUSTIBLE_MATERIALS = "combustibleMaterials"
    CORROSIVE_MATERIALS = "corrosiveMaterials"
    DEBRIS = "debris"
    EMPTY = "empty"
    EXPLOSIVE_MATERIALS = "explosiveMaterials"
    EXTRA_HIGH_LOAD = "extraHighLoad"
    EXTRA_LONG_LOAD = "extraLongLoad"
    EXTRA_WIDE_LOAD = "extraWideLoad"
    FUEL = "fuel"
    GLASS = "glass"
    GOODS = "goods"
    HAZARDOUS_MATERIALS = "hazardousMaterials"
    LIQUID = "liquid"
    LIVESTOCK = "livestock"
    MATERIALS = "materials"
    MATERIALS_DANGEROUS_FOR_PEOPLE = "materialsDangerousForPeople"
    MATERIALS_DANGEROUS_FOR_THE_ENVIRONMENT = "materialsDangerousForTheEnvironment"
    MATERIALS_DANGEROUS_FOR_WATER = "materialsDangerousForWater"
    OIL = "oil"
    ORDINARY = "ordinary"
    PERISHABLE_PRODUCTS = "perishableProducts"
    PETROL = "petrol"
    PHARMACEUTICAL_MATERIALS = "pharmaceuticalMaterials"
    RADIOACTIVE_MATERIALS = "radioactiveMaterials"
    REFUSE = "refuse"
    TOXIC_MATERIALS = "toxicMaterials"
    VEHICLES = "vehicles"
    OTHER = "other"


class LocationDescriptorEnum(Enum):
    AROUND_ABEND_IN_ROAD = "aroundABendInRoad"
    AT_MOTORWAY_INTERCHANGE = "atMotorwayInterchange"
    AT_REST_AREA = "atRestArea"
    AT_SERVICE_AREA = "atServiceArea"
    AT_TOLL_PLAZA = "atTollPlaza"
    AT_TUNNEL_ENTRY_OR_EXIT = "atTunnelEntryOrExit"
    INBOUND = "inbound"
    IN_GALLERY = "inGallery"
    IN_THE_CENTRE = "inTheCentre"
    IN_THE_OPPOSITE_DIRECTION = "inTheOppositeDirection"
    IN_TUNNEL = "inTunnel"
    ON_BORDER = "onBorder"
    ON_BRIDGE = "onBridge"
    ON_CONNECTOR = "onConnector"
    ON_ELEVATED_SECTION = "onElevatedSection"
    ON_FLYOVER = "onFlyover"
    ON_ICE_ROAD = "onIceRoad"
    ON_LEVEL_CROSSING = "onLevelCrossing"
    ON_LINK_ROAD = "onLinkRoad"
    ON_PASS = "onPass"
    ON_ROUNDABOUT = "onRoundabout"
    ON_THE_LEFT = "onTheLeft"
    ON_THE_RIGHT = "onTheRight"
    ON_THE_ROADWAY = "onTheRoadway"
    ON_UNDERGROUND_SECTION = "onUndergroundSection"
    ON_UNDERPASS = "onUnderpass"
    OUTBOUND = "outbound"
    OVER_CREST_OF_HILL = "overCrestOfHill"
    WITHIN_JUNCTION = "withinJunction"


class MaintenanceVehicleActionsEnum(Enum):
    MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW = "maintenanceVehiclesMergingIntoTrafficFlow"
    SALT_AND_GRIT_SPREADING = "saltAndGritSpreading"
    SLOW_MOVING = "slowMoving"
    SNOW_CLEARING = "snowClearing"
    STOPPING_TO_SERVICE_EQUIPMENTS = "stoppingToServiceEquipments"


class MatrixFaultEnum(Enum):
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    INCORRECT_ASPECT_DISPLAYED = "incorrectAspectDisplayed"
    OUT_OF_SERVICE = "outOfService"
    POWER_FAILURE = "powerFailure"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"


class MeasuredOrDerivedDataTypeEnum(Enum):
    HUMIDITY_INFORMATION = "humidityInformation"
    INDIVIDUAL_VEHICLE_MEASUREMENTS = "individualVehicleMeasurements"
    POLLUTION_INFORMATION = "pollutionInformation"
    PRECIPITATION_INFORMATION = "precipitationInformation"
    PRESSURE_INFORMATION = "pressureInformation"
    RADIATION_INFORMATION = "radiationInformation"
    ROAD_SURFACE_CONDITION_INFORMATION = "roadSurfaceConditionInformation"
    TEMPERATURE_INFORMATION = "temperatureInformation"
    TRAFFIC_CONCENTRATION = "trafficConcentration"
    TRAFFIC_FLOW = "trafficFlow"
    TRAFFIC_HEADWAY = "trafficHeadway"
    TRAFFIC_SPEED = "trafficSpeed"
    TRAFFIC_STATUS_INFORMATION = "trafficStatusInformation"
    TRAVEL_TIME_INFORMATION = "travelTimeInformation"
    VISIBILITY_INFORMATION = "visibilityInformation"
    WIND_INFORMATION = "windInformation"


class MobilityEnum(Enum):
    MOBILE = "mobile"
    STATIONARY = "stationary"
    UNKNOWN = "unknown"


class MonthOfYearEnum(Enum):
    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"


@dataclass
class MultilingualStringValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1024,
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class NonWeatherRelatedRoadConditionTypeEnum(Enum):
    DIESEL_ON_ROAD = "dieselOnRoad"
    LEAVES_ON_ROAD = "leavesOnRoad"
    LOOSE_CHIPPINGS = "looseChippings"
    LOOSE_SAND_ON_ROAD = "looseSandOnRoad"
    MUD_ON_ROAD = "mudOnRoad"
    OIL_ON_ROAD = "oilOnRoad"
    PETROL_ON_ROAD = "petrolOnRoad"
    ROAD_SURFACE_IN_POOR_CONDITION = "roadSurfaceInPoorCondition"
    SLIPPERY_ROAD = "slipperyRoad"
    OTHER = "other"


class ObstructionTypeEnum(Enum):
    AIR_CRASH = "airCrash"
    CHILDREN_ON_ROADWAY = "childrenOnRoadway"
    CLEARANCE_WORK = "clearanceWork"
    CRANE_OPERATING = "craneOperating"
    CYCLISTS_ON_ROADWAY = "cyclistsOnRoadway"
    DEBRIS = "debris"
    EXPLOSION = "explosion"
    EXPLOSION_HAZARD = "explosionHazard"
    HAZARDS_ON_THE_ROAD = "hazardsOnTheRoad"
    HIGH_SPEED_CHASE = "highSpeedChase"
    HOUSE_FIRE = "houseFire"
    INCIDENT = "incident"
    INDUSTRIAL_ACCIDENT = "industrialAccident"
    OBJECT_ON_THE_ROAD = "objectOnTheRoad"
    OBJECTS_FALLING_FROM_MOVING_VEHICLE = "objectsFallingFromMovingVehicle"
    OBSTRUCTION_ON_THE_ROAD = "obstructionOnTheRoad"
    PEOPLE_ON_ROADWAY = "peopleOnRoadway"
    RAIL_CRASH = "railCrash"
    RECKLESS_DRIVER = "recklessDriver"
    RESCUE_AND_RECOVERY_WORK = "rescueAndRecoveryWork"
    SEVERE_FROST_DAMAGED_ROADWAY = "severeFrostDamagedRoadway"
    SHED_LOAD = "shedLoad"
    SNOW_AND_ICE_DEBRIS = "snowAndIceDebris"
    SPILLAGE_OCCURRING_FROM_MOVING_VEHICLE = "spillageOccurringFromMovingVehicle"
    SPILLAGE_ON_THE_ROAD = "spillageOnTheRoad"
    UNPROTECTED_ACCIDENT_AREA = "unprotectedAccidentArea"
    OTHER = "other"


class OperatingModeEnum(Enum):
    OPERATING_MODE0 = "operatingMode0"
    OPERATING_MODE1 = "operatingMode1"
    OPERATING_MODE2 = "operatingMode2"
    OPERATING_MODE3 = "operatingMode3"


class OperatorActionOriginEnum(Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"


class OperatorActionStatusEnum(Enum):
    REQUESTED = "requested"
    APPROVED = "approved"
    BEING_IMPLEMENTED = "beingImplemented"
    IMPLEMENTED = "implemented"
    REJECTED = "rejected"
    TERMINATION_REQUESTED = "terminationRequested"
    BEING_TERMINATED = "beingTerminated"


class OverallSeverityEnum(Enum):
    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE = "none"
    UNKNOWN = "unknown"


class PersonCategoryEnum(Enum):
    ADULT = "adult"
    CHILD = "child"
    EMERGENCY_SERVICES_PERSON = "emergencyServicesPerson"
    FIREMAN = "fireman"
    INFANT = "infant"
    MEDICAL_STAFF = "medicalStaff"
    MEMBER_OF_THE_PUBLIC = "memberOfThePublic"
    POLICEMAN = "policeman"
    POLITICIAN = "politician"
    PUBLIC_TRANSPORT_PASSENGER = "publicTransportPassenger"
    SICK_PERSON = "sickPerson"
    TRAFFIC_OFFICER = "trafficOfficer"
    TRAFFIC_WARDEN = "trafficWarden"
    VERY_IMPORTANT_PERSON = "veryImportantPerson"


class PlacesEnum(Enum):
    AROUND_BENDS_IN_THE_ROAD = "aroundBendsInTheRoad"
    AT_CUSTOMS_POSTS = "atCustomsPosts"
    AT_HIGH_ALTITUDES = "atHighAltitudes"
    AT_TOLL_PLAZAS = "atTollPlazas"
    IN_GALLERIES = "inGalleries"
    IN_LOW_LYING_AREAS = "inLowLyingAreas"
    IN_ROADWORKS_AREAS = "inRoadworksAreas"
    IN_SHADED_AREAS = "inShadedAreas"
    IN_THE_CITY_CENTRE = "inTheCityCentre"
    IN_THE_INNER_CITY_AREAS = "inTheInnerCityAreas"
    IN_TUNNELS = "inTunnels"
    ON_BRIDGES = "onBridges"
    ON_ELEVATED_SECTIONS = "onElevatedSections"
    ON_ENTERING_OR_LEAVING_TUNNELS = "onEnteringOrLeavingTunnels"
    ON_ENTERING_THE_COUNTRY = "onEnteringTheCountry"
    ON_FLYOVERS = "onFlyovers"
    ON_LEAVING_THE_COUNTRY = "onLeavingTheCountry"
    ON_MOTORWAYS = "onMotorways"
    ON_NON_MOTORWAYS = "onNonMotorways"
    ON_ROUNDABOUTS = "onRoundabouts"
    ON_SLIP_ROADS = "onSlipRoads"
    ON_UNDERGROUND_SECTIONS = "onUndergroundSections"
    ON_UNDERPASSES = "onUnderpasses"
    OVER_THE_CREST_OF_HILLS = "overTheCrestOfHills"
    OTHER = "other"


class PollutantTypeEnum(Enum):
    BENZENE_TOLUENE_XYLENE = "benzeneTolueneXylene"
    CARBON_MONOXIDE = "carbonMonoxide"
    LEAD = "lead"
    METHANE = "methane"
    NITRIC_OXIDE = "nitricOxide"
    NITROGEN_DIOXIDE = "nitrogenDioxide"
    NITROGEN_MONOXIDE = "nitrogenMonoxide"
    NITROGEN_OXIDES = "nitrogenOxides"
    NON_METHANE_HYDROCARBONS = "nonMethaneHydrocarbons"
    OZONE = "ozone"
    PARTICULATES10 = "particulates10"
    POLYCYCLIC_AROMATIC_HYDROCARBONS = "polycyclicAromaticHydrocarbons"
    PRIMARY_PARTICULATE = "primaryParticulate"
    SULPHUR_DIOXIDE = "sulphurDioxide"
    TOTAL_HYDROCARBONS = "totalHydrocarbons"


class PoorEnvironmentTypeEnum(Enum):
    BAD_WEATHER = "badWeather"
    BLIZZARD = "blizzard"
    BLOWING_DUST = "blowingDust"
    BLOWING_SNOW = "blowingSnow"
    CROSSWINDS = "crosswinds"
    DAMAGING_HAIL = "damagingHail"
    DENSE_FOG = "denseFog"
    ECLIPSE = "eclipse"
    EXTREME_COLD = "extremeCold"
    EXTREME_HEAT = "extremeHeat"
    FOG = "fog"
    FREEZING_FOG = "freezingFog"
    FROST = "frost"
    GALES = "gales"
    GUSTY_WINDS = "gustyWinds"
    HAIL = "hail"
    HEAVY_FROST = "heavyFrost"
    HEAVY_RAIN = "heavyRain"
    HEAVY_SNOWFALL = "heavySnowfall"
    HURRICANE_FORCE_WINDS = "hurricaneForceWinds"
    LOW_SUN_GLARE = "lowSunGlare"
    MODERATE_FOG = "moderateFog"
    OZONE_POLLUTION = "ozonePollution"
    POLLUTION = "pollution"
    PATCHY_FOG = "patchyFog"
    PRECIPITATION_IN_THE_AREA = "precipitationInTheArea"
    RAIN = "rain"
    RAIN_CHANGING_TO_SNOW = "rainChangingToSnow"
    SAND_STORMS = "sandStorms"
    SEVERE_EXHAUST_POLLUTION = "severeExhaustPollution"
    SEVERE_SMOG = "severeSmog"
    SHOWERS = "showers"
    SLEET = "sleet"
    SMOG_ALERT = "smogAlert"
    SMOKE_HAZARD = "smokeHazard"
    SNOW_CHANGING_TO_RAIN = "snowChangingToRain"
    SNOWFALL = "snowfall"
    SPRAY_HAZARD = "sprayHazard"
    STORM_FORCE_WINDS = "stormForceWinds"
    STRONG_GUSTS_OF_WIND = "strongGustsOfWind"
    STRONG_WINDS = "strongWinds"
    SWARMS_OF_INSECTS = "swarmsOfInsects"
    TEMPERATURE_FALLING = "temperatureFalling"
    THUNDERSTORMS = "thunderstorms"
    TORNADOES = "tornadoes"
    VERY_STRONG_GUSTS_OF_WIND = "veryStrongGustsOfWind"
    VISIBILITY_REDUCED = "visibilityReduced"
    WHITE_OUT = "whiteOut"
    WINTER_STORM = "winterStorm"


class PrecipitationTypeEnum(Enum):
    DRIZZLE = "drizzle"
    FREEZING_RAIN = "freezingRain"
    HAIL = "hail"
    RAIN = "rain"
    SLEET = "sleet"
    SNOW = "snow"


class ProbabilityOfOccurrenceEnum(Enum):
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"


class PublicEventTypeEnum(Enum):
    AGRICULTURAL_SHOW = "agriculturalShow"
    AIR_SHOW = "airShow"
    ATHLETICS_MEETING = "athleticsMeeting"
    COMMERCIAL_EVENT = "commercialEvent"
    CULTURAL_EVENT = "culturalEvent"
    BALL_GAME = "ballGame"
    BASEBALL_GAME = "baseballGame"
    BASKETBALL_GAME = "basketballGame"
    BICYCLE_RACE = "bicycleRace"
    BOAT_RACE = "boatRace"
    BOAT_SHOW = "boatShow"
    BOXING_TOURNAMENT = "boxingTournament"
    BULL_FIGHT = "bullFight"
    CEREMONIAL_EVENT = "ceremonialEvent"
    CONCERT = "concert"
    CRICKET_MATCH = "cricketMatch"
    EXHIBITION = "exhibition"
    FAIR = "fair"
    FESTIVAL = "festival"
    FILM_TVMAKING = "filmTVMaking"
    FOOTBALL_MATCH = "footballMatch"
    FUNFAIR = "funfair"
    GARDENING_OR_FLOWER_SHOW = "gardeningOrFlowerShow"
    GOLF_TOURNAMENT = "golfTournament"
    HOCKEY_GAME = "hockeyGame"
    HORSE_RACE_MEETING = "horseRaceMeeting"
    INTERNATIONAL_SPORTS_MEETING = "internationalSportsMeeting"
    MAJOR_EVENT = "majorEvent"
    MARATHON = "marathon"
    MARKET = "market"
    MATCH = "match"
    MOTOR_SHOW = "motorShow"
    MOTOR_SPORT_RACE_MEETING = "motorSportRaceMeeting"
    PARADE = "parade"
    PROCESSION = "procession"
    RACE_MEETING = "raceMeeting"
    RUGBY_MATCH = "rugbyMatch"
    SEVERAL_MAJOR_EVENTS = "severalMajorEvents"
    SHOW = "show"
    SHOW_JUMPING = "showJumping"
    SPORTS_MEETING = "sportsMeeting"
    STATE_OCCASION = "stateOccasion"
    TENNIS_TOURNAMENT = "tennisTournament"
    TOURNAMENT = "tournament"
    TRADE_FAIR = "tradeFair"
    WATER_SPORTS_MEETING = "waterSportsMeeting"
    WINTER_SPORTS_MEETING = "winterSportsMeeting"
    OTHER = "other"


class ReferencePointDirectionEnum(Enum):
    BOTH = "both"
    NEGATIVE = "negative"
    POSITIVE = "positive"
    UNKNOWN = "unknown"


class RelativeTrafficFlowEnum(Enum):
    TRAFFIC_VERY_MUCH_HEAVIER_THAN_NORMAL = "trafficVeryMuchHeavierThanNormal"
    TRAFFIC_HEAVIER_THAN_NORMAL = "trafficHeavierThanNormal"
    TRAFFIC_FLOW_NORMAL = "trafficFlowNormal"
    TRAFFIC_LIGHTER_THAN_NORMAL = "trafficLighterThanNormal"
    TRAFFIC_VERY_MUCH_LIGHTER_THAN_NORMAL = "trafficVeryMuchLighterThanNormal"


class RequestTypeEnum(Enum):
    CATALOGUE = "catalogue"
    FILTER = "filter"
    REQUEST_DATA = "requestData"
    REQUEST_HISTORICAL_DATA = "requestHistoricalData"
    SUBSCRIPTION = "subscription"


class ReroutingManagementTypeEnum(Enum):
    DO_NOT_FOLLOW_DIVERSION_SIGNS = "doNotFollowDiversionSigns"
    DO_NOT_USE_ENTRY = "doNotUseEntry"
    DO_NOT_USE_EXIT = "doNotUseExit"
    DO_NOT_USE_INTERSECTION_OR_JUNCTION = "doNotUseIntersectionOrJunction"
    FOLLOW_DIVERSION_SIGNS = "followDiversionSigns"
    FOLLOW_LOCAL_DIVERSION = "followLocalDiversion"
    FOLLOW_SPECIAL_MARKERS = "followSpecialMarkers"
    USE_ENTRY = "useEntry"
    USE_EXIT = "useExit"
    USE_INTERSECTION_OR_JUNCTION = "useIntersectionOrJunction"


class ResponseEnum(Enum):
    ACKNOWLEDGE = "acknowledge"
    CATALOGUE_REQUEST_DENIED = "catalogueRequestDenied"
    FILTER_REQUEST_DENIED = "filterRequestDenied"
    REQUEST_DENIED = "requestDenied"
    SUBSCRIPTION_REQUEST_DENIED = "subscriptionRequestDenied"


class RoadMaintenanceTypeEnum(Enum):
    CLEARANCE_WORK = "clearanceWork"
    CONTROLLED_AVALANCHE = "controlledAvalanche"
    INSTALLATION_WORK = "installationWork"
    GRASS_CUTTING_WORK = "grassCuttingWork"
    MAINTENANCE_WORK = "maintenanceWork"
    OVERHEAD_WORKS = "overheadWorks"
    REPAIR_WORK = "repairWork"
    RESURFACING_WORK = "resurfacingWork"
    ROAD_MARKING_WORK = "roadMarkingWork"
    ROADSIDE_WORK = "roadsideWork"
    ROADWORKS_CLEARANCE = "roadworksClearance"
    ROADWORKS = "roadworks"
    ROCK_FALL_PREVENTATIVE_MAINTENANCE = "rockFallPreventativeMaintenance"
    SALTING_IN_PROGRESS = "saltingInProgress"
    SNOWPLOUGHS_IN_USE = "snowploughsInUse"
    TREE_AND_VEGETATION_CUTTING_WORK = "treeAndVegetationCuttingWork"
    OTHER = "other"


class RoadOperatorServiceDisruptionTypeEnum(Enum):
    EMERGENCY_TELEPHONE_NUMBER_OUT_OF_SERVICE = "emergencyTelephoneNumberOutOfService"
    INFORMATION_SERVICE_TELEPHONE_NUMBER_OUT_OF_SERVICE = "informationServiceTelephoneNumberOutOfService"
    NO_TRAFFIC_OFFICER_PATROL_SERVICE = "noTrafficOfficerPatrolService"


class RoadOrCarriagewayOrLaneManagementTypeEnum(Enum):
    CAR_POOL_LANE_IN_OPERATION = "carPoolLaneInOperation"
    CARRIAGEWAY_CLOSURES = "carriagewayClosures"
    CLEAR_ALANE_FOR_EMERGENCY_VEHICLES = "clearALaneForEmergencyVehicles"
    CLEAR_ALANE_FOR_SNOWPLOUGHS_AND_GRITTING_VEHICLES = "clearALaneForSnowploughsAndGrittingVehicles"
    CLOSED_PERMANENTLY_FOR_THE_WINTER = "closedPermanentlyForTheWinter"
    CONTRAFLOW = "contraflow"
    DO_NOT_USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "doNotUseSpecifiedLanesOrCarriageways"
    HARD_SHOULDER_RUNNING_IN_OPERATION = "hardShoulderRunningInOperation"
    INTERMITTENT_SHORT_TERM_CLOSURES = "intermittentShortTermClosures"
    KEEP_TO_THE_LEFT = "keepToTheLeft"
    KEEP_TO_THE_RIGHT = "keepToTheRight"
    LANE_CLOSURES = "laneClosures"
    LANES_DEVIATED = "lanesDeviated"
    NARROW_LANES = "narrowLanes"
    NEW_ROADWORKS_LAYOUT = "newRoadworksLayout"
    OVERNIGHT_CLOSURES = "overnightClosures"
    ROAD_CLEARED = "roadCleared"
    ROAD_CLOSED = "roadClosed"
    ROLLING_ROAD_BLOCK = "rollingRoadBlock"
    RUSH_HOUR_LANE_IN_OPERATION = "rushHourLaneInOperation"
    SINGLE_ALTERNATE_LINE_TRAFFIC = "singleAlternateLineTraffic"
    TIDAL_FLOW_LANE_IN_OPERATION = "tidalFlowLaneInOperation"
    TURN_AROUND_IN_OPERATION = "turnAroundInOperation"
    USE_OF_SPECIFIED_LANES_OR_CARRIAGEWAYS_ALLOWED = "useOfSpecifiedLanesOrCarriagewaysAllowed"
    USE_SPECIFIED_LANES_OR_CARRIAGEWAYS = "useSpecifiedLanesOrCarriageways"
    VEHICLE_STORAGE_IN_OPERATION = "vehicleStorageInOperation"
    OTHER = "other"


class RoadsideAssistanceTypeEnum(Enum):
    AIR_AMBULANCE = "airAmbulance"
    BUS_PASSENGER_ASSISTANCE = "busPassengerAssistance"
    EMERGENCY_SERVICES = "emergencyServices"
    FIRST_AID = "firstAid"
    FOOD_DELIVERY = "foodDelivery"
    HELICOPTER_RESCUE = "helicopterRescue"
    VEHICLE_REPAIR = "vehicleRepair"
    VEHICLE_RECOVERY = "vehicleRecovery"
    OTHER = "other"


class RoadsideServiceDisruptionTypeEnum(Enum):
    BAR_CLOSED = "barClosed"
    DIESEL_SHORTAGE = "dieselShortage"
    FUEL_SHORTAGE = "fuelShortage"
    LPG_SHORTAGE = "lpgShortage"
    METHANE_SHORTAGE = "methaneShortage"
    NO_DIESEL_FOR_HEAVY_VEHICLES = "noDieselForHeavyVehicles"
    NO_DIESEL_FOR_LIGHT_VEHICLES = "noDieselForLightVehicles"
    NO_PUBLIC_TELEPHONES = "noPublicTelephones"
    NO_TOILET_FACILITIES = "noToiletFacilities"
    NO_VEHICLE_REPAIR_FACILITIES = "noVehicleRepairFacilities"
    PETROL_SHORTAGE = "petrolShortage"
    REST_AREA_BUSY = "restAreaBusy"
    REST_AREA_CLOSED = "restAreaClosed"
    REST_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_REST_AREA = "restAreaOvercrowdedDriveToAnotherRestArea"
    SERVICE_AREA_BUSY = "serviceAreaBusy"
    SERVICE_AREA_CLOSED = "serviceAreaClosed"
    SERVICE_AREA_FUEL_STATION_CLOSED = "serviceAreaFuelStationClosed"
    SERVICE_AREA_OVERCROWDED_DRIVE_TO_ANOTHER_SERVICE_AREA = "serviceAreaOvercrowdedDriveToAnotherServiceArea"
    SERVICE_AREA_RESTAURANT_CLOSED = "serviceAreaRestaurantClosed"
    SOME_COMMERCIAL_SERVICES_CLOSED = "someCommercialServicesClosed"
    WATER_SHORTAGE = "waterShortage"


class RoadworksDurationEnum(Enum):
    LONG_TERM = "longTerm"
    MEDIUM_TERM = "mediumTerm"
    SHORT_TERM = "shortTerm"


class RoadworksScaleEnum(Enum):
    MAJOR = "major"
    MEDIUM = "medium"
    MINOR = "minor"


class SourceTypeEnum(Enum):
    AUTOMOBILE_CLUB_PATROL = "automobileClubPatrol"
    CAMERA_OBSERVATION = "cameraObservation"
    FREIGHT_VEHICLE_OPERATOR = "freightVehicleOperator"
    INDUCTION_LOOP_MONITORING_STATION = "inductionLoopMonitoringStation"
    INFRARED_MONITORING_STATION = "infraredMonitoringStation"
    MICROWAVE_MONITORING_STATION = "microwaveMonitoringStation"
    MOBILE_TELEPHONE_CALLER = "mobileTelephoneCaller"
    NON_POLICE_EMERGENCY_SERVICE_PATROL = "nonPoliceEmergencyServicePatrol"
    OTHER_INFORMATION = "otherInformation"
    OTHER_OFFICIAL_VEHICLE = "otherOfficialVehicle"
    POLICE_PATROL = "policePatrol"
    PRIVATE_BREAKDOWN_SERVICE = "privateBreakdownService"
    PUBLIC_AND_PRIVATE_UTILITIES = "publicAndPrivateUtilities"
    REGISTERED_MOTORIST_OBSERVER = "registeredMotoristObserver"
    ROAD_AUTHORITIES = "roadAuthorities"
    ROAD_OPERATOR_PATROL = "roadOperatorPatrol"
    ROADSIDE_TELEPHONE_CALLER = "roadsideTelephoneCaller"
    SPOTTER_AIRCRAFT = "spotterAircraft"
    TRAFFIC_MONITORING_STATION = "trafficMonitoringStation"
    TRANSIT_OPERATOR = "transitOperator"
    VEHICLE_PROBE_MEASUREMENT = "vehicleProbeMeasurement"
    VIDEO_PROCESSING_MONITORING_STATION = "videoProcessingMonitoringStation"


class SpeedManagementTypeEnum(Enum):
    ACTIVE_SPEED_CONTROL_IN_OPERATION = "activeSpeedControlInOperation"
    DO_NOT_SLOWDOWN_UNNECESSARILY = "doNotSlowdownUnnecessarily"
    OBSERVE_SPEED_LIMIT = "observeSpeedLimit"
    POLICE_SPEED_CHECKS_IN_OPERATION = "policeSpeedChecksInOperation"
    REDUCE_YOUR_SPEED = "reduceYourSpeed"
    OTHER = "other"


class SubjectTypeOfWorksEnum(Enum):
    BRIDGE = "bridge"
    BURIED_CABLES = "buriedCables"
    BURIED_SERVICES = "buriedServices"
    CRASH_BARRIER = "crashBarrier"
    GALLERY = "gallery"
    GANTRY = "gantry"
    GAS_MAIN_WORK = "gasMainWork"
    INTERCHANGE = "interchange"
    JUNCTION = "junction"
    LEVEL_CROSSING = "levelCrossing"
    LIGHTING_SYSTEM = "lightingSystem"
    MEASUREMENT_EQUIPMENT = "measurementEquipment"
    NOISE_PROTECTION = "noiseProtection"
    ROAD = "road"
    ROADSIDE_DRAINS = "roadsideDrains"
    ROADSIDE_EMBANKMENT = "roadsideEmbankment"
    ROADSIDE_EQUIPMENT = "roadsideEquipment"
    ROAD_SIGNS = "roadSigns"
    ROUNDABOUT = "roundabout"
    TOLL_GATE = "tollGate"
    TUNNEL = "tunnel"
    WATER_MAIN = "waterMain"
    OTHER = "other"


class SubscriptionStateEnum(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


class TpegLoc01AreaLocationSubtypeEnum(Enum):
    LARGE_AREA = "largeArea"
    OTHER = "other"


class TpegLoc01FramedPointLocationSubtypeEnum(Enum):
    FRAMED_POINT = "framedPoint"


class TpegLoc01LinearLocationSubtypeEnum(Enum):
    SEGMENT = "segment"


class TpegLoc01SimplePointLocationSubtypeEnum(Enum):
    INTERSECTION = "intersection"
    NON_LINKED_POINT = "nonLinkedPoint"


class TpegLoc02DirectionTypeEnum(Enum):
    ALL_DIRECTIONS = "allDirections"
    ANTICLOCKWISE = "anticlockwise"
    BOTH_WAYS = "bothWays"
    CLOCKWISE = "clockwise"
    EAST_BOUND = "eastBound"
    INNER_RING = "innerRing"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    NORTH_WEST_BOUND = "northWestBound"
    OPPOSITE = "opposite"
    OUTER_RING = "outerRing"
    SOUTH_BOUND = "southBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    UNKNOWN = "unknown"
    OTHER = "other"


class TpegLoc03AreaDescriptorSubtypeEnum(Enum):
    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AREA_NAME = "areaName"
    COUNTY_NAME = "countyName"
    LAKE_NAME = "lakeName"
    NATION_NAME = "nationName"
    POLICE_FORCE_CONTROL_AREA_NAME = "policeForceControlAreaName"
    REGION_NAME = "regionName"
    SEA_NAME = "seaName"
    TOWN_NAME = "townName"
    OTHER = "other"


class TpegLoc03IlcPointDescriptorSubtypeEnum(Enum):
    TPEG_ILC_NAME1 = "tpegIlcName1"
    TPEG_ILC_NAME2 = "tpegIlcName2"
    TPEG_ILC_NAME3 = "tpegIlcName3"


class TpegLoc03JunctionPointDescriptorSubtypeEnum(Enum):
    JUNCTION_NAME = "junctionName"


class TpegLoc03OtherPointDescriptorSubtypeEnum(Enum):
    ADMINISTRATIVE_AREA_NAME = "administrativeAreaName"
    ADMINISTRATIVE_REFERENCE_NAME = "administrativeReferenceName"
    AIRPORT_NAME = "airportName"
    AREA_NAME = "areaName"
    BUILDING_NAME = "buildingName"
    BUS_STOP_IDENTIFIER = "busStopIdentifier"
    BUS_STOP_NAME = "busStopName"
    CANAL_NAME = "canalName"
    COUNTY_NAME = "countyName"
    FERRY_PORT_NAME = "ferryPortName"
    INTERSECTION_NAME = "intersectionName"
    LAKE_NAME = "lakeName"
    LINK_NAME = "linkName"
    LOCAL_LINK_NAME = "localLinkName"
    METRO_STATION_NAME = "metroStationName"
    NATION_NAME = "nationName"
    NON_LINKED_POINT_NAME = "nonLinkedPointName"
    PARKING_FACILITY_NAME = "parkingFacilityName"
    POINT_NAME = "pointName"
    POINT_OF_INTEREST_NAME = "pointOfInterestName"
    RAILWAY_STATION = "railwayStation"
    REGION_NAME = "regionName"
    RIVER_NAME = "riverName"
    SEA_NAME = "seaName"
    SERVICE_AREA_NAME = "serviceAreaName"
    TIDAL_RIVER_NAME = "tidalRiverName"
    TOWN_NAME = "townName"
    OTHER = "other"


class TpegLoc04HeightTypeEnum(Enum):
    ABOVE = "above"
    ABOVE_SEA_LEVEL = "aboveSeaLevel"
    ABOVE_STREET_LEVEL = "aboveStreetLevel"
    AT = "at"
    AT_SEA_LEVEL = "atSeaLevel"
    AT_STREET_LEVEL = "atStreetLevel"
    BELOW = "below"
    BELOW_SEA_LEVEL = "belowSeaLevel"
    BELOW_STREET_LEVEL = "belowStreetLevel"
    UNDEFINED = "undefined"
    UNKNOWN = "unknown"
    OTHER = "other"


class TrafficConstrictionTypeEnum(Enum):
    CARRIAGEWAY_BLOCKED = "carriagewayBlocked"
    CARRIAGEWAY_PARTIALLY_OBSTRUCTED = "carriagewayPartiallyObstructed"
    LANES_BLOCKED = "lanesBlocked"
    LANES_PARTIALLY_OBSTRUCTED = "lanesPartiallyObstructed"
    ROAD_BLOCKED = "roadBlocked"
    ROAD_PARTIALLY_OBSTRUCTED = "roadPartiallyObstructed"


class TrafficFlowCharacteristicsEnum(Enum):
    ERRATIC_FLOW = "erraticFlow"
    SMOOTH_FLOW = "smoothFlow"
    STOP_AND_GO = "stopAndGo"
    TRAFFIC_BLOCKED = "trafficBlocked"


class TrafficStatusEnum(Enum):
    IMPOSSIBLE = "impossible"
    CONGESTED = "congested"
    HEAVY = "heavy"
    FREE_FLOW = "freeFlow"
    UNKNOWN = "unknown"


class TrafficTrendTypeEnum(Enum):
    TRAFFIC_BUILDING_UP = "trafficBuildingUp"
    TRAFFIC_EASING = "trafficEasing"
    TRAFFIC_STABLE = "trafficStable"
    UNKNOWN = "unknown"


class TrafficTypeEnum(Enum):
    ACCESS_ONLY_TRAFFIC = "accessOnlyTraffic"
    DESTINED_FOR_AIRPORT = "destinedForAirport"
    DESTINED_FOR_AIRPORT_ARRIVALS = "destinedForAirportArrivals"
    DESTINED_FOR_AIRPORT_DEPARTURES = "destinedForAirportDepartures"
    DESTINED_FOR_FERRY_SERVICE = "destinedForFerryService"
    DESTINED_FOR_RAIL_SERVICE = "destinedForRailService"
    HOLIDAY_TRAFFIC = "holidayTraffic"
    LOCAL_TRAFFIC = "localTraffic"
    LONG_DISTANCE_TRAFFIC = "longDistanceTraffic"
    REGIONAL_TRAFFIC = "regionalTraffic"
    RESIDENTS_ONLY_TRAFFIC = "residentsOnlyTraffic"
    THROUGH_TRAFFIC = "throughTraffic"
    VISITOR_TRAFFIC = "visitorTraffic"


class TransitServiceInformationEnum(Enum):
    CANCELLATIONS = "cancellations"
    DELAY_DUE_TO_BAD_WEATHER = "delayDueToBadWeather"
    DELAY_DUE_TO_REPAIRS = "delayDueToRepairs"
    DELAYED_UNTIL_FURTHER_NOTICE = "delayedUntilFurtherNotice"
    DELAYS_DUE_TO_FLOTSAM = "delaysDueToFlotsam"
    DEPARTURE_ON_SCHEDULE = "departureOnSchedule"
    FERRY_REPLACED_BY_ICE_ROAD = "ferryReplacedByIceRoad"
    FREE_SHUTTLE_SERVICE_OPERATING = "freeShuttleServiceOperating"
    INFORMATION_SERVICE_NOT_AVAILABLE = "informationServiceNotAvailable"
    IRREGULAR_SERVICE_DELAYS = "irregularServiceDelays"
    LOAD_CAPACITY_CHANGED = "loadCapacityChanged"
    RESTRICTIONS_FOR_LONGER_VEHICLES = "restrictionsForLongerVehicles"
    SERVICE_DELAYS = "serviceDelays"
    SERVICE_DELAYS_OF_UNCERTAIN_DURATION = "serviceDelaysOfUncertainDuration"
    SERVICE_FULLY_BOOKED = "serviceFullyBooked"
    SERVICE_NOT_OPERATING = "serviceNotOperating"
    SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE = "serviceNotOperatingSubstituteServiceAvailable"
    SERVICE_SUSPENDED = "serviceSuspended"
    SERVICE_WITHDRAWN = "serviceWithdrawn"
    SHUTTLE_SERVICE_OPERATING = "shuttleServiceOperating"
    TEMPORARY_CHANGES_TO_TIMETABLES = "temporaryChangesToTimetables"
    OTHER = "other"


class TransitServiceTypeEnum(Enum):
    AIR = "air"
    BUS = "bus"
    FERRY = "ferry"
    HYDROFOIL = "hydrofoil"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND_METRO = "undergroundMetro"


class TravelTimeTrendTypeEnum(Enum):
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"


class TravelTimeTypeEnum(Enum):
    BEST = "best"
    ESTIMATED = "estimated"
    INSTANTANEOUS = "instantaneous"
    RECONSTITUTED = "reconstituted"


class UpdateMethodEnum(Enum):
    ALL_ELEMENT_UPDATE = "allElementUpdate"
    SINGLE_ELEMENT_UPDATE = "singleElementUpdate"
    SNAPSHOT = "snapshot"


class UrgencyEnum(Enum):
    EXTREMELY_URGENT = "extremelyUrgent"
    URGENT = "urgent"
    NORMAL_URGENCY = "normalUrgency"


class UrlLinkTypeEnum(Enum):
    DOCUMENT_PDF = "documentPdf"
    HTML = "html"
    IMAGE = "image"
    RSS = "rss"
    VIDEO_STREAM = "videoStream"
    VOICE_STREAM = "voiceStream"
    OTHER = "other"


class ValidityStatusEnum(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"


class VehicleEquipmentEnum(Enum):
    NOT_USING_SNOW_CHAINS = "notUsingSnowChains"
    NOT_USING_SNOW_CHAINS_OR_TYRES = "notUsingSnowChainsOrTyres"
    SNOW_CHAINS_IN_USE = "snowChainsInUse"
    SNOW_TYRES_IN_USE = "snowTyresInUse"
    SNOW_CHAINS_OR_TYRES_IN_USE = "snowChainsOrTyresInUse"
    WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD = "withoutSnowTyresOrChainsOnBoard"


class VehicleObstructionTypeEnum(Enum):
    ABANDONED_VEHICLE = "abandonedVehicle"
    ABNORMAL_LOAD = "abnormalLoad"
    BROKEN_DOWN_BUS = "brokenDownBus"
    BROKEN_DOWN_HEAVY_LORRY = "brokenDownHeavyLorry"
    BROKEN_DOWN_VEHICLE = "brokenDownVehicle"
    CONVOY = "convoy"
    DAMAGED_VEHICLE = "damagedVehicle"
    DANGEROUS_SLOW_MOVING_VEHICLE = "dangerousSlowMovingVehicle"
    EMERGENCY_VEHICLE = "emergencyVehicle"
    HIGH_SPEED_EMERGENCY_VEHICLE = "highSpeedEmergencyVehicle"
    LONG_LOAD = "longLoad"
    MILITARY_CONVOY = "militaryConvoy"
    OVERHEIGHT_VEHICLE = "overheightVehicle"
    PROHIBITED_VEHICLE_ON_THE_ROADWAY = "prohibitedVehicleOnTheRoadway"
    SALTING_OR_GRITTING_VEHICLE_IN_USE = "saltingOrGrittingVehicleInUse"
    SLOW_MOVING_MAINTENANCE_VEHICLE = "slowMovingMaintenanceVehicle"
    SLOW_VEHICLE = "slowVehicle"
    SNOWPLOUGH = "snowplough"
    TRACK_LAYING_VEHICLE = "trackLayingVehicle"
    UNLIT_VEHICLE_ON_THE_ROAD = "unlitVehicleOnTheRoad"
    VEHICLE_ON_FIRE = "vehicleOnFire"
    VEHICLE_CARRYING_HAZARDOUS_MATERIALS = "vehicleCarryingHazardousMaterials"
    VEHICLE_IN_DIFFICULTY = "vehicleInDifficulty"
    VEHICLE_ON_WRONG_CARRIAGEWAY = "vehicleOnWrongCarriageway"
    VEHICLE_STUCK = "vehicleStuck"
    VEHICLE_STUCK_UNDER_BRIDGE = "vehicleStuckUnderBridge"
    VEHICLE_WITH_OVERHEIGHT_LOAD = "vehicleWithOverheightLoad"
    VEHICLE_WITH_OVERWIDE_LOAD = "vehicleWithOverwideLoad"
    OTHER = "other"


class VehicleStatusEnum(Enum):
    ABANDONED = "abandoned"
    BROKEN_DOWN = "brokenDown"
    BURNT_OUT = "burntOut"
    DAMAGED = "damaged"
    DAMAGED_AND_IMMOBILIZED = "damagedAndImmobilized"
    ON_FIRE = "onFire"


class VehicleTypeEnum(Enum):
    ANY_VEHICLE = "anyVehicle"
    ARTICULATED_VEHICLE = "articulatedVehicle"
    BICYCLE = "bicycle"
    BUS = "bus"
    CAR = "car"
    CARAVAN = "caravan"
    CAR_OR_LIGHT_VEHICLE = "carOrLightVehicle"
    CAR_WITH_CARAVAN = "carWithCaravan"
    CAR_WITH_TRAILER = "carWithTrailer"
    FOUR_WHEEL_DRIVE = "fourWheelDrive"
    HIGH_SIDED_VEHICLE = "highSidedVehicle"
    LORRY = "lorry"
    MOPED = "moped"
    MOTORCYCLE = "motorcycle"
    MOTORCYCLE_WITH_SIDE_CAR = "motorcycleWithSideCar"
    MOTORSCOOTER = "motorscooter"
    TANKER = "tanker"
    THREE_WHEELED_VEHICLE = "threeWheeledVehicle"
    TRAILER = "trailer"
    TRAM = "tram"
    TWO_WHEELED_VEHICLE = "twoWheeledVehicle"
    VAN = "van"
    VEHICLE_WITH_CATALYTIC_CONVERTER = "vehicleWithCatalyticConverter"
    VEHICLE_WITHOUT_CATALYTIC_CONVERTER = "vehicleWithoutCatalyticConverter"
    VEHICLE_WITH_CARAVAN = "vehicleWithCaravan"
    VEHICLE_WITH_TRAILER = "vehicleWithTrailer"
    WITH_EVEN_NUMBERED_REGISTRATION_PLATES = "withEvenNumberedRegistrationPlates"
    WITH_ODD_NUMBERED_REGISTRATION_PLATES = "withOddNumberedRegistrationPlates"
    OTHER = "other"


class VehicleUsageEnum(Enum):
    AGRICULTURAL = "agricultural"
    COMMERCIAL = "commercial"
    EMERGENCY_SERVICES = "emergencyServices"
    MILITARY = "military"
    NON_COMMERCIAL = "nonCommercial"
    PATROL = "patrol"
    RECOVERY_SERVICES = "recoveryServices"
    ROAD_MAINTENANCE_OR_CONSTRUCTION = "roadMaintenanceOrConstruction"
    ROAD_OPERATOR = "roadOperator"
    TAXI = "taxi"


class VmsFaultEnum(Enum):
    COMMUNICATIONS_FAILURE = "communicationsFailure"
    INCORRECT_MESSAGE_DISPLAYED = "incorrectMessageDisplayed"
    INCORRECT_PICTOGRAM_DISPLAYED = "incorrectPictogramDisplayed"
    OUT_OF_SERVICE = "outOfService"
    POWER_FAILURE = "powerFailure"
    UNABLE_TO_CLEAR_DOWN = "unableToClearDown"
    UNKNOWN = "unknown"
    OTHER = "other"


class VmsTypeEnum(Enum):
    COLOUR_GRAPHIC = "colourGraphic"
    CONTINUOUS_SIGN = "continuousSign"
    MONOCHROME_GRAPHIC = "monochromeGraphic"
    OTHER = "other"


class WeatherRelatedRoadConditionTypeEnum(Enum):
    BLACK_ICE = "blackIce"
    DEEP_SNOW = "deepSnow"
    DRY = "dry"
    FREEZING_OF_WET_ROADS = "freezingOfWetRoads"
    FREEZING_PAVEMENTS = "freezingPavements"
    FREEZING_RAIN = "freezingRain"
    FRESH_SNOW = "freshSnow"
    ICE = "ice"
    ICE_BUILD_UP = "iceBuildUp"
    ICE_WITH_WHEEL_BAR_TRACKS = "iceWithWheelBarTracks"
    ICY_PATCHES = "icyPatches"
    LOOSE_SNOW = "looseSnow"
    NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS = "normalWinterConditionsForPedestrians"
    PACKED_SNOW = "packedSnow"
    ROAD_SURFACE_MELTING = "roadSurfaceMelting"
    SLIPPERY_ROAD = "slipperyRoad"
    SLUSH_ON_ROAD = "slushOnRoad"
    SLUSH_STRINGS = "slushStrings"
    SNOW_DRIFTS = "snowDrifts"
    SNOW_ON_PAVEMENT = "snowOnPavement"
    SNOW_ON_THE_ROAD = "snowOnTheRoad"
    SURFACE_WATER = "surfaceWater"
    WET = "wet"
    WET_AND_ICY_ROAD = "wetAndIcyRoad"
    WET_ICY_PAVEMENT = "wetIcyPavement"
    OTHER = "other"


class WeekOfMonthEnum(Enum):
    FIRST_WEEK_OF_MONTH = "firstWeekOfMonth"
    SECOND_WEEK_OF_MONTH = "secondWeekOfMonth"
    THIRD_WEEK_OF_MONTH = "thirdWeekOfMonth"
    FOURTH_WEEK_OF_MONTH = "fourthWeekOfMonth"
    FIFTH_WEEK_OF_MONTH = "fifthWeekOfMonth"


class WinterEquipmentManagementTypeEnum(Enum):
    DO_NO_USE_STUD_TYRES = "doNoUseStudTyres"
    USE_SNOW_CHAINS = "useSnowChains"
    USE_SNOW_CHAINS_OR_TYRES = "useSnowChainsOrTyres"
    USE_SNOW_TYRES = "useSnowTyres"
    WINTER_EQUIPMENT_ON_BOARD_REQUIRED = "winterEquipmentOnBoardRequired"
    OTHER = "other"


@dataclass
class AlertClinear:
    class Meta:
        name = "AlertCLinear"

    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clinear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCpoint:
    class Meta:
        name = "AlertCPoint"

    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_cpoint_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AxleSpacing:
    axle_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    axle_spacing_sequence_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleSpacingSequenceIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    axle_spacing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleSpacingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AxleWeight:
    axle_position_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axlePositionIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    maximum_permitted_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumPermittedAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    axle_weight_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "axleWeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class CatalogueReference:
    key_catalogue_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyCatalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    catalogue_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "catalogueReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Cause:
    cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "causeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class DayWeekMonth:
    applicable_day: List[DayEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 7,
        },
    )
    applicable_week: List[WeekOfMonthEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableWeek",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 5,
        },
    )
    applicable_month: List[MonthOfYearEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 12,
        },
    )
    day_week_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dayWeekMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Delays:
    delay_band: Optional[DelayBandEnum] = field(
        default=None,
        metadata={
            "name": "delayBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delays_type: Optional[DelaysTypeEnum] = field(
        default=None,
        metadata={
            "name": "delaysType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delay_time_value: Optional[float] = field(
        default=None,
        metadata={
            "name": "delayTimeValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delays_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "delaysExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Destination:
    destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "destinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class ExternalReferencing:
    external_location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    external_referencing_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    external_referencing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class FilterExitManagement:
    filter_end: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterEnd",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    filter_out_of_range: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOutOfRange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    filter_exit_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterExitManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class FilterReference:
    delete_filter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteFilter",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    filter_operation_approved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOperationApproved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    key_filter_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyFilterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    filter_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GrossWeightCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    gross_vehicle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossVehicleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    gross_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "grossWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GroupOfLocations:
    group_of_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GroupOfPeopleInvolved:
    number_of_people: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfPeople",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    injury_status: Optional[InjuryStatusTypeEnum] = field(
        default=None,
        metadata={
            "name": "injuryStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    involvement_role: Optional[InvolvementRolesEnum] = field(
        default=None,
        metadata={
            "name": "involvementRole",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    category_of_people_involved: Optional[PersonCategoryEnum] = field(
        default=None,
        metadata={
            "name": "categoryOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_people_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfPeopleInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class HeaderInformation:
    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "areaOfInterest",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    confidentiality: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    information_status: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    urgency: Optional[UrgencyEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class HeaviestAxleWeightCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    heaviest_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    heaviest_axle_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class HeightCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    vehicle_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    height_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "heightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Humidity:
    relative_humidity: Optional[float] = field(
        default=None,
        metadata={
            "name": "relativeHumidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    humidity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class InternationalIdentifier:
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    international_identifier_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class LengthCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    vehicle_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    length_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "lengthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class LifeCycleManagement:
    cancel: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    end: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    life_cycle_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "lifeCycleManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class LocationCharacteristicsOverride:
    measurement_lanes_override: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "measurementLanesOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    reversed_flow: Optional[bool] = field(
        default=None,
        metadata={
            "name": "reversedFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_characteristics_override_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverrideExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MaintenanceVehicles:
    number_of_maintenance_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfMaintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    maintenance_vehicle_actions: List[MaintenanceVehicleActionsEnum] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceVehicleActions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    maintenance_vehicles_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceVehiclesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Mobility:
    mobility_type: Optional[MobilityEnum] = field(
        default=None,
        metadata={
            "name": "mobilityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    mobility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "mobilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MultilingualString:
    values: Optional["MultilingualString.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )

    @dataclass
    class Values:
        value: List[MultilingualStringValue] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
                "min_occurs": 1,
            },
        )


@dataclass
class NumberOfAxlesCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    number_of_axles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfAxles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    number_of_axles_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "numberOfAxlesCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class OffsetDistance:
    offset_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    offset_distance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "offsetDistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PointCoordinates:
    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    point_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PollutionMeasurement:
    pollutant_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "pollutantConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    pollutant_type: Optional[PollutantTypeEnum] = field(
        default=None,
        metadata={
            "name": "pollutantType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    pollution_measurement_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionMeasurementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PrecipitationDetail:
    deposition_depth: Optional[float] = field(
        default=None,
        metadata={
            "name": "depositionDepth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "precipitationIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_type: Optional[PrecipitationTypeEnum] = field(
        default=None,
        metadata={
            "name": "precipitationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_detail_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationDetailExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class ReferenceSettings:
    predefined_location_set_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    traffic_status_default: Optional[TrafficStatusEnum] = field(
        default=None,
        metadata={
            "name": "trafficStatusDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    reference_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "referenceSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadSurfaceConditionMeasurements:
    de_icing_application_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "deIcingApplicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    de_icing_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "deIcingConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    depth_of_snow: Optional[float] = field(
        default=None,
        metadata={
            "name": "depthOfSnow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    protection_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "protectionTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_surface_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "roadSurfaceTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    water_film_thickness: Optional[float] = field(
        default=None,
        metadata={
            "name": "waterFilmThickness",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_surface_condition_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SpeedPercentile:
    vehicle_percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehiclePercentage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    speed_percentile: Optional[float] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    speed_percentile_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedPercentileExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Subjects:
    subject_type_of_works: Optional[SubjectTypeOfWorksEnum] = field(
        default=None,
        metadata={
            "name": "subjectTypeOfWorks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    number_of_subjects: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSubjects",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subjects_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subjectsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SupplementaryPositionalDescription:
    carriageway: List[CarriagewayEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    footpath: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    lane: List[LaneEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    length_affected: Optional[float] = field(
        default=None,
        metadata={
            "name": "lengthAffected",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_descriptor: List[LocationDescriptorEnum] = field(
        default_factory=list,
        metadata={
            "name": "locationDescriptor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "locationPrecision",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    sequential_ramp_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "sequentialRampNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    supplementary_positional_description_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Target:
    address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    protocol: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    target_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "targetExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Temperature:
    air_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "airTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    dew_point_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "dewPointTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    maximum_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    minimum_temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    temperature_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TimePeriodOfDay:
    time_period_of_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodOfDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegHeight:
    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    height_type: Optional[TpegLoc04HeightTypeEnum] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_height_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegHeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegPoint:
    tpeg_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegPointLocation:
    tpeg_direction: Optional[TpegLoc02DirectionTypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VehicleDetectionTime:
    arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "arrivalTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exit_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "exitTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    passage_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "passageTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    presence_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "presenceTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time_gap: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_detection_time_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleDetectionTimeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VehicleHeadway:
    distance_gap: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    distance_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VehicleSpeed:
    individual_vehicle_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "individualVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    vehicle_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Visibility:
    minimum_visibility_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumVisibilityDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    visibility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class WidthCharacteristic:
    comparison_operator: Optional[ComparisonOperatorEnum] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    vehicle_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    width_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "widthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Wind:
    maximum_wind_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumWindSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_direction_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "windDirectionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_direction_compass: Optional[DirectionCompassEnum] = field(
        default=None,
        metadata={
            "name": "windDirectionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_measurement_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "windMeasurementHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "windSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCdirection:
    class Meta:
        name = "AlertCDirection"

    alert_cdirection_coded: Optional[AlertCdirectionEnum] = field(
        default=None,
        metadata={
            "name": "alertCDirectionCoded",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cdirection_named: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCDirectionNamed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_cdirection_sense: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alertCDirectionSense",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_cdirection_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCDirectionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertClocation:
    class Meta:
        name = "AlertCLocation"

    alert_clocation_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "alertCLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_location: Optional[int] = field(
        default=None,
        metadata={
            "name": "specificLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_clocation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class BasicDataValue:
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    computational_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationalMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    fault: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    fault_reason: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "faultReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_incomplete_inputs: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIncompleteInputs",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_input_values_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfInputValuesUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    standard_deviation: Optional[float] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    supplier_calculated_data_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplierCalculatedDataQuality",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pertinent_location: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "pertinentLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    basic_data_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "basicDataValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Comment:
    comment: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    comment_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "commentDateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    comment_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "commentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GroupOfLocationsByReference(GroupOfLocations):
    predefined_location_set_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    group_of_locations_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfLocationsByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class HazardousMaterials:
    chemical_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chemicalName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    dangerous_goods_flash_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsFlashPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    dangerous_goods_regulations: Optional[DangerousGoodsRegulationsEnum] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsRegulations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazard_code_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardCodeIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    hazard_code_version_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "hazardCodeVersionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazard_substance_item_page_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardSubstanceItemPageNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    trem_card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "tremCardNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    undg_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "undgNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    volume_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "volumeOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    weight_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "weightOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazardous_materials_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "hazardousMaterialsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Impact:
    capacity_remaining: Optional[float] = field(
        default=None,
        metadata={
            "name": "capacityRemaining",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_lanes_restricted: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfLanesRestricted",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_operational_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfOperationalLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    original_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    residual_road_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "residualRoadWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_constriction_type: Optional[TrafficConstrictionTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficConstrictionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delays: Optional[Delays] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    impact_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "impactExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Location:
    external_referencing: List[ExternalReferencing] = field(
        default_factory=list,
        metadata={
            "name": "externalReferencing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_for_display: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "locationForDisplay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class ManagedCause(Cause):
    managed_cause: Optional[str] = field(
        default=None,
        metadata={
            "name": "managedCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Management:
    life_cycle_management: Optional[LifeCycleManagement] = field(
        default=None,
        metadata={
            "name": "lifeCycleManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    filter_exit_management: Optional[FilterExitManagement] = field(
        default=None,
        metadata={
            "name": "filterExitManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "managementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class NonManagedCause(Cause):
    cause_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "causeDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    cause_type: Optional[CauseTypeEnum] = field(
        default=None,
        metadata={
            "name": "causeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    non_managed_cause_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonManagedCauseExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PayloadPublication:
    feed_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "feedDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    feed_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    publication_creator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "publicationCreator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    payload_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Period:
    start_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    end_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "periodName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    recurring_time_period_of_day: List[TimePeriodOfDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringTimePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    recurring_day_week_month_period: List[DayWeekMonth] = field(
        default_factory=list,
        metadata={
            "name": "recurringDayWeekMonthPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "periodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PointByCoordinates:
    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    point_by_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadsideReferencePoint:
    roadside_reference_point_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    administrative_area: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "administrativeArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    direction_bound: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBound",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    direction_relative: Optional[ReferencePointDirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionRelative",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    distance_from_previous: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceFromPrevious",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    distance_to_next: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceToNext",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    elevated_road_section: Optional[bool] = field(
        default=None,
        metadata={
            "name": "elevatedRoadSection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Source:
    source_country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "name": "sourceCountry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    source_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    source_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    source_type: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "sourceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    reliable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    source_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "sourceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Subscription:
    delete_subscription: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteSubscription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    delivery_interval: Optional[float] = field(
        default=None,
        metadata={
            "name": "deliveryInterval",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operating_mode: Optional[OperatingModeEnum] = field(
        default=None,
        metadata={
            "name": "operatingMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    subscription_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    subscription_state: Optional[SubscriptionStateEnum] = field(
        default=None,
        metadata={
            "name": "subscriptionState",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    subscription_stop_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "subscriptionStopTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    update_method: Optional[UpdateMethodEnum] = field(
        default=None,
        metadata={
            "name": "updateMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    target: List[Target] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    filter_reference: Optional[FilterReference] = field(
        default=None,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    catalogue_reference: Optional[CatalogueReference] = field(
        default=None,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subscription_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "subscriptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TimePeriodByHour(TimePeriodOfDay):
    start_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "startTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    end_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "endTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    time_period_by_hour_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodByHourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegAreaLocation:
    tpeg_area_location_type: Optional[TpegLoc01AreaLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_height: Optional[TpegHeight] = field(
        default=None,
        metadata={
            "name": "tpegHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegDescriptor:
    descriptor: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegLinearLocation:
    tpeg_direction: Optional[TpegLoc02DirectionTypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_linear_location_type: Optional[TpegLoc01LinearLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_linear_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegSimplePoint(TpegPointLocation):
    tpeg_simple_point_location_type: Optional[TpegLoc01SimplePointLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegSimplePointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    point: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_simple_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegSimplePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class UrlLink:
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    url_link_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "urlLinkDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link_type: Optional[UrlLinkTypeEnum] = field(
        default=None,
        metadata={
            "name": "urlLinkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "urlLinkExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VehicleCharacteristics:
    fuel_type: Optional[FuelTypeEnum] = field(
        default=None,
        metadata={
            "name": "fuelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    load_type: Optional[LoadTypeEnum] = field(
        default=None,
        metadata={
            "name": "loadType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_equipment: Optional[VehicleEquipmentEnum] = field(
        default=None,
        metadata={
            "name": "vehicleEquipment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_type: List[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_usage: Optional[VehicleUsageEnum] = field(
        default=None,
        metadata={
            "name": "vehicleUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    gross_weight_characteristic: List[GrossWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "grossWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    height_characteristic: List[HeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    length_characteristic: List[LengthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "lengthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    width_characteristic: List[WidthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "widthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    heaviest_axle_weight_characteristic: List[HeaviestAxleWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heaviestAxleWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    number_of_axles_characteristic: List[NumberOfAxlesCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "numberOfAxlesCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    vehicle_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCarea:
    class Meta:
        name = "AlertCArea"

    alert_clocation_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    alert_clocation_table_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    area_location: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "areaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_carea_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertClinearByCode(AlertClinear):
    class Meta:
        name = "AlertCLinearByCode"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    location_code_for_linear_location: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "locationCodeForLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_clinear_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod2PrimaryPointLocation:
    class Meta:
        name = "AlertCMethod2PrimaryPointLocation"

    alert_clocation: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_primary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod2SecondaryPointLocation:
    class Meta:
        name = "AlertCMethod2SecondaryPointLocation"

    alert_clocation: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod4PrimaryPointLocation:
    class Meta:
        name = "AlertCMethod4PrimaryPointLocation"

    alert_clocation: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod4SecondaryPointLocation:
    class Meta:
        name = "AlertCMethod4SecondaryPointLocation"

    alert_clocation: Optional[AlertClocation] = field(
        default=None,
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    offset_distance: Optional[OffsetDistance] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Exchange:
    changed_flag: Optional[ChangedFlagEnum] = field(
        default=None,
        metadata={
            "name": "changedFlag",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    client_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    delivery_break: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deliveryBreak",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    deny_reason: Optional[DenyReasonEnum] = field(
        default=None,
        metadata={
            "name": "denyReason",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    historical_start_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "historicalStartDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    historical_stop_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "historicalStopDate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    keep_alive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "keepAlive",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    request_type: Optional[RequestTypeEnum] = field(
        default=None,
        metadata={
            "name": "requestType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    response: Optional[ResponseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subscription_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "subscriptionReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    supplier_identification: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "supplierIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    target: Optional[Target] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subscription: Optional[Subscription] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    filter_reference: List[FilterReference] = field(
        default_factory=list,
        metadata={
            "name": "filterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    catalogue_reference: List[CatalogueReference] = field(
        default_factory=list,
        metadata={
            "name": "catalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exchange_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "exchangeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GenericPublication(PayloadPublication):
    generic_publication_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericPublicationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    generic_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "genericPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GroupOfNonOrderedLocations(GroupOfLocations):
    location_contained_in_group: List[Location] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    group_of_non_ordered_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfNonOrderedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GroupOfVehiclesInvolved:
    number_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_vehicles_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfVehiclesInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Itinerary(GroupOfLocations):
    location_contained_in_itinerary: List["Itinerary.LocationContainedInItinerary"] = field(
        default_factory=list,
        metadata={
            "name": "locationContainedInItinerary",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    route_destination: List[Destination] = field(
        default_factory=list,
        metadata={
            "name": "routeDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    itinerary_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )

    @dataclass
    class LocationContainedInItinerary(Location):
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class LocationByReference(Location):
    predefined_location_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    location_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MeasuredValue:
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    location_characteristics_override: Optional[LocationCharacteristicsOverride] = field(
        default=None,
        metadata={
            "name": "locationCharacteristicsOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    basic_data_value: Optional[BasicDataValue] = field(
        default=None,
        metadata={
            "name": "basicDataValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    measured_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MeasurementSpecificCharacteristics:
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_lane: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "specificLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_measurement_value_type: Optional[MeasuredOrDerivedDataTypeEnum] = field(
        default=None,
        metadata={
            "name": "specificMeasurementValueType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    specific_vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "specificVehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_specific_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSpecificCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class NetworkLocation(Location):
    supplementary_positional_description: Optional[SupplementaryPositionalDescription] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    destination: Optional[Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class OverallPeriod:
    overall_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    overall_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallEndTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    valid_period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "validPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exception_period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "exceptionPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    overall_period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "overallPeriodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PredefinedLocation:
    predefined_location_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    predefined_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RoadsideReferencePointPrimaryLocation:
    roadside_reference_point: Optional[RoadsideReferencePoint] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_reference_point_primary_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointPrimaryLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadsideReferencePointSecondaryLocation:
    roadside_reference_point: Optional[RoadsideReferencePoint] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_reference_point_secondary_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointSecondaryLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegAreaDescriptor(TpegDescriptor):
    tpeg_area_descriptor_type: Optional[TpegLoc03AreaDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_area_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegPointDescriptor(TpegDescriptor):
    tpeg_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficStatusValue(BasicDataValue):
    traffic_status: Optional[TrafficStatusEnum] = field(
        default=None,
        metadata={
            "name": "trafficStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_status_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficStatusValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficValue(BasicDataValue):
    for_vehicles_with_characteristics_of: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TravelTimeValue(BasicDataValue):
    travel_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "travelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    travel_time_trend_type: Optional[TravelTimeTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    travel_time_type: Optional[TravelTimeTypeEnum] = field(
        default=None,
        metadata={
            "name": "travelTimeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    free_flow_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "freeFlowSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    free_flow_travel_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "freeFlowTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    normally_expected_travel_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "normallyExpectedTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_type: List[VehicleTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    travel_time_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "travelTimeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Vehicle:
    vehicle_colour: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_country_of_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleCountryOfOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleManufacturer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_registration_plate_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleRegistrationPlateIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    axle_spacing_on_vehicle: List[AxleSpacing] = field(
        default_factory=list,
        metadata={
            "name": "axleSpacingOnVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_axle_weight: List[AxleWeight] = field(
        default_factory=list,
        metadata={
            "name": "specificAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazardous_goods_associated_with_vehicle: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "hazardousGoodsAssociatedWithVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class WeatherValue(BasicDataValue):
    weather_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod2Linear(AlertClinear):
    class Meta:
        name = "AlertCMethod2Linear"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_primary_point_location: Optional[AlertCmethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_secondary_point_location: Optional[AlertCmethod2SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod2Point(AlertCpoint):
    class Meta:
        name = "AlertCMethod2Point"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_primary_point_location: Optional[AlertCmethod2PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod2_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod4Linear(AlertClinear):
    class Meta:
        name = "AlertCMethod4Linear"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location: Optional[AlertCmethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_secondary_point_location: Optional[AlertCmethod4SecondaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AlertCmethod4Point(AlertCpoint):
    class Meta:
        name = "AlertCMethod4Point"

    alert_cdirection: Optional[AlertCdirection] = field(
        default=None,
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_primary_point_location: Optional[AlertCmethod4PrimaryPointLocation] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    alert_cmethod4_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4PointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Area(Location):
    alert_carea: Optional[AlertCarea] = field(
        default=None,
        metadata={
            "name": "alertCArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_area_location: Optional[TpegAreaLocation] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class D2LogicalModel1:
    class Meta:
        name = "D2LogicalModel"

    exchange: Optional[Exchange] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    payload_publication: Optional[PayloadPublication] = field(
        default=None,
        metadata={
            "name": "payloadPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    d2_logical_model_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "d2LogicalModelExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    model_base_version: str = field(
        init=False,
        default="2.0RC1",
        metadata={
            "name": "modelBaseVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class HumidityInformation(WeatherValue):
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    humidity_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class IndividualVehicleMeasurements(TrafficValue):
    vehicle_speed: Optional[VehicleSpeed] = field(
        default=None,
        metadata={
            "name": "vehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_detection_time: Optional[VehicleDetectionTime] = field(
        default=None,
        metadata={
            "name": "vehicleDetectionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_headway: Optional[VehicleHeadway] = field(
        default=None,
        metadata={
            "name": "vehicleHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    individual_vehicle_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "individualVehicleMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MeasurementSiteRecord:
    measurement_site_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    computation_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_equipment_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementSiteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    measurement_side: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "measurementSide",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_specific_characteristics: List["MeasurementSiteRecord.MeasurementSpecificCharacteristics"] = field(
        default_factory=list,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "measurementSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    measurement_site_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass
    class MeasurementSpecificCharacteristics(MeasurementSpecificCharacteristics):
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class Point(NetworkLocation):
    tpeg_point_location: Optional[TpegPointLocation] = field(
        default=None,
        metadata={
            "name": "tpegPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_cpoint: Optional[AlertCpoint] = field(
        default=None,
        metadata={
            "name": "alertCPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point: Optional[RoadsideReferencePoint] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_by_coordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PollutionInformation(WeatherValue):
    pollution_measurement: List[PollutionMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "pollutionMeasurement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    pollution_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PrecipitationInformation(WeatherValue):
    no_precipitation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPrecipitation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    precipitation_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "precipitationInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PredefinedLocationSet:
    predefined_location_set_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location_set_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location: List[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    predefined_location_set_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RoadSurfaceConditionInformation(WeatherValue):
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    road_surface_condition_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadsideReferencePointLinear:
    roadside_reference_point_primary_location: Optional[RoadsideReferencePointPrimaryLocation] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointPrimaryLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_reference_point_secondary_location: Optional[RoadsideReferencePointSecondaryLocation] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointSecondaryLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_reference_point_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SiteMeasurements:
    measurement_site_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    measurement_time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    measured_value: List["SiteMeasurements.MeasuredValue"] = field(
        default_factory=list,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    site_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "siteMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )

    @dataclass
    class MeasuredValue(MeasuredValue):
        index: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass
class TemperatureInformation(WeatherValue):
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    temperature_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "temperatureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegGeometricArea(TpegAreaLocation):
    radius: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    centre_point: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "centrePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    name: Optional[TpegAreaDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_geometric_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegGeometricAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegIlcPointDescriptor(TpegPointDescriptor):
    tpeg_ilc_point_descriptor_type: Optional[TpegLoc03IlcPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_ilc_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegJunctionPointDescriptor(TpegPointDescriptor):
    tpeg_junction_point_descriptor_type: Optional[TpegLoc03JunctionPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_junction_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegNamedOnlyArea(TpegAreaLocation):
    name: List[TpegAreaDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    tpeg_named_only_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNamedOnlyAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegOtherPointDescriptor(TpegPointDescriptor):
    tpeg_other_point_descriptor_type: Optional[TpegLoc03OtherPointDescriptorSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_other_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficConcentration(TrafficValue):
    concentration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    occupancy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_concentration_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficConcentrationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficFlow(TrafficValue):
    axle_flow: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pcu_flow: Optional[int] = field(
        default=None,
        metadata={
            "name": "pcuFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    percentage_long_vehicles: Optional[float] = field(
        default=None,
        metadata={
            "name": "percentageLongVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_flow: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_flow_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficFlowExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficHeadway(TrafficValue):
    average_distance_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "averageDistanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    average_time_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "averageTimeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficSpeed(TrafficValue):
    average_vehicle_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "averageVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    speed_percentile: Optional[SpeedPercentile] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Validity:
    validity_status: Optional[ValidityStatusEnum] = field(
        default=None,
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    overrunning: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VisibilityInformation(WeatherValue):
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    visibility_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class WindInformation(WeatherValue):
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    wind_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AreaDestination(Destination):
    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    area_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class ElaboratedData:
    forecast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    basic_data_value: Optional[BasicDataValue] = field(
        default=None,
        metadata={
            "name": "basicDataValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    elaborated_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Linear(NetworkLocation):
    tpeg_linear_location: Optional[TpegLinearLocation] = field(
        default=None,
        metadata={
            "name": "tpegLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    alert_clinear: Optional[AlertClinear] = field(
        default=None,
        metadata={
            "name": "alertCLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadside_reference_point_linear: Optional[RoadsideReferencePointLinear] = field(
        default=None,
        metadata={
            "name": "roadsideReferencePointLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MeasuredDataPublication(PayloadPublication):
    measurement_site_table_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    site_measurements: List[SiteMeasurements] = field(
        default_factory=list,
        metadata={
            "name": "siteMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measured_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MeasurementSiteTable:
    measurement_site_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    measurement_site_table_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_record: List[MeasurementSiteRecord] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PointDestination(Destination):
    point: Optional[Point] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    point_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PredefinedLocationsPublication(PayloadPublication):
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    predefined_location_set: List[PredefinedLocationSet] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocationSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    predefined_locations_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SituationRecord:
    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationRecordVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    confidentiality_override: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "name": "confidentialityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    non_general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TpegJunction(TpegPoint):
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    name: Optional[TpegJunctionPointDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    ilc: List[TpegIlcPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    other_name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "name": "otherName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    tpeg_junction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TpegNonJunctionPoint(TpegPoint):
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    tpeg_non_junction_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNonJunctionPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class D2LogicalModel(D2LogicalModel1):
    class Meta:
        name = "d2LogicalModel"
        namespace = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class ElaboratedDataPublication(PayloadPublication):
    forecast_default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "forecastDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period_default: Optional[float] = field(
        default=None,
        metadata={
            "name": "periodDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    reference_settings: Optional[ReferenceSettings] = field(
        default=None,
        metadata={
            "name": "referenceSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    elaborated_data: List[ElaboratedData] = field(
        default_factory=list,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    elaborated_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "elaboratedDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GenericSituationRecord(SituationRecord):
    generic_situation_record_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericSituationRecordName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    generic_situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "genericSituationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MeasurementSiteTablePublication(PayloadPublication):
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    measurement_site_table: List[MeasurementSiteTable] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class NonRoadEventInformation(SituationRecord):
    non_road_event_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonRoadEventInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class OperatorAction(SituationRecord):
    action_origin: Optional[OperatorActionOriginEnum] = field(
        default=None,
        metadata={
            "name": "actionOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operator_action_status: Optional[OperatorActionStatusEnum] = field(
        default=None,
        metadata={
            "name": "operatorActionStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operator_action_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "operatorActionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Situation:
    overall_severity: Optional[OverallSeverityEnum] = field(
        default=None,
        metadata={
            "name": "overallSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    related_situation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    situation_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record: List[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    situation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TpegFramedPoint(TpegPointLocation):
    tpeg_framed_point_location_type: Optional[TpegLoc01FramedPointLocationSubtypeEnum] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    framed_point: Optional[TpegNonJunctionPoint] = field(
        default=None,
        metadata={
            "name": "framedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    to: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    from_value: Optional[TpegPoint] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    tpeg_framed_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegFramedPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficElement(SituationRecord):
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AbnormalTraffic(TrafficElement):
    abnormal_traffic_type: Optional[AbnormalTrafficTypeEnum] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_vehicles_waiting: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehiclesWaiting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    queue_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "queueLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    relative_traffic_flow: Optional[RelativeTrafficFlowEnum] = field(
        default=None,
        metadata={
            "name": "relativeTrafficFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_flow_characteristics: Optional[TrafficFlowCharacteristicsEnum] = field(
        default=None,
        metadata={
            "name": "trafficFlowCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    abnormal_traffic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Accident(TrafficElement):
    accident_cause: Optional[AccidentCauseEnum] = field(
        default=None,
        metadata={
            "name": "accidentCause",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    accident_type: List[AccidentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "accidentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    total_number_of_people_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    total_number_of_vehicles_involved: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumberOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_involved: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "vehicleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_vehicles_involved: List[GroupOfVehiclesInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfVehiclesInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    accident_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "accidentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Activity(TrafficElement):
    mobility_of_activity: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfActivity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "activityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class CarParks(NonRoadEventInformation):
    car_park_configuration: Optional[CarParkConfigurationEnum] = field(
        default=None,
        metadata={
            "name": "carParkConfiguration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    car_park_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "carParkIdentity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    car_park_occupancy: Optional[float] = field(
        default=None,
        metadata={
            "name": "carParkOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    car_park_status: Optional[CarParkStatusEnum] = field(
        default=None,
        metadata={
            "name": "carParkStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exit_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "exitRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    fill_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "fillRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_vacant_parking_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVacantParkingSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    occupied_spaces: Optional[int] = field(
        default=None,
        metadata={
            "name": "occupiedSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    queuing_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "queuingTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCapacity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    car_parks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "carParksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Conditions(TrafficElement):
    driving_condition_type: Optional[DrivingConditionTypeEnum] = field(
        default=None,
        metadata={
            "name": "drivingConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "conditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class EquipmentOrSystemFault(TrafficElement):
    equipment_or_system_fault_type: Optional[EquipmentOrSystemFaultTypeEnum] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    faulty_equipment_or_system_type: Optional[EquipmentOrSystemTypeEnum] = field(
        default=None,
        metadata={
            "name": "faultyEquipmentOrSystemType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    equipment_or_system_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class NetworkManagement(OperatorAction):
    compliance_option: Optional[ComplianceOptionEnum] = field(
        default=None,
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    applicable_for_traffic_direction: List[DirectionEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    applicable_for_traffic_type: List[TrafficTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    places_at_which_applicable: List[PlacesEnum] = field(
        default_factory=list,
        metadata={
            "name": "placesAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    automatically_initiated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "automaticallyInitiated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    for_vehicles_with_characteristics_of: List[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Obstruction(TrafficElement):
    number_of_obstructions: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfObstructions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    mobility_of_obstruction: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfObstruction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "obstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadOperatorServiceDisruption(NonRoadEventInformation):
    road_operator_service_disruption_type: List[RoadOperatorServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadOperatorServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    road_operator_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadOperatorServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadsideAssistance(OperatorAction):
    roadside_assistance_type: Optional[RoadsideAssistanceTypeEnum] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    roadside_assistance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideAssistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadsideServiceDisruption(NonRoadEventInformation):
    roadside_service_disruption_type: List[RoadsideServiceDisruptionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadsideServiceDisruptionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    roadside_service_disruption_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadsideServiceDisruptionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class Roadworks(OperatorAction):
    roadworks_duration: Optional[RoadworksDurationEnum] = field(
        default=None,
        metadata={
            "name": "roadworksDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadworks_scale: Optional[RoadworksScaleEnum] = field(
        default=None,
        metadata={
            "name": "roadworksScale",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    under_traffic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "underTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    urgent_roadworks: Optional[bool] = field(
        default=None,
        metadata={
            "name": "urgentRoadworks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    mobility: Optional[Mobility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subjects: Optional[Subjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    maintenance_vehicles: Optional[MaintenanceVehicles] = field(
        default=None,
        metadata={
            "name": "maintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadworks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadworksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SignSetting(OperatorAction):
    datex_pictogram: List[DatexPictogramEnum] = field(
        default_factory=list,
        metadata={
            "name": "datexPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
        },
    )
    pictogram_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "pictogramList",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    pictogram_list_entry: List[str] = field(
        default_factory=list,
        metadata={
            "name": "pictogramListEntry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 2,
            "max_length": 1024,
        },
    )
    reason_for_setting: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForSetting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    set_by: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "setBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    sign_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "signAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    time_last_set: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeLastSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "signSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SituationPublication(PayloadPublication):
    situation: List[Situation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficViewRecord:
    record_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "recordSequenceNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    traffic_element: Optional[TrafficElement] = field(
        default=None,
        metadata={
            "name": "trafficElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    operator_action: Optional[OperatorAction] = field(
        default=None,
        metadata={
            "name": "operatorAction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    elaborated_data: Optional[ElaboratedData] = field(
        default=None,
        metadata={
            "name": "elaboratedData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link: List[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_view_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TransitInformation(NonRoadEventInformation):
    journey_destination: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    journey_origin: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "journeyOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    journey_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "journeyReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    transit_service_information: Optional[TransitServiceInformationEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    transit_service_type: Optional[TransitServiceTypeEnum] = field(
        default=None,
        metadata={
            "name": "transitServiceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    scheduled_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "scheduledDepartureTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    transit_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "transitInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AnimalPresenceObstruction(Obstruction):
    alive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    animal_presence_type: Optional[AnimalPresenceTypeEnum] = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    animal_presence_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class AuthorityOperation(Activity):
    authority_operation_type: Optional[AuthorityOperationTypeEnum] = field(
        default=None,
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    authority_operation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "authorityOperationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class ConstructionWorks(Roadworks):
    construction_work_type: Optional[ConstructionWorkTypeEnum] = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    construction_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "constructionWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class DisturbanceActivity(Activity):
    disturbance_activity_type: Optional[DisturbanceActivityTypeEnum] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    disturbance_activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class EnvironmentalObstruction(Obstruction):
    depth: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    environmental_obstruction_type: Optional[EnvironmentalObstructionTypeEnum] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    environmental_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "environmentalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GeneralInstructionToRoadUsers(NetworkManagement):
    general_instruction_to_road_users_type: Optional[GeneralInstructionToRoadUsersTypeEnum] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    general_instruction_to_road_users_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalInstructionToRoadUsersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GeneralNetworkManagement(NetworkManagement):
    general_network_management_type: Optional[GeneralNetworkManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    traffic_manually_directed_by: Optional[PersonCategoryEnum] = field(
        default=None,
        metadata={
            "name": "trafficManuallyDirectedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    general_network_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class GeneralObstruction(Obstruction):
    obstruction_type: List[ObstructionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    general_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class InfrastructureDamageObstruction(Obstruction):
    infrastructure_damage_type: Optional[InfrastructureDamageTypeEnum] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    infrastructure_damage_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "infrastructureDamageObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class LinearTrafficView:
    linear_predefined_location_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearPredefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    traffic_view_record: List[TrafficViewRecord] = field(
        default_factory=list,
        metadata={
            "name": "trafficViewRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    linear_traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearTrafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MaintenanceWorks(Roadworks):
    road_maintenance_type: List[RoadMaintenanceTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    maintenance_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class MatrixSignSetting(SignSetting):
    aspect_displayed: Optional[str] = field(
        default=None,
        metadata={
            "name": "aspectDisplayed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    matrix_fault: List[MatrixFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "matrixFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    matrix_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "matrixIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    matrix_sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "matrixSignSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PoorEnvironmentConditions(Conditions):
    poor_environment_type: List[PoorEnvironmentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pollution_measurement: List[PollutionMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "pollutionMeasurement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    poor_environment_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class PublicEvent(Activity):
    public_event_type: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "publicEventType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    public_event_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "publicEventExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class ReroutingManagement(NetworkManagement):
    rerouting_management_type: List[ReroutingManagementTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "reroutingManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    rerouting_itinerary_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reroutingItineraryDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    signed_rerouting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "signedRerouting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    entry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    exit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    road_or_junction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadOrJunctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    alternative_route: List[Itinerary] = field(
        default_factory=list,
        metadata={
            "name": "alternativeRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    rerouting_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "reroutingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadConditions(Conditions):
    road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class RoadOrCarriagewayOrLaneManagement(NetworkManagement):
    road_or_carriageway_or_lane_management_type: Optional[RoadOrCarriagewayOrLaneManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    minimum_car_occupancy: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumCarOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specified_carriageway: List[CarriagewayEnum] = field(
        default_factory=list,
        metadata={
            "name": "specifiedCarriageway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specified_lane: List[LaneEnum] = field(
        default_factory=list,
        metadata={
            "name": "specifiedLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_or_carriageway_or_lane_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class SpeedManagement(NetworkManagement):
    speed_management_type: Optional[SpeedManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "speedManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    temporary_speed_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "temporarySpeedLimit",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    speed_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "speedManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VariableMessageSignSetting(SignSetting):
    number_of_characters: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfCharacters",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    number_of_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vms_fault: List[VmsFaultEnum] = field(
        default_factory=list,
        metadata={
            "name": "vmsFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vms_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    vms_legend: List[MultilingualString] = field(
        default_factory=list,
        metadata={
            "name": "vmsLegend",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vms_type: Optional[VmsTypeEnum] = field(
        default=None,
        metadata={
            "name": "vmsType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    variable_message_sign_setting_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "variableMessageSignSettingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class VehicleObstruction(Obstruction):
    vehicle_obstruction_type: Optional[VehicleObstructionTypeEnum] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    obstructing_vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class WinterDrivingManagement(NetworkManagement):
    winter_equipment_management_type: Optional[WinterEquipmentManagementTypeEnum] = field(
        default=None,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    winter_driving_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "winterDrivingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class NonWeatherRelatedRoadConditions(RoadConditions):
    non_weather_related_road_condition_type: List[NonWeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "nonWeatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    non_weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonWeatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficView:
    traffic_view_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "trafficViewTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    predefined_location_set_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    linear_traffic_view: List[LinearTrafficView] = field(
        default_factory=list,
        metadata={
            "name": "linearTrafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    traffic_view_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class WeatherRelatedRoadConditions(RoadConditions):
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    weather_related_road_conditions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "weatherRelatedRoadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )


@dataclass
class TrafficViewPublication(PayloadPublication):
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    traffic_view: List[TrafficView] = field(
        default_factory=list,
        metadata={
            "name": "trafficView",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    traffic_view_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficViewPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
