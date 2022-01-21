from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class FeatureRefStructure:
    """
    Type for reference to a FEATURE.

    :ivar feature_id_ref: Unique identfiier of referenced element, eg
        TOId.
    :ivar feature_type: Type for identifier of FEATURE.
    """

    feature_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeatureIdRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        },
    )
    feature_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )


@dataclass
class AbstractProjection:
    """
    :ivar features: GIS Features that this element projects onto.
    """

    features: Optional["AbstractProjection.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class Features:
        """
        :ivar gis_feature_ref: Identifier of FEATURE in a GIS data
            system.
        """

        gis_feature_ref: List[FeatureRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "GisFeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 1,
            },
        )


@dataclass
class PointProjectionStructure(AbstractProjection):
    """Type for geospatial Position of a point.

    May be expressed in concrete WGS 84 Coordinates or any GML
    compatible point coordinates format.

    :ivar longitude: Longitude from Greenwich Meridian. -180° (East) to
        +180° (West).
    :ivar latitude: Latitude from equator. -90° (South) to +90° (North).
    :ivar altitude: Altitude.
    :ivar coordinates: Coordinates of points in a GML compatible format,
        as indicated by srsName attribute.
    :ivar precision: Precision for point measurement. In meters.
    :ivar id: Identifier of POINT.
    :ivar srs_name: identifier of data reference system for geocodes, if
        point is specified as GML compatible Coordinates. A GML value.
        If not specified taken from system configuration.
    """

    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    altitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_inclusive": Decimal("-1000"),
            "max_inclusive": Decimal("5000"),
        },
    )
    coordinates: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "tokens": True,
        },
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )


@dataclass
class PointProjection(PointProjectionStructure):
    """
    Points may be defined in tagged format or using GM coordinates element.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"


@dataclass
class LinkProjectionStructure(AbstractProjection):
    """
    Type for PROJECTION as a geospatial polyline.

    :ivar line: Ordered sequence of points. There must always be a start
        and end point.
    """

    line: Optional["LinkProjectionStructure.Line"] = field(
        default=None,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class Line:
        point_projection: List[PointProjection] = field(
            default_factory=list,
            metadata={
                "name": "PointProjection",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 2,
            },
        )


@dataclass
class ZoneProjectionStructure(AbstractProjection):
    """
    Type for PROJECTION as a geospatial zone.

    :ivar boundary: Boundary line of Zone as an ordered set of points.
    """

    boundary: List["ZoneProjectionStructure.Boundary"] = field(
        default_factory=list,
        metadata={
            "name": "Boundary",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )

    @dataclass
    class Boundary:
        point_projection: List[PointProjection] = field(
            default_factory=list,
            metadata={
                "name": "PointProjection",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 3,
            },
        )


@dataclass
class LinkProjection(LinkProjectionStructure):
    """
    Projection as a geospatial polyline.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"


@dataclass
class ZoneProjection(ZoneProjectionStructure):
    """
    PROJECTION onto a geospatial zone.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
