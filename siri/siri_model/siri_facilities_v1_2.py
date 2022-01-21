from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AccessFacilityEnumeration(Enum):
    """
    Values for Access Facility.
    """

    UNKNOWN = "unknown"
    LIFT = "lift"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    STAIRS = "stairs"
    SHUTTLE = "shuttle"
    NARROW_ENTRANCE = "narrowEntrance"
    BARRIER = "barrier"
    PALLET_ACCESS_LOW_FLOOR = "palletAccess_lowFloor"
    VALIDATOR = "validator"


class AccommodationFacilityEnumeration(Enum):
    """
    Values for Accomodation Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    PTI23_3 = "pti23_3"
    SLEEPER = "sleeper"
    PTI23_4 = "pti23_4"
    COUCHETTE = "couchette"
    PTI23_5 = "pti23_5"
    SPECIAL_SEATING = "specialSeating"
    PTI23_11 = "pti23_11"
    FREE_SEATING = "freeSeating"
    PTI23_12 = "pti23_12"
    RECLINING_SEATS = "recliningSeats"
    PTI23_13 = "pti23_13"
    BABY_COMPARTMENT = "babyCompartment"
    FAMILY_CARRIAGE = "familyCarriage"


class AssistanceFacilityEnumeration(Enum):
    """
    Values for Assistance Facility.
    """

    UNKNOWN = "unknown"
    POLICE = "police"
    FIRST_AID = "firstAid"
    SOS_POINT = "sosPoint"
    SPECIFIC_ASSISTANCE = "specificAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    BOARDING_ASSISTANCE = "boardingAssistance"


class FareClassFacilityEnumeration(Enum):
    """
    Values for FareClass Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    PTI23_0 = "pti23_0"
    PTI23_6 = "pti23_6"
    FIRST_CLASS = "firstClass"
    PTI23_7 = "pti23_7"
    SECOND_CLASS = "secondClass"
    PTI23_8 = "pti23_8"
    THIRD_CLASS = "thirdClass"
    PTI23_9 = "pti23_9"
    ECONOMY_CLASS = "economyClass"
    PTI23_10 = "pti23_10"
    BUSINESS_CLASS = "businessClass"


class HireFacilityEnumeration(Enum):
    """
    Values for Hire Facility.
    """

    UNKNOWN = "unknown"
    CAR_HIRE = "carHire"
    MOTOR_CYCLE_HIRE = "motorCycleHire"
    CYCLE_HIRE = "cycleHire"
    TAXI = "taxi"
    RECREATION_DEVICE_HIRE = "recreationDeviceHire"


class LuggageFacilityEnumeration(Enum):
    """
    Values for Luggage Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    PTI23_17 = "pti23_17"
    BIKE_CARRIAGE = "bikeCarriage"
    BAGGAGE_STORAGE = "baggageStorage"
    LEFT_LUGGAGE = "leftLuggage"
    PORTERAGE = "porterage"
    BAGGAGE_TROLLEYS = "baggageTrolleys"


class MobilityFacilityEnumeration(Enum):
    """
    Values for Mobility Facility: TPEG pti_table 23.
    """

    PTI23_255_4 = "pti23_255_4"
    UNKNOWN = "unknown"
    PTI23_16 = "pti23_16"
    SUITABLE_FOR_WHEEL_CHAIRS = "suitableForWheelChairs"
    PTI23_16_1 = "pti23_16_1"
    LOW_FLOOR = "lowFloor"
    PTI23_16_2 = "pti23_16_2"
    BOARDING_ASSISTANCE = "boardingAssistance"
    PTI23_16_3 = "pti23_16_3"
    STEP_FREE_ACCESS = "stepFreeAccess"
    TACTILE_PATFORM_EDGES = "tactilePatformEdges"
    ONBOARD_ASSISTANCE = "onboardAssistance"
    UNACCOMPANIED_MINOR_ASSISTANCE = "unaccompaniedMinorAssistance"
    AUDIO_INFORMATION = "audioInformation"
    VISUAL_INFORMATION = "visualInformation"
    DISPLAYS_FOR_VISUALLY_IMPAIRED = "displaysForVisuallyImpaired"
    AUDIO_FOR_HEARING_IMPAIRED = "audioForHearingImpaired"


class NuisanceFacilityEnumeration(Enum):
    """
    Values for Nuisance Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    SMOKING = "smoking"
    NO_SMOKING = "noSmoking"
    MOBILE_PHONE_USE_ZONE = "mobilePhoneUseZone"
    MOBILE_PHONE_FREE_ZONE = "mobilePhoneFreeZone"


class ParkingFacilityEnumeration(Enum):
    """
    Values for Access Facility.
    """

    UNKNOWN = "unknown"
    CAR_PARK = "carPark"
    PARK_AND_RIDE_PARK = "parkAndRidePark"
    MOTORCYCLE_PARK = "motorcyclePark"
    CYCLE_PARK = "cyclePark"
    RENTAL_CAR_PARK = "rentalCarPark"
    COACH_PARK = "coachPark"


class PassengerCommsFacilityEnumeration(Enum):
    """
    Values for PassengerComms Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    FACCOMMS_1 = "faccomms_1"
    PASSENGER_WIFI = "passengerWifi"
    PTI23_21 = "pti23_21"
    TELEPHONE = "telephone"
    PTI23_14 = "pti23_14"
    AUDIO_SERVICES = "audioServices"
    PTI23_15 = "pti23_15"
    VIDEO_SERVICES = "videoServices"
    PTI23_25 = "pti23_25"
    BUSINESS_SERVICES = "businessServices"
    INTERNET = "internet"
    POSTOFFICE = "postoffice"
    LETTERBOX = "letterbox"


class PassengerInformationFacilityEnumeration(Enum):
    """
    Values for Passenger Information Facility.
    """

    UNKNOWN = "unknown"
    NEXT_STOP_INDICATOR = "nextStopIndicator"
    STOP_ANNOUNCEMENTS = "stopAnnouncements"
    PASSENGER_INFORMATION_DISPLAY = "passengerInformationDisplay"
    AUDIO_INFORMATION = "audioInformation"
    VISUAL_INFORMATION = "visualInformation"
    TACTILE_PLATFORM_EDGES = "tactilePlatformEdges"
    TACTILE_INFORMATION = "tactileInformation"
    WALKING_GUIDANCE = "walkingGuidance"
    JOURNEY_PLANNING = "journeyPlanning"
    LOST_FOUND = "lostFound"
    INFORMATION_DESK = "informationDesk"
    INTERACTIVE_KIOSK_DISPLAY = "interactiveKiosk-Display"
    PRINTED_PUBLIC_NOTICE = "printedPublicNotice"


class RefreshmentFacilityEnumeration(Enum):
    """
    Values for Refreshment Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    PTI23_1 = "pti23_1"
    RESTAURANT_SERVICE = "restaurantService"
    PTI23_2 = "pti23_2"
    SNACKS_SERVICE = "snacksService"
    PTI23 = "pti23"
    TROLLEY = "trolley"
    PTI23_18 = "pti23_18"
    BAR = "bar"
    PTI23_19 = "pti23_19"
    FOOD_NOT_AVAILABLE = "foodNotAvailable"
    PTI23_20 = "pti23_20"
    BEVERAGES_NOT_AVAILABLE = "beveragesNotAvailable"
    PTI23_26 = "pti23_26"
    BISTRO = "bistro"
    FOOD_VENDING_MACHINE = "foodVendingMachine"
    BEVERAGE_VENDING_MACHINE = "beverageVendingMachine"


class ReservedSpaceFacilityEnumeration(Enum):
    """
    Values for Reserved Space Facility.
    """

    UNKNOWN = "unknown"
    LOUNGE = "lounge"
    HALL = "hall"
    MEETINGPOINT = "meetingpoint"
    GROUP_POINT = "groupPoint"
    RECEPTION = "reception"
    SHELTER = "shelter"
    SEATS = "seats"


class RetailFacilityEnumeration(Enum):
    """
    Values for Retail Facility.
    """

    UNKNOWN = "unknown"
    FOOD = "food"
    NEWSPAPER_TOBACCO = "newspaperTobacco"
    RECREATION_TRAVEL = "recreationTravel"
    HYGIENE_HEALTH_BEAUTY = "hygieneHealthBeauty"
    FASHION_ACCESSORIES = "fashionAccessories"
    BANK_FINANCE_INSURANCE = "bankFinanceInsurance"
    CASH_MACHINE = "cashMachine"
    CURRENCY_EXCHANGE = "currencyExchange"
    TOURISM_SERVICE = "tourismService"
    PHOTO_BOOTH = "photoBooth"


class SanitaryFacilityEnumeration(Enum):
    """
    Values for Sanitary Facility: TPEG pti_table 23.
    """

    UNKNOWN = "unknown"
    PTI23_22 = "pti23_22"
    TOILET = "toilet"
    PTI23_23 = "pti23_23"
    NO_TOILET = "noToilet"
    SHOWER = "shower"
    WHEELCHAIR_ACCCESS_TOILET = "wheelchairAcccessToilet"
    BABY_CHANGE = "babyChange"


class TicketingFacilityEnumeration(Enum):
    """
    Values for Ticketing Facility.
    """

    UNKNOWN = "unknown"
    TICKET_MACHINES = "ticketMachines"
    TICKET_OFFICE = "ticketOffice"
    TICKET_ON_DEMAND_MACHINES = "ticketOnDemandMachines"
    TICKET_SALES = "ticketSales"
    MOBILE_TICKETING = "mobileTicketing"
    TICKET_COLLECTION = "ticketCollection"
    CENTRAL_RESERVATIONS = "centralReservations"
    LOCAL_TICKETS = "localTickets"
    NATIONAL_TICKETS = "nationalTickets"
    INTERNATIONAL_TICKETS = "internationalTickets"


@dataclass
class AccessFacility:
    """
    Classification of Access Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AccessFacilityEnumeration = field(
        default=AccessFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class AccommodationFacility:
    """Classification of Accomodation Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AccommodationFacilityEnumeration = field(
        default=AccommodationFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class AllFacilitiesFeatureStructure:
    """
    Description of the features of any of the available facilities.
    """

    access_facility: Optional[AccessFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accommodation_facility: Optional[AccommodationFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    assistance_facility: Optional[AssistanceFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    fare_class_facility: Optional[FareClassFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClassFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    hire_facility: Optional[HireFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "HireFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    luggage_facility: Optional[LuggageFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "LuggageFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mobility_facility: Optional[MobilityFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    nuisance_facility: Optional[NuisanceFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "NuisanceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    parking_facility: Optional[ParkingFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ParkingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_comms_facility: Optional[PassengerCommsFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerCommsFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passenger_information_facility: Optional[PassengerInformationFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    refreshment_facility: Optional[RefreshmentFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "RefreshmentFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reserved_space_facility: Optional[ReservedSpaceFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ReservedSpaceFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    retail_facility: Optional[RetailFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "RetailFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sanitary_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "SanitaryFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ticketing_facility: Optional[TicketingFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "TicketingFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AssistanceFacility:
    """
    Classification of Assistance Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AssistanceFacilityEnumeration = field(
        default=AssistanceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class FareClassFacility:
    """Classification of FareClass Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FareClassFacilityEnumeration = field(
        default=FareClassFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class HireFacility:
    """
    Classification of Hire Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: HireFacilityEnumeration = field(
        default=HireFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class LuggageFacility:
    """Classification of Luggage Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: LuggageFacilityEnumeration = field(
        default=LuggageFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class MobilityFacility:
    """Classification of Mobility Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: MobilityFacilityEnumeration = field(
        default=MobilityFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class NuisanceFacility:
    """Classification of Nuisance Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: NuisanceFacilityEnumeration = field(
        default=NuisanceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class ParkingFacility:
    """
    Classification of Access Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[ParkingFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class PassengerCommsFacility:
    """Classification of PassengerComms Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PassengerCommsFacilityEnumeration = field(
        default=PassengerCommsFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class PassengerInformationFacility:
    """Classification of PassengerInfo Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PassengerInformationFacilityEnumeration = field(
        default=PassengerInformationFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class RefreshmentFacility:
    """Classification of Refreshment Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RefreshmentFacilityEnumeration = field(
        default=RefreshmentFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class ReservedSpaceFacility:
    """
    Classification of Reserved Space Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class RetailFacility:
    """
    Classification of Retail Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class SanitaryFacility:
    """Classification of Sanitary Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SanitaryFacilityEnumeration = field(
        default=SanitaryFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class TicketingFacility:
    """Classification of Ticketing Facility type - Tpeg pti23."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
