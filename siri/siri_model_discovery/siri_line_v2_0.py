from dataclasses import dataclass, field
from typing import List, Optional
from siri.siri_model.siri_journey_v2_0 import DirectionStructure
from siri.siri_model_discovery.siri_stop_point_v2_0 import AnnotatedStopPointStructure
from siri.siri_utility.siri_location_v2_0 import LineShapeStructure
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AnnotatedDestinationStructure:
    """
    Type for DESTINATION and place name.

    :ivar destination_ref:
    :ivar place_name: Name of destination TOPOGRAPHIC PLACE.  (Unbounded
        since SIRI 2.0)
    :ivar direction_ref: Direction in which destination lies. relatoive
        to currernt stop SIRI 2.0
    """

    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
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
class StopPointInPatternStructure(AnnotatedStopPointStructure):
    """
    Summary information about a stop within line.

    :ivar order: Order of STOP POINT in route +SIRI v2.0
    :ivar onward_link_shape: Plot of points from this stop to next Stop.
        Detail level is 'full'. +SIRI v2.0
    :ivar extensions:
    """

    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    onward_link_shape: Optional[LineShapeStructure] = field(
        default=None,
        metadata={
            "name": "OnwardLinkShape",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class Destination(AnnotatedDestinationStructure):
    """
    Description of a DESTINATION.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class RouteDirectionStructure(DirectionStructure):
    """
    Summary information about a  Direction of a Line.

    :ivar stops: Ordered collection of STOP POINTs the LINE and
        direction . Detail level is  'stops'. +SIRI v2.0
    :ivar extensions:
    """

    stops: Optional["RouteDirectionStructure.Stops"] = field(
        default=None,
        metadata={
            "name": "Stops",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Stops:
        """
        :ivar stop_point_in_pattern: Stop within Route of LINE. Detail
            level is 'stop' +SIRI v2.0
        """

        stop_point_in_pattern: List[StopPointInPatternStructure] = field(
            default_factory=list,
            metadata={
                "name": "StopPointInPattern",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 2,
            },
        )


@dataclass
class AnnotatedLineStructure:
    """
    Summary information about a LINE type.

    :ivar line_ref: Identifier of LINE.
    :ivar line_name: Name of LINE.   (Unbounded since SIRI 2.0)
    :ivar monitored: Whether the LINE has real-time info. Default is
        'true'.
    :ivar destinations: DESTINATIONs to which the LINE runs. Detail
        level is 'normal'
    :ivar directions: DIRECTIONs and Stops for the LINE. 'normal'
    :ivar extensions:
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
    line_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    monitored: bool = field(
        default=True,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    destinations: Optional["AnnotatedLineStructure.Destinations"] = field(
        default=None,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    directions: Optional["AnnotatedLineStructure.Directions"] = field(
        default=None,
        metadata={
            "name": "Directions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Destinations:
        destination: List[Destination] = field(
            default_factory=list,
            metadata={
                "name": "Destination",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Directions:
        """
        :ivar direction: Directions of Route
        """

        direction: List[RouteDirectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "Direction",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AnnotatedLineRef(AnnotatedLineStructure):
    """
    Information about LINEs covered by server.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
