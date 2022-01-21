from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from siri.siri_model.siri_situation_identity_v1_1 import (
    SituationFullRef,
    SituationRef,
)
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AllModesEnumeration(Enum):
    """
    Union of VEHICLE and continuous MODEs.
    """

    WALK = "walk"
    CAR = "car"
    TAXI = "taxi"
    CYCLE = "cycle"
    DRT = "drt"
    MOVING_WALKWAY = "movingWalkway"
    THROUGH = "through"


@dataclass
class ConnectionLinkRef:
    """
    Reference to a CONNECTION link.
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
class JourneyPatternRef:
    """
    Reference to a JOURNEY PATTERN.
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
class LineDirectionStructure:
    """
    Type for LINEand DIRECTION.

    :ivar line_ref: Line Reference.
    :ivar direction_ref: Direction Reference.
    """

    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class LineRef:
    """
    Reference to a LINE.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class OccupancyEnumeration(Enum):
    """
    Passenger load status of a VEHICLE.
    """

    FULL = "full"
    SEATS_AVAILABLE = "seatsAvailable"
    STANDING_AVAILABLE = "standingAvailable"


@dataclass
class Order:
    """
    For implementations for which the overall Order is not used for
    VisitNumber, (i.e. if VisitNumberIsOrder is false) then can be used to
    associate the stop Order as well if useful.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class StopPointRef:
    """Reference to a SCHEDULED STOP POINT.

    Reference to a STOP POINT.
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
class TimingPoint:
    """Whether the stop is a TIMING POINT.

    Times for stops that are not timing points are sometimes
    interpolated crudely from the timing points, and may represent a
    lower level of accuracy. Default is 'true'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        },
    )


@dataclass
class VehicleAtStop:
    """Whether VEHICLE is currently at stop.

    Default is false (xml  default added from SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )


class VehicleModesEnumeration(Enum):
    """
    MODEs of transport applicable to timetabled public transport.
    """

    AIR = "air"
    BUS = "bus"
    COACH = "coach"
    FERRY = "ferry"
    METRO = "metro"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND = "underground"


@dataclass
class VehicleRef:
    """
    Reference to a VEHICLE.
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
class VersionRef:
    """
    Version Identifier.
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
class VisitNumber:
    """Sequence of visit to SCHEDULED STOP POINT.within VEHICLE JOURNEY.

    Increases monotonically, but not necessarily sequentially.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ModesStructure:
    """
    Type for Transport MODEs.

    :ivar mode: A method of transportation such as bus, rail, etc.
    :ivar exclude: if true, listed modes to be excluded from list.
    """

    mode: List[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    exclude: bool = field(
        default=False,
        metadata={
            "name": "Exclude",
            "type": "Attribute",
        },
    )


@dataclass
class NoteStructure:
    """
    DataType for a NOTICe.

    :ivar situation_ref:
    :ivar situation_simple_ref:
    :ivar situation_full_ref:
    :ivar note: Text annotation that applies to an element.
    """

    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_simple_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationSimpleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_full_ref: Optional[SituationFullRef] = field(
        default=None,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    note: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PlaceNameStructure:
    """Names of VIA points, used to help identify the LINE, for example, Luton
    to Luton via Sutton.

    Currently 3 in VDV. Should only be included if the detail level was
    requested.

    :ivar place_ref: Reference to a TOPOGRAPHIC PLACE.
    :ivar place_name: Names of place used to help identify the LINE.
    :ivar place_short_name: Short name of TOPOGRAPHIC PLACE. Should only
        be included if the detail level was requested.
    """

    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PublishedLineName(NaturalLanguageStringStructure):
    """
    Name or Number by which the LINEis known to the public.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class RouteName(NaturalLanguageStringStructure):
    """
    Description of route by which it can be recogniozed.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopPointName(NaturalLanguageStringStructure):
    """
    Name of SCHEDULED STOP POINT.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
