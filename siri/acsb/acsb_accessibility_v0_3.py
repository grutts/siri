from dataclasses import dataclass, field
from typing import List, Optional
from siri.acsb.acsb_limitations_v0_2 import AccessibilityEnumeration
from siri.acsb.acsb_passenger_mobility_v0_3 import SuitabilityStructure
from siri.ifopt.ifopt_time_v0_2 import ValidityConditionStructure
from siri.ifopt.ifopt_types_v0_2 import Extensions

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class AccessibilityLimitationStructure:
    """
    Type for limitation on navigation.

    :ivar limitation_id: Identifier of LIMITATION.
    :ivar validity_condition: Validty condition governing applicability
        of LIMITATION.
    :ivar wheelchair_access:
    :ivar step_free_access:
    :ivar escalator_free_access:
    :ivar lift_free_access:
    :ivar audible_signals_available: Whether a PLACE / SITE ELEMENT has
        Audible signals for the viusally impaired.
    :ivar visual_signs_available: Whether a PLACE / SITE ELEMENT has
        Visual signals for the hearing impaired.
    :ivar extensions:
    """

    limitation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LimitationId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    wheelchair_access: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.FALSE,
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        },
    )
    step_free_access: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    escalator_free_access: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    lift_free_access: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    audible_signals_available: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    visual_signs_available: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )


@dataclass
class AccessibilityAssessmentStructure:
    """
    Type for Assesment.

    :ivar mobility_impaired_access: Summary indication as to whether the
        component is considered to be accessible or not.
    :ivar limitations: The Limitations that apply to component.
    :ivar suitabilities: The Suitability of the component to meet
        specifc user needs.
    :ivar extensions:
    """

    mobility_impaired_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        },
    )
    limitations: Optional["AccessibilityAssessmentStructure.Limitations"] = field(
        default=None,
        metadata={
            "name": "Limitations",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    suitabilities: Optional["AccessibilityAssessmentStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class Limitations:
        """
        :ivar accessibility_limitation: The accessibility limitations of
            a component.
        """

        accessibility_limitation: List[AccessibilityLimitationStructure] = field(
            default_factory=list,
            metadata={
                "name": "AccessibilityLimitation",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Suitabilities:
        """
        :ivar suitability: The Suitability of com[onent to meet a
            specifc user need.
        """

        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "min_occurs": 1,
            },
        )
