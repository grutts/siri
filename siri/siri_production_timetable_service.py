from dataclasses import dataclass, field
from typing import List, Optional
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractItemStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_model.siri_dated_vehicle_journey_v2_0 import (
    DatedVehicleJourneyStructure,
    ServiceJourneyInterchangeStructure,
)
from siri.siri_model.siri_journey_support_v2_0 import FirstOrLastJourneyEnumeration
from siri.siri_model.siri_model_permissions_v2_0 import (
    ConnectionCapabilityAccessControlStructure,
    PermissionsStructure,
    ProductionTimetablePermission,
)
from siri.siri_model.siri_reference_v2_0 import (
    LineDirectionStructure,
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_time_v1_2 import ClosedTimestampRangeStructure
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedTimetableVersionFrameStructure(AbstractItemStructure):
    """
    Type for Production Timetable of a LINE.

    :ivar version_ref: Timetable Version.
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
    :ivar operator_ref: OPERATOR of a VEHICLE JOURNEY.   Note that the
        operator may change over the course of a journey.  This shoudl
        show teh operator for the curent point in the journey.  Use
        Journey Parts tp record all the operators in the whole journeyh.
    :ivar product_category_ref: Product Classification of VEHICLE
        JOURNEY- subdivides a transport mode. e.g. express, loacl.
    :ivar service_feature_ref: Classification of service into arbitrary
        Service categories, e.g. school bus. Recommended SIRI values
        based on TPEG are given in SIRI documentation and enumerated in
        the siri_facilities package. Corresponds to NeTEX TYPE OF
        SERVICe.
    :ivar vehicle_feature_ref: Features of VEHICLE providing journey.
        Recommended SIRI values based on TPEG are given in SIRI
        documentation and enumerated in the siri_facilities package.
    :ivar destination_display: Description of the destination stop
        (vehicle signage) to show on vehicle, Can be overwritten for a
        journey, and then also section by section by the entry in an
        Individual Call.  (Unbounded since SIRI 2.0)
    :ivar line_note: Additional Text associated with LINE.  (Unbounded
        since SIRI 2.0)
    :ivar first_or_last_journey: Whether journey is first or last
        jouurney of day. +SIRI v2.0
    :ivar headway_service: Whether this is a Headway Service, that is,
        one shown as operating at a prescribed interval rather than to a
        fixed timetable.
    :ivar monitored: Whether VEHICLE JOURNEYs of LINE are normally
        monitored. Provides a default value for the Monitored element on
        individual journeys of the timetable.
    :ivar dated_vehicle_journey: Complete list of all planned VEHICLE
        JOURNEYs for this LINE and DIRECTION.
    :ivar service_journey_interchange: Connection paramters for a
        SERVICE JOURNEY INTERCHANGE between a feeder and distributor
        journey. SIRI 2.0
    :ivar extensions:
    """

    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionRef",
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
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_note: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    first_or_last_journey: Optional[FirstOrLastJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey: List[DatedVehicleJourneyStructure] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_journey_interchange: List[ServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyInterchange",
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
class ProductionTimetableCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about ProductionTimetable Service Capabilities.

    Answered with a ProductionTimetableCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for Estimated ProductionCapability Request Policy.

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
class ProductionTimetablePermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    production_timetable_permission: List[ProductionTimetablePermission] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetablePermission",
            "type": "Element",
        },
    )


@dataclass
class ProductionTimetableRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Production Timetables.

    :ivar validity_period: Start and end of timetable validity (time
        window) of journeys for which schedules are to be returned.
        Refers to the departure time at the first stop of each VEHICLE
        JOURNEY If blank the configured data horizon will be used.
    :ivar timetable_version_ref: Communicate only differences to the
        timetable specified by this VERSION of the TIMETABLe.
    :ivar operator_ref: Filter the results to include journeys for only
        the specified OPERATORs.
    :ivar lines: Filter the results to include only vehicles along the
        given LINEs.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar incremental_updates: Whether to return the whole timetable, or
        just differences from the inidicated version. Default is
        'false'.
    :ivar extensions:
    :ivar version: Version number of request. Fixed.
    """

    validity_period: Optional[ClosedTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
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
    lines: Optional["ProductionTimetableRequestStructure.Lines"] = field(
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
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Lines:
        """
        :ivar line_direction: Iinclude only vehicles along the given
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
class ProductionTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for ProductionTimetable Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policiy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["ProductionTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
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
    subscription_policy: Optional["ProductionTimetableServiceCapabilitiesStructure.SubscriptionPolicy"] = field(
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
        :ivar filter_by_validity_period:
        :ivar filter_by_operator_ref:
        :ivar filter_by_line_ref:
        :ivar filter_by_version_ref: Whether results can be filtered by
            TIMETABLE VERSION Default is 'true'.
        """

        filter_by_validity_period: bool = field(
            default=True,
            metadata={
                "name": "FilterByValidityPeriod",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
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
        filter_by_version_ref: bool = field(
            default=True,
            metadata={
                "name": "FilterByVersionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )

    @dataclass
    class SubscriptionPolicy:
        """
        :ivar has_incremental_updates: Whether incremental updates can
            be specified for updates Default is ' true'.
        """

        has_incremental_updates: bool = field(
            default=True,
            metadata={
                "name": "HasIncrementalUpdates",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )


@dataclass
class DatedTimetableVersionFrame(DatedTimetableVersionFrameStructure):
    """
    A TIMETABLE FRAME to run on a specified date.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableRequest(ProductionTimetableRequestStructure):
    """
    Request for daily production timetables.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableServiceCapabilities(ProductionTimetableServiceCapabilitiesStructure):
    """
    Capabilities of ProductionTimetableService.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for ProductionTimetable Capability.

    :ivar production_timetable_service_capabilities:
    :ivar production_timetable_permissions:
    :ivar extensions:
    :ivar version: Version number of response. fixed.
    """

    production_timetable_service_capabilities: Optional[ProductionTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    production_timetable_permissions: Optional[ProductionTimetablePermissions] = field(
        default=None,
        metadata={
            "name": "ProductionTimetablePermissions",
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
class ProductionTimetableDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Delivery for Production Timetable Service type.

    :ivar dated_timetable_version_frame: A TIMETABLE to run on a
        specified date.
    :ivar extensions:
    :ivar version: Version number of response. fixed.
    """

    dated_timetable_version_frame: List[DatedTimetableVersionFrame] = field(
        default_factory=list,
        metadata={
            "name": "DatedTimetableVersionFrame",
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
class ProductionTimetableSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Subscription Request for Production Timetable Service.

    :ivar production_timetable_request:
    :ivar incremental_updates: Whether the producer should return the
        complete set of current data, or only provide updates to the
        last data returned, i.e. additions, modifications and deletions.
        If false each subscription response will contain the full
        information as specified in this request.
    :ivar extensions:
    """

    production_timetable_request: Optional[ProductionTimetableRequest] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableRequest",
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
class ProductionTimetableCapabilitiesResponse(ProductionTimetableCapabilitiesResponseStructure):
    """Capabilities for ProductionTimetable Service.

    Answers a Answered with a ProductionTimetableCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableDelivery(ProductionTimetableDeliveryStructure):
    """
    Delivery for Production Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableSubscriptionRequest(ProductionTimetableSubscriptionStructure):
    """
    Request for a subscription to the Production Timetable Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ProductionTimetableDeliveriesStructure:
    """Type for deliveries of production timetable service.

    Used in WSDL.
    """

    production_timetable_delivery: List[ProductionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
