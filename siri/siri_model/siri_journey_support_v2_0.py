from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ArrivalBoardingActivityEnumeration(Enum):
    """
    Allowed types activity for Alighting.
    """

    ALIGHTING = "alighting"
    NO_ALIGHTING = "noAlighting"
    PASS_THRU = "passThru"


class CallStatusEnumeration(Enum):
    """Classification of the timeliness of the CALL, according to a fixed list
    of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are still classified as on-time.
    Applications may use this to guide their own presentation of times.

    :cvar ON_TIME: Service is on time.
    :cvar EARLY: Service is earlier than expected.
    :cvar DELAYED: Service is delayed.
    :cvar CANCELLED: Service is cancelled.
    :cvar ARRIVED: Service has arrived.
    :cvar DEPARTED:
    :cvar MISSED:
    :cvar NO_REPORT: There is no information about the service.
    :cvar NOT_EXPECTED: Service is not expected to call this stop. For
        instance a flexible service that has not yet been preordered.
    """

    ON_TIME = "onTime"
    EARLY = "early"
    DELAYED = "delayed"
    CANCELLED = "cancelled"
    ARRIVED = "arrived"
    DEPARTED = "departed"
    MISSED = "missed"
    NO_REPORT = "noReport"
    NOT_EXPECTED = "notExpected"


@dataclass
class DatedVehicleJourneyRef:
    """
    Reference to a DATED VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class DepartureBoardingActivityEnumeration(Enum):
    """
    Allowed types activity for Boarding.
    """

    BOARDING = "boarding"
    NO_BOARDING = "noBoarding"
    PASS_THRU = "passThru"


@dataclass
class DestinationRef:
    """
    Reference to the destination SCHEDULED STOP POINT of the journey.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class FirstOrLastJourneyEnumeration(Enum):
    """
    Allowed types activity for FirstOrLastJourney.
    """

    FIRST_SERVICE_OF_DAY = "firstServiceOfDay"
    OTHER_SERVICE = "otherService"
    LAST_SERVICE_OF_DAY = "lastServiceOfDay"
    UNSPECIFIED = "unspecified"


@dataclass
class FramedVehicleJourneyRefStructure:
    """
    Type for identifer of a VEHICLE JOURNEY within data Horizon of a service.

    :ivar data_frame_ref: identifier of data frame within particpant
        service. Used to ensure that the Reference to a DATED VEGICLE
        JOURNEY is unique with the data horizon of the service. Often
        the OperationalDayType is used for this purpose.
    :ivar dated_vehicle_journey_ref: A reference to the dated VEHICLE
        JOURNEY that the VEHICLE is making.
    """

    data_frame_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    dated_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class InterchangeRef:
    """
    Reference to a SERVCIE JOURNEY  INTERCHANGE.
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
class OriginRef:
    """
    Reference to the origin SCHEDULED STOP POINT of the journey.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class ProgressRateEnumeration(Enum):
    """
    Classification of the rate of progress of VEHICLE according a fixed list of
    values.

    :cvar NO_PROGRESS: Vehicle is stationary.
    :cvar SLOW_PROGRESS: Vehicle is proceeding slower than normal.
    :cvar NORMAL_PROGRESS: Vehicle is proceeding at a normal rate.
    :cvar FAST_PROGRESS: Vehicle is proceeding faster than normal.
    :cvar UNKNOWN: There is no data.
    """

    NO_PROGRESS = "noProgress"
    SLOW_PROGRESS = "slowProgress"
    NORMAL_PROGRESS = "normalProgress"
    FAST_PROGRESS = "fastProgress"
    UNKNOWN = "unknown"


class QualityIndexEnumeration(Enum):
    """Classification of the quality of the prediction of the CALL, according
    to a fixed list of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are stiull classified as on-time.
    Applications may use this to guide their own presentation of times.

    :cvar CERTAIN: Data is certain (1/5).
    :cvar VERY_RELIABLE: Data has confidence level of very reliable
        (2/5).
    :cvar RELIABLE: Data has confidence lvel of reliabel (3/5).
    :cvar PROBABLY_RELIABLE: Data is thought to be reliable (4/5)
    :cvar UNCONFIRMED: Data is unconfirmed (5/5).
    """

    CERTAIN = "certain"
    VERY_RELIABLE = "veryReliable"
    RELIABLE = "reliable"
    PROBABLY_RELIABLE = "probablyReliable"
    UNCONFIRMED = "unconfirmed"


@dataclass
class VehicleJourneyRef:
    """
    Reference to a VEHICLE JOURNEY.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class VehicleStatusEnumeration(Enum):
    """Classification of the State of the VEHICLE JORUNEY according to a fixed
    list of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are still classified as on-time.
    Applications may use this to guide their own presentation of times.

    :cvar EXPECTED: Service is expected to be performed.
    :cvar NOT_EXPECTED: Service is not expected to be run. For instance
        a flexible service that has not yet been preordered.
    :cvar CANCELLED:
    :cvar ASSIGNED:
    :cvar SIGNED_ON:
    :cvar AT_ORIGIN:
    :cvar IN_PROGRESS: Service has departed from first stop.
    :cvar ABORTED:
    :cvar OFF_ROUTE:
    :cvar COMPLETED: It has been detected that the Service was
        completed.
    :cvar ASSUMED_COMPLETED: It is assumed that the Service has
        completed.
    :cvar NOT_RUN:
    """

    EXPECTED = "expected"
    NOT_EXPECTED = "notExpected"
    CANCELLED = "cancelled"
    ASSIGNED = "assigned"
    SIGNED_ON = "signedOn"
    AT_ORIGIN = "atOrigin"
    IN_PROGRESS = "inProgress"
    ABORTED = "aborted"
    OFF_ROUTE = "offRoute"
    COMPLETED = "completed"
    ASSUMED_COMPLETED = "assumedCompleted"
    NOT_RUN = "notRun"


@dataclass
class ViaRef:
    """
    Reference to a SCHEDULED STOP POINT that is a VIA point on the journey.
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
class ConnectingJourneyRefStructure:
    """
    Type for a reference to a connecting journey.

    :ivar framed_vehicle_journey_ref: A reference to the DATE VEHICLE
        JOURNEY that the VEHICLE is making, unique with the data horizon
        of the service.
    :ivar line_ref: LINE Reference.
    :ivar participant_ref:
    """

    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
