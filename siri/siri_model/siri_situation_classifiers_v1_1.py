from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictabilityEnumeration(Enum):
    """
    Values for Predictability Status.
    """

    PLANNED = "planned"
    UNPLANNED = "unplanned"
    ALL = "all"


class ServiceConditionEnumeration(Enum):
    """Values for Service Condition.

    Corresponds to TPEG Pti13 Service Condition values.

    :cvar PTI13_0:
    :cvar UNKNOWN: TPEG Pti13_unknown.
    :cvar PTI13_1:
    :cvar ALTERED: TPEG Pti13_altered.
    :cvar PTI13_2:
    :cvar CANCELLED: TPEG Pti13_cancelled.
    :cvar PTI13_3:
    :cvar DELAYED: TPEG Pti13_delayed.
    :cvar PTI13_4:
    :cvar DIVERTED: TPEG Pti13_diverted.
    :cvar PTI13_5:
    :cvar NO_SERVICE: TPEG Pti13_no service.
    :cvar PTI13_6:
    :cvar DISRUPTED: TPEG Pti13_disrupted.
    :cvar PTI13_7:
    :cvar ADDITIONAL_SERVICE: TPEG Pti13_additional service.
    :cvar PTI13_8:
    :cvar SPECIAL_SERVICE: TPEG Pti13_special service.
    :cvar PTI13_9:
    :cvar ON_TIME: TPEG Pti13_on time.
    :cvar PTI13_10:
    :cvar NORMAL_SERVICE: TPEG Pti13_normal service.
    :cvar PTI13_11:
    :cvar INTERMITTENT_SERVICE: TPEG Pti13_intermittent service.
    :cvar PTI13_12:
    :cvar SHORT_FORMED_SERVICE: TPEG Pti13_short formed service.
    :cvar PTI13_13:
    :cvar FULL_LENGTH_SERVICE: TPEG Pti13_full length service.
    :cvar PTI13_14:
    :cvar EXTENDED_SERVICE: TPEG Pti13_extended service.
    :cvar PTI13_15:
    :cvar SPLITTING_TRAIN: TPEG Pti13_splitting train.
    :cvar PTI13_16:
    :cvar REPLACEMENT_TRANSPORT: TPEG Pti13_replacement transport.
    :cvar PTI13_17:
    :cvar ARRIVES_EARLY: TPEG Pti13_arrives early.
    :cvar PTI13_18:
    :cvar SHUTTLE_SERVICE: TPEG Pti13_shuttle service.
    :cvar PTI13_19:
    :cvar REPLACEMENT_SERVICE: TPEG Pti13_replacement service.
    :cvar PTI13_255:
    :cvar UNDEFINED_SERVICE_INFORMATION: TPEG Pti13_Undefined service
        information.
    """

    PTI13_0 = "pti13_0"
    UNKNOWN = "unknown"
    PTI13_1 = "pti13_1"
    ALTERED = "altered"
    PTI13_2 = "pti13_2"
    CANCELLED = "cancelled"
    PTI13_3 = "pti13_3"
    DELAYED = "delayed"
    PTI13_4 = "pti13_4"
    DIVERTED = "diverted"
    PTI13_5 = "pti13_5"
    NO_SERVICE = "noService"
    PTI13_6 = "pti13_6"
    DISRUPTED = "disrupted"
    PTI13_7 = "pti13_7"
    ADDITIONAL_SERVICE = "additionalService"
    PTI13_8 = "pti13_8"
    SPECIAL_SERVICE = "specialService"
    PTI13_9 = "pti13_9"
    ON_TIME = "onTime"
    PTI13_10 = "pti13_10"
    NORMAL_SERVICE = "normalService"
    PTI13_11 = "pti13_11"
    INTERMITTENT_SERVICE = "intermittentService"
    PTI13_12 = "pti13_12"
    SHORT_FORMED_SERVICE = "shortFormedService"
    PTI13_13 = "pti13_13"
    FULL_LENGTH_SERVICE = "fullLengthService"
    PTI13_14 = "pti13_14"
    EXTENDED_SERVICE = "extendedService"
    PTI13_15 = "pti13_15"
    SPLITTING_TRAIN = "splittingTrain"
    PTI13_16 = "pti13_16"
    REPLACEMENT_TRANSPORT = "replacementTransport"
    PTI13_17 = "pti13_17"
    ARRIVES_EARLY = "arrivesEarly"
    PTI13_18 = "pti13_18"
    SHUTTLE_SERVICE = "shuttleService"
    PTI13_19 = "pti13_19"
    REPLACEMENT_SERVICE = "replacementService"
    PTI13_255 = "pti13_255"
    UNDEFINED_SERVICE_INFORMATION = "undefinedServiceInformation"


class SeverityEnumeration(Enum):
    """Values for Severity.

    Correspond to TPEG Pti26 Severity values.

    :cvar PTI26_0:
    :cvar UNKNOWN: TPEG Pti26_0: unknown.
    :cvar PTI26_1:
    :cvar VERY_SLIGHT: TPEG Pti26_1: very slight.
    :cvar PTI26_2:
    :cvar SLIGHT: TPEG Pti26_2: slight.
    :cvar PTI26_3:
    :cvar NORMAL: TPEG Pti26_3: normal.
    :cvar PTI26_4:
    :cvar SEVERE: TPEG Pti26_4: severe.
    :cvar PTI26_5:
    :cvar VERY_SEVERE: TPEG Pti26_5: verySevere.
    :cvar PTI26_6:
    :cvar NO_IMPACT: TPEG Pti26_6: noImpact.
    :cvar PTI26_255:
    :cvar UNDEFINED: TPEG Pti26_255: undefined.
    """

    PTI26_0 = "pti26_0"
    UNKNOWN = "unknown"
    PTI26_1 = "pti26_1"
    VERY_SLIGHT = "verySlight"
    PTI26_2 = "pti26_2"
    SLIGHT = "slight"
    PTI26_3 = "pti26_3"
    NORMAL = "normal"
    PTI26_4 = "pti26_4"
    SEVERE = "severe"
    PTI26_5 = "pti26_5"
    VERY_SEVERE = "verySevere"
    PTI26_6 = "pti26_6"
    NO_IMPACT = "noImpact"
    PTI26_255 = "pti26_255"
    UNDEFINED = "undefined"


class VerificationStatusEnumeration(Enum):
    """
    Values for Verification Status Corresponds to TPEG pti_table 32.
    """

    PTI32_0 = "pti32_0"
    UNKNOWN = "unknown"
    PTI32_1 = "pti32_1"
    UNVERIFIED = "unverified"
    PTI32_255 = "pti32_255"
    VERIFIED = "verified"
    VERIFIED_AS_DUPLICATE = "verifiedAsDuplicate"


@dataclass
class Condition:
    """Classification of effect on service.

    TPEG Pti13 Service Condition values.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[ServiceConditionEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Predictability:
    """
    Classification of Predictability status.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[VerificationStatusEnumeration] = field(default=None)


@dataclass
class Severity:
    """Severity of Incident.

    Corresponds to TPEG Pti26 severities. Defautl is 'normal'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SeverityEnumeration = field(
        default=SeverityEnumeration.NORMAL,
        metadata={
            "required": True,
        },
    )


@dataclass
class VerificationStatus:
    """
    Classification of verification status TPEG Pti13 Service Condition values.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[VerificationStatusEnumeration] = field(default=None)
