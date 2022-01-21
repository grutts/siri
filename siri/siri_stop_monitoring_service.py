from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractIdentifiedItemStructure,
    AbstractItemStructure,
    AbstractReferencingItemStructure,
    AbstractRequiredIdentifiedItemStructure,
    AbstractRequiredReferencingItemStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    CapabilitySubscriptionPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_model_permissions_v2_0 import (
    LinePermissions,
    MonitoringCapabilityAccessControlStructure,
    OperatorPermissions,
    PermissionsStructure,
    StopMonitorPermissionStructure,
)
from siri.siri_model.siri_monitored_vehicle_journey_v2_0 import MonitoredVehicleJourneyStructure
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_situation_identity_v1_1 import SituationRef
from siri.siri_utility.siri_permissions_v2_0 import AbstractPermissionStructure
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ServiceExceptionEnumeration(Enum):
    """
    Classification of the service exception.

    :cvar BEFORE_FIRST_JOURNEY: No transport services returned because
        currently before first journey of day.
    :cvar AFTER_LAST_JOURNEY: No transport services returned because
        currently after first journey of day.
    :cvar NO_SERVICE_TODAY: No transport services returned because no
        services today.
    :cvar TRANSPORT_TEMPORARILY_SUSPENDED: No transport services
        returned because services currently suspended.
    :cvar TRANSPORT_LONGTERM_SUSPENDED: No transport services returned
        because prolonged suspension of services.
    :cvar TRANSPORT_SEVERLY_DISRUPTED: Transport services returned
        subject to severe disruptions.
    :cvar REALTIME_DATA_NOT_AVAILABLE: No transport services returned
        because real-time services not available.
    :cvar REALTIME_DATA_AVAILABLE:
    """

    BEFORE_FIRST_JOURNEY = "beforeFirstJourney"
    AFTER_LAST_JOURNEY = "afterLastJourney"
    NO_SERVICE_TODAY = "noServiceToday"
    TRANSPORT_TEMPORARILY_SUSPENDED = "transportTemporarilySuspended"
    TRANSPORT_LONGTERM_SUSPENDED = "transportLongtermSuspended"
    TRANSPORT_SEVERLY_DISRUPTED = "transportSeverlyDisrupted"
    REALTIME_DATA_NOT_AVAILABLE = "realtimeDataNotAvailable"
    REALTIME_DATA_AVAILABLE = "realtimeDataAvailable"


class StopMonitoringDetailEnumeration(Enum):
    """
    Detail Levels for Stop Monitoring Request.

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


class StopVisitTypeEnumeration(Enum):
    """
    Visit Types to Return.

    :cvar ALL: Return all Stop Visits.
    :cvar ARRIVALS: Return only arrival Stop Visits.
    :cvar DEPARTURES: Return only departure Stop Visits.
    """

    ALL = "all"
    ARRIVALS = "arrivals"
    DEPARTURES = "departures"


@dataclass
class DeliveryVariantStructure:
    """
    Type for Delivery Variant +SIRI v2.0.

    :ivar variant_type: Classification of DELIVERY VARIANT +SIRI v2.0.
    :ivar content: Variant text. SIRI v".0
    """

    variant_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "VariantType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    content: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class MonitoredStopVisitCancellationStructure(AbstractReferencingItemStructure):
    """
    Type for Cancellation of an earlier Stop Visit.

    :ivar monitoring_ref: Reference to a stop monitoring point to which
        cancellation applies.
    :ivar visit_number:
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a LINE DIRECTION DIRECTION,
        typically outward or return.
    :ivar vehicle_journey_ref: VEHICLE JOURNEY of Stop Visit that is
        being cancelled.
    :ivar clear_down_ref: Cleardown identifier of Stop Visit that is
        being deleted.
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
    vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    clear_down_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClearDownRef",
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
class MonitoredStopVisitStructure(AbstractIdentifiedItemStructure):
    """Type for Visit of a VEHICLE to a stop monitoring point.

    May provide information about the arrival, the departure or both.

    :ivar valid_until_time: Time until when data is valid. +SIRI 2.0
    :ivar monitoring_ref: Reference to a stop monitoring point to which
        Stop Visit applies.
    :ivar clear_down_ref: Identifier associated with Stop Visit for use
        in direct wireless communication between bus and stop display.
        Cleardown codes are short arbitrary identifiers suitable for
        radio transmission.
    :ivar monitored_vehicle_journey: Provides real-time information
        about the VEHICLE JOURNEY along which a VEHICLE is running.
    :ivar stop_visit_note: Text associated with Stop Visit.
    :ivar stop_facility: Facility associated with  stop visit
    :ivar extensions:
    """

    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
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
        },
    )
    clear_down_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClearDownRef",
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
    stop_visit_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopVisitNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_facility: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopFacility",
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
class ServiceExceptionStructure(AbstractItemStructure):
    """
    Type for whether service is unavailable for all or some services SIRI 2.0.

    :ivar line_ref:
    :ivar direction_ref: Reference to a LINE DIRECTION to which
        exception applies.
    :ivar stop_point_ref:
    :ivar service_status: Status of service, Service not yet started,
        Service ended for day, no service today, etc.
    :ivar notice: Text explanation of service exception.
    :ivar situation_ref: Reference to a SITUATION providing further
        information about exception
    """

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
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_status: Optional[ServiceExceptionEnumeration] = field(
        default=None,
        metadata={
            "name": "ServiceStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notice: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class StopLineNoticeCancellationStructure(AbstractReferencingItemStructure):
    """
    Type for Cancellation of an earlier Stop Line Notice.

    :ivar monitoring_ref: Reference to a stop monitoring point to which
        LINE notice applies.
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a LINE DIRECTION DIRECTION,
        typically outward or return.
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
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class StopMonitoringCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Stop Monitoring Service Capabilities.

    Answered with StopMonitoringCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
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
class StopMonitoringFilterStructure:
    """
    Type for an individual Stop Monitoring a Multiple Request.

    :ivar preview_interval: Forward duration for which Visits should be
        included, that is, interval before predicted arrival at the stop
        for which to include Visits: only journeys which will arrive or
        depart within this time span will be returned.
    :ivar start_time: Start time for PreviewInterval. If absent, then
        current time is assumed.
    :ivar monitoring_ref: Reference to Monitoring Point(s) about which
        data is requested. May be a STOP POINT, timing point, or a group
        of points under a single reference.
    :ivar operator_ref: Filter the results to include only Stop Visits
        for VEHICLEs run by the specified OPERATOR.
    :ivar line_ref: Filter the results to include only Stop Visits for
        VEHICLEs for the given LINE.
    :ivar direction_ref: Filter the results to include only Stop Visits
        for vehicles running in a specific relative DIRECTION, for
        example, "inbound" or "outbound". (Direction does not specify a
        destination.)
    :ivar destination_ref: Filter the results to include only journeys
        to the DESTINATION of the journey.
    :ivar stop_visit_types: Whether to include arrival Visits, departure
        Visits, or all. Default is 'all'.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar maximum_stop_visits: The maximum number of Stop Visits to
        include in a given delivery. The first n Stop Visits within the
        look ahead window are included. Only Visits within the Lookahead
        Interval are returned. The MinimumStopVisits parameter can be
        used to reduce the the number of entries for each LINE within
        the total returned.
    :ivar minimum_stop_visits_per_line: The minimum number of Stop
        Visits for a given LINE to include in a given delivery. If there
        are more Visits within the LookAheadInterval than allowed by
        MaximumStopVisits and a MinimumStopVisits value is specified,
        then at least the minimum number will be delivered for each
        LINE. I.e Stop Visits will be included even if the Stop Visits
        are later than those for some other LINE for which the minimum
        number of Stop Visits has already been supplied. This allows the
        Consumer to obtain at least one entry for every available LINE
        with vehicles approaching the stop. Only STOP Visits within the
        Look ahead Interval are returned.
    :ivar minimum_stop_visits_per_line_via: The minimum number of Stop
        Visits for a given LINE and VIA combination to include in a
        given delivery. As for MinimumStopVisitsPerLine but with Via
        also taken into account. SIRI+v2.0
    :ivar maximum_text_length: Maximum length of text to return for text
        elements. Default is 30.
    :ivar stop_monitoring_detail_level: Level of detail to include in
        response. Default is 'normal'.
    :ivar include_situations: Whether any related SITUATIONs should be
        included in the ServiceDelivery. Default is 'false'. +SIRI v2.0
    :ivar maximum_number_of_calls: If calls are to be returned, maximum
        number of calls to include in response. If absent, exclude all
        calls.
    :ivar extensions:
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
    monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_visit_types: Optional[StopVisitTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopVisitTypes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: Optional[bool] = field(
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
    maximum_stop_visits: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumStopVisits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_stop_visits_per_line: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumStopVisitsPerLine",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_stop_visits_per_line_via: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumStopVisitsPerLineVia",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_text_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumTextLength",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_detail_level: Optional[StopMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "StopMonitoringDetailLevel",
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
    maximum_number_of_calls: Optional["StopMonitoringFilterStructure.MaximumNumberOfCalls"] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfCalls",
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
    class MaximumNumberOfCalls:
        """
        :ivar previous: Maximum number of ONWARDS CALLs to include in
            results. Only applies if StopMonitoringDetailLevel of
            'calls' specified. Zero for none. If
            StopMonitoringDetailLevel of 'calls' specified but
            MaximumNumberOfCalls.Previous absent, include all ONWARDS
            CALLs.
        :ivar onwards: Maximum number of ONWARDS CALLs  to include in
            results. Zero for none. Only applies if
            StopMonitoringDetailLevel of 'calls'specified. Zero for
            none. If StopMonitoringDetailLevel of 'calls' specified but
            MaximumNumberOfCalls.Onwards absent, include all ONWARDS
            CALLs.
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
class StopMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Stop Monitoring Service.

    :ivar preview_interval: Forward duration for which Visits should be
        included, that is, interval before predicted arrival at the stop
        for which to include Visits: only journeys which will arrive or
        depart within this time span will be returned.
    :ivar start_time: Start time for PreviewInterval. If absent, then
        current time is assumed.
    :ivar monitoring_ref: Reference to Monitoring Point(s) about which
        data is requested. May be a STOP POINT, timing point, or a group
        of points under a single reference.
    :ivar operator_ref: Filter the results to include only Stop Visits
        for VEHICLEs run by the specified OPERATOR.
    :ivar line_ref: Filter the results to include only Stop Visits for
        VEHICLEs for the given LINE.
    :ivar direction_ref: Filter the results to include only Stop Visits
        for vehicles running in a specific relative DIRECTION, for
        example, "inbound" or "outbound". (Direction does not specify a
        destination.)
    :ivar destination_ref: Filter the results to include only journeys
        to the DESTINATION of the journey.
    :ivar stop_visit_types: Whether to include arrival Visits, departure
        Visits, or all. Default is 'all'.
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar maximum_stop_visits: The maximum number of Stop Visits to
        include in a given delivery. The first n Stop Visits within the
        look ahead window are included. Only Visits within the Lookahead
        Interval are returned. The MinimumStopVisits parameter can be
        used to reduce the the number of entries for each LINE within
        the total returned.
    :ivar minimum_stop_visits_per_line: The minimum number of Stop
        Visits for a given LINE to include in a given delivery. If there
        are more Visits within the LookAheadInterval than allowed by
        MaximumStopVisits and a MinimumStopVisits value is specified,
        then at least the minimum number will be delivered for each
        LINE. I.e Stop Visits will be included even if the Stop Visits
        are later than those for some other LINE for which the minimum
        number of Stop Visits has already been supplied. This allows the
        Consumer to obtain at least one entry for every available LINE
        with vehicles approaching the stop. Only STOP Visits within the
        Look ahead Interval are returned.
    :ivar minimum_stop_visits_per_line_via: The minimum number of Stop
        Visits for a given LINE and VIA combination to include in a
        given delivery. As for MinimumStopVisitsPerLine but with Via
        also taken into account. SIRI+v2.0
    :ivar maximum_text_length: Maximum length of text to return for text
        elements. Default is 30.
    :ivar stop_monitoring_detail_level: Level of detail to include in
        response. Default is 'normal'.
    :ivar include_situations: Whether any related SITUATIONs should be
        included in the ServiceDelivery. Default is 'false'. +SIRI v2.0
    :ivar maximum_number_of_calls: If calls are to be returned, maximum
        number of calls to include in response. If absent, exclude all
        calls.
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
    monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_visit_types: Optional[StopVisitTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopVisitTypes",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: Optional[bool] = field(
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
    maximum_stop_visits: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumStopVisits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_stop_visits_per_line: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumStopVisitsPerLine",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_stop_visits_per_line_via: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimumStopVisitsPerLineVia",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_text_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumTextLength",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_detail_level: Optional[StopMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "StopMonitoringDetailLevel",
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
    maximum_number_of_calls: Optional["StopMonitoringRequestStructure.MaximumNumberOfCalls"] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfCalls",
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
        :ivar previous: Maximum number of ONWARDS CALLs to include in
            results. Only applies if StopMonitoringDetailLevel of
            'calls' specified. Zero for none. If
            StopMonitoringDetailLevel of 'calls' specified but
            MaximumNumberOfCalls.Previous absent, include all ONWARDS
            CALLs.
        :ivar onwards: Maximum number of ONWARDS CALLs  to include in
            results. Zero for none. Only applies if
            StopMonitoringDetailLevel of 'calls'specified. Zero for
            none. If StopMonitoringDetailLevel of 'calls' specified but
            MaximumNumberOfCalls.Onwards absent, include all ONWARDS
            CALLs.
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
class StopMonitoringServicePermissionStructure(AbstractPermissionStructure):
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
    stop_monitor_permissions: Optional["StopMonitoringServicePermissionStructure.StopMonitorPermissions"] = field(
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
class StopNoticeCancellationStructure(AbstractRequiredReferencingItemStructure):
    """
    Type for Cancellation of an earlier Stop Notice.

    :ivar monitoring_ref: Reference to a stop monitoring point to which
        Notice applies.
    :ivar stop_point_ref:
    :ivar applies_from_time: In case of a delayed cancellation this time
        tells from when the cancellation applies.
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
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    applies_from_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AppliesFromTime",
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
class StopNoticeStructure(AbstractRequiredIdentifiedItemStructure):
    """
    :ivar monitoring_ref: Reference to a stop monitoring point to which
        SITUATION applies.
    :ivar stop_point_ref:
    :ivar situation_ref:
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
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: List[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
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
class MonitoredStopVisit(MonitoredStopVisitStructure):
    """
    A visit to a stop by a VEHICLE as an arrival and /or departure.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class MonitoredStopVisitCancellation(MonitoredStopVisitCancellationStructure):
    """
    Reference to an previously communicated Stop Visit which should now be
    removed from the arrival/departure board for the stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceException(ServiceExceptionStructure):
    """
    Exceptions to service availability for all or some services SIRI 2.0.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopLineNoticeCancellation(StopLineNoticeCancellationStructure):
    """
    Reference to an previously communicated LINE notice which should now be
    removed from the arrival/departure board for the stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopLineNoticeStructure(AbstractIdentifiedItemStructure):
    """
    Type for a Stop Line Notice.

    :ivar monitoring_ref: Reference to a stop monitoring point to which
        LINE notice applies.
    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a LINE DIRECTION DIRECTION,
        typically outward or return.
    :ivar published_line_name: Name or Number by which the LINE is known
        to the public. +SIRI v2.0
    :ivar line_note: Special text associated with LINE.
    :ivar delivery_variant: Variant of a notice for use in a particular
        media channel. +SIRI v2.0
    :ivar situation_ref:
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
    published_line_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delivery_variant: List[DeliveryVariantStructure] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryVariant",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: List[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
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
class StopMonitoringMultipleRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Stop Monitoring Service on multiple
    stops.

    :ivar stop_monitoring_filter: Request particulars for an individual
        stop as part of a list of multiple= requests.
    :ivar version:
    """

    stop_monitoring_filter: List[StopMonitoringFilterStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringFIlter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StopMonitoringPermissions(PermissionsStructure):
    """
    Participants permissions to use the service, Only returned if requested.

    :ivar stop_monitoring_permission: Permission for a single
        participant or all participants to use an aspect of the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    stop_monitoring_permission: List[StopMonitoringServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringPermission",
            "type": "Element",
        },
    )


@dataclass
class StopMonitoringRequest(StopMonitoringRequestStructure):
    """
    Request for information about Stop Visits, i.e. arrivals and departures at
    a stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for Stop Monitoring Capabilities.

    :ivar topic_filtering: Available Filtering Capabilities.
    :ivar request_policy: Available Request Policy capabilities.
    :ivar subscription_policy: Available Subscription Policy
        capabilities.
    :ivar access_control: Available Optional Access control
        capabilities.
    :ivar response_features: Available Optional Response capabilities.
    """

    topic_filtering: Optional["StopMonitoringServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["StopMonitoringServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional[MonitoringCapabilityAccessControlStructure] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional["StopMonitoringServiceCapabilitiesStructure.ResponseFeatures"] = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class TopicFiltering:
        """
        :ivar default_preview_interval: Default preview interval.
            Default is 60 minutes.
        :ivar by_start_time: Whether a start time other than now can be
            specified for preview interval. Default  is 'truet.
        :ivar filter_by_monitoring_ref:
        :ivar filter_by_line_ref:
        :ivar filter_by_direction_ref:
        :ivar filter_by_destination:
        :ivar filter_by_visit_type: Whether results can be filtered by
            VistitType, e.g. arrivals, departures. Default True.
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
        by_start_time: Optional[bool] = field(
            default=None,
            metadata={
                "name": "ByStartTime",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
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
        filter_by_destination: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByDestination",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        filter_by_visit_type: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByVisitType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class RequestPolicy(StopMonitoringCapabilityRequestPolicyStructure):
        """
        :ivar has_detail_level: Whether Detail level filtering is
            supported. Default is ' false'.
        :ivar default_detail_level: Default Detail level if non
            specified on request. Default Normal.
        :ivar has_maximum_visits: Whether results can be limited to a
            maximum number. Default is 'true'.
        :ivar has_minimum_visits_per_line: Whether results can be
            limited to include a minimum number per LINE. Default is
            'true'.
        :ivar has_minimum_visits_per_via: Whether results can be limited
            to include a minimum numVIA (i.e. per JOURNEY PATTERN).
            +SIRI v2.0. default is 'false'.
        :ivar has_number_of_onwards_calls: If system can return detailed
            calling pattern, whether a number of onwards calls to
            include can be specified. Default is 'false'.
        :ivar has_number_of_previous_calls: If system can return
            detailed calling pattern, whether a number of previouscalls
            to include can be specified. Default is 'false'.
        """

        has_detail_level: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        default_detail_level: Optional[StopMonitoringDetailEnumeration] = field(
            default=None,
            metadata={
                "name": "DefaultDetailLevel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_maximum_visits: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMaximumVisits",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_minimum_visits_per_line: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMinimumVisitsPerLine",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        has_minimum_visits_per_via: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasMinimumVisitsPerVia",
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
    class ResponseFeatures:
        """
        :ivar has_line_notices: Whether result supports LINE events.
            Default is 'true'.
        :ivar has_situations: Whether result supports SITUATION
            REFERENCESs. Default is 'false'. +SIRI v2.0
        """

        has_line_notices: Optional[bool] = field(
            default=None,
            metadata={
                "name": "HasLineNotices",
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
class StopNotice(StopNoticeStructure):
    """
    Notice for stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopNoticeCancellation(StopNoticeCancellationStructure):
    """
    Reference to an previously communicated Notice which should now be removed
    from the arrival/departure board for the stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopLineNotice(StopLineNoticeStructure):
    """
    LINE notice for stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringMultipleRequest(StopMonitoringMultipleRequestStructure):
    """Request for information about Stop Visits, i.e. arrivals and departures
    at multiple stops stop.

    SIRI 1.3
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringServiceCapabilities(StopMonitoringServiceCapabilitiesStructure):
    """
    Capabilities of StopMonitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Type for Subscription Request for Stop Monitoring Service.

    :ivar stop_monitoring_request:
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

    stop_monitoring_request: Optional[StopMonitoringRequest] = field(
        default=None,
        metadata={
            "name": "StopMonitoringRequest",
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
class StopMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Stop Monitoring Service.

    :ivar stop_monitoring_service_capabilities:
    :ivar stop_monitoring_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    stop_monitoring_service_capabilities: Optional[StopMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "StopMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_permissions: Optional[StopMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "StopMonitoringPermissions",
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
class StopMonitoringDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Type for Delivery for Stop Monitoring Service.

    :ivar monitoring_ref: Reference to a stop monitoring point (LOGICAL
        DISPLAY that was requested. This can a be used to return the
        reference to the requested Monitoring Point  if there are no
        stop visits for the stop. Normally tere will only be one. SIRI
        v1.3
    :ivar monitoring_name: Name to use to describe monitoring point
        (Stop or display). Normally Consumer will already have access to
        this in its reference data but may be included to increase
        utility of delivery data i to devices that do not hold reference
        data, e.g. for SIRI LITE services(+SIRI v2.0).
    :ivar monitored_stop_visit:
    :ivar monitored_stop_visit_cancellation:
    :ivar stop_line_notice:
    :ivar stop_line_notice_cancellation:
    :ivar stop_notice: Notice for stop. (SIRI 2.0++)
    :ivar stop_notice_cancellation: Reference to an previously
        communicated Notice which should now be removed from the
        arrival/departure board for the stop.  (SIRI 2.0++)
    :ivar service_exception: Information about unavailablilty of some or
        all services at the  SIRI 2.0
    :ivar note: Text associated with whole delivery.  (Unbounded since
        SIRI 2.0)
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    monitoring_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringRef",
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
    monitored_stop_visit: List[MonitoredStopVisit] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredStopVisit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_stop_visit_cancellation: List[MonitoredStopVisitCancellation] = field(
        default_factory=list,
        metadata={
            "name": "MonitoredStopVisitCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_line_notice: List[StopLineNotice] = field(
        default_factory=list,
        metadata={
            "name": "StopLineNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_line_notice_cancellation: List[StopLineNoticeCancellation] = field(
        default_factory=list,
        metadata={
            "name": "StopLineNoticeCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_notice: List[StopNotice] = field(
        default_factory=list,
        metadata={
            "name": "StopNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_notice_cancellation: List[StopNoticeCancellation] = field(
        default_factory=list,
        metadata={
            "name": "StopNoticeCancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_exception: List[ServiceException] = field(
        default_factory=list,
        metadata={
            "name": "ServiceException",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Note",
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
class StopMonitoringSubscriptionRequest(StopMonitoringSubscriptionStructure):
    """
    Request for a subscription to Stop Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringCapabilitiesResponse(StopMonitoringCapabilitiesResponseStructure):
    """Capabilities for Stop Monitoring Service.

    Answers a StopMonitoringCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringDelivery(StopMonitoringDeliveryStructure):
    """
    Delivery for Stop Monitoring Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class StopMonitoringDeliveriesStructure:
    """Type for Deliveries for Stop Monitoring Service.

    Used in WSDL.

    :ivar stop_monitoring_delivery: Delivery for Stop Event service.
    """

    stop_monitoring_delivery: List[StopMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
