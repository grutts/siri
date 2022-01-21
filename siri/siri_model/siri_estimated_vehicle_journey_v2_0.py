from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri_model.siri_facility_v2_0 import (
    FacilityChangeElement,
    FacilityConditionElement,
)
from siri.siri_model.siri_journey_support_v2_0 import (
    ArrivalBoardingActivityEnumeration,
    CallStatusEnumeration,
    ConnectingJourneyRefStructure,
    DepartureBoardingActivityEnumeration,
    FirstOrLastJourneyEnumeration,
    FramedVehicleJourneyRefStructure,
)
from siri.siri_model.siri_journey_v2_0 import (
    ArrivalPlatformName,
    ArrivalProximityText,
    DeparturePlatformName,
    DepartureProximityText,
    JourneyNote,
    PredictionQualityStructure,
    SimpleContactStructure,
    StopAssignmentStructure,
    ViaNameStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    OccupancyEnumeration,
    PublishedLineName,
    StopPointName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_situation_identity_v1_1 import SituationRef
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import (
    EmptyType,
    Extensions,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourneyIndirectRefStructure:
    """
    Type for Origin and Destination stop of a VEHICLE JOURNEY.

    :ivar origin_ref: The origin is used to help identify the VEHICLE
        JOURNEY.
    :ivar aimed_departure_time: Departure time from origin SCHEDULED
        STOP POINT.
    :ivar destination_ref: The destination is used to help identify the
        VEHICLE JOURNEY.
    :ivar aimed_arrival_time: Arrival time at destination SCHEDULED STOP
        POINT.
    """

    origin_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
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


@dataclass
class WillWaitStructure:
    """
    Type for Will Wait details.

    :ivar wait_until_time: Time up until which the distributor will
        wait. +SIRI v2.0
    :ivar driver_has_acknowledge_will_wait: Whether an acknowledgement
        has been received that the driver will wait. +SIRI v2.0
    """

    wait_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "WaitUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    driver_has_acknowledge_will_wait: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DriverHasAcknowledgeWIllWait",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class EstimatedCallStructure:
    """
    Type for Rea-ltime info about a VEHICLE JOURNEY Stop.

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    :ivar extra_call: This call is additional and unplanned. If omitted:
        CALL is planned.
    :ivar cancellation: This call is a cancellation of a previously
        announced call.
    :ivar prediction_inaccurate: Whether the prediction for the specific
        stop is considered to be of a useful accuracy or not. Default is
        'false', i.e. prediction is not known to be inaccurate. {DOUBLE
        NEGATIVE IS BAD _ BETTER AS PredictionAccurate. Default is
        'true'?]. If prediction is degraded, e.g. because in congestion,
        used to 9indicate a lowered quality of data. Inherited property.
        {SHOULD THIS JUST BE THE SPECIFIC InCongestion INDICATOR
        INSTEAD, OR IS IT MORE GENERAL]
    :ivar occupancy: How full the bus is at the stop. If omitted:
        Passenger load is unknown.
    :ivar timing_point:
    :ivar boarding_stretch: Whether this is a Hail and Ride Stop.
        Default is 'false'.
    :ivar request_stop: Whether Vehicle stops only if requested
        explicitly by passenger. Default is 'false'.
    :ivar destination_display: Destination to show for the VEHICLE at
        the specific stop (vehicle signage), if different to the
        Destination Name for the full journey.
    :ivar call_note: Text annotation that applies to this CALL.
    :ivar facility_condition_element: Information about a change of
        Equipment availabilti at stop or on vehicle that may affect
        access or use.
    :ivar facility_change_element:
    :ivar situation_ref:
    :ivar aimed_arrival_time:
    :ivar expected_arrival_time:
    :ivar expected_arrival_prediction_quality: Prediction quality,
        either as approximate level, or more quantitayive percentile
        range of   predictions will  fall within a given range of times.
        +SIRI v2.0
    :ivar arrival_status:
    :ivar arrival_proximity_text:
    :ivar arrival_platform_name: Bay or platform (QUAY) name to show
        passenger i.e. expected platform for vehicel to arrive
        at.Inheritable property. Can be omitted if the same as the
        DeparturePlatformName If there no arrival platform name separate
        from the departure platform name, the precedence is (i) any
        arrival platform on any related dated timetable element, (ii)
        any departure platform name on this estimated element; (iii) any
        departure platform name on any related dated timetable CALL.
    :ivar arrival_boarding_activity: Nature of boarding and alighting
        allowed at stop. Default is 'Alighting'.
    :ivar arrival_stop_assignment: Assignment of arrival of Scheduled
        STOP POINT to a phsyical QUAY (platform). If not given, assume
        same as for departure +SIRI v2.0.
    :ivar arrival_operator_refs: OPERATORs of of servcie up until
        arrival.. May change for departure. +SIRI v2.0.
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE, most likely taking into account all control actions
        such as waiting.
    :ivar provisional_expected_departure_time: Expected departure time
        of VEHICLE without waiting time due to operational actions. For
        people at stop this would normally be shown if different from
        Expected departure time. So if servcie decides not to wait may
        leave earler than expected departure time +SIRI v2.0.
    :ivar earliest_expected_departure_time: Earliest time at which
        VEHICLE may leave the stop. Used to secure connections. Used for
        passenger announcements. Passengers must be at boarding point by
        this time to be sure of catching VEHICLE.  i.e. "Vehicle will
        not leave before this time" - may be revised from original aimed
        time. +SIRI v2.0
    :ivar expected_departure_prediction_quality: Prediction quality,
        either as approximate level, or more quantitayive percentile
        range of   predictions will  fall within a given range of times.
        +SIRI v2.0
    :ivar aimed_latest_passenger_access_time: Target Latest time at
        which a PASSENGER should aim to arrive at the STOP PLACE
        containing the stop. This time may be earlier than the VEHICLE
        departure times as itmay include time for processes such as
        checkin, security, etc.(As specified by CHECK CONSTRAINT DELAYs
        in the underlying data) If absent assume to be the same as
        Earliest expected departure time, +SIRI v2.0
    :ivar expected_latest_passenger_access_time: Expected Latest time at
        which a PASSENGER should aim to arrive at the STOP PLACE
        containing the stop. This time may be earlier than the VEHICLE
        departure times as it may include time for processes such as
        checkin, security, etc.(As specified by CHECK CONSTRAINT DELAYs
        in the underlying data) If absent assume to be the same as
        Earliest expected departure time, +SIRI v2.0
    :ivar departure_status:
    :ivar departure_proximity_text:
    :ivar departure_platform_name: Departure QUAY ( Bay or platform)
        name. Defaulted taken from  from planned timetable..
    :ivar departure_boarding_activity:
    :ivar departure_stop_assignment: Assignments of departure platfiorm
        for Scheduled STOP POINT to a physical QUAY. +SIRI v2.0.
    :ivar departure_operator_refs: OPERATORs of of service for
        departure and onwards.. May change from that for arrival. +SIRI
        v2.0.
    :ivar aimed_headway_interval:
    :ivar expected_headway_interval:
    :ivar distance_from_stop: Distance of VEHICLE from stop of CALL as
        measured along ROUTE track. Only shown if detail level is
        'calls' or higher. Positive value denotes distance before stop.
        +SIRI v2.0.
    :ivar number_of_stops_away: Count of stops along SERVICE PATTERN
        between current position of VEHICLE and stop of CALL as measured
        along ROUTE track. Only shown if detail level is 'calls' or
        higher. +SIRI v2.0.
    :ivar extensions:
    """

    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
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
    extra_call: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occupancy: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timing_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding_stretch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingStretch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequestStop",
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
    call_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "CallNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_condition_element: List[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
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
    expected_arrival_prediction_quality: Optional[PredictionQualityStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalPredictionQuality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_proximity_text: Optional[ArrivalProximityText] = field(
        default=None,
        metadata={
            "name": "ArrivalProximityText",
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
    arrival_boarding_activity: Optional[ArrivalBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_stop_assignment: Optional[StopAssignmentStructure] = field(
        default=None,
        metadata={
            "name": "ArrivalStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_operator_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ArrivalOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    provisional_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ProvisionalExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    earliest_expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EarliestExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_prediction_quality: Optional[PredictionQualityStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedDeparturePredictionQuality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_latest_passenger_access_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_latest_passenger_access_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedLatestPassengerAccessTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_status: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_proximity_text: Optional[DepartureProximityText] = field(
        default=None,
        metadata={
            "name": "DepartureProximityText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: Optional[DeparturePlatformName] = field(
        default=None,
        metadata={
            "name": "DeparturePlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_boarding_activity: Optional[DepartureBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "DepartureBoardingActivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_stop_assignment: Optional[StopAssignmentStructure] = field(
        default=None,
        metadata={
            "name": "DepartureStopAssignment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_operator_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DepartureOperatorRefs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AimedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ExpectedHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distance_from_stop: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number_of_stops_away: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfStopsAway",
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
class EstimatedServiceJourneyInterchangeStructure:
    """
    Type for Estimated SERVICE JOURNEY INTERCHANGE.

    :ivar interchange_ref:
    :ivar feeder_journey_ref: Reference to a connecting distributor
        VEHICLE JOURNEY. +SIRI v2.0
    :ivar distributor_journey_ref: Reference to a connecting distributor
        VEHICLE JOURNEY. +SIRI v2.0
    :ivar will_not_wait: Distributor will not wait (i.e. connection
        broken) SIRI w.0
    :ivar will_wait: Nature of wait that distributer will make. +SIRI
        v2.0
    :ivar expected_departure_time_of_distributor: Time at which
        distributor VEHICLE is expected to depart. +SIRI v2.0
    :ivar connection_monitoring: Whether connection monitoring is active
        or not for this connection +SIRI v2.0
    """

    interchange_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_journey_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FeederJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_journey_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributorJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    will_not_wait: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "WillNotWait",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    will_wait: Optional[WillWaitStructure] = field(
        default=None,
        metadata={
            "name": "WillWait",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_time_of_distributor: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTimeOfDistributor",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoring",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class RecordedCallStructure:
    """
    Type for  recroded Real-time info about a VEHICLE JOURNEY Stop.

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    :ivar extra_call: This call is additional and unplanned. If omitted:
        CALL is planned.
    :ivar cancellation: This call is a cancellation of a previously
        announced call.
    :ivar prediction_inaccurate: Whether the prediction for the specific
        stop is considered to be of a useful accuracy or not. Default is
        'false', i.e. prediction is not known to be inaccurate. {DOUBLE
        NEGATIVE IS BAD _ BETTER AS PredictionAccurate. Default is
        'true'?]. If prediction is degraded, e.g. because in congestion,
        used to 9indicate a lowered quality of data. Inherited property.
        {SHOULD THIS JUST BE THE SPECIFIC InCongestion INDICATOR
        INSTEAD, OR IS IT MORE GENERAL]
    :ivar occupancy: How full the bus is at the stop. If omitted:
        Passenger load is unknown.
    :ivar aimed_arrival_time:
    :ivar expected_arrival_time:
    :ivar actual_arrival_time:
    :ivar arrival_platform_name: Bay or platform (QUAY) name to show
        passenger i.e. expected platform for vehicel to arrive
        at.Inheritable property. Can be omitted if the same as the
        DeparturePlatformName If there no arrival platform name separate
        from the departure platform name, the precedence is (i) any
        arrival platform on any related dated timetable element, (ii)
        any departure platform name on this estimated element; (iii) any
        departure platform name on any related dated timetable CALL.
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE.
    :ivar departure_platform_name: Departure QUAY ( Bay or platform)
        name. Defaulted taken from  from planned timetable..
    :ivar actual_departure_time: Estimated time of departure of VEHICLE.
    :ivar extensions:
    """

    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
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
    extra_call: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occupancy: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "Occupancy",
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
    actual_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
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
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    departure_platform_name: Optional[DeparturePlatformName] = field(
        default=None,
        metadata={
            "name": "DeparturePlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTime",
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
class EstimatedCall(EstimatedCallStructure):
    """
    Ordered sequence of SCHEDULED STOP POINTs called at by the VEHICLE JOURNEY
    If IsCompleteStopSequence is false, may be just those stops that are
    altered.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedServiceJourneyInterchange(EstimatedServiceJourneyInterchangeStructure):
    """
    A VEHICLE JOURNEY taking place on a particular date that will be managed by
    an AVMs.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class RecordedCall(RecordedCallStructure):
    """
    Ordered sequence of SCHEDULED STOP POINTs called at by the VEHICLE JOURNEY
    If IsCompleteStopSequence is false, may be just those stops that are
    altered.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EstimatedVehicleJourneyStructure:
    """
    Type for Real-time info about a VEHICLE JOURNEY.

    :ivar line_ref: Reference to a LINE.
    :ivar direction_ref: Reference to a LINE DIRECTION DIRECTION,
        typically outward or return.
    :ivar dated_vehicle_journey_ref: Reference to a dated VEHICLE
        JOURNEY.
    :ivar dated_vehicle_journey_indirect_ref: If no VEHICLE JOURNEY
        reference is available, identify it by origin and destination
        and the scheduled times at these stops.
    :ivar estimated_vehicle_journey_code: If this is the first message
        about an extra unplanned VEHICLE JOURNEY, a new and unique code
        must be given for it. ExtraJourney should be set to 'true'.
    :ivar extra_journey: Whether this VEHICLE JOURNEY is an addition to
        the planning data already sent. Default is 'false': i.e. not an
        additional journey.
    :ivar cancellation: Whether this VEHICLE JOURNEY is a deletion of a
        previous scheduled journey. Default is 'false': this is not a
        VEHICLE JOURNEY that has been cancelled. An Extra Journey may be
        deleted.
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
    :ivar origin_ref:
    :ivar origin_name: Name of the origin of the journey.  (Unbounded
        since SIRI 2.0)
    :ivar origin_short_name: Short name of the origin of the journey;
        used to help identify the VEHICLE JOURNEY on arrival boards. If
        absent, same as Origin Name.
    :ivar destination_display_at_origin: DIRECTION name shown for
        joruney at the origin. +SIRI v2.0
    :ivar via: Names of VIA points, used to help identify the LINE, for
        example, Luton to Luton via Sutton. Currently 3 in VDV. Should
        only be included if the detail level was requested.
    :ivar destination_ref: Reference to a DESTINATION.
    :ivar destination_name: Description of the destination stop (vehicle
        signage), Can be overwritten for a journey, and then also
        section by section by the entry in an individual CALl.
        (Unbounded since SIRI 2.0)
    :ivar destination_short_name: Short name of the DESTINATION.of the
        journey; used to help identify the VEHICLE JOURNEY on arrival
        boards. If absent, same as DestinationName.  (Unbounded since
        SIRI 2.0)
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
    :ivar vehicle_journey_name: For train services with named journeys.
        Train name, e.g. “West Coast Express”. If omitted: No train
        name. Inherited property.  (Unbounded since SIRI 2.0)
    :ivar journey_note:
    :ivar public_contact: Contact details for use by members of public.
        +SIRI v2.0
    :ivar operations_contact: Contact details for use by operational
        staff. +SIRI v2.0
    :ivar headway_service: Whether this is a Headway Service, that is
        shown as operating at a prescribed interval rather than to a
        fixed timetable. Inherited property: if omitted: same as
        indicated by (i) any preceding update message, or (ii) if no
        preceding update, by the referenced dated VEHICLE JOURNEY.
    :ivar first_or_last_journey:
    :ivar facility_condition_element: Information about a change of
        Equipment availabilti at stop or on vehicle that may affect
        access or use.
    :ivar facility_change_element:
    :ivar situation_ref:
    :ivar monitored: Whether the VEHICLE JOURNEY is monitored by an
        AVMS: true if active. Inherited property: if omitted: same as
        indicated by (i) any preceding update message, or (ii) if no
        preceding update, by the referenced dated VEHICLE JOURNEY.
    :ivar prediction_inaccurate: Whether the prediction for the journey
        is considered to be of a useful accuracy or not. Default is
        'false'.
    :ivar occupancy: How full the bus is. If omitted: Passenger load is
        unknown.
    :ivar block_ref: BLOCK that VEHICLE is running.
    :ivar course_of_journey_ref: COURSE OF JOURNEY ('Run') that VEHICLE
        is running.
    :ivar vehicle_journey_ref:
    :ivar vehicle_ref:
    :ivar additional_vehicle_journey_ref: Refercence to other VEHICLE
        Journeys (+SIRI v2.0)
    :ivar driver_ref: A reference to the DRIVER or Crew currently logged
        in to operate a monitored VEHICLE. May be omitted if real-time
        data is not available - i.e. it is timetabled data. +SIRI v2.0
    :ivar driver_name: The name oo the Driver or Crew   +SIRI v2.0
    :ivar estimated_calls:
    :ivar is_complete_stop_sequence: Whether the above call sequence is
        complete, i.e. represents every CALL of the SERVICE PATTERN and
        so can be used to replace a previous call sequence. Default is
        'false'.
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
    dated_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey_indirect_ref: Optional[DatedVehicleJourneyIndirectRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyIndirectRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_vehicle_journey_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstimatedVehicleJourneyCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extra_journey: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
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
    origin_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display_at_origin: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayAtOrigin",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    via: List[ViaNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
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
    destination_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationShortName",
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
    vehicle_journey_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_note: List[JourneyNote] = field(
        default_factory=list,
        metadata={
            "name": "JourneyNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    public_contact: Optional[SimpleContactStructure] = field(
        default=None,
        metadata={
            "name": "PublicContact",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operations_contact: Optional[SimpleContactStructure] = field(
        default=None,
        metadata={
            "name": "OperationsContact",
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
    first_or_last_journey: Optional[FirstOrLastJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_condition_element: List[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
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
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occupancy: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    block_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    course_of_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneyRef",
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
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    additional_vehicle_journey_ref: List[FramedVehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    driver_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    driver_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DriverName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_calls: Optional["EstimatedVehicleJourneyStructure.EstimatedCalls"] = field(
        default=None,
        metadata={
            "name": "EstimatedCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    is_complete_stop_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCompleteStopSequence",
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
    class EstimatedCalls:
        estimated_call: List[EstimatedCall] = field(
            default_factory=list,
            metadata={
                "name": "EstimatedCall",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class EstimatedVehicleJourney(EstimatedVehicleJourneyStructure):
    """
    A VEHICLE JOURNEY taking place on a particular date that will be managed by
    an AVMs.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
