from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
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
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_journey_v2_0 import ProgressBetweenStopsStructure
from siri.siri_model.siri_model_permissions_v2_0 import (
    LinePermissions,
    OperatorPermissions,
    PermissionsStructure,
)
from siri.siri_model.siri_monitored_vehicle_journey_v2_0 import MonitoredVehicleJourneyStructure
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_utility.siri_permissions_v2_0 import (
    AbstractPermissionStructure,
    AbstractTopicPermissionStructure,
    CapabilityAccessControlStructure,
)
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleMonitoringDetailEnumeration(Enum):
    """
    Detail Levels for Request.

    :cvar MINIMUM: Return only the minimum amount of optional data for
        each stop event to provide a display, A time, line name and
        destination name.
    :cvar BASIC: Return minimum and other available basic details for
        each stop event. Do not include data on time at next stop or
        destination.
    :cvar NORMAL: Return all basic data, and also arrival times at
        DESTINATION.
    :cvar CALLS: Return all available data for each stop event,
        including previous and onward  CALLs with  passing times for
        JOURNEY PATTERN.
    """

    MINIMUM = "minimum"
    BASIC = "basic"
    NORMAL = "normal"
    CALLS = "calls"


@dataclass
class VehicleActivityCancellationStructure(AbstractReferencingItemStructure):
    """
    Type for cancellation of an earlier Vehicle Activity.

    :ivar vehicle_monitoring_ref:
    :ivar vehicle_journey_ref: Reference to VEHICLE JOURNEY that VEHICLE
        is making.
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a LINE DIRECTION DIRECTION,
        typically outward or return.
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

    vehicle_monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
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
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
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
class VehicleActivityStructure(AbstractIdentifiedItemStructure):
    """
    Type for a Vehicle Activity.

    :ivar valid_until_time: Time until when data is valid.
    :ivar vehicle_monitoring_ref: Reference to monitored VEHICLE or
        GROUP OF VEHICLEs.
    :ivar monitoring_name: Name associated with Monitoring Reference.
        Supports SIRI LITE servcies  (+SIRI v2.0).
    :ivar progress_between_stops: Provides information about the
        progress of the VEHICLE along its current link, that is link
        from previous visited top to current position.
    :ivar monitored_vehicle_journey: Monitored VEHICLE JOURNEY that
        VEHICLE is following.
    :ivar vehicle_activity_note: Text associated with Delivery.
    :ivar extensions:
    """

    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    vehicle_monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_between_stops: Optional[ProgressBetweenStopsStructure] = field(
        default=None,
        metadata={
            "name": "ProgressBetweenStops",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_vehicle_journey: Optional[MonitoredVehicleJourneyStructure] = field(
        default=None,
        metadata={
            "name": "MonitoredVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    vehicle_activity_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivityNote",
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
class VehicleMonitorPermissionStructure(AbstractTopicPermissionStructure):
    """
    Type for MonitoringPoint Permission.

    :ivar vehicle_monitoring_ref: Vehicle Monitoring reference for which
        permission is made.
    """

    vehicle_monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class VehicleMonitoringCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Vehicle Monitoring Service Capabilities.

    Answered with a VehicleMontoringCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMonitoringCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for capability request policy.

    :ivar has_references: Whether results should return references.
    :ivar has_names: Whether results should return references.
    """

    has_references: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasReferences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_names: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasNames",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class VehicleMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Vehicle Monitoring Service.

    :ivar vehicle_monitoring_ref: A predefined scope for making VEHICLE
        requests.
    :ivar vehicle_ref: Reference to a specific VEHICLE about which data
        is requested.
    :ivar line_ref: Filter the results to include only vehicles for the
        specific LINE.
    :ivar direction_ref: Filter the results to include only VEHICLEs
        going to this DIRECTION.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar maximum_vehicles: The maximum number of MONITORED VEHICLE
        JOURNEYs to include in a given delivery. The most recent n
        Events within the look ahead window are included.
    :ivar vehicle_monitoring_detail_level: Level of detail to include in
        response.
    :ivar maximum_number_of_calls: If calls are to be returned, maximum
        number of calls to include in response. If absent, exclude all
        calls.  +SIRI v2.0.
    :ivar include_situations: Whether any related Situations  should be
        included in the ServiceDelivery. Default is 'false'. +SIRI v2.0
    :ivar extensions:
    :ivar version: Version number of request. Fixed
    """

    vehicle_monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
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
    maximum_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumVehicles",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_detail_level: Optional[VehicleMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringDetailLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_number_of_calls: Optional["VehicleMonitoringRequestStructure.MaximumNumberOfCalls"] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_situations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeSituations",
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
    class MaximumNumberOfCalls:
        """
        :ivar previous: Maximum number of previous calls to include.
            Only applies if VehicleMonitoringDetailLevel of Calls
            specified. Zero for none. If VehicleMonitoringDetailLevel of
            Calls specified  but MaximumNumberOfCalls.Previous absent,
            include all previous calls. +SIRI v2.0.
        :ivar onwards: Maximum number of onwards calls to include. Zero
            for none. Only applies if VehicleMonitoringDetailLevel of
            'calls' specified. Zero for none. If
            VehicleMonitoringDetailLevel calls specified but
            MaximumNumberOfCalls.Onwards absent, include all onwards
            calls. +SIRI v2.0.
        """

        previous: Optional[int] = field(
            default=None,
            metadata={
                "name": "Previous",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        onwards: Optional[int] = field(
            default=None,
            metadata={
                "name": "Onwards",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class VehicleMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Vehicle Monitoring Capabilities.

    :ivar topic_filtering: Topic Filtering Capabilities.
    :ivar request_policy: Request Policy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar response_features: Optional Response capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["VehicleMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["VehicleMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional["VehicleMonitoringServiceCapabilitiesStructure.AccessControl"] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional["VehicleMonitoringServiceCapabilitiesStructure.ResponseFeatures"] = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
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
        :ivar default_preview_interval: Default preview interval.
            Default is 60 minutes.
        :ivar filter_by_vehicle_monitoring_ref: Whether results can be
            filtered by Vehicle Monitoring  Fixed as 'true'.
        :ivar filter_by_vehicle_ref:
        :ivar filter_by_line_ref:
        :ivar filter_by_direction_ref:
        """

        default_preview_interval: XmlDuration = field(
            default=XmlDuration("PT60M"),
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_vehicle_monitoring_ref: bool = field(
            init=False,
            default=True,
            metadata={
                "name": "FilterByVehicleMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_vehicle_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByVehicleRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_line_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
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
    class RequestPolicy(CapabilityRequestPolicyStructure):
        """
        :ivar has_detail_level: Whether Detail level filtering is
            supported. Default is ' false'.
        :ivar default_detail_level: Detail level. Default Normal.
        :ivar has_maximum_vehicles: Whether results can be limited to a
            maximum number. Default is 'true'.
        :ivar has_maximum_number_of_calls: If system can return detailed
            calling pattern, whether a number of  calls to include can
            be specified. Default is 'false'. +SIRI 2.0
        :ivar has_number_of_onwards_calls: If system can return detailed
            calling pattern, whether a number of onwards calls to
            include can be specified. Default is 'false'. +SIRI 2.0
        :ivar has_number_of_previous_calls: If system can return
            detailed calling pattern, whether a number of previous calls
            to include can be specified. Default is 'false'. +SIRI 2.0
        """

        has_detail_level: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        default_detail_level: Optional[VehicleMonitoringDetailEnumeration] = field(
            default=None,
            metadata={
                "name": "DefaultDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_maximum_vehicles: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumVehicles",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_maximum_number_of_calls: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumNumberOfCalls",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_number_of_onwards_calls: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasNumberOfOnwardsCalls",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_number_of_previous_calls: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasNumberOfPreviousCalls",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class AccessControl(CapabilityAccessControlStructure):
        """
        :ivar check_operator_ref:
        :ivar check_line_ref:
        :ivar check_vehicle_monitoring_ref: If access control is
            supported, whether access control by monitoring point is
            supported. Default is 'true'.
        """

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
        check_vehicle_monitoring_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "CheckVehicleMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class ResponseFeatures:
        """
        :ivar has_location: Whether result has location. Default is
            'true'.
        :ivar has_situations: Whether result supports SITUATION
            REFERENCESs. Default is 'false'. +SIRI v2.0
        """

        has_location: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasLocation",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_situations: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasSituations",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class VehicleMonitoringDeliveryStructure(AbstractServiceDeliveryStructure):
    """Type for Delivery for Vehicle Monitoring Service.

    Provides information about one or more vehicles; each has its own
    VEHICLE activity element.

    :ivar vehicle_activity: Describes the progress of a VEHICLE along
        its route.
    :ivar vehicle_activity_cancellation: Reference to an previously
        communicated VEHICLE activity which should now be removed from
        the system.
    :ivar vehicle_activity_note: Annotation to accompany of Vehicle
        Activities.
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    vehicle_activity: List[VehicleActivityStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_activity_cancellation: List[VehicleActivityCancellationStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivityCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_activity_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivityNote",
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
class VehicleMonitoringRequest(VehicleMonitoringRequestStructure):
    """
    Request for information about Vehicle Movements.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMonitoringServiceCapabilities(VehicleMonitoringServiceCapabilitiesStructure):
    """
    Capabilities of Vehicle Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMonitoringServicePermissionStructure(AbstractPermissionStructure):
    """
    Type for Monitoring Service Permissions.

    :ivar operator_permissions:
    :ivar line_permissions:
    :ivar vehicle_monitoring_permissions: The Vehicle Monitors (DIUSPLAY
        ASSIGNMENTs) that the participant may access.
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
    vehicle_monitoring_permissions: Optional[
        "VehicleMonitoringServicePermissionStructure.VehicleMonitoringPermissions"
    ] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringPermissions",
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
    class VehicleMonitoringPermissions:
        """
        :ivar allow_all:
        :ivar vehicle_monitor_permission: Participant's permission for
            this Vehicle Monitor (DISPLAY SSIGNMENT).
        """

        allow_all: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AllowAll",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        vehicle_monitor_permission: List[VehicleMonitorPermissionStructure] = field(
            default_factory=list,
            metadata={
                "name": "VehicleMonitorPermission",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class VehicleMonitoringDelivery(VehicleMonitoringDeliveryStructure):
    """
    Delivery for Vehicle Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMonitoringPermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.

    :ivar vehicle_monitoring_permission: Permissions for use of VEHICLE
        MONITORING. Can be used to specify which Consumers can see which
        vehicles
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    vehicle_monitoring_permission: List[VehicleMonitoringServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringPermission",
            "type": "Element",
        },
    )


@dataclass
class VehicleMonitoringSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Type for Subscription Request for Vehicle Monitoring Service.

    :ivar vehicle_monitoring_request:
    :ivar incremental_updates: Whether the producer will return the
        complete set of current data, or only  provide updates to this
        data, i.e. additions, modifications and deletions. If false or
        omitted, each subscription response will contain the full
        information as specified in this request.
    :ivar change_before_updates: The amount of change to the VEHICLE
        expected arrival time at next stop that can happen before an
        update is sent (i.e. if ChangeBeforeUpdate is set to 2 minutes,
        the subscriber will not be told that a bus is 30 seconds delayed
        - an update will only be sent when the bus is at least 2 minutes
        delayed).
    :ivar update_interval: Time interval in seconds in which new data is
        to be transmitted. If unspecified, default to system
        configuration.
    :ivar extensions:
    """

    vehicle_monitoring_request: Optional[VehicleMonitoringRequest] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRequest",
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
    update_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "UpdateInterval",
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
class VehicleMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Vehicle Monitoring Service.

    :ivar vehicle_monitoring_service_capabilities:
    :ivar vehicle_monitoring_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    vehicle_monitoring_service_capabilities: Optional[VehicleMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_permissions: Optional[VehicleMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringPermissions",
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
class VehicleMonitoringDeliveriesStructure:
    """
    Type for Deliveries for VEHICLE monitoring services Used in WSDL.

    :ivar vehicle_monitoring_delivery: Delivery for Vehicle Moniroting
        Service.
    """

    vehicle_monitoring_delivery: List[VehicleMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class VehicleMonitoringSubscriptionRequest(VehicleMonitoringSubscriptionStructure):
    """
    Request for a subscription to the Vehicle Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleMonitoringCapabilitiesResponse(VehicleMonitoringCapabilitiesResponseStructure):
    """Capabilities for Vehicle Monitoring Service.

    Answers a VehicleMontoringCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
