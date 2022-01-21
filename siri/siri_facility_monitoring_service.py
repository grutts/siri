from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.acsb.acsb_passenger_mobility_v0_3 import UserNeedStructure
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    CapabilitySubscriptionPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_model.siri_facility_v2_0 import FacilityConditionStructure
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_model_permissions_v2_0 import (
    LinePermissions,
    OperatorPermissions,
    PermissionsStructure,
)
from siri.siri_utility.siri_permissions_v2_0 import (
    AbstractPermissionStructure,
    CapabilityAccessControlStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AccessibilityNeedsFilterStructure:
    """
    Type for information about Accessibility Facilities status.

    :ivar user_need: User need to be monitored.
    """

    user_need: List[UserNeedStructure] = field(
        default_factory=list,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class FacilityCondition(FacilityConditionStructure):
    """
    Condition of a Facility that is being monitored.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityMonitoringCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Vehicle Monitoring Service Capabilities.

    Answered with a VehicleMontoringCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Vehicle Monitoring Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar response_features: Optional Response capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["FacilityMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["FacilityMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional["FacilityMonitoringServiceCapabilitiesStructure.AccessControl"] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional["FacilityMonitoringServiceCapabilitiesStructure.ResponseFeatures"] = field(
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
        :ivar filter_by_facility_ref:
        :ivar filter_by_location_ref: Whether results can be filtered by
            location. Fixed as 'true'.
        :ivar filter_by_vehicle_ref:
        :ivar filter_by_line_ref:
        :ivar filter_by_stop_point_ref:
        :ivar filter_by_vehicle_journey_ref:
        :ivar filter_by_connection_link_ref:
        :ivar filter_by_interchange_ref:
        :ivar filter_by_specific_need: Whether results can be filtered
            by Specific Needs. Default is 'true'.
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
        filter_by_facility_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByFacilityRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        filter_by_location_ref: bool = field(
            init=False,
            default=True,
            metadata={
                "name": "FilterByLocationRef",
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
        filter_by_stop_point_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByStopPointRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_vehicle_journey_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByVehicleJourneyRef",
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
        filter_by_interchange_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByInterchangeRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_specific_need: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterBySpecificNeed",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class RequestPolicy(CapabilityRequestPolicyStructure):
        """
        :ivar has_maximum_facility_status: Whether a maximum number of
            Facility Status to include can be specified. Default is
            'false'.
        """

        has_maximum_facility_status: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumFacilityStatus",
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

    @dataclass
    class ResponseFeatures:
        """
        :ivar has_remedy: Whether result supports remedy information.
            Default is 'false'
        :ivar has_facility_location: Whether result supports facility
            location information. Default is 'true'.
        """

        has_remedy: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasRemedy",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_facility_location: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasFacilityLocation",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class FacilityMonitoringServicePermissionStructure(AbstractPermissionStructure):
    """
    Type for Facility Monitoring Service Permissions.
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
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class FacilityMonitoringDeliveryStructure(AbstractServiceDeliveryStructure):
    """Type for Delivery for Vehicle Monitoring Service.

    Provides information about one or more vehicles; each has its own
    VEHICLE activity element.

    :ivar facility_condition:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    facility_condition: List[FacilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "FacilityCondition",
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
class FacilityMonitoringPermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    facility_monitoring_permission: List[FacilityMonitoringServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringPermission",
            "type": "Element",
        },
    )


@dataclass
class FacilityMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Facility Monitoring Service.

    :ivar preview_interval: Forward duration for which Facilities status
        change: only status change which will occur within this time
        span will be returned.
    :ivar start_time: Start time for PreviewInterval. If absent, then
        current time is assumed.
    :ivar facility_ref:
    :ivar feature_ref:
    :ivar line_ref:
    :ivar stop_point_ref:
    :ivar connection_link_ref:
    :ivar framed_vehicle_journey_ref: Refercence to a VEHICLE JOURNEY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref:
    :ivar interchange_ref:
    :ivar vehicle_ref:
    :ivar stop_place_ref: Reference to a stop place.
    :ivar stop_place_component_ref: Reference to a stop place component.
    :ivar accessibility_needs_filter: Filter only for facility changes
        that affect the following accessibility needs.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar maximum_number_of_facility_conditions: The maximum number of
        facility status in a given delivery. The most recent n Events
        within the look ahead window are included.
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
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feature_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeatureRef",
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
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
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
    vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
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
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_component_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_needs_filter: List[AccessibilityNeedsFilterStructure] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityNeedsFilter",
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
    maximum_number_of_facility_conditions: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfFacilityConditions",
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
class FacilityMonitoringServiceCapabilities(FacilityMonitoringServiceCapabilitiesStructure):
    """
    Capabilities of Vehicle Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Vehicle Monitoring Service.

    :ivar facility_monitoring_service_capabilities:
    :ivar facility_monitoring_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    facility_monitoring_service_capabilities: Optional[FacilityMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_permissions: Optional[FacilityMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringPermissions",
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
class FacilityMonitoringDelivery(FacilityMonitoringDeliveryStructure):
    """
    Delivery for Vehicle Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityMonitoringRequest(FacilityMonitoringRequestStructure):
    """
    Request for information about Facilities status.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityMonitoringCapabilitiesResponse(FacilityMonitoringCapabilitiesResponseStructure):
    """Capabilities for Vehicle Monitoring Service.

    Answers a VehicleMontoringCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityMonitoringDeliveriesStructure:
    """
    Type for Deliveries for VEHICLE monitoring services Used in WSDL.

    :ivar facility_monitoring_delivery: Delivery for Vehicle Activity
        Service.
    """

    facility_monitoring_delivery: List[FacilityMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class FacilityMonitoringSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Type for Subscription Request for Vehicle Monitoring Service.

    :ivar facility_monitoring_request:
    :ivar incremental_updates: Whether the producer will return the
        complete set of current data, or only  provide updates to this
        data, i.e. additions, modifications and deletions. If false or
        omitted, each subscription response will contain the full
        information as specified in this request.
    :ivar extensions:
    """

    facility_monitoring_request: Optional[FacilityMonitoringRequest] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringRequest",
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
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class FacilityMonitoringSubscriptionRequest(FacilityMonitoringSubscriptionStructure):
    """
    Request for a subscription to the Vehicle Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
