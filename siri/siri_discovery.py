from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from siri.siri.siri_requests_v2_0 import (
    AbstractDiscoveryDeliveryStructure,
    AbstractDiscoveryRequestStructure,
)
from siri.siri_model.siri_facility_v2_0 import AnnotatedFacilityStructure
from siri.siri_model.siri_reference_v2_0 import LineDirectionStructure
from siri.siri_model_discovery.siri_connection_link_v2_0 import AnnotatedConnectionLinkRef
from siri.siri_model_discovery.siri_feature_v2_0 import (
    ProductCategory,
    ServiceFeature,
    VehicleFeature,
)
from siri.siri_model_discovery.siri_info_channel_v2_0 import InfoChannel
from siri.siri_model_discovery.siri_line_v2_0 import AnnotatedLineRef
from siri.siri_model_discovery.siri_stop_point_v2_0 import AnnotatedStopPointRef
from siri.siri_utility.siri_location_v2_0 import (
    BoundingBoxStructure,
    LocationStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ConnectionLinksDetailEnumeration(Enum):
    """Detail Levels for CONNECTION LINKs Discovery Request.

    +SIRI v2.0

    :cvar MINIMUM: Return only the name and identifier of the connection
        link.
    :cvar NORMAL: Return name, identifier of the connection link and
        connected stops's identifiers.
    :cvar FULL: Return all available data for each connection link.
    """

    MINIMUM = "minimum"
    NORMAL = "normal"
    FULL = "full"


class FacilityDetailEnumeration(Enum):
    """Detail Levels for Facility Points Request.

    +SIRI v2.0

    :cvar MINIMUM: Return only the name and identifier of the Facility.
    :cvar NORMAL: Return name, identifier and coordinates of the
        Facility.
    :cvar FULL: Return all available data for each Facility.
    """

    MINIMUM = "minimum"
    NORMAL = "normal"
    FULL = "full"


class LinesDetailEnumeration(Enum):
    """Detail Levels for Lines Discovery Request.

    +SIRI v2.0

    :cvar MINIMUM: Return only the name and identifier of the stop.
    :cvar NORMAL: Return name, dientifier and coordinates of the stop.
    :cvar STOPS:
    :cvar FULL: Return all available data for each stop.
    """

    MINIMUM = "minimum"
    NORMAL = "normal"
    STOPS = "stops"
    FULL = "full"


class StopPointsDetailEnumeration(Enum):
    """Detail Levels for Stop Points Discovery Request.

    +SIRI v2.0

    :cvar MINIMUM: Return only the name and identifier of the stop.
    :cvar NORMAL: Return name, dientifier and coordinates of the stop.
    :cvar FULL: Return all available data for each stop.
    """

    MINIMUM = "minimum"
    NORMAL = "normal"
    FULL = "full"


@dataclass
class ConnectionLinksDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """Response with CONNECTION LINKs available to make requests.

    +SIR v2.0

    :ivar annotated_connection_link_ref:
    :ivar extensions:
    :ivar version: Version number of response. Fixed.
    """

    annotated_connection_link_ref: List[AnnotatedConnectionLinkRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotatedConnectionLinkRef",
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
    version: str = field(
        init=False,
        default="2.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ConnectionLinksDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    """Requests for CONNECTION LINK data for use in service requests.

    +SIRI v2.0

    :ivar bounding_box: Rectangle containing stops of ConnectionLinks be
        returned.
    :ivar circle: Circle containing stops for ConnectionLinks  be
        returned. Point indicates centre, precision indicates radius
    :ivar place_ref: Filter the results to include only ConnectionLinks
        for stops assoicated with  the place .
    :ivar line_ref: Filter the results to include only ConnectionLinks
        for stops assoicated with the specified line.
    :ivar operator_ref: Filter the results to include only Stop d run by
        the specified OPERATOR.
    :ivar language: Preferred language in which to return text values.
        +SIRI v2.0
    :ivar connection_links_detail_level: Level of detail to include in
        response. Default is 'normal'. +SIRI v2.0
    :ivar version: Version number of request. Fixed
    """

    bounding_box: Optional[BoundingBoxStructure] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    circle: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Circle",
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
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_links_detail_level: Optional[ConnectionLinksDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionLinksDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        init=False,
        default="2.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class FacilityDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Response with Facilities available to make requests.

    :ivar annotated_facility: Facility Definition.
    :ivar extensions:
    :ivar version: Version number of response. Fixed.
    """

    annotated_facility: List[AnnotatedFacilityStructure] = field(
        default_factory=list,
        metadata={
            "name": "AnnotatedFacility",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FacilityRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Requests for info channels for use in service requests.

    :ivar bounding_box: Rectangle containing Facilities  be returned.
        (+SIRI v2.0)
    :ivar place_ref: Filter the results to include only Facilities
        associated with  the TOPOGRAPHIC PLACE . (+SIRI v2.0)
    :ivar operator_ref: Filter the results to include only Facilities
        run by the specified OPERATOR.  (+SIRI v2.0)
    :ivar line_ref: Filter the results to include only Facilities for
        the given LINE. (+SIRI v2.0)
    :ivar language: Preferred language in which to return text values.
        +SIRI v2.0
    :ivar facility_detail_level: Level of detail to include in response.
        Default is 'normal'. +SIRI v2.0
    :ivar version: Version number of request. Fixed
    """

    bounding_box: Optional[BoundingBoxStructure] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
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
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
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
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_detail_level: Optional[FacilityDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "FacilityDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InfoChannelDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Type for Response with Info channels categories available to make requests.

    :ivar info_channel:
    :ivar extensions:
    :ivar version: Version number of response. Fixed.
    """

    info_channel: List[InfoChannel] = field(
        default_factory=list,
        metadata={
            "name": "InfoChannel",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InfoChannelDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Requests for info channels for use in service requests.

    :ivar version: Version number of request. Fixed
    """

    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LinesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Response with LINEs available to make requests.

    :ivar annotated_line_ref:
    :ivar extensions:
    :ivar version: Version number of response. Fixed.
    """

    annotated_line_ref: List[AnnotatedLineRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotatedLineRef",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LinesDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Requests for LINE data for use in service requests.

    :ivar bounding_box: Rectangle containing stops of lines be returned.
        (+SIRI v2.0)
    :ivar circle: Circle containing stops for lines  be returned. Point
        indicates centre, precision indicates radius (+SIRI v2.0)
    :ivar place_ref: Filter the results to include only lines for  stops
        assoicated with  the place . (+SIRI v2.0)
    :ivar line_direction_ref: Reference to line for which details are to
        be returned (v2.0)
    :ivar operator_ref: Filter the results to include only Stop d run by
        the specified OPERATOR.  (+SIRI v2.0)
    :ivar language: Preferred language in which to return text values.
        +SIRI v2.0
    :ivar lines_detail_level: Level of detail to include in response.
        Default is 'normal'. +SIRI v2.0
    :ivar version: Version number of request. Fixed
    """

    bounding_box: Optional[BoundingBoxStructure] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    circle: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Circle",
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
    line_direction_ref: Optional[LineDirectionStructure] = field(
        default=None,
        metadata={
            "name": "LineDirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines_detail_level: Optional[LinesDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "LinesDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ProductCategoriesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Type for Response with Product Categories available to make requests.

    :ivar product_category:
    :ivar extensions:
    :ivar version: Version number of response. Fixed.
    """

    product_category: List[ProductCategory] = field(
        default_factory=list,
        metadata={
            "name": "ProductCategory",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ProductCategoriesDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Requests for TYPE OF PRODUCT CATEGORY reference data for use in service
    requests.

    :ivar language: Preferred language in which to return text values.
        +SIRI v2.0
    :ivar version: Version number of request. Fixed
    """

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ServiceFeaturesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Type for Response with SERVICE FEATUREs available to make requests.

    :ivar service_feature:
    :ivar version: Version number of response. Fixed.
    """

    service_feature: List[ServiceFeature] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ServiceFeaturesDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Type for equests for TYPE OF PRODUCT CATEGORY reference data for use in
    service requests.

    :ivar version: Version number of request. Fixed
    """

    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StopPointsDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Response with STOP POINTs available to make requests.

    :ivar annotated_stop_point_ref:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    annotated_stop_point_ref: List[AnnotatedStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotatedStopPointRef",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StopPointsDiscoveryRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Requests for stop reference data for use in service requests.

    :ivar bounding_box: Rectangle containing stops  be returned. (+SIRI
        v2.0)
    :ivar circle: Circle containing stops  be returned. Point indicates
        centre, precision indicates radius (+SIRI v2.0)
    :ivar place_ref: Filter the results to include only stops associated
        with  the PLACE . (+SIRI v2.0)
    :ivar operator_ref: Filter the results to include only stops run by
        the specified OPERATOR.  (+SIRI v2.0)
    :ivar line_ref: Filter the results to include only stops for the
        given LINE. (+SIRI v2.0)
    :ivar language: Preferred language in which to return text values.
        +SIRI v2.0
    :ivar stop_points_detail_level: Level of detail to include in
        response. Default is 'normal'. +SIRI v2.0
    :ivar version: Version number of request. Fixed
    """

    bounding_box: Optional[BoundingBoxStructure] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    circle: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Circle",
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
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
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
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points_detail_level: Optional[StopPointsDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPointsDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VehicleFeaturesDeliveryStructure(AbstractDiscoveryDeliveryStructure):
    """
    Type for Response with Vehicle Features available to make requests.

    :ivar vehicle_feature:
    :ivar extensions:
    :ivar version: Version number of response. Fixed.
    """

    vehicle_feature: List[VehicleFeature] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeature",
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VehicleFeaturesRequestStructure(AbstractDiscoveryRequestStructure):
    """
    Requests for VEHICLE feature data for use in service requests.

    :ivar language: Preferred language in which to return text values.
        +SIRI v2.0
    :ivar version: Version number of request. Fixed
    """

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ConnectionLinksDelivery(ConnectionLinksDeliveryStructure):
    """Returns the CONNECTION LINKs covered by a web service.

    Answers a LINEsRequest. +Siri v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionLinksRequest(ConnectionLinksDiscoveryRequestStructure):
    """Requests a list of the CONNECTION LINKs covered by a Producer.

    +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityDelivery(FacilityDeliveryStructure):
    """Returns the Facilities covered by a service.

    Answers a StopPointsRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityRequest(FacilityRequestStructure):
    """
    Requests a list of the Facilities covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class InfoChannelDelivery(InfoChannelDeliveryStructure):
    """Returns the Info Channels covered by a service.

    Answers a InfoChannelRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class InfoChannelRequest(InfoChannelDiscoveryRequestStructure):
    """
    Requests a list of the Info Channels covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class LinesDelivery(LinesDeliveryStructure):
    """Returns the LINEs covered by a web service.

    Answers a LINEsRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class LinesRequest(LinesDiscoveryRequestStructure):
    """
    Requests a list of the LINEs covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductCategoriesDelivery(ProductCategoriesDeliveryStructure):
    """Returns the Product Categories covered by a service.

    Answers a ProductCategoriesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductCategoriesRequest(ProductCategoriesDiscoveryRequestStructure):
    """
    Requests a list of the Product Categories covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeaturesDelivery(ServiceFeaturesDeliveryStructure):
    """Returns the SERVICE FEATUREs covered by a service.

    Answers a ServiceFeaturesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeaturesRequest(ServiceFeaturesDiscoveryRequestStructure):
    """
    Requests a list of the Service Features covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopPointsDelivery(StopPointsDeliveryStructure):
    """Returns basic details about the  STOP POINTs/places covered by a
    service.

    Answers a StopPointsRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopPointsRequest(StopPointsDiscoveryRequestStructure):
    """
    Requests a list of the STOP POINTs and places covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleFeaturesDelivery(VehicleFeaturesDeliveryStructure):
    """Returns the Vehicle Features covered by a service.

    Answers a VehicleFeaturesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleFeaturesRequest(VehicleFeaturesRequestStructure):
    """
    Requests a list of the Vehicle Features covered by a Producer.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
