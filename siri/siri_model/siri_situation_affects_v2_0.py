from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.acsb.acsb_accessibility_v0_3 import AccessibilityAssessmentStructure
from siri.ifopt.ifopt_checkpoint_v0_3 import AccessibilityFeatureEnumeration
from siri.ifopt.ifopt_location_v0_3 import (
    LinkProjection,
    LinkProjectionStructure,
    PointProjection,
    ZoneProjection,
)
from siri.ifopt.ifopt_modes_v0_2 import AccessModesEnumeration
from siri.ifopt.ifopt_stop_v0_3 import (
    StopPlaceComponentTypeEnumeration,
    StopPlaceTypeEnumeration,
)
from siri.siri_model.siri_journey_support_v2_0 import (
    ArrivalBoardingActivityEnumeration,
    CallStatusEnumeration,
    DepartureBoardingActivityEnumeration,
    FramedVehicleJourneyRefStructure,
)
from siri.siri_model.siri_journey_v2_0 import (
    ArrivalPlatformName,
    DeparturePlatformName,
    DirectionStructure,
)
from siri.siri_model.siri_modes_v1_1 import (
    AirSubmodesOfTransportEnumeration,
    BusSubmodesOfTransportEnumeration,
    CoachSubmodesOfTransportEnumeration,
    MetroSubmodesOfTransportEnumeration,
    RailSubmodesOfTransportEnumeration,
    TramSubmodesOfTransportEnumeration,
    VehicleModesOfTransportEnumeration,
    WaterSubmodesOfTransportEnumeration,
)
from siri.siri_model.siri_reference_v2_0 import PublishedLineName
from siri.siri_model.siri_situation_service_types_v1_0 import (
    InterchangeStatusEnumeration,
    RoutePointTypeEnumeration,
    StopPointTypeEnumeration,
)
from siri.siri_utility.siri_location_v2_0 import LocationStructure
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import (
    EmptyType,
    Extensions,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CasualtiesStructure:
    """
    Type for Information on casualties.

    :ivar number_of_deaths: Number of fatalities.
    :ivar number_of_injured: Number of injured presons.
    """

    number_of_deaths: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfDeaths",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number_of_injured: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfInjured",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


class ConnectionDirectionEnumeration(Enum):
    """
    Values for DIRECTION of CONNECTION link or SERVCIE JOURNEY INTERCHANGE.
    """

    TO = "to"
    FROM = "from"
    BOTH = "both"


@dataclass
class OffsetStructure:
    """
    Type for information about the LINEs affected by an SITUATION.

    :ivar distance_from_start: Distance in metres from start of link at
        which SITUATION is to be shown. I f absent use start of link.
    :ivar distance_from_end: Distance in metres from end of link at
        which SITUATION is to be shown. I f absent use end of link.
    """

    distance_from_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distance_from_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromEnd",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AffectedModesStructure:
    """
    Type for TRANSPORT MODEs affecetd by a SITUATION.

    :ivar all_modes: All known modes for stop.
    :ivar mode: Mode affected by SITUATION.
    """

    all_modes: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllModes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mode: List["AffectedModesStructure.Mode"] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Mode:
        vehicle_mode: Optional[VehicleModesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "VehicleMode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        air_submode: Optional[AirSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "AirSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        bus_submode: Optional[BusSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "BusSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        coach_submode: Optional[CoachSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "CoachSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        metro_submode: Optional[MetroSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "MetroSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        rail_submode: Optional[RailSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "RailSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        tram_submode: Optional[TramSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "TramSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        water_submode: Optional[WaterSubmodesOfTransportEnumeration] = field(
            default=None,
            metadata={
                "name": "WaterSubmode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        access_mode: Optional[AccessModesEnumeration] = field(
            default=None,
            metadata={
                "name": "AccessMode",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class AffectedOperatorStructure:
    """
    Type for Annotated reference to an OPERATOR affected by a SITUATION.

    :ivar operator_ref: Reference to an OPERATOR.
    :ivar operator_name: Public Name of OPERATOR. Can be derived from
        OperatorRef.  (Unbounded since SIRI 2.0)
    :ivar operator_short_name: Short Name for OPERATOR. Can be derived
        from OperatorRef.  (Unbounded since SIRI 2.0)
    :ivar operational_unit_ref: OPERATIONAL UNIT responsible for
        managing services.
    :ivar extensions:
    """

    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_short_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operational_unit_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationalUnitRef",
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
class AffectedPathLinkStructure:
    """
    Information about a CONNECTION link from a given stop affected by a
    SITUATION.

    :ivar link_ref: Identifier of CONNECTION link.
    :ivar link_name: Description of Link.  (Unbounded since SIRI 2.0)
    :ivar accessibility_feature: Nature of CONNECTION link.
    :ivar link_direction: Description of a DIRECTION of CONNECTION link.
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    :ivar extensions:
    """

    link_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LinkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_feature: Optional[AccessibilityFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessibilityFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_direction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
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
class AffectedPlaceStructure:
    """
    Type for annotated references to a TOPOGRAPHIC PLACE.

    :ivar place_ref: Reference to a SITE or TOPOGRAPHIC PLACE
        (Locality).
    :ivar private_code: Alternative identifier of SITE or TOPOGRAPHIC
        PLACE
    :ivar place_name: Name of SITE or TOPOGRAPHIC PLACE (locality) in
        which stop is found.  (Unbounded since SIRI 2.0)
    :ivar location: Spatial coordinates of STOP POINT. Derivable from
        StopRef.
    :ivar place_category: Category of TOPGRAPHIC PLACE or SITE.
    :ivar equipment_ref: Reference to an EQUIPMENT found at location.
    :ivar accessibility_assessment: Changes to accessibility for SITE.
    :ivar extensions:
    """

    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceCategory",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
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
class AffectedSectionStructure:
    """
    Type for information about the sectons affected by an SITUATION.

    :ivar section_ref: Reference to a section of ROUTE affected by a
        SITUATION.
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    :ivar extensions:
    """

    section_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
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
class AffectedStopPlaceElementStructure:
    """
    Type for information about the quays affected by an SITUATION.

    :ivar accessibility_assessment: Disruption of accessibility.
    """

    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class NetworkStructure:
    """
    Type for Annotated reference to a NETWORK affected by a SITUATION.

    :ivar network_ref: Reference to a NETWORK.
    :ivar network_name: Name of NETWORK. Can be derived from NetworkRef.
        (Unbounded since SIRI 2.0)
    :ivar vehicle_mode:
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar metro_submode:
    :ivar rail_submode:
    :ivar tram_submode:
    :ivar water_submode:
    :ivar access_mode:
    """

    network_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "NetworkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: Optional[VehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    air_submode: Optional[AirSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bus_submode: Optional[BusSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    coach_submode: Optional[CoachSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    metro_submode: Optional[MetroSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    rail_submode: Optional[RailSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    tram_submode: Optional[TramSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    water_submode: Optional[WaterSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AffectedConnectionLinkStructure:
    """
    Type for a reference Information about a CONNECTION link from a given stop
    that is affected by a SITUATION.

    :ivar connection_link_ref: Reference to a CONNECTION link affected
        by a  SITUATION.
    :ivar connection_name: Name of CONNECTION link affected by a
        SITUATION.
    :ivar all_lines:
    :ivar line_ref:
    :ivar connecting_stop_point_ref: Reference to  other connecting STOP
        POINT of a CONNECTION link. If blank, both feeder and
        distributor vehicles go to same stop. Reference to a STOP POINT.
    :ivar connecting_stop_point_name: Name of other connecting STOP
        POINT of a CONNECTION link. Derivable from StopRef.  (Unbounded
        since SIRI 2.0)
    :ivar connecting_zone_ref: Zone in which connecting stop lies.
    :ivar connection_direction: Direction of SERVICE JOURNEY
        INTERCHANGE. Default is 'both'.
    :ivar affected_path_link: PATH LINKs affected by a SITUATION.
    :ivar extensions:
    """

    connection_link_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_lines: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllLines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectingStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_zone_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectingZoneRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_direction: Optional[ConnectionDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_path_link: List[AffectedPathLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedPathLink",
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
class AffectedRouteStructure:
    """
    Type for information about the routes affected by a SITUATION.

    :ivar route_ref: Reference to a ROUTE affected by SITUATION.
    :ivar direction: DIRECTIONS affected by SITUATION.
    :ivar sections: Sections of ROUTE affected by SITUATION.
    :ivar route_links: ROUTE LINKs affected by SITUATION.
    :ivar extensions:
    """

    route_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction: List[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sections: Optional["AffectedRouteStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_links: Optional["AffectedRouteStructure.RouteLinks"] = field(
        default=None,
        metadata={
            "name": "RouteLinks",
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
    class Sections:
        """
        :ivar affected_section: Sections of ROUTE that is affected by
            SITUATION.
        """

        affected_section: List[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class RouteLinks:
        route_link_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "RouteLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedStopPlaceComponentStructure(AffectedStopPlaceElementStructure):
    """
    Type for information about the quays affected by an SITUATION.

    :ivar component_ref: Reference to a Stop Place.
    :ivar component_name: Name of component.  (Unbounded since SIRI 2.0)
    :ivar component_type: Type of Component.
    :ivar point_projection:
    :ivar link_projection:
    :ivar zone_projection:
    :ivar offset: Further qualifcation of affected part of Link
        projection,
    :ivar extensions:
    """

    component_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    component_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ComponentName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    component_type: Optional[StopPlaceComponentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ComponentType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    point_projection: Optional[PointProjection] = field(
        default=None,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    link_projection: Optional[LinkProjection] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    zone_projection: Optional[ZoneProjection] = field(
        default=None,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
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
class AffectedInterchangeStructure:
    """
    Information about a SERVICE JOURNEY INTERCHANGE at CONNECTION link from a
    given SCHEDULED STOP POINT.

    :ivar interchange_ref: Reference to a SERVICE JOURNEY INTERCHANGE
        affected by a SITUATION.
    :ivar interchange_stop_point_ref: Identifier of STOP POINT of a stop
        at which VEHICLE JOURNEY meets for interchange If blank, same
        stop as destination. Reference to a STOP POINT.
    :ivar interchange_stop_point_name: Name of other Connecting STOP
        POINT of a connection. Derivable from InterchangeStopRef.
        (Unbounded since SIRI 2.0)
    :ivar connecting_vehicle_journey_ref: Reference to connecting
        VEHICLE JOURNEY affected by a SITUATION.
    :ivar interchange_status_type:
    :ivar connection_link: Reference to a CONNECTION Link affected by a
        SITUATION.
    :ivar extensions:
    """

    interchange_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectingVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_status_type: Optional[InterchangeStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "InterchangeStatusType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link: List[AffectedConnectionLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLink",
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
class AffectedStopPlaceStructure(AffectedStopPlaceElementStructure):
    """
    Type for information about the Stop Places affected by an SITUATION.

    :ivar stop_place_ref: Stop Place affected by SITUATION.
    :ivar place_name: Name of stop place.  (Unbounded since SIRI 2.0)
    :ivar stop_place_type: Type of Stop Place.
    :ivar affected_components: Quays affected by SITUATION.
    :ivar affected_navigation_paths: PathLinks affected by SITUATION.
    :ivar extensions:
    """

    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
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
        },
    )
    stop_place_type: Optional[StopPlaceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_components: Optional["AffectedStopPlaceStructure.AffectedComponents"] = field(
        default=None,
        metadata={
            "name": "AffectedComponents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_navigation_paths: Optional["AffectedStopPlaceStructure.AffectedNavigationPaths"] = field(
        default=None,
        metadata={
            "name": "AffectedNavigationPaths",
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
    class AffectedComponents:
        """
        :ivar affected_component: Quay affected by SITUATION.
        """

        affected_component: List[AffectedStopPlaceComponentStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedComponent",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class AffectedNavigationPaths:
        navigation_path_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NavigationPathRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedStopPointStructure:
    """
    Type for an SCHEDUELD STOP POINT affected by a SITUATION.

    :ivar stop_point_ref:
    :ivar private_ref: Alternative private code of stop.
    :ivar stop_point_name: Name of SCHEDULED STOP POIHT.  (Unbounded
        since SIRI 2.0)
    :ivar stop_point_type: Type of stop type. Normally implicit in
        VEHICLE mode. TPEG table pti 17_4
    :ivar location: Spatial coordinates of STOP POINT. Derivable from
        StopRef.
    :ivar affected_modes: Modes within station/stop affected by the
        SITUATION. If not specified, assume all modes of that station.
    :ivar place_ref: Refernce to a SITE or TOPOGRAPHIC PLACE affected by
        the Locality of stop (In UK NPtg Locality Code). Derivable from
        StopRef.
    :ivar place_name: Name of locality in which stop is found. Derivable
        from LocalityRef.  (Unbounded since SIRI 2.0)
    :ivar accessibility_assessment: Assesmentof current ACCESSIBIKITY of
        the STOP POINT as affected by the SITUATION.
    :ivar connection_links: CONNECTION links from stop.
    :ivar extensions:
    """

    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    private_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_type: Optional[StopPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPointType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_modes: Optional[AffectedModesStructure] = field(
        default=None,
        metadata={
            "name": "AffectedModes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_links: Optional["AffectedStopPointStructure.ConnectionLinks"] = field(
        default=None,
        metadata={
            "name": "ConnectionLinks",
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
    class ConnectionLinks:
        """
        :ivar affected_connection_link: CONNECTION LINKs from stop that
            are affected by the SITUATION.
        """

        affected_connection_link: List[AffectedConnectionLinkStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedConnectionLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedCallStructure(AffectedStopPointStructure):
    """
    Type for information about a CALL affected by an SITUATION.

    :ivar order: Order of visit to stop within JORUNYE PATTERN of
        journey.
    :ivar call_condition: Status of CALL TPEG 13_6
    :ivar vehicle_at_stop:
    :ivar vehicle_location_at_stop: Exact location that VEHICLE will
        take up / or has taken at STOP POINT.
    :ivar aimed_arrival_time: Target arrival time of VEHICLE according
        to latest working timetable.
    :ivar actual_arrival_time: Observed time of arrival of VEHICLE.
    :ivar expected_arrival_time: Estimated time of arriival of VEHICLE.
    :ivar arrival_status:
    :ivar arrival_platform_name:
    :ivar arrival_boarding_activity:
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar actual_departure_time: Observed time of departure of VEHICLE
        from stop.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE from stop. May include waiting time. For people on a
        VEHICLE this is the time that would normally be shown.
    :ivar departure_status:
    :ivar departure_platform_name:
    :ivar departure_boarding_activity:
    :ivar aimed_headway_interval:
    :ivar expected_headway_interval:
    :ivar affected_interchange:
    """

    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    call_condition: Optional[RoutePointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "CallCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location_at_stop: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocationAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_platform_name: Optional[ArrivalPlatformName] = field(
        default=None,
        metadata={
            "name": "ArrivalPlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_boarding_activity: Optional[ArrivalBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: Optional[DeparturePlatformName] = field(
        default=None,
        metadata={
            "name": "DeparturePlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_boarding_activity: Optional[DepartureBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_interchange: List[AffectedInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AffectedLineStructure:
    """
    Type for information about the LINEs affected by an SITUATION.

    :ivar affected_operator: Operators of LINEs affected by incident.
        Overrides any value specified for (i) Affected Network (ii)
        General Context.
    :ivar line_ref:
    :ivar destinations: DESTINATIONs to which the  LINE runs.
    :ivar direction: DIRECTIONs affected.
    :ivar routes: ROUTEs affected if  LINE has multiple ROUTEs.
    :ivar sections: Sections of  LINE affected.
    :ivar extensions:
    """

    affected_operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    destinations: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction: List[DirectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    routes: Optional["AffectedLineStructure.Routes"] = field(
        default=None,
        metadata={
            "name": "Routes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sections: Optional["AffectedLineStructure.Sections"] = field(
        default=None,
        metadata={
            "name": "Sections",
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
    class Routes:
        """
        :ivar affected_route: Route.
        """

        affected_route: List[AffectedRouteStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedRoute",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Sections:
        affected_section: List[AffectedSectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedSection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class AffectedNetworkStructure:
    """Type for information about the parts of the network affected by an
    incident.

    If not explclitly overrided Modes and submodes will be defaulted to
    any values present in the general Context.

    :ivar affected_operator: Operators of LINEs affected by incident.
        Overrides any value specified for (i) General Context.
    :ivar network_ref: Network of affected LINE. If absent, may be taken
        from context.
    :ivar network_name: Name of Network.  (Unbounded since SIRI 2.0)
    :ivar routes_affected: Textual description of overall routes
        affected. Should correspond to any structured description in the
        AffectedLines element.  (Unbounded since SIRI 2.0)
    :ivar vehicle_mode:
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar metro_submode:
    :ivar rail_submode:
    :ivar tram_submode:
    :ivar water_submode:
    :ivar access_mode:
    :ivar all_lines: All LINEs in the network are affected.
    :ivar selected_routes: Only some ROUTEs are affected,  LINE level
        information not available. See the AffectedRoutes element for
        textual description.
    :ivar affected_line: Information about the indvidual LINEs in the
        network that are affected. If not explclitly overrided Modes and
        submodes will be defaulted to any values present (i) in the
        AffectedNetwork (ii) In the general Context.
    :ivar extensions:
    """

    affected_operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedOperator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "NetworkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    routes_affected: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "RoutesAffected",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: Optional[VehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    air_submode: Optional[AirSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bus_submode: Optional[BusSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    coach_submode: Optional[CoachSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    metro_submode: Optional[MetroSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    rail_submode: Optional[RailSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    tram_submode: Optional[TramSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    water_submode: Optional[WaterSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_lines: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllLines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    selected_routes: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "SelectedRoutes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_line: List[AffectedLineStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedLine",
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
class AffectedVehicleJourneyStructure:
    """
    Type for information about a VEHICLE JOURNEY affected by an SITUATION.

    :ivar framed_vehicle_journey_ref: Refercence to a VEHICLE JOURENY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref: Reference to a service VEHICLE JOURNEY
        affected by an SITUATION.
    :ivar dated_vehicle_journey_ref: Reference to a specific DATED
        VEHICLE JOURNEY affected by an SITUATION.
    :ivar journey_name: Name of journey affected by an SITUATION.
        (Unbounded since SIRI 2.0)
    :ivar operator: OPERATOR of LINE affected by SITUATION.
    :ivar line_ref: Reference to the LINE of the journey  affected by an
        SITUATION.
    :ivar published_line_name:
    :ivar direction_ref: DIRECTION of LINE in which journey runs.
    :ivar origins: Origin SCHEDULED STOP POINTs from which the LINE
        runs. [equivalent to pti15 1 start_point route_description_type]
    :ivar destinations: Destination SCHEDULED STOP POINTs  to which the
        LINE runs. [equivalent to pti15 2 destination
        route_description_type]
    :ivar route: ROUTE affected by the SITUATION.
    :ivar origin_aimed_departure_time: Timetabled departure tme  of
        journey from Origin.
    :ivar destination_aimed_arrival_time: Timetabled arrival time of
        journey at Destination.
    :ivar accessibility_assessment:
    :ivar calls: CALLs making up VEHICLE JOURNEY [equivalent to TPEG
        pti15 3 stop, 15_5 not-stopping, 15-6 temporary stop
        route_description_type]
    :ivar extensions:
    """

    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journey_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "JourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator: Optional[AffectedOperatorStructure] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    published_line_name: Optional[PublishedLineName] = field(
        default=None,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    origins: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origins",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destinations: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route: List[AffectedRouteStructure] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    origin_aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OriginAimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DestinationAimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    calls: Optional["AffectedVehicleJourneyStructure.Calls"] = field(
        default=None,
        metadata={
            "name": "Calls",
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
    class Calls:
        call: List[AffectedCallStructure] = field(
            default_factory=list,
            metadata={
                "name": "Call",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
