from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class AccessibilityEnumeration(Enum):
    """
    Enumeration of values for an accessibility value.
    """

    UNKNOWN = "unknown"
    FALSE = "false"
    TRUE = "true"


@dataclass
class AudibleSignalsAvailable:
    """
    Whether a PLACE / SITE ELEMENT is wheelchair accessible.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.FALSE,
        metadata={
            "required": True,
        },
    )


@dataclass
class EscalatorFreeAccess:
    """
    Whether a PLACE / SITE ELEMENT has escalator free access.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class GuideDogAccess:
    """
    Whether a PLACE / SITE ELEMENT allows guide dog access.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class LiftFreeAccess:
    """
    Whether a PLACE / SITE ELEMENT has lift free access.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class StepFreeAccess:
    """
    Whether a PLACE / SITE ELEMENT has step free access.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class VisualSignsAvailable:
    """
    Whether a PLACE / SITE ELEMENT has Visual signals availble for the free
    access.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )


@dataclass
class WheelchairAccess:
    """
    Whether a PLACE / SITE ELEMENT is wheelchair accessible.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.FALSE,
        metadata={
            "required": True,
        },
    )
