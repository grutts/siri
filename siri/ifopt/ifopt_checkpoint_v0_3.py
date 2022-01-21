from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDuration
from siri.ifopt.ifopt_time_v0_2 import ValidityConditionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class AccessibilityFeatureEnumeration(Enum):
    """
    Allowed values for a CHECK CONSTRAINT.
    """

    LIFT = "lift"
    STAIRS = "stairs"
    SERIES_OF_STAIRS = "seriesOfStairs"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    SHUTTLE = "shuttle"
    BARRIER = "barrier"
    NARROW_ENTRANCE = "narrowEntrance"
    CONFINED_SPACE = "confinedSpace"
    QUEUE_MANAGEMENT = "queueManagement"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"


class CheckPointProcessEnumeration(Enum):
    """
    Allowed values for a CHECK CONSTRAINT.
    """

    NONE = "none"
    UNKNOWN = "unknown"
    TICKET_PURCHASE = "ticketPurchase"
    TICKET_COLLECTION = "ticketCollection"
    TICKET_VALIDATION = "ticketValidation"
    BAGGAGE_CHECK_IN = "baggageCheckIn"
    OVERSIZE_BAGGAGE_CHECK_IN = "oversizeBaggageCheckIn"
    OVERSIZE_BAGGAGE_RECLAIM = "oversizeBaggageReclaim"
    BAGGAGE_RECLAIM = "baggageReclaim"
    LEFT_LUGGAGE_DEPOSIT = "leftLuggageDeposit"
    LEFT_LUGGAGE_RECLAIM = "leftLuggageReclaim"
    FIRSTCLASS_CHECKIN = "firstclassCheckin"
    SPECIAL_NEEDS_CHECKIN = "specialNeedsCheckin"
    BAGGAGE_SECURITY_CHECK = "baggageSecurityCheck"
    SECURITY_CHECK = "securityCheck"
    OUTGOING_PASSPORT_CONTROL = "outgoingPassportControl"
    INCOMING_PASSPORT_CONTROL = "incomingPassportControl"
    FASTTRACK_DEPARTURES = "fasttrackDepartures"
    FASTTRACK_ARRIVALS = "fasttrackArrivals"
    INCOMING_DUTY_FREE = "incomingDutyFree"
    OUTGOING_DUTY_FREE = "outgoingDutyFree"
    TAX_REFUNDS = "taxRefunds"
    OUTGOING_CUSTOMS = "outgoingCustoms"
    INCOMING_CUSTOMS = "incomingCustoms"


class CheckPointServiceEnumeration(Enum):
    """
    Allowed values for a CHECK CONSTRAINT.
    """

    SELFSERVICE_MACHINE = "selfserviceMachine"
    COUNTER_SERVICE = "counterService"
    OTHER = "other"


class CongestionEnumeration(Enum):
    """
    Allowed values for a CHECK CONSTRAINT.
    """

    NO_WAITING = "noWaiting"
    QUEUE = "queue"
    CROWDING = "crowding"
    FULL = "full"


@dataclass
class CheckPointStructure:
    """
    Type for a CHECK CONSTRAINT Hazard that can be associated with.

    :ivar check_point_id: Identifier of CHECK CONSTRAINt.
    :ivar validity_condition: Validty condition governing applicability
        of CHECK CONSTRAINT.
    :ivar check_point_process: Type of process that may occur at CHECK
        CONSTRAINt.
    :ivar check_point_service: Type of process that may occur at CHECK
        CONSTRAINt.
    :ivar access_feature_type: Type of physical featrue that may slow
        use of CHECK CONSTRAINt.
    :ivar congestion: Type of crowding that may slow use of CHECK
        CONSTRAINt.
    :ivar facility_ref: Classification of feature of CHECK CONSTRAINT.
    :ivar minimum_likely_delay: Minimum duration needed to pass through
        CHECK CONSTRAINT.
    :ivar average_delay: Average duration expected to pass through CHECK
        CONSTRAINT.
    :ivar maximum_likely_delay: Maximum duration expected to pass
        through CHECK CONSTRAINT.
    """

    check_point_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckPointId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    check_point_process: Optional[CheckPointProcessEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckPointProcess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    check_point_service: Optional[CheckPointServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "CheckPointService",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    access_feature_type: Optional[AccessibilityFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    congestion: Optional[CongestionEnumeration] = field(
        default=None,
        metadata={
            "name": "Congestion",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    minimum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    average_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AverageDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    maximum_likely_delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumLikelyDelay",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
