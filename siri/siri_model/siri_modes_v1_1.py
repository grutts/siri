from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AirSubmodesOfTransportEnumeration(Enum):
    """
    Values for Air ModesOfTransport: TPEG pti_table_08.
    """

    PTI8_0 = "pti8_0"
    LOC15_0 = "loc15_0"
    UNKNOWN = "unknown"
    PTI8_1 = "pti8_1"
    LOC15_2 = "loc15_2"
    INTERNATIONAL_FLIGHT = "internationalFlight"
    PTI8_2 = "pti8_2"
    DOMESTIC_FLIGHT = "domesticFlight"
    PTI8_3 = "pti8_3"
    LOC15_1 = "loc15_1"
    INTERCONTINENTAL_FLIGHT = "intercontinentalFlight"
    PTI8_4 = "pti8_4"
    LOC15_4 = "loc15_4"
    DOMESTIC_SCHEDULED_FLIGHT = "domesticScheduledFlight"
    PTI8_5 = "pti8_5"
    LOC15_9 = "loc15_9"
    SHUTTLE_FLIGHT = "shuttleFlight"
    PTI8_6 = "pti8_6"
    LOC15_5 = "loc15_5"
    INTERCONTINENTAL_CHARTER_FLIGHT = "intercontinentalCharterFlight"
    PTI8_7 = "pti8_7"
    LOC15_6 = "loc15_6"
    INTERNATIONAL_CHARTER_FLIGHT = "internationalCharterFlight"
    PTI8_8 = "pti8_8"
    ROUND_TRIP_CHARTER_FLIGHT = "roundTripCharterFlight"
    PTI8_9 = "pti8_9"
    LOC15_8 = "loc15_8"
    SIGHTSEEING_FLIGHT = "sightseeingFlight"
    PTI8_10 = "pti8_10"
    LOC15_10 = "loc15_10"
    HELICOPTER_SERVICE = "helicopterService"
    PTI8_11 = "pti8_11"
    LOC15_7 = "loc15_7"
    DOMESTIC_CHARTER_FLIGHT = "domesticCharterFlight"
    PTI8_12 = "pti8_12"
    SCHENGEN_AREA_FLIGHT = "SchengenAreaFlight"
    PTI8_13 = "pti8_13"
    AIRSHIP_SERVICE = "airshipService"
    PTI8_14 = "pti8_14"
    ALL_AIR_SERVICES = "allAirServices"
    LOC14_3 = "loc14_3"
    SHORT_HAUL_INTERNATIONAL_FLIGHT = "shortHaulInternationalFlight"
    PTI8_255 = "pti8_255"
    LOC15_255 = "loc15_255"
    UNDEFINED_AIRCRAFT_SERVICE = "undefinedAircraftService"


class BusSubmodesOfTransportEnumeration(Enum):
    """
    Values for Bus ModesOfTransport: TPEG pti_table_05, loc_table_10.
    """

    PTI5_0 = "pti5_0"
    LOC10_0 = "loc10_0"
    UNKNOWN = "unknown"
    PTI5_1 = "pti5_1"
    LOC10_6 = "loc10_6"
    REGIONAL_BUS = "regionalBus"
    PTI5_2 = "pti5_2"
    LOC10_1 = "loc10_1"
    EXPRESS_BUS = "expressBus"
    PTI5_3 = "pti5_3"
    BUS = "bus"
    PTI5_4 = "pti5_4"
    LOC10_5 = "loc10_5"
    LOCAL_BUS_SERVICE = "localBusService"
    PTI5_5 = "pti5_5"
    LOC10_2 = "loc10_2"
    NIGHT_BUS = "nightBus"
    PTI5_6 = "pti5_6"
    LOC10_4 = "loc10_4"
    POST_BUS = "postBus"
    PTI5_7 = "pti5_7"
    LOC10_8 = "loc10_8"
    SPECIAL_NEEDS_BUS = "specialNeedsBus"
    PTI5_8 = "pti5_8"
    MOBILITY_BUS = "mobilityBus"
    PTI5_9 = "pti5_9"
    MOBILITY_BUS_FOR_REGISTERED_DISABLED = "mobilityBusForRegisteredDisabled"
    PTI5_10 = "pti5_10"
    LOC10_9 = "loc10_9"
    SIGHTSEEING_BUS = "sightseeingBus"
    PTI5_11 = "pti5_11"
    SHUTTLE_BUS = "shuttleBus"
    PTI5_12 = "pti5_12"
    LOC10_7 = "loc10_7"
    SCHOOL_BUS = "schoolBus"
    PTI5_13 = "pti5_13"
    LOC10_13 = "loc10_13"
    SCHOOL_AND_PUBLIC_SERVICE_BUS = "schoolAndPublicServiceBus"
    PTI5_14 = "pti5_14"
    RAIL_REPLACEMENT_BUS = "railReplacementBus"
    PTI5_15 = "pti5_15"
    DEMAND_AND_RESPONSE_BUS = "demandAndResponseBus"
    PTI5_16 = "pti5_16"
    ALL_BUS_SERVICES = "allBusServices"
    LOC_10 = "loc_10"
    AIRPORT_LINK_BUS = "airportLinkBus"
    PTI5_255 = "pti5_255"
    LOC10_255 = "loc10_255"
    UNDEFINED = "undefined"


class CoachSubmodesOfTransportEnumeration(Enum):
    """
    Values for Coach ModesOfTransport: TPEG pti_table_03.
    """

    PTI3_0 = "pti3_0"
    UNKNOWN = "unknown"
    PTI3_1 = "pti3_1"
    INTERNATIONAL_COACH_SERVICE = "internationalCoachService"
    PTI3_2 = "pti3_2"
    NATIONAL_COACH_SERVICE = "nationalCoachService"
    PTI3_3 = "pti3_3"
    SHUTTLE_COACH_SERVICE = "shuttleCoachService"
    PTI3_4 = "pti3_4"
    REGIONAL_COACH_SERVICE = "regionalCoachService"
    PTI3_5 = "pti3_5"
    SPECIAL_COACH_SERVICE = "specialCoachService"
    PTI3_6 = "pti3_6"
    SIGHTSEEING_COACH_SERVICE = "sightseeingCoachService"
    PTI3_7 = "pti3_7"
    TOURIST_COACH_SERVICE = "touristCoachService"
    PTI3_8 = "pti3_8"
    COMMUTER_COACH_SERVICE = "commuterCoachService"
    PTI3_9 = "pti3_9"
    ALL_COACH_SERVICES = "allCoachServices"
    PTI3_255 = "pti3_255"
    UNDEFINED = "undefined"


class FunicularSubmodesOfTransportEnumeration(Enum):
    """
    Values for Funicular ModesOfTransport: TPEG pti_table_10.
    """

    PTI10_0 = "pti10_0"
    UNKNOWN = "unknown"
    PTI10_1 = "pti10_1"
    LOC14_2 = "loc14_2"
    FUNICULAR = "funicular"
    PTI10_2 = "pti10_2"
    ALL_FUNICULAR_SERVICES = "allFunicularServices"
    PTI10_255 = "pti10_255"
    UNDEFINED_FUNICULAR = "undefinedFunicular"


class MetroSubmodesOfTransportEnumeration(Enum):
    """
    Values for Metro ModesOfTransport: TPEG pti_table_04.
    """

    PTI4_0 = "pti4_0"
    UNKNOWN = "unknown"
    PTI4_1 = "pti4_1"
    METRO = "metro"
    PTI4_2 = "pti4_2"
    TUBE = "tube"
    PTI4_3 = "pti4_3"
    URBAN_RAILWAY = "urbanRailway"
    PTI4_4 = "pti4_4"
    ALL_RAIL_SERVICES = "allRailServices"
    PTI4_255 = "pti4_255"
    UNDEFINED = "undefined"


class RailSubmodesOfTransportEnumeration(Enum):
    """
    Values for Rail ModesOfTransport: TPEG pti_table_02, train link
    loc_table_13.
    """

    PTI2_0 = "pti2_0"
    LOC13_0 = "loc13_0"
    UNKNOWN = "unknown"
    PTI2_1 = "pti2_1"
    HIGH_SPEED_RAIL_SERVICE = "highSpeedRailService"
    PTI2_2 = "pti2_2"
    LOC13_3 = "loc13_3"
    LONG_DISTANCE_TRAIN = "longDistanceTrain"
    PTI2_3 = "pti2_3"
    LOC13_2 = "loc13_2"
    INTER_REGIONAL_RAIL_SERVICE = "interRegionalRailService"
    PTI2_4 = "pti2_4"
    CAR_TRANSPORT_RAIL_SERVICE = "carTransportRailService"
    PTI2_5 = "pti2_5"
    SLEEPER_RAIL_SERVICE = "sleeperRailService"
    PTI2_6 = "pti2_6"
    LOC13_4 = "loc13_4"
    REGIONAL_RAIL = "regionalRail"
    PTI2_7 = "pti2_7"
    LOC13_7 = "loc13_7"
    TOURIST_RAILWAY = "touristRailway"
    PTI2_8 = "pti2_8"
    RAIL_SHUTTLE = "railShuttle"
    PTI2_9 = "pti2_9"
    LOC13_5 = "loc13_5"
    SUBURBAN_RAILWAY = "suburbanRailway"
    PTI2_10 = "pti2_10"
    REPLACEMENT_RAIL_SERVICE = "replacementRailService"
    PTI2_11 = "pti2_11"
    SPECIAL_TRAIN_SERVICE = "specialTrainService"
    PTI2_12 = "pti2_12"
    LORRY_TRANSPORT_RAIL_SERVICE = "lorryTransportRailService"
    PTI2_13 = "pti2_13"
    ALL_RAIL_SERVICES = "allRailServices"
    PTI2_14 = "pti2_14"
    CROSS_COUNTRY_RAIL_SERVICE = "crossCountryRailService"
    PTI2_15 = "pti2_15"
    VEHICLE_RAIL_TRANSPORT_SERVICE = "vehicleRailTransportService"
    PTI2_16 = "pti2_16"
    LOC13_8 = "loc13_8"
    RACK_AND_PINION_RAILWAY = "rackAndPinionRailway"
    PTI2_17 = "pti2_17"
    ADDITIONAL_TRAIN_SERVICE = "additionalTrainService"
    PTI2_255 = "pti2_255"
    UNDEFINED = "undefined"
    LOC13_6 = "loc13_6"
    LOCAL = "local"
    LOC13_1 = "loc13_1"
    INTERBATIONAL = "interbational"


class SelfDriveSubmodesOfTransportEnumeration(Enum):
    """
    Values for SelfDrive ModesOfTransport: TPEG pti_table_12.
    """

    PTI12_0 = "pti12_0"
    UNKNOWN = "unknown"
    PTI12_1 = "pti12_1"
    HIRE_CAR = "hireCar"
    PTI12_2 = "pti12_2"
    HIRE_VAN = "hireVan"
    PTI12_3 = "pti12_3"
    HIRE_MOTORBIKE = "hireMotorbike"
    PTI12_4 = "pti12_4"
    HIRE_CYCLE = "hireCycle"
    PTI12_5 = "pti12_5"
    ALL_HIRE_VEHICLES = "allHireVehicles"
    PTI12_255 = "pti12_255"
    UNDEFINED_HIRE_VEHICLE = "undefinedHireVehicle"


class TaxiSubmodesOfTransportEnumeration(Enum):
    """
    Values for Taxi ModesOfTransport: TPEG pti_table_11.
    """

    PTI11_0 = "pti11_0"
    UNKNOWN = "unknown"
    PTI11_1 = "pti11_1"
    COMMUNAL_TAXI = "communalTaxi"
    PTI11_2 = "pti11_2"
    WATER_TAXI = "waterTaxi"
    PTI11_3 = "pti11_3"
    RAIL_TAXI = "railTaxi"
    PTI11_4 = "pti11_4"
    BIKE_TAXI = "bikeTaxi"
    PTI11_5 = "pti11_5"
    BLACK_CAB = "blackCab"
    PTI11_6 = "pti11_6"
    MINI_CAB = "miniCab"
    PTI11_7 = "pti11_7"
    ALL_TAXI_SERVICES = "allTaxiServices"
    PTI11_255 = "pti11_255"
    UNDEFINED_TAXI_SERVICE = "undefinedTaxiService"


class TelecabinSubmodesOfTransportEnumeration(Enum):
    """
    Values for Telecabin ModesOfTransport: TPEG pti_table_09, loc_table_14.
    """

    PTI9_0 = "pti9_0"
    LOC14_0 = "loc14_0"
    UNKNOWN = "unknown"
    PTI9_1 = "pti9_1"
    LOC14_1 = "loc14_1"
    TELECABIN = "telecabin"
    PTI9_2 = "pti9_2"
    LOC14_3 = "loc14_3"
    CABLE_CAR = "cableCar"
    PTI9_3 = "pti9_3"
    LOC14_4 = "loc14_4"
    LIFT = "lift"
    PTI9_4 = "pti9_4"
    LOC14_52 = "loc14_52"
    CHAIR_LIFT = "chairLift"
    PTI9_5 = "pti9_5"
    LOC14_6 = "loc14_6"
    DRAG_LIFT = "dragLift"
    PTI9_6 = "pti9_6"
    SMALL_TELECABIN = "smallTelecabin"
    PTI9_7 = "pti9_7"
    ALL_TELECABIN_SERVICES = "allTelecabinServices"
    PTI9_255 = "pti9_255"
    UNDEFINED = "undefined"
    LOC14_7 = "loc14_7"
    EGG_LIFT = "eggLift"
    LOC14_8 = "loc14_8"
    MINERAL_BUCKETS = "mineralBuckets"
    LOC14_255 = "loc14_255"
    TELECABIN_LINK = "telecabinLink"


class TramSubmodesOfTransportEnumeration(Enum):
    """
    Values for Tram ModesOfTransport: TPEG pti_table_06, loc_table_12.
    """

    PTI6_0 = "pti6_0"
    LOC12_0 = "loc12_0"
    UNKNOWN = "unknown"
    PTI6_1 = "pti6_1"
    LOC12_1 = "loc12_1"
    CITY_TRAM = "cityTram"
    PTI6_2 = "pti6_2"
    LOCAL_TRAM_SERVICE = "localTramService"
    PTI6_3 = "pti6_3"
    REGIONAL_TRAM = "regionalTram"
    PTI6_4 = "pti6_4"
    LOC12_2 = "loc12_2"
    SIGHTSEEING_TRAM = "sightseeingTram"
    PTI6_5 = "pti6_5"
    SHUTTLE_TRAM = "shuttleTram"
    PTI6_6 = "pti6_6"
    ALL_TRAM_SERVICES = "allTramServices"
    PTI6_255 = "pti6_255"
    LOC12_255 = "loc12_255"
    UNDEFINED_TRAM_SERVICE = "undefinedTramService"


class VehicleModesOfTransportEnumeration(Enum):
    """Values for ModesOfTransport : TPEG pti_table 01.

    :cvar PTI1_0:
    :cvar UNKNOWN:
    :cvar PTI1_1:
    :cvar RAILWAY_SERVICE: See pti2_x.
    :cvar RAIL:
    :cvar PTI1_2:
    :cvar COACH_SERVICE: See pti3_x.
    :cvar COACH:
    :cvar PTI1_3:
    :cvar SUBURBAN_RAILWAY_SERVICE:
    :cvar SUBURBAN_RAIL:
    :cvar PTI1_4:
    :cvar URBAN_RAILWAY_SERVICE: See pti4_x.
    :cvar URBAN_RAIL:
    :cvar PTI1_5:
    :cvar METRO_SERVICE:
    :cvar METRO:
    :cvar PTI1_6:
    :cvar UNDERGROUND_SERVICE:
    :cvar UNDERGROUND:
    :cvar PTI1_7:
    :cvar BUS_SERVICE: See pti5_x.
    :cvar BUS:
    :cvar PTI1_8:
    :cvar TROLLEY_BUS_SERVICE:
    :cvar TROLLEY_BUS:
    :cvar PTI1_9:
    :cvar TRAM_SERVICE: See pti6_x.
    :cvar TRAM:
    :cvar PTI1_10:
    :cvar WATER_TRANSPORT_SERVICE: See pti7_x.
    :cvar WATER_TRANSPORT:
    :cvar PTI1_11:
    :cvar AIR_SERVICE: See pti8_x.
    :cvar AIR:
    :cvar PTI1_12:
    :cvar FERRY_SERVICE:
    :cvar WATER:
    :cvar PTI1_13:
    :cvar TELECABIN_SERVICE: See pti9_x.
    :cvar TELECABIN:
    :cvar PTI1_14:
    :cvar FUNICULAR_SERVICE: See pti10_x.
    :cvar FUNICULAR:
    :cvar PTI1_15:
    :cvar TAXI_SERVICE: pti11_x.
    :cvar TAXI:
    :cvar PTI1_16:
    :cvar SELF_DRIVE: See pti12_x.
    :cvar PTI1_17:
    :cvar ALL_SERVICES:
    :cvar ALL:
    :cvar PTI1_18:
    :cvar ALL_SERVICES_EXCEPT:
    """

    PTI1_0 = "pti1_0"
    UNKNOWN = "unknown"
    PTI1_1 = "pti1_1"
    RAILWAY_SERVICE = "railwayService"
    RAIL = "rail"
    PTI1_2 = "pti1_2"
    COACH_SERVICE = "coachService"
    COACH = "coach"
    PTI1_3 = "pti1_3"
    SUBURBAN_RAILWAY_SERVICE = "suburbanRailwayService"
    SUBURBAN_RAIL = "suburbanRail"
    PTI1_4 = "pti1_4"
    URBAN_RAILWAY_SERVICE = "urbanRailwayService"
    URBAN_RAIL = "urbanRail"
    PTI1_5 = "pti1_5"
    METRO_SERVICE = "metroService"
    METRO = "metro"
    PTI1_6 = "pti1_6"
    UNDERGROUND_SERVICE = "undergroundService"
    UNDERGROUND = "underground"
    PTI1_7 = "pti1_7"
    BUS_SERVICE = "busService"
    BUS = "bus"
    PTI1_8 = "pti1_8"
    TROLLEY_BUS_SERVICE = "trolleyBusService"
    TROLLEY_BUS = "trolleyBus"
    PTI1_9 = "pti1_9"
    TRAM_SERVICE = "tramService"
    TRAM = "tram"
    PTI1_10 = "pti1_10"
    WATER_TRANSPORT_SERVICE = "waterTransportService"
    WATER_TRANSPORT = "waterTransport"
    PTI1_11 = "pti1_11"
    AIR_SERVICE = "airService"
    AIR = "air"
    PTI1_12 = "pti1_12"
    FERRY_SERVICE = "ferryService"
    WATER = "water"
    PTI1_13 = "pti1_13"
    TELECABIN_SERVICE = "telecabinService"
    TELECABIN = "telecabin"
    PTI1_14 = "pti1_14"
    FUNICULAR_SERVICE = "funicularService"
    FUNICULAR = "funicular"
    PTI1_15 = "pti1_15"
    TAXI_SERVICE = "taxiService"
    TAXI = "taxi"
    PTI1_16 = "pti1_16"
    SELF_DRIVE = "selfDrive"
    PTI1_17 = "pti1_17"
    ALL_SERVICES = "allServices"
    ALL = "all"
    PTI1_18 = "pti1_18"
    ALL_SERVICES_EXCEPT = "allServicesExcept"


class WaterSubmodesOfTransportEnumeration(Enum):
    """
    Values for Water ModesOfTransport: TPEG pti_table_07.
    """

    PTI7_0 = "pti7_0"
    UNKNOWN = "unknown"
    PTI7_1 = "pti7_1"
    INTERNATIONAL_CAR_FERRY_SERVICE = "internationalCarFerryService"
    PTI7_2 = "pti7_2"
    NATIONAL_CAR_FERRY_SERVICE = "nationalCarFerryService"
    PTI7_3 = "pti7_3"
    REGIONAL_CAR_FERRY_SERVICE = "regionalCarFerryService"
    PTI7_4 = "pti7_4"
    LOCAL_CAR_FERRY_SERVICE = "localCarFerryService"
    PTI7_5 = "pti7_5"
    INTERNATIONAL_PASSENGER_FERRY = "internationalPassengerFerry"
    PTI7_6 = "pti7_6"
    NATIONAL_PASSENGER_FERRY = "nationalPassengerFerry"
    PTI7_7 = "pti7_7"
    REGIONAL_PASSENGER_FERRY = "regionalPassengerFerry"
    PTI7_8 = "pti7_8"
    LOCAL_PASSENGER_FERRY = "localPassengerFerry"
    PTI7_9 = "pti7_9"
    POST_BOAT = "postBoat"
    PTI7_10 = "pti7_10"
    TRAIN_FERRY = "trainFerry"
    PTI7_11 = "pti7_11"
    ROAD_FERRY_LINK = "roadFerryLink"
    PTI7_12 = "pti7_12"
    AIRPORT_BOAT_LINK = "airportBoatLink"
    PTI7_13 = "pti7_13"
    HIGH_SPEED_VEHICLE_SERVICE = "highSpeedVehicleService"
    PTI7_14 = "pti7_14"
    HIGH_SPEED_PASSENGER_SERVICE = "highSpeedPassengerService"
    PTI7_15 = "pti7_15"
    SIGHTSEEING_SERVICE = "sightseeingService"
    PTI7_16 = "pti7_16"
    SCHOOL_BOAT = "schoolBoat"
    PTI7_17 = "pti7_17"
    CABLE_FERRY = "cableFerry"
    PTI7_18 = "pti7_18"
    RIVER_BUS = "riverBus"
    PTI7_19 = "pti7_19"
    SCHEDULED_FERRY = "scheduledFerry"
    PTI7_20 = "pti7_20"
    SHUTTLE_FERRY_SERVICE = "shuttleFerryService"
    PTI7_21 = "pti7_21"
    ALL_WATER_TRANSPORT_SERVICES = "allWaterTransportServices"
    PTI7_255 = "pti7_255"
    UNDEFINED_WATER_TRANSPORT = "undefinedWaterTransport"


@dataclass
class AirSubmode:
    """
    TPEG pti08 Air submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AirSubmodesOfTransportEnumeration = field(
        default=AirSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class BusSubmode:
    """
    TPEG pti05 Bus submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: BusSubmodesOfTransportEnumeration = field(
        default=BusSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class CoachSubmode:
    """
    TPEG pti03 Coach submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: CoachSubmodesOfTransportEnumeration = field(
        default=CoachSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class FunicularSubmode:
    """
    TPEG pti10 Funicular submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FunicularSubmodesOfTransportEnumeration = field(
        default=FunicularSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class MetroSubmode:
    """
    TPEG pti04 Metro submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MetroSubmodesOfTransportEnumeration = field(
        default=MetroSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class RailSubmode:
    """
    TPEG pti02 Rail submodes loc13.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RailSubmodesOfTransportEnumeration = field(
        default=RailSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class SelfDriveSubmode:
    """
    TPEG pti12 SelfDrive submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SelfDriveSubmodesOfTransportEnumeration = field(
        default=SelfDriveSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class TaxiSubmode:
    """
    TPEG pti11 Taxi submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TaxiSubmodesOfTransportEnumeration = field(
        default=TaxiSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class TelecabinSubmode:
    """
    TPEG pti09 Telecabin submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TelecabinSubmodesOfTransportEnumeration = field(
        default=TelecabinSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class TramSubmode:
    """
    TPEG pti06 Tram submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TramSubmodesOfTransportEnumeration = field(
        default=TramSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class VehicleMode:
    """
    Vehicle mode- Tpeg ModeType pti1.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: VehicleModesOfTransportEnumeration = field(
        default=VehicleModesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class WaterSubmode:
    """
    TPEG pti07 Water submodes.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: WaterSubmodesOfTransportEnumeration = field(
        default=WaterSubmodesOfTransportEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
