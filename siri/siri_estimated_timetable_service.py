from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
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
from siri.siri_model.siri_estimated_vehicle_journey_v2_0 import (
    EstimatedServiceJourneyInterchange,
    EstimatedVehicleJourney,
)
from siri.siri_model.siri_model_permissions_v2_0 import (
    ConnectionCapabilityAccessControlStructure,
    ConnectionServicePermissionStructure,
    PermissionsStructure,
)
from siri.siri_model.siri_reference_v2_0 import LineDirectionStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EstimatedTimetableDetailEnumeration(Enum):
    """
    Detail Levels for Estimated Timetable Request.

    :cvar MINIMUM: Return only the minimum amount of optional data for
        each Stop Visit to provide a display, A time at stop, LINE name
        and destination name.
    :cvar BASIC: Return minimum and other available basic details for
        each Stop Visit. Do not include data on times at next stop or
        destination.
    :cvar NORMAL: Return all basic data, and also origin VIA points and
        destination.
    :cvar CALLS: Return in addition to normal data, the CALL data for
        each Stop Visit, including PREVIOUS and ONWARD CALLs with
        passing times.
    :cvar FULL: Return all available data for each Stop Visit, including
        calls.
    """

    MINIMUM = "minimum"
    BASIC = "basic"
    NORMAL = "normal"
    CALLS = "calls"
    FULL = "full"


@dataclass
class EstimatedTimetableCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Estimated Timetable Service Capabilities.

    Answered with a EstimatedTimetableCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedTimetableCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for Estimated Timetable Capability Request Policy.

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
class EstimatedTimetablePermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.

    :ivar estimated_timetable_permission: Permission for a single
        participant or all participants to use an aspect of the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    estimated_timetable_permission: List[ConnectionServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetablePermission",
            "type": "Element",
        },
    )


@dataclass
class EstimatedTimetableRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Type for Functional Service Request for Estimated Timetable.

    :ivar preview_interval: Forward duration for which journeys should
        be included. For subscriptions, this duration is a continuously
        rolling window from the present time. For immediate requests,
        this duration is measured from the time of the request.
    :ivar timetable_version_ref: Communicate only differences to the
        timetable specified by this version of the timetable.
    :ivar operator_ref: Filter the results to include journeys for only
        the specified OPERATORs.
    :ivar lines: Filter the results to include only VEHICLEs along the
        given LINEs.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar estimated_timetable_detail_level: Level of detail to include
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
    timetable_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimetableVersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["EstimatedTimetableRequestStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
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
    estimated_timetable_detail_level: Optional[EstimatedTimetableDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableDetailLevel",
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
    class Lines:
        """
        :ivar line_direction: Include only vehicles along the given
            LINE.
        """

        line_direction: List[LineDirectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "LineDirection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class EstimatedTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Estimated Timetable Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["EstimatedTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional[CapabilityRequestPolicyStructure] = field(
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
        :ivar default_preview_interval: Preview interval available for
            estimations.
        :ivar filter_by_operator_ref:
        :ivar filter_by_line_ref:
        :ivar filter_by_version_ref: Whether results can be filtered by
            TIMETABLE VERSION Default is 'true'.
        """

        default_preview_interval: Optional[XmlDuration] = field(
            default=None,
            metadata={
                "name": "DefaultPreviewInterval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_operator_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByOperatorRef",
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
        filter_by_version_ref: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByVersionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class EstimatedVersionFrameStructure(AbstractItemStructure):
    """
    Type for version frame structure.

    :ivar version_ref:
    :ivar estimated_vehicle_journey:
    :ivar estimated_service_journey_interchange: Connection parameters
        for a monitored SERVICE JOURNEY INTERCHANGE between a feeder and
        distributor journey. SIRI 2.0
    """

    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_vehicle_journey: List[EstimatedVehicleJourney] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    estimated_service_journey_interchange: List[EstimatedServiceJourneyInterchange] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class EstimatedTimetableDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Type for Delivery for Real-time Timetable Service.

    :ivar estimated_journey_version_frame: Estimated Journeys of a
        common TIMETABLE VERSION FRAME, grouped by timetable version.
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    estimated_journey_version_frame: List[EstimatedVersionFrameStructure] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedJourneyVersionFrame",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
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
class EstimatedTimetableRequest(EstimatedTimetableRequestStructure):
    """
    Request for information about the estimated timetable.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedTimetableServiceCapabilities(EstimatedTimetableServiceCapabilitiesStructure):
    """
    Capabilities of Estimated TimetableService.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Estimated Timetable Capability.
    """

    estimated_timetable_service_capabilities: Optional[EstimatedTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_permissions: Optional[EstimatedTimetablePermissions] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetablePermissions",
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
class EstimatedTimetableDelivery(EstimatedTimetableDeliveryStructure):
    """
    Delivery for Estimated Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Subscription Request for the Estimated Timetable Service.

    :ivar estimated_timetable_request:
    :ivar incremental_updates: Whether the producer should return the
        complete set of data, or only provide updates to the previously
        returned data i.e. changes to the expected deviation (delay or
        early time). Default is 'true'. If true only changes at the
        first stop will be returned and the client must interpolate the
        If false each subscription response will contain the full
        information as specified in this request.
    :ivar change_before_updates: The amount of change to the arrival or
        departure time that can happen before an update is sent (i.e. if
        ChangeBeforeUpdate is set to 2 minutes, the subscriber will not
        be told that a timetable is changed by 30 seconds - an update
        will only be sent when the timetable is changed by at least
        least 2 minutes.
    :ivar extensions:
    """

    estimated_timetable_request: Optional[EstimatedTimetableRequest] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableRequest",
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
class EstimatedTimetableCapabilitiesResponse(EstimatedTimetableCapabilitiesResponseStructure):
    """Capabilities for Estimated Timetable Service.

    Answers a EstimatedTimetableCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedTimetableDeliveriesStructure:
    """Type for Deliveries for Real-time Timetable Service.

    Used in WSDL.
    """

    estimated_timetable_delivery: List[EstimatedTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class EstimatedTimetableSubscriptionRequest(EstimatedTimetableSubscriptionStructure):
    """
    Request for a subscription to the Estimated Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
