from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractIdentifiedItemStructure,
    AbstractReferencingItemStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    CapabilitySubscriptionPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_model.siri_interchange_journey_v2_0 import InterchangeJourneyStructure
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_model_permissions_v2_0 import (
    ConnectionCapabilityAccessControlStructure,
    ConnectionServicePermissionStructure,
    PermissionsStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    StopPointName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_time_v1_2 import ClosedTimestampRangeStructure
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFeederItemStructure(AbstractIdentifiedItemStructure):
    """
    Type for an SERVICE JOURNEY INTERCHANGE feeder Activity.

    :ivar valid_until_time: Time until when data is valid. +SIRI 2.0
    :ivar interchange_ref: Reference to the the SERVICE JOURNEY
        INTERCHANGE between two journeys for which data is being
        returned.
    :ivar connection_link_ref: Reference to the CONNECTION link or
        ACCESS  ZONE for which data is to be returned. i.e. associated
        with known feeder arrival and distributor departure STOP POINTs.
    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    """

    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ConnectionTimetableCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Connection Timetable Service Capabilities.

    Answered with a ConnectionTimetableCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionTimetableCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for capability request.

    :ivar foreign_journeys_only: Whether results returns foreign
        journeys only.
    """

    foreign_journeys_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForeignJourneysOnly",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ConnectionTimetableRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Request for Connection Timetable Service.

    :ivar arrival_window: Earliest and latest time. If absent, default
        to the data horizon of the service.
    :ivar connection_link_ref: CONNECTION link for which data is to be
        supplied.
    :ivar line_ref: Feeder LINE for which data is to be supplied.
    :ivar direction_ref: Feeder DIRECTION for which data is to be
        supplied.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar extensions:
    :ivar version: Version number of request. Fixed
    """

    arrival_window: Optional[ClosedTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "ArrivalWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
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
    include_translations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
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
class ConnectionTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Connection Timetable Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["ConnectionTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["ConnectionTimetableServiceCapabilitiesStructure.RequestPolicy"] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_policy: Optional[CapabilitySubscriptionPolicyStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_control: Optional[ConnectionCapabilityAccessControlStructure] = field(
        default=None,
        metadata={
            "name": "AccessControl",
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
    class TopicFiltering:
        """
        :ivar filter_by_line_ref:
        :ivar filter_by_connection_link_ref: Whether results can be
            filtered by Connection link. Default is ' true'.
        """

        filter_by_line_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_connection_link_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByConnectionLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )

    @dataclass
    class RequestPolicy(CapabilityRequestPolicyStructure):
        """
        :ivar foreign_journeys_only: Whether service returns only
            foreign journeys. Default is 'false'.
        """

        foreign_journeys_only: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ForeignJourneysOnly",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class TimetabledFeederArrivalCancellationStructure(AbstractReferencingItemStructure):
    """
    Type for Timetabled Deletion of a feeder connection.

    :ivar interchange_ref: Reference to the the SERVICE JOURNEY
        INTERCHANGE between two journeys for which data is being
        returned.
    :ivar connection_link_ref: Reference to the CONNECTION link or
        ACCESS  ZONE for which data is to be returned. i.e. associated
        with known feeder arrival and distributor departure STOP POINTs.
    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a DIRECTION, typically outward or
        return.
    :ivar vehicle_journey_ref: Reference to a VEHICLE JOURNEY.
    :ivar journey_pattern_ref: Identifier of JOURNEY PATTERN that
        journey follows.
    :ivar journey_pattern_name: Name of Joruney Pattern
    :ivar vehicle_mode: A means of transportation such as bus, rail,
        etc.
    :ivar route_ref: Identifier of ROUTE that journey follows.
    :ivar published_line_name: Name or Number by which the LINE is known
        to the public.  (Unbounded since SIRI 2.0)
    :ivar group_of_lines_ref: Reference to a GROUP OF LINEs to which
        journey belongs. SIRI 2.0
    :ivar direction_name: Description of the DIRECTION. May correspond
        to a DESTINATION DISPLAY.  (Unbounded since SIRI 2.0)
    :ivar external_line_ref: Alternative identifier of LINE that an
        external system may associate with journey.
    :ivar reason: Reason for deletion.  (Unbounded since SIRI 2.0)
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
    connection_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
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
            "required": True,
        },
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    journey_pattern_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_pattern_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: List[VehicleModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    published_line_name: List[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_of_lines_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Reason",
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
class ConnectionTimetableRequest(ConnectionTimetableRequestStructure):
    """
    Request for information about timetabled connections at a stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionTimetableServiceCapabilities(ConnectionTimetableServiceCapabilitiesStructure):
    """
    Capabilities of Connection Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class TimetabledFeederArrivalCancellation(TimetabledFeederArrivalCancellationStructure):
    """
    Cancellation of a previously issued Feeder Arrival.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class TimetabledFeederArrivalStructure(AbstractFeederItemStructure):
    """
    Type for incoming visit by feeder journey to SERVICE JOURNEY NTERCHANGE.

    :ivar feeder_journey: Information about the feeder journey.
    :ivar aimed_arrival_time: Planned arrival time at the connection
        point.
    :ivar extensions:
    """

    feeder_journey: Optional[InterchangeJourneyStructure] = field(
        default=None,
        metadata={
            "name": "FeederJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
class ConnectionTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Connection TimetableService.

    :ivar connection_timetable_service_capabilities:
    :ivar connection_timetable_permissions: Participant's permissions to
        use the service, Only returned if requested.
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    connection_timetable_service_capabilities: Optional[ConnectionTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_permissions: Optional[
        "ConnectionTimetableCapabilitiesResponseStructure.ConnectionTimetablePermissions"
    ] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetablePermissions",
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
    class ConnectionTimetablePermissions(PermissionsStructure):
        """
        :ivar connection_timetable_permission: Permission for a single
            participant or all participants to use an aspect of the
            service.
        """

        connection_timetable_permission: List[ConnectionServicePermissionStructure] = field(
            default_factory=list,
            metadata={
                "name": "ConnectionTimetablePermission",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class ConnectionTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Type for Subscription Request for Connection Protection.
    """

    connection_timetable_request: Optional[ConnectionTimetableRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
class TimetabledFeederArrival(TimetabledFeederArrivalStructure):
    """
    A feeder arrival at the arrival SCHEDUELD STOP POINT of the CONNECTION link
    .
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionTimetableCapabilitiesResponse(ConnectionTimetableCapabilitiesResponseStructure):
    """Capabilities for Connection Timetable Service.

    Answers a ConnectionTimetableCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionTimetableDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Type for Delivery for Connection Protection.

    :ivar timetabled_feeder_arrival:
    :ivar timetabled_feeder_arrival_cancellation:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    timetabled_feeder_arrival: List[TimetabledFeederArrival] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledFeederArrival",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timetabled_feeder_arrival_cancellation: List[TimetabledFeederArrivalCancellation] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledFeederArrivalCancellation",
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
class ConnectionTimetableSubscriptionRequest(ConnectionTimetableSubscriptionStructure):
    """
    Subscription Request for information about Timetabled connections at a
    stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionTimetableDelivery(ConnectionTimetableDeliveryStructure):
    """
    Delivery for Connection Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionTimetableDeliveriesStructure:
    """Type for Deliveries for Connection Timetable Service.

    Used in WSDl.
    """

    connection_timetable_delivery: Optional[ConnectionTimetableDelivery] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
