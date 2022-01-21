from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AliasStructure:
    """
    Alternative Private Code.

    :ivar private_code: Alternative identifier.
    :ivar identifier_type: Type of Identifier.
    """

    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        },
    )
    identifier_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )


class StopPlaceComponentTypeEnumeration(Enum):
    """
    Enumeration of SITE COMPONENT Types.
    """

    QUAY = "quay"
    ACCESS_SPACE = "accessSpace"
    ENTRANCE = "entrance"
    BOARDING_POSITION = "boardingPosition"
    STOPPING_PLACE = "stoppingPlace"


@dataclass
class StopPlaceRef:
    """
    Reference to a STOP PLACE.
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
class StopPlaceRefsStructure:
    """
    Type for a collection of one or more references to a STOP PLACE.
    """

    stop_place_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )


class StopPlaceTypeEnumeration(Enum):
    """
    Enumeration of STOP PLACE types.
    """

    AIRPORT = "airport"
    RAIL_STATION = "railStation"
    METRO_STATION = "metroStation"
    COACH_STATION = "coachStation"
    BUS_STATION = "busStation"
    HARBOUR_PORT = "harbourPort"
    FERRYT_PORT = "ferrytPort"
    FERRY_STOP = "ferryStop"
    ON_STREET_BUS = "onStreetBus"
    ON_STREET_TRAM = "onStreetTram"
    SKI_LIFT = "skiLift"
    OTHER = "other"
