from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class BookingStatusEnumeration(Enum):
    """
    Values for TBookingStatus TPEG pti_table 24.
    """

    PTI24_0 = "pti24_0"
    UNKNOWN = "unknown"
    PTI17_1 = "pti17_1"
    AVAILABLE = "available"
    PTI24_2 = "pti24_2"
    LIMITED = "limited"
    PTI24_3 = "pti24_3"
    VERY_LIMITED = "veryLimited"
    PTI24_4 = "pti24_4"
    FULL = "full"
    PTI24_5 = "pti24_5"
    WAITING_LIST = "waitingList"
    PTI24_6 = "pti24_6"
    NO_BOOKING_REQUIRED = "noBookingRequired"
    PTI24_7 = "pti24_7"
    BOOKING_REQUIRED = "bookingRequired"
    PTI24_8 = "pti24_8"
    BOOKING_OPTIONAL = "bookingOptional"
    PTI24_255 = "pti24_255"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"


class InterchangeStatusEnumeration(Enum):
    """
    Values for Interchange Status TPEG cross reference pti_table 31.
    """

    PTI31_0 = "pti31_0"
    UNKNOWN = "unknown"
    PTI31_1 = "pti31_1"
    CONNECTION = "connection"
    PTI31_2 = "pti31_2"
    REPLACEMENT = "replacement"
    PTI31_3 = "pti31_3"
    ALTERNATIVE = "alternative"
    PTI31_4 = "pti31_4"
    CONNECTION_NOT_HELD = "connectionNotHeld"
    PTI31_5 = "pti31_5"
    CONNECTION_HELD = "connectionHeld"
    PTI31_6 = "pti31_6"
    STATUS_OF_CONENCTION_UNDECIDED = "statusOfConenctionUndecided"
    PTI31_255 = "pti31_255"
    UNDEFINED_CROSS_REFERENCE_INFORMATION = "undefinedCrossReferenceInformation"


class ReportTypeEnumeration(Enum):
    """
    Values for Report Type TPEG pti_table 27.
    """

    VALUE_27_0 = "27_0"
    UNKNOWN = "unknown"
    VALUE_27_1 = "27_1"
    INCIDENT = "incident"
    VALUE_27_1_ALIAS_1 = "27_1_Alias_1"
    GENERAL = "general"
    VALUE_2_27_1_ALIAS_2 = "2_27_1_Alias_2"
    OPERATOR = "operator"
    VALUE_2_27_1_ALIAS_3 = "2_27_1_Alias_3"
    NETWORK = "network"
    VALUE_27_3 = "27_3"
    ROUTE = "route"
    VALUE_27_2 = "27_2"
    STATION_TERMINAL = "stationTerminal"
    VALUE_27_2_ALIAS_1 = "27_2_Alias_1"
    STOP_POINT = "stopPoint"
    VALUE_27_2_ALIAS_2 = "27_2_Alias_2"
    CONNECTION_LINK = "connectionLink"
    VALUE_27_2_ALIAS_3 = "27_2_Alias_3"
    POINT = "point"
    VALUE_27_4 = "27_4"
    INDIVIDUAL_SERVICE = "individualService"
    VALUE_27_255 = "27_255"
    UNDEFINED = "undefined"


class RoutePointTypeEnumeration(Enum):
    """
    route_point_type TPEG pti_table15.
    """

    PTI15_0 = "pti15_0"
    UNKNOWN = "unknown"
    PTI15_1 = "pti15_1"
    START_POINT = "startPoint"
    PTI15_2 = "pti15_2"
    DESTINATION = "destination"
    PTI15_3 = "pti15_3"
    STOP = "stop"
    PTI15_4 = "pti15_4"
    VIA = "via"
    PTI15_5 = "pti15_5"
    NOT_STOPPING = "notStopping"
    PTI15_6 = "pti15_6"
    TEMPORARY_STOP = "temporaryStop"
    PTI15_7 = "pti15_7"
    TEMPORARILY_NOT_STOPPING = "temporarilyNotStopping"
    PTI15_8 = "pti15_8"
    EXCEPTIONAL_STOP = "exceptionalStop"
    PTI15_9 = "pti15_9"
    ADDITIONAL_STOP = "additionalStop"
    PTI15_10 = "pti15_10"
    REQUEST_STOP = "requestStop"
    PTI15_11 = "pti15_11"
    FRONT_TRAIN_DESTINATION = "frontTrainDestination"
    PTI15_12 = "pti15_12"
    REAR_TRAIN_DESTINATION = "rearTrainDestination"
    PTI15_13 = "pti15_13"
    THROUGH_SERVICE_DESTINATION = "throughServiceDestination"
    PTI15_14 = "pti15_14"
    NOT_VIA = "notVia"
    PTI15_15 = "pti15_15"
    ALTERED_START_POINT = "alteredStartPoint"
    PTI15_16 = "pti15_16"
    ALTERED_DESTINATION = "alteredDestination"
    PTI15_255 = "pti15_255"
    UNDEFINED_ROUTE_POINT = "undefinedRoutePoint"


class StopPointTypeEnumeration(Enum):
    """
    Values for TBookingStatus TPEG pti_table17.
    """

    PTI17_0 = "pti17_0"
    UNKNOWN = "unknown"
    PTI17_1 = "pti17_1"
    PLATFORM_NUMBER = "platformNumber"
    PTI17_2 = "pti17_2"
    TERMINAL_GATE = "terminalGate"
    PTI17_3 = "pti17_3"
    FERRY_BERTH = "ferryBerth"
    PTI17_4 = "pti17_4"
    HARBOUR_PIER = "harbourPier"
    PTI17_5 = "pti17_5"
    LANDING_STAGE = "landingStage"
    PTI17_6 = "pti17_6"
    BUS_STOP = "busStop"
    PTI17_255 = "pti17_255"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"


class TicketRestrictionEnumeration(Enum):
    """
    Values for TicketRestrictionTypeTPEG pti_table 25.
    """

    PTI25_0 = "pti25_0"
    UNKNOWN = "unknown"
    PTI25_1 = "pti25_1"
    ALL_TICKET_CLASSES_VALID = "allTicketClassesValid"
    PTI25_2 = "pti25_2"
    FULL_FARE_ONLY = "fullFareOnly"
    PTI25_3 = "pti25_3"
    CERTAIN_TICKETS_ONLY = "certainTicketsOnly"
    PTI25_4 = "pti25_4"
    TICKET_WITH_RESERVATION = "ticketWithReservation"
    PTI25_5 = "pti25_5"
    SPECIAL_FARE = "specialFare"
    PTI25_6 = "pti25_6"
    ONLY_TICKETS_OF_SPECIFIED_OPERATOR = "onlyTicketsOfSpecifiedOperator"
    PTI25_7 = "pti25_7"
    NO_RESTRICTIONS = "noRestrictions"
    PTI25_8 = "pti25_8"
    NO_OFF_PEAK_TICKETS = "noOffPeakTickets"
    PTI25_9 = "pti25_9"
    NO_WEEKEND_RETURN_TICKETS = "noWeekendReturnTickets"
    PTI25_10 = "pti25_10"
    NO_REDUCED_FARE_TICKETS = "noReducedFareTickets"
    PTI25_255 = "pti25_255"
    UNKNOWN_TICKET_RESTRICTION = "unknownTicketRestriction"


class TimetableTypeEnumeration(Enum):
    """
    Values for timetable type TPEG pti_table 33.
    """

    PTI33_0 = "pti33_0"
    UNKNOWN = "unknown"
    PTI33_1 = "pti33_1"
    WINTER = "winter"
    PTI33_2 = "pti33_2"
    SPRING = "spring"
    PTI33_3 = "pti33_3"
    SUMMER = "summer"
    PTI33_4 = "pti33_4"
    AUTUMN = "autumn"
    PTI33_5 = "pti33_5"
    SPECIAL = "special"
    PTI33_6 = "pti33_6"
    EMERGENCY = "emergency"
    PTI33_255 = "pti33_255"
    UNDEFINED_TIMETABLE_TYPE = "undefinedTimetableType"


@dataclass
class BookingStatusType:
    """Booking Status - Tpeg Report Type pti24."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: BookingStatusEnumeration = field(
        default=BookingStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class InterchangeStatusType:
    """
    Status of a SERVICE JOURNEY INTERCHANGE Status TPEG cross reference pti31.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: InterchangeStatusEnumeration = field(
        default=InterchangeStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class ReportType:
    """Scope of incident - Tpeg Report Type pti27."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ReportTypeEnumeration = field(
        default=ReportTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class RoutePointType:
    """
    Route point type Tpeg Report Type pti15.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RoutePointTypeEnumeration = field(
        default=RoutePointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class StopPointType:
    """
    STOP POINT type Tpeg Report Type pti17.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: StopPointTypeEnumeration = field(
        default=StopPointTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class TicketRestrictionType:
    """Ticket restrictions - Tpeg Report Type pti25."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TicketRestrictionEnumeration = field(
        default=TicketRestrictionEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class TimetableType:
    """Timetable type - Tpeg pti33."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TimetableTypeEnumeration = field(
        default=TimetableTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
