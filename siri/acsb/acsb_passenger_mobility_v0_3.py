from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class EncumbranceEnumeration(Enum):
    """
    Enumeration of specific encumbrances USER NEEDs.
    """

    LUGGAGE_ENCUMBERED = "luggageEncumbered"
    PUSHCHAIR = "pushchair"
    BAGGAGE_TROLLEY = "baggageTrolley"
    OVERSIZE_BAGGAGE = "oversizeBaggage"
    GUIDE_DOG = "guideDog"
    OTHER_ANIMAL = "otherAnimal"
    OTHER_ENCUMBRANCE = "otherEncumbrance"


class MedicalNeedEnumeration(Enum):
    """
    Enumeration of specific Medical USER NEEDs.
    """

    ALLERGIC = "allergic"
    HEART_CONDITION = "heartCondition"
    OTHER_MEDICAL_NEED = "otherMedicalNeed"


class MobilityEnumeration(Enum):
    """
    Identification of mobility USER NEEDs.
    """

    WHEELCHAIR = "wheelchair"
    ASSISTED_WHEELCHAIR = "assistedWheelchair"
    MOTORIZED_WHEELCHAIR = "motorizedWheelchair"
    WALKING_FRAME = "walkingFrame"
    RESTRICTED_MOBILITY = "restrictedMobility"
    OTHER_MOBILITY_NEED = "otherMobilityNeed"


class PyschosensoryNeedEnumeration(Enum):
    """
    Enumeration of specific psychosensory USER NEEDs.
    """

    VISUAL_IMPAIRMENT = "visualImpairment"
    AUDITORY_IMPAIRMENT = "auditoryImpairment"
    COGNITIVE_INPUT_IMPAIRMENT = "cognitiveInputImpairment"
    AVERSE_TO_LIFTS = "averseToLifts"
    AVERSE_TO_ESCALATORS = "averseToEscalators"
    AVERSE_TO_CONFINED_SPACES = "averseToConfinedSpaces"
    AVERSE_TO_CROWDS = "averseToCrowds"
    OTHER_PSYCHOSENSORY_NEED = "otherPsychosensoryNeed"


class SuitabilityEnumeration(Enum):
    """
    Identification of specific SUITABILITY.
    """

    SUITABLE = "suitable"
    NOT_SUITABLE = "notSuitable"


@dataclass
class UserNeedStructure:
    """
    Type for of a specific need.

    :ivar mobility_need: Passenger mobility USER NEED for which
        SUITABILITY is specified.
    :ivar psychosensory_need: Passenger mobility USER NEED for which
        SUITABILITY is specified.
    :ivar medical_need: Passenger medical USER NEED for which
        SUITABILITY is specified.
    :ivar encumbrance_need: Passenger enceumbrance USER NEED for which
        SUITABILITY is specified.
    :ivar excluded: Whether USER NEED is included or excluded. Default
        is 'included'.
    :ivar need_ranking: Relative ranking of USER NEED on a sclae 1-5
    :ivar extensions: Extensions to USETR NEED.
    """

    mobility_need: Optional[MobilityEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    psychosensory_need: Optional[PyschosensoryNeedEnumeration] = field(
        default=None,
        metadata={
            "name": "PsychosensoryNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    medical_need: Optional[MedicalNeedEnumeration] = field(
        default=None,
        metadata={
            "name": "MedicalNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    encumbrance_need: Optional[EncumbranceEnumeration] = field(
        default=None,
        metadata={
            "name": "EncumbranceNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    excluded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    need_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )


@dataclass
class PassengerAccessibilityNeedsStructure:
    """Type for accessibility needs.

    Records the requirementrs of a passenger that may affect choice of
    facilities.

    :ivar user_need: Specific pyschosensory need that may constrain
        choice of services and facilities.
    :ivar accompanied_by_carer: Whether the passenger is accompanied by
        a carer or assistant.
    """

    user_need: List[UserNeedStructure] = field(
        default_factory=list,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    accompanied_by_carer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )


@dataclass
class SuitabilityStructure:
    """
    Type for of a specific SUITABILITY.

    :ivar suitable: Whether the Facility is suitable.
    :ivar user_need: USER NEED for which SUITABILITY is specified.
    """

    suitable: Optional[SuitabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "Suitable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        },
    )
    user_need: Optional[UserNeedStructure] = field(
        default=None,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        },
    )
