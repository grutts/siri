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
    DepartureBoardingActivityEnumeration,
    FirstOrLastJourneyEnumeration,
    FramedVehicleJourneyRefStructure,
    ProgressRateEnumeration,
    QualityIndexEnumeration,
    VehicleStatusEnumeration,
)
from siri.siri_model.siri_journey_v2_0 import (
    AbstractMonitoredCallStructure,
    ArrivalPlatformName,
    ArrivalProximityText,
    DeparturePlatformName,
    DepartureProximityText,
    JourneyNote,
    OnwardCallsStructure,
    PredictionQualityStructure,
    SimpleContactStructure,
    StopAssignmentStructure,
    ViaNameStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    OccupancyEnumeration,
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_situation_identity_v1_1 import SituationRef
from siri.siri_utility.siri_location_v2_0 import LocationStructure
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyPartInfoStructure:
    """Type for a refernces to  JOURNEY PARTs.

    +SIRI v2.0

    :ivar journey_part_ref: Refrence to a JOURNEY part. +SIRI v2.0
    :ivar train_number_ref: Train Number for JOURNEY PART +SIRI v2.0
    :ivar operator_ref: Operator of JOURNEY PART. +SIRI v2.0
    """

    journey_part_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    train_number_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
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


@dataclass
class MonitoredCallStructure(AbstractMonitoredCallStructure):
    """
    Type for Current CALL at stop.

    :ivar vehicle_at_stop:
    :ivar vehicle_location_at_stop: Exact location that VEHICLE will
        take up / or has taken at STOP POINT.
    :ivar reverses_at_stop: Whether VEHICLE will reverse at stop.
        Default is 'false'.
    :ivar platform_traversal: For Rail, whether this is a platform
        traversal at speed, typically triggering an announcement to
        stand back from platform. If so Boarding Activity of arrival and
        deparure should be passthrough.
    :ivar signal_status: Status of signal clearance for TRAIN. This may
        affect the prioritiisition and emphasis given to arrival or
        departure on displays - e.g. cleared trains appear first,
        flashing in green.
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
    :ivar aimed_arrival_time: Target arrival time of VEHICLE according
        to latest working timetable.
    :ivar actual_arrival_time: Observed time of arrival of VEHICLE.
    :ivar expected_arrival_time: Estimated time of arriival of VEHICLE.
    :ivar latest_expected_arrival_time: Latest time at which a VEHICLE
        will arrive at stop. +SIRI v2.0
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
    :ivar actual_departure_time: Observed time of departure of VEHICLE
        from stop.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE from stop. May include waiting time. For people on a
        VEHICLE this is the time that would normally be shown.
    :ivar provisional_expected_departure_time: Expected departure time
        of VEHICLE without waiting time due to operational actions. For
        people at stop this would normally be shown if different from
        Expected Departure time. +SIRI v2.0.
    :ivar earliest_expected_departure_time: Earliest time at which
        VEHICLE may leave the stop. Used to secure connections.
        Passengers must be at boarding point by this time to be sure of
        catching VEHICLE. +SIRI v2.0
    :ivar expected_departure_prediction_quality: Prediction quality,
        either as approcimate level, or more quantitatyive percentile
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

    vehicle_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location_at_stop: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocationAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reverses_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversesAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    platform_traversal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlatformTraversal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    signal_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignalStatus",
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
    actual_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
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
    latest_expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestExpectedArrivalTime",
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
    actual_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTime",
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
class PreviousCallStructure(AbstractMonitoredCallStructure):
    """
    Type for CALL at previous stop.

    :ivar vehicle_at_stop:
    :ivar aimed_arrival_time: Target arrival time of VEHICLE according
        to latest working timetable.
    :ivar actual_arrival_time: Observed time of arrival of VEHICLE.
    :ivar expected_arrival_time: Estimated time of arriival of VEHICLE.
    :ivar aimed_departure_time: Target departure time of VEHICLE
        according to latest working timetable.
    :ivar actual_departure_time: Observed time of departure of VEHICLE
        from stop.
    :ivar expected_departure_time: Estimated time of departure of
        VEHICLE from stop. May include waiting time. For people on a
        VEHICLE this is the time that would normally be shown.
    :ivar extensions:
    """

    vehicle_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
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
    actual_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTime",
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
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
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
class TrainBlockPartStructure:
    """
    Type for BLOCK part elements of VEHICLE JOURNEY.

    :ivar number_of_block_parts: Total number of BLOCK parts making up
        the train of which this is part.
    :ivar train_part_ref: Reference to a train BLOCK part.
    :ivar position_of_train_block_part: Description of position of Train
        BLOCK Part within Train to guide passengers where to find it.
        E.g. 'Front four coaches'.
    """

    number_of_block_parts: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfBlockParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    train_part_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainPartRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    position_of_train_block_part: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PositionOfTrainBlockPart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PreviousCallsStructure:
    """
    Type for Ordered list of CALLs at previous stop.
    """

    previous_call: List[PreviousCallStructure] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class MonitoredVehicleJourneyStructure:
    """
    Type for Monitored VEHICLE JOURNEY.

    :ivar line_ref: Reference to LINE of journey.
    :ivar direction_ref: Reference to DIRECTION of journey.
    :ivar framed_vehicle_journey_ref: A reference to the DATED VEHICLE
        JOURNEY that the VEHICLE is making, unique with the data horizon
        of the service.
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
        fixed timetable. Default is 'false'.
    :ivar origin_aimed_departure_time: Timetabled departure time from
        Origin.
    :ivar destination_aimed_arrival_time: Timetabled arrival time at
        Destination.
    :ivar first_or_last_journey:
    :ivar facility_condition_element: Information about a change of
        Equipment availabilti at stop or on vehicle that may affect
        access or use.
    :ivar facility_change_element:
    :ivar situation_ref:
    :ivar monitored: Whether there is real-time information available
        for journey; if not present, not known.
    :ivar monitoring_error: Condition indicating nature of real-time
        fault. Present if VEHICLE JOURNEY is normally monitored but
        temporarily cannot be Monitored for a known reason.
    :ivar in_congestion: Whether the VEHICLE iis in traffic congestion.
        If not, present, not known.
    :ivar in_panic: Whether the panic alarm on the VEHICLE is activated.
        This may lead to indeterminate predictions. If absent, default
        is 'false'.
    :ivar prediction_inaccurate: Whether the prediction should be judged
        as inaccurate.
    :ivar data_source: System originating real-time data. Can be used to
        make judgements of relative quality and accuracy compared to
        other feeds.
    :ivar confidence_level: Confidence QUALITY LEVEL of data. Default is
        'reliable'.
    :ivar vehicle_location: Current geospatial location of VEHICLE.
        Measured to front of vehicle.
    :ivar bearing: Bearing in compass degrees in which VEHICLE is
        heading.
    :ivar progress_rate: Rate of progress of VEHICLE. Default is
        'normal'
    :ivar velocity: Velocity of VEHICLE. EIther actual speed or average
        speed may be used. +SIRI v2.0
    :ivar engine_on: Whether the engine of the vehicle is on. Default is
        'true' (+SIRI 2.0)
    :ivar occupancy: How full the VEHICLE is.  If omitted, not known.
    :ivar delay: Delay of VEHICLE against schedule, to a precision in
        seconds. Early times are shown as negative values.
    :ivar progress_status: An arbitrary textual  status description of
        the running of this VEHICLE JOURNEY.  (Unbounded 0:* since SIRI
        2.0)
    :ivar vehicle_status: An classification of the progress state of
        running of this VEHICLE JOURNEY. +SIRI 2.0
    :ivar train_block_part: If a VEHICLE JOURNEY is a coupled journey,
        i.e. comprises several coupled BLOCKparts, there will be a
        separate delivery for each BLOCKp art and this element will
        indicate the vehicles that the journey part uses.
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
    :ivar train_numbers: TRAIN NUMBERs for journey. +SIRI v2.0
    :ivar journey_parts: JOURNEY PARTs making up JOURNEY +SIRIv2.0 e.
    :ivar previous_calls: Information on stops called at previously,
        origin and all intermediate stops up to but not including the
        current stop, in order or visits. Should only be included if the
        detail level was requested.
    :ivar monitored_call: Monitored CALL at the current stop. For SIRI-
        SM this is the stop for which data is requested. For SIRI-VM
        this is the most recent stop visited by the VEHICLE.
    :ivar onward_calls: Information on CALLs at the intermediate stops
        beyond the current stop, up to and including the destination, in
        order of visits. Should only be included if the detail level was
        requested.
    :ivar is_complete_stop_sequence: Whether the above CALL sequence is
        complete, i.e. represents every CALL of the ROUTE and so can be
        used to replace a previous CALL sequence. Default is 'false'.
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
    origin_aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OriginAimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DestinationAimedArrivalTime",
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
    monitoring_error: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    in_congestion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InCongestion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    in_panic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InPanic",
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
    data_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    confidence_level: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "ConfidenceLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_rate: Optional[ProgressRateEnumeration] = field(
        default=None,
        metadata={
            "name": "ProgressRate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    velocity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Velocity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    engine_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EngineOn",
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
    delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_status: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ProgressStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_status: Optional[VehicleStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_block_part: List[TrainBlockPartStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
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
    train_numbers: Optional["MonitoredVehicleJourneyStructure.TrainNumbers"] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_parts: Optional["MonitoredVehicleJourneyStructure.JourneyParts"] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    previous_calls: Optional[PreviousCallsStructure] = field(
        default=None,
        metadata={
            "name": "PreviousCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_call: Optional[MonitoredCallStructure] = field(
        default=None,
        metadata={
            "name": "MonitoredCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    onward_calls: Optional[OnwardCallsStructure] = field(
        default=None,
        metadata={
            "name": "OnwardCalls",
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

    @dataclass
    class TrainNumbers:
        """
        :ivar train_number_ref: TRAIN NUMBER  assigned to VEHICLE
            JOURNEY.  +SIRI  2.0
        """

        train_number_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "TrainNumberRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class JourneyParts:
        """
        :ivar journey_part_info: Information about Parts of JOURNEY
            +SIRI v2.0
        """

        journey_part_info: List[JourneyPartInfoStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
