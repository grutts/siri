from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractItemStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    CapabilitySubscriptionPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_connection_timetable_service import AbstractFeederItemStructure
from siri.siri_model.siri_interchange_journey_v2_0 import InterchangeJourneyStructure
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_journey_v2_0 import ArrivalPlatformName
from siri.siri_model.siri_model_permissions_v2_0 import (
    ConnectionCapabilityAccessControlStructure,
    ConnectionServicePermissionStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_utility.siri_location_v2_0 import LocationStructure
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConnectingJourneyFilterStructure:
    """
    Type for filter for connecting journeys.

    :ivar dated_vehicle_journey_ref: A reference to a dated VEHICLE
        JOURNEY.
    :ivar visit_number:
    :ivar timetabled_arrival_time: Timetabled arrival time at the
        connection point.
    """

    dated_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
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
    timetabled_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimetabledArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class ConnectingTimeFilterStructure:
    """
    Type for time filter for connecting journeys.

    :ivar line_ref: Feeder LINE for which data is to be supplied.
    :ivar direction_ref: Feeder for which data is to be supplied.
    :ivar earliest_arrival_time: Earliest managed arrival time at the
        connection point.
    :ivar latest_arrival_time: Latest managedarrival time at the
        connection point.
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
            "required": True,
        },
    )
    earliest_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EarliestArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    latest_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


class ConnectionMonitoringDetailEnumeration(Enum):
    """
    Detail Levels for Connection Monitoring Request.

    :cvar MINIMUM: Return only the minimum amount of optional data for
        each Stop Visit to provide a display, A time at stop, LINE name
        and destination name.
    :cvar BASIC: Return minimum and other available basic details for
        each Stop Visit. Do not include data on times at next stop or
        destination.
    :cvar NORMAL: Return all basic data, and also origin VIA points and
        destination.
    :cvar FULL: Return all available data for each Stop Visit, including
        calls.
    """

    MINIMUM = "minimum"
    BASIC = "basic"
    NORMAL = "normal"
    FULL = "full"


@dataclass
class AbstractDistributorItemStructure(AbstractItemStructure):
    """
    Type for an SERVICE JOURNEY INTERCHANGE Activity.

    :ivar interchange_ref: Reference to the SERVICE JOURNEY INTERCHANGE
        between two journeys for which data is being returned.
    :ivar connection_link_ref: Reference to the CONNECTION link or
        ACCESS ZONE for which data is to be returned and at which
        SERVICE JOURNEY INTERCHANGE takes place. A reference associated
        with known feeder arrival and distributor departure STOP POINTs.
    :ivar stop_point_ref: Reference to a STOP POINT within CONNECTION
        link from which distributor leaves. Reference to a STOP POINT.
    :ivar distributor_visit_number: Order of visit to a stop within
        JOURNEY PATTERN of distributor VEHICLE JOURNEY.
    :ivar distributor_order: For implementations for which Order is not
        used for VisitNumber, (i.e. if VisitNumberIsOrder is false) then
        Order can be used to associate the Order as well if useful for
        translation.
    :ivar distributor_journey: Information about the connecting
        Distributor (fetcher) VEHICLE JOURNEY.
    :ivar feeder_vehicle_journey_ref: Reference to a feeder VEHICLE
        JOURNEY or journeys for which the Distributor (fetcher) will
        wait .
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
    distributor_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistributorVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistributorOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_journey: Optional[InterchangeJourneyStructure] = field(
        default=None,
        metadata={
            "name": "DistributorJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    feeder_vehicle_journey_ref: List[FramedVehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "FeederVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ConnectionMonitoringCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Connection Monitoring Service
    Capabilities.

    Answered with a ConnectionMontoringCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionMonitoringCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for Connection Monitoring Capability Request Policy.

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
class ConnectionMonitoringPermissions:
    """
    Participants permissions to use the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    connection_monitoring_permission: List[ConnectionServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringPermission",
            "type": "Element",
        },
    )


@dataclass
class ConnectionMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Request Connection Monitoring Service.

    :ivar preview_interval: Forward duration for which events should be
        included, that is, interval before predicted arrival at the stop
        for which to include events: only journeys which will arrive or
        depart within this time span will be returned.
    :ivar connection_link_ref: CONNECTION LINK for which data is to be
        supplied.
    :ivar connecting_time_filter: Return only journeys for the specified
        time.
    :ivar connecting_journey_filter: Return only the specified journeys.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar connection_monitoring_detail_level: Level of detail to include
        in response. Default is 'normal'.
    :ivar extensions:
    :ivar version: Version number of request. Fixed
    """

    preview_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreviewInterval",
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
    connecting_time_filter: Optional[ConnectingTimeFilterStructure] = field(
        default=None,
        metadata={
            "name": "ConnectingTimeFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_journey_filter: List[ConnectingJourneyFilterStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectingJourneyFilter",
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
    connection_monitoring_detail_level: Optional[ConnectionMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringDetailLevel",
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
class ConnectionMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Connection Monitoring Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["ConnectionMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["ConnectionMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
        :ivar default_preview_interval: Default preview horizon used.
        :ivar filter_by_connection_link_ref:
        :ivar filter_by_journey: Whether results can be filtered by
            journey.
        :ivar filter_by_time: Whether results can be filtered by time
            Filter of Connection. Default is ' true'.
        """

        default_preview_interval: Optional[XmlDuration] = field(
            default=None,
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_connection_link_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByConnectionLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_journey: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByJourney",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_time: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByTime",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class RequestPolicy(CapabilityRequestPolicyStructure):
        """
        :ivar foreign_journeys_only: Whether only foreign journeys are
            included.
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
class MonitoredFeederArrivalCancellationStructure(AbstractFeederItemStructure):
    """
    Type for Deletion of a feeder connection.

    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a DIRECTION, typically outward or
        return.
    :ivar vehicle_journey_ref: Reference to a Feeder VEHICLE JOURNEY.
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
    :ivar reason: Reason for cancellation. (Unbounded since SIRI 2.0)
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
class MonitoredFeederArrivalStructure(AbstractFeederItemStructure):
    """
    Type for Real time connection at a stop.

    :ivar clear_down_ref: Direct Cleardown identifier of connection
        arrival Activity that is being deleted.
    :ivar feeder_journey: Information about the feeder journey.
    :ivar vehicle_at_stop:
    :ivar number_of_transfer_passengers: Number of passengers who wish
        to transfer at the connection. If absent, not known.
    :ivar aimed_arrival_time:
    :ivar expected_arrival_time: Predicted arrival time at the
        connection zone.
    :ivar arrival_platform_name:
    :ivar suggested_wait_decision_time: Latest time by which the feeder
        needs informationabout the connection from the distributor as to
        whether it will wait and for how long. +SIRI v2.0
    :ivar extensions:
    """

    clear_down_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClearDownRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_journey: Optional[InterchangeJourneyStructure] = field(
        default=None,
        metadata={
            "name": "FeederJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    number_of_transfer_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTransferPassengers",
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
    expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalTime",
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
    suggested_wait_decision_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SuggestedWaitDecisionTime",
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
class ConnectionMonitoringRequest(ConnectionMonitoringRequestStructure):
    """
    Request for information about changes to connections at a stop for
    Connection Monitoring service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionMonitoringServiceCapabilities(ConnectionMonitoringServiceCapabilitiesStructure):
    """
    Capabilities of Connection Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DistributorDepartureCancellationStructure(AbstractDistributorItemStructure):
    """
    Type for Cancellation of a Distributor VEHICLE JOURNEY from a connection.

    :ivar reason: Reason for failure of connection.  (Unbounded since
        SIRI 2.0)
    :ivar extensions:
    """

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
class MonitoredFeederArrival(MonitoredFeederArrivalStructure):
    """
    A feeder arrival at the connection point.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class MonitoredFeederArrivalCancellation(MonitoredFeederArrivalCancellationStructure):
    """
    Cancellation of a feeder arrival at a connection point.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StoppingPositionChangedDepartureStructure(AbstractDistributorItemStructure):
    """
    Type for Change to a Distributor stop position.

    :ivar change_note: Description of the revised stopping position of
        the Distributor (fetcher) in the connection zone.  (Unbounded
        since SIRI 2.0)
    :ivar new_location: New location from which Distributor will leave.
    :ivar extensions:
    """

    change_note: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "ChangeNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    new_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "NewLocation",
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
class WaitProlongedDepartureStructure(AbstractDistributorItemStructure):
    """
    Type for Distributor prolonged wait action.

    :ivar expected_departure_time: Estimated departure time from the
        connection.
    :ivar extensions:
    """

    expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTime",
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
class ConnectionMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Connection Monitoring Capability.

    :ivar connection_monitoring_service_capabilities:
    :ivar connection_monitoring_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    connection_monitoring_service_capabilities: Optional[ConnectionMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_permissions: Optional[ConnectionMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringPermissions",
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
class ConnectionMonitoringDistributorDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Type for Distributor Delivery for Connection Monitoring Service.

    :ivar wait_prolonged_departure: An action to delay the Distributor
        (fetcher) until a specified time.
    :ivar stopping_position_changed_departure: A Change to a stop
        position.
    :ivar distributor_departure_cancellation: Deletion of previous
        connection.
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    wait_prolonged_departure: List[WaitProlongedDepartureStructure] = field(
        default_factory=list,
        metadata={
            "name": "WaitProlongedDeparture",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stopping_position_changed_departure: List[StoppingPositionChangedDepartureStructure] = field(
        default_factory=list,
        metadata={
            "name": "StoppingPositionChangedDeparture",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_departure_cancellation: List[DistributorDepartureCancellationStructure] = field(
        default_factory=list,
        metadata={
            "name": "DistributorDepartureCancellation",
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
class ConnectionMonitoringFeederDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Type for Delivery for Connection Monitoring.

    :ivar monitored_feeder_arrival:
    :ivar monitored_feeder_arrival_cancellation:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    monitored_feeder_arrival: List[MonitoredFeederArrival] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredFeederArrival",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_feeder_arrival_cancellation: List[MonitoredFeederArrivalCancellation] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredFeederArrivalCancellation",
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
class ConnectionMonitoringSubscriptionRequestStructure(AbstractSubscriptionStructure):
    """
    Subscription Request for Connection Monitoring.

    :ivar connection_monitoring_request:
    :ivar change_before_updates: The amount of change to the arrival
        time that can happen before an update is sent (i.e. if
        ChangeBeforeUpdate is set to 2 minutes, the subscriber will not
        be told that a bus is 30 seconds delayed - an update will only
        be sent when the bus is at least 2 minutes delayed). Default is
        zero - all changes will be sent regardless.
    :ivar extensions:
    """

    connection_monitoring_request: Optional[ConnectionMonitoringRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
class ConnectionMonitoringCapabilitiesResponse(ConnectionMonitoringCapabilitiesResponseStructure):
    """Capabilities for Connection Monitoring Service.

    Answers a ConnectionMontoringCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionMonitoringDistributorDelivery(ConnectionMonitoringDistributorDeliveryStructure):
    """
    Distributor Delivery for Connection Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionMonitoringFeederDelivery(ConnectionMonitoringFeederDeliveryStructure):
    """
    Feeder Delivery for Connection Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionMonitoringSubscriptionRequest(ConnectionMonitoringSubscriptionRequestStructure):
    """
    Request for a subscription to Connection Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionMonitoringDeliveriesStructure:
    """Type for Deliveries for Connection Monitoring Service.

    Used in WSDL.

    :ivar connection_monitoring_feeder_delivery: Delivery for Connection
        Protection Feeder Service.
    :ivar connection_monitoring_distributor_delivery: Delivery for
        Connection Protection Distributor i.e. Fetcher Service.
    """

    connection_monitoring_feeder_delivery: List[ConnectionMonitoringFeederDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringFeederDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_distributor_delivery: List[ConnectionMonitoringDistributorDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringDistributorDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
