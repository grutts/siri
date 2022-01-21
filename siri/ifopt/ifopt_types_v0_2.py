from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class Extensions:
    """
    Arbitrary extensions.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class InfoLink:
    """
    Info Link .
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class InfoLinksStructure:
    """
    Type for collection of info links.
    """

    info_link: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
