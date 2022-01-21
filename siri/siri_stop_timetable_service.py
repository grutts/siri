from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractIdentifiedItemStructure,
    AbstractReferencingItemStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_model_permissions_v2_0 import (
    LinePermissions,
    OperatorPermissions,
    PermissionsStructure,
    StopMonitorPermissionStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_targeted_vehicle_journey_v2_0 import TargetedVehicleJourney
from siri.siri_model.siri_time_v1_2 import ClosedTimestampRangeStructure
from siri.siri_utility.siri_permissions_v2_0 import (
    AbstractPermissionStructure,
    CapabilityAccessControlStructure,
)
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopTimetableCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """
    Request for information about Stop Timetable Service Capabilities Answered
    with a StopTimetableCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopTimetableCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for Monitoring Service Capability Request Policy.

    :ivar use_references: Whether results can return references for
        stops. Default is 'true'.
    :ivar use_names: Whether results can return names for stop.
    """

    use_references: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReferences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    use_names: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseNames",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class StopTimetableRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Stop Timetables.

    :ivar departure_window: Earliest and latest departure time. If
        absent, default to the data horizon of the service.
    :ivar monitoring_ref: The stop monitoring point about which data is
        requested. May be a STOP POINT, timing point or other display
        point.
    :ivar line_ref: Filter the results to include only data for journeys
        for the given LINE.
    :ivar direction_ref: Filter the results to include only data for
        journeys running in a specific relative DIRECTION, for example,
        "inbound" or "outbound".
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar extensions:
    :ivar version: Version number of request. Fixed
    """

    departure_window: Optional[ClosedTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "DepartureWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
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
class StopTimetableServicePermissionStructure(AbstractPermissionStructure):
    """
    Type for Monitoring Service Permission.

    :ivar operator_permissions:
    :ivar line_permissions:
    :ivar stop_monitor_permissions: The monitoring points that the
        participant may access.
    :ivar extensions:
    """

    operator_permissions: Optional[OperatorPermissions] = field(
        default=None,
        metadata={
            "name": "OperatorPermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    line_permissions: Optional[LinePermissions] = field(
        default=None,
        metadata={
            "name": "LinePermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    stop_monitor_permissions: Optional["StopTimetableServicePermissionStructure.StopMonitorPermissions"] = field(
        default=None,
        metadata={
            "name": "StopMonitorPermissions",
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
    class StopMonitorPermissions:
        """
        :ivar allow_all:
        :ivar stop_monitor_permission: Participant's permission for this
            Monitoring Point (LOGICAL DISPLAY)
        """

        allow_all: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AllowAll",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        stop_monitor_permission: List[StopMonitorPermissionStructure] = field(
            default_factory=list,
            metadata={
                "name": "StopMonitorPermission",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class TimetabledStopVisitCancellationStructure(AbstractReferencingItemStructure):
    """Type for Cancellation of Timetabled Visit of a VEHICLE to a stop.

    May provide information about the arrival, the departure or both.

    :ivar monitoring_ref: Reference to a stop monitoring point to which
        Stop Visit applies.
    :ivar visit_number:
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a DIRECTION, typically outward or
        return.
    :ivar framed_vehicle_journey_ref: A reference to the dated VEHICLE
        JOURNEY that the VEHICLE is making.
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
    :ivar reason: Reason for cancellation.  (Unbounded since SIRI 2.0)
    :ivar extensions:
    """

    monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
class TimetabledStopVisitStructure(AbstractIdentifiedItemStructure):
    """Type for Timetabled Visit of a VEHICLE to a stop.

    May provide information about the arrival, the departure or both.

    :ivar monitoring_ref: Reference to a  stop monitoring point /
        LOGICAL DISPLAY to which Stop Visit applies.
    :ivar targeted_vehicle_journey:
    :ivar extensions:
    """

    monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    targeted_vehicle_journey: Optional[TargetedVehicleJourney] = field(
        default=None,
        metadata={
            "name": "TargetedVehicleJourney",
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
class StopTimetableDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Data type Delivery for Stop Timetable Service.

    :ivar timetabled_stop_visit: A visit to a stop by a VEHICLE as an
        arrival and /or departure, as timetabled in the production
        timetable.
    :ivar timetabled_stop_visit_cancellation: A cancellation of a
        previously issued TimetabledStopVisit.
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    timetabled_stop_visit: List[TimetabledStopVisitStructure] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledStopVisit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timetabled_stop_visit_cancellation: List[TimetabledStopVisitCancellationStructure] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledStopVisitCancellation",
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
class StopTimetablePermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.

    :ivar stop_timetable_permission: Permission for a single participant
        or all participants to use an aspect of the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    stop_timetable_permission: List[StopTimetableServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetablePermission",
            "type": "Element",
        },
    )


@dataclass
class StopTimetableRequest(StopTimetableRequestStructure):
    """
    Request for information about Stop Visits, i.e. arrival and departure at a
    stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Capabilities of Stop Timetable Service.

    :ivar topic_filtering: Available Filtering Capabilities.
    :ivar request_policy: Available request policy options.
    :ivar access_control: Access control that can be used.
    :ivar extensions:
    """

    topic_filtering: Optional["StopTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional[StopTimetableCapabilityRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_control: Optional["StopTimetableServiceCapabilitiesStructure.AccessControl"] = field(
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
        filter_by_monitoring_ref: bool = field(
            init=False,
            default=True,
            metadata={
                "name": "FilterByMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_line_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_direction_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByDirectionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class AccessControl(CapabilityAccessControlStructure):
        check_operator_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "CheckOperatorRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        check_line_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "CheckLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        check_monitoring_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "CheckMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class StopTimetableDelivery(StopTimetableDeliveryStructure):
    """
    Delivery for Stop Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopTimetableServiceCapabilities(StopTimetableServiceCapabilitiesStructure):
    """
    Capabilities of Stop Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Subscription Request for Stop Timetables.

    :ivar stop_timetable_request:
    :ivar incremental_updates: Whether the producer should return the
        complete set of current data, or only provide updates to the
        last data returned, i.e. additions, modifications and deletions.
        If false each subscription response will contain the full
        information as specified in this request.
    :ivar change_before_updates: The amount of change to the arrival or
        departure time that can happen before an update is sent (i.e. if
        ChangeBeforeUpdate is set to 2 minutes, the subscriber will not
        be told that a bus is 30 seconds delayed - an update will only
        be sent when the bus is at least 2 minutes delayed). Default is
        zero - all changes will be sent regardless.
    :ivar extensions:
    """

    stop_timetable_request: Optional[StopTimetableRequest] = field(
        default=None,
        metadata={
            "name": "StopTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    change_before_updates: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ChangeBeforeUpdates",
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
class StopTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Stop Timetable Service.

    :ivar stop_timetable_service_capabilities:
    :ivar stop_timetable_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    stop_timetable_service_capabilities: Optional[StopTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "StopTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_permissions: Optional[StopTimetablePermissions] = field(
        default=None,
        metadata={
            "name": "StopTimetablePermissions",
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
class StopTimetableDeliveriesStructure:
    """Type for stop timetable deliveries.

    Used in WSDL.
    """

    stop_timetable_delivery: Optional[StopTimetableDelivery] = field(
        default=None,
        metadata={
            "name": "StopTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class StopTimetableSubscriptionRequest(StopTimetableSubscriptionStructure):
    """
    Request for a subscription to Stop TimetablesService.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopTimetableCapabilitiesResponse(StopTimetableCapabilitiesResponseStructure):
    """Delivery for Stop Timetable Service.

    Answers a StopTimetableCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
