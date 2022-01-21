from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LocationStructure:
    """Type for gepspatial Position of a point.

    May be expressed in concrete WGS 84 Coordinates or any gml
    compatible point coordinates format.

    :ivar longitude: Longitude from Greenwich Meridian. -180 (East) to
        +180 (West). Decimal degrees. eg 2.356
    :ivar latitude: Latitude from equator. -90 (South) to +90 (North).
        Decimal degrees. eg 56.356
    :ivar coordinates: Coordinates of points in a GML compatibe format,
        as indicated by srsName attribute.
    :ivar precision: Precision for point measurement. In meters.
    :ivar id: Identifier of POINT.
    :ivar srs_name: identifier of data reference system for geocodes if
        point is specified as gml compatible Coordinates. A gml value.
        If not specified taken from system configuration.
    """

    longitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("-180"),
            "max_inclusive": Decimal("180"),
        },
    )
    latitude: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("-90"),
            "max_inclusive": Decimal("90"),
        },
    )
    coordinates: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    precision: Optional[int] = field(
        default=None,
        metadata={
            "name": "Precision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
class SrsName:
    """
    GML Spatial coordinate reference system.
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
class BoundingBoxStructure:
    """Defines a bounding box using two corner points.

    GML terminology.  +SIRI v2.0

    :ivar upper_left: A geospatial point. Upper Left corner. .
    :ivar lower_right: A geospatial point. Lower right corner. .
    """

    upper_left: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    lower_right: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class LineShapeStructure:
    """
    Defines a line shape +SIRI v2.0.

    :ivar point: A geospatial point. +SIRI v2.0 .
    """

    point: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 2,
        },
    )
