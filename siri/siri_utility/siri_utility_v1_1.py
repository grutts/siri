from dataclasses import dataclass, field
from enum import Enum
from typing import List

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EmptyType(Enum):
    """
    A type with no allowed content, used when simply the presence of an element
    is significant.
    """

    VALUE = ""


@dataclass
class ExtensionsStructure:
    """Type for Extensions to schema.

    Wraps an 'any' tag to ensure decidability.

    :ivar any_element: Placeholder for user extensions.
    """

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Extensions(ExtensionsStructure):
    """Extensions to schema.

    (Wrapper tag used to avoid problems with handling of optional 'any'
    by some validators).
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
