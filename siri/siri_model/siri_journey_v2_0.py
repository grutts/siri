from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri_model.siri_journey_support_v2_0 import (
    ArrivalBoardingActivityEnumeration,
    CallStatusEnumeration,
    DepartureBoardingActivityEnumeration,
    FirstOrLastJourneyEnumeration,
    QualityIndexEnumeration,
)
from siri.siri_model.siri_reference_v2_0 import (
    PlaceNameStructure,
    StopPointName,
)
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ActualArrivalTime:
    """
    Observed time of arrival of VEHICLE at stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ActualDepartureTime:
    """
    Observed time of departure of VEHICLE from stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class AimedArrivalTime:
    """
    Target arrival time of VEHICLE at stop according to latest working
    timetable.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class AimedDepartureTime:
    """
    Target departure time of VEHICLE from stop according to latest working
    timetable.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class AimedHeadwayInterval:
    """
    For frequency based services, target interval between vehicles at stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class AimedLatestPassengerAccessTime:
    """Latest target time at which a PASSENGER should aim to arrive at the STOP
    PLACE containing the stop.

    This time may be earlier than the VEHICLE departure times and may
    include time for processes such as checkin, security, etc.(As
    specified by CHECK CONSTRAINT DELAYs in the underlying data) If
    absent assume to be the same as Earliest expected departure time,
    +SIRI 2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ExpectedArrivalTime:
    """
    Estimated time of arriival of VEHICLE at stop .
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ExpectedDepartureTime:
    """
    Estimated time of departure of VEHICLE from stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ExpectedHeadwayInterval:
    """
    For frequency based services, expected interval between vehicles at stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ExpectedLatestPassengerAccessTime:
    """Latest expected time at which a PASSENGER should aim to arrive at the
    STOP PLACE containing the stop.

    This time may be earlier than the VEHICLE departure times and may
    include time for processes such as checkin, security, etc.(As
    specified by CHECK CONSTRAINT DELAYs in the underlying data) If
    absent assume to be the same as Earliest expected departure time,
    +SIRI 2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class ProgressBetweenStopsStructure:
    """
    Type for Progress between stops.

    :ivar link_distance: The total distance in metres between the
        previous stop and the next stop.
    :ivar percentage: Percentage along link that VEHICLE has travelled.
    """

    link_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LinkDistance",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SimpleContactStructure:
    """
    Type for Simple Contact Details.

    :ivar phone_number: Phone number +SIRI v2.0
    :ivar url: Url for contact +SIRI v2.0
    """

    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractCallStructure:
    """
    Type for Abstract CALL at stop.

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
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


@dataclass
class AbstractMonitoredCallStructure:
    """
    Type for Abstract CALL at stop.

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    """

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
class ArrivalBoardingActivity:
    """Type of boarding and alighting allowed at stop.

    Default is 'Alighting'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ArrivalBoardingActivityEnumeration = field(
        default=ArrivalBoardingActivityEnumeration.ALIGHTING,
        metadata={
            "required": True,
        },
    )


@dataclass
class ArrivalPlatformName(NaturalLanguageStringStructure):
    """Bay or platform name.

    Inheritable property. Can be omitted if the same as the
    DeparturePlatformName If there no arrival platform name separate
    from the departure platform name, the precedence is (i) any arrival
    platform on any related dated timetable element, (ii) any departure
    platform name on this estimated element; (iii) any departure
    platform name on any related dated timetable CALL.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalProximityText(NaturalLanguageStringStructure):
    """Arbitrary text string to show to indicate the status of the departure of
    the VEHICLE for example, “Enroute”, “5 Km”, “Approaching”.

    May depend on the policy of the OPERATOR, for example show
    “Approaching” if less than 200metres away from stop. +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalStatus:
    """Classification of the timeliness of the visit according to a fixed list
    of values.

    If not specified, same as DepartureStatus.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class DepartureBoardingActivity:
    """Nature of boarding allowed at stop.

    Default is 'Boarding'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DepartureBoardingActivityEnumeration = field(
        default=DepartureBoardingActivityEnumeration.BOARDING,
        metadata={
            "required": True,
        },
    )


@dataclass
class DeparturePlatformName(NaturalLanguageStringStructure):
    """Departure QUAY ( Bay or platform) name.

    Inheritable property.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DepartureProximityText(NaturalLanguageStringStructure):
    """Arbitrary text string to show to indicate the status of the departure of
    the vehicle, for example, “Boarding”, “GatesClosed”.

    +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DepartureStatus:
    """Classification of the timeliness of the departure part of the CALL,
    according to a fixed list of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are still classified as on-time.
    Applications may use this to guide their own presentation of times.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class DestinationName(NaturalLanguagePlaceNameStructure):
    """The name of the DESTINATION of the journey; used to help identify the
    VEHICLE to the public.

    Note when used in a CALL, this is the Dynamic Destination Display:
    since vehicles can change their destination during a journey, the
    destination included here should be what the VEHICLE will display
    when it reaches the stop.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DestinationStructure:
    """
    Type for Information about a DESTINATION.

    :ivar destination_ref: Identifer of Destinatioin
    :ivar destination_name: Name of Destination
    """

    destination_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    destination_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class DirectionStructure:
    """
    Type for DIRECTION.

    :ivar direction_ref: Identifer of DIRECTION,
    :ivar direction_name: Description of DIRECTION.  (Unbounded since
        SIRI 2.0)
    """

    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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


@dataclass
class FirstOrLastJourney:
    """Whether journey is first or last journey of day.

    +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FirstOrLastJourneyEnumeration = field(
        default=FirstOrLastJourneyEnumeration.UNSPECIFIED,
        metadata={
            "required": True,
        },
    )


@dataclass
class JourneyNote(NaturalLanguageStringStructure):
    """Additional descriptive text associated with journey.

    Inherited property.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class OriginName(NaturalLanguagePlaceNameStructure):
    """
    The name of the origin of the journey; used to help identify the VEHICLE
    JOURNEY on arrival boards.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class PlannedStopAssignmentStructure:
    """
    Type for assignment of a SCHEDULED STOP POINT to a specific QUAY or
    platform +SIRI v2.0.

    :ivar aimed_quay_ref: Physical QUAY to use according to the planned
        timetable. +SIRI v2.0
    :ivar aimed_quay_name: Scheduled Platform name. +SIRI v2.0
    """

    aimed_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AimedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_quay_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AimedQuayName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PredictionQualityStructure:
    """
    Type for Prediction Quality quantifcation.

    :ivar prediction_level: An approxiimate characterisation of
        prediction quality as one of five values . +SIRI v2.0
    :ivar percentile: Percentile associated with range as specified by
        lower and upper bound +SIRI v2.0
    :ivar lower_time_limit: Lower bound on time of for prediction  for
        confidence level if different from defaults  +SIRI v2.0
    :ivar higher_time_limit: Upper bound on time of for predictios  for
        confidence level if different from defaults  +SIRI v2.0
    """

    prediction_level: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "PredictionLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    percentile: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentile",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lower_time_limit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LowerTimeLimit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    higher_time_limit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "HigherTimeLimit",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class StopAssignmentStructure:
    """
    Type for assignment of a SCHEDULED STOP POINT to a specific QUAY or
    platform +SIRI v2.0.

    :ivar aimed_quay_ref: Physical QUAY to use according to the planned
        timetable. +SIRI v2.0
    :ivar aimed_quay_name: Scheduled Platform name. Can be used to
        indicate platfrom change. +SIRI v2.0
    :ivar expected_quay_ref: Physical QUAY to use accoring to the real-
        time prediction. +SIRI v2.0
    :ivar actual_quay_ref: Physical QUAY actually used. +SIRI v2.0
    """

    aimed_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AimedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_quay_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AimedQuayName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpectedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_quay_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ViaName(NaturalLanguagePlaceNameStructure):
    """Names of VIA points, used to help identify the LINEfor example, Luton to
    Luton via Sutton.

    Currently 3 in VDV. Should only be included if the detail level was
    requested.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ViaNameStructure(PlaceNameStructure):
    """
    Type for VIA NAMes structure.

    :ivar via_priority: Relative priority to give to VIA name in
        displays. 1=high. Default is 2. +SIRI v2.0
    """

    via_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ViaPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class Direction(DirectionStructure):
    """
    Description of a DIRECTION.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class OnwardCallStructure(AbstractMonitoredCallStructure):
    """
    Type Onwards CALLs at stop.

    :ivar vehicle_at_stop:
    :ivar timing_point:
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

    vehicle_at_stop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
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
class OnwardCallsStructure:
    """
    Type for CALLing pattern for JOURNEY PATTERN.
    """

    onward_call: List[OnwardCallStructure] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
