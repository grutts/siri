from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from siri.siri_model.siri_facility_v2_0 import (
    FacilityChangeElement,
    FacilityConditionElement,
)
from siri.siri_model.siri_journey_support_v2_0 import (
    FirstOrLastJourneyEnumeration,
    FramedVehicleJourneyRefStructure,
)
from siri.siri_model.siri_journey_v2_0 import (
    JourneyNote,
    SimpleContactStructure,
    ViaNameStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    VehicleModesEnumeration,
)
from siri.siri_model.siri_situation_identity_v1_1 import SituationRef
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InterchangeJourneyStructure:
    """
    Type for feeder or Distributor Journey info about a VEHICLE JOURNEY.

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
    :ivar monitored: Whether there is real-time information available
        for journey; if not present, not known.
    :ivar aimed_departure_time: On a Distributor journey , a Timetabled
        departure time of the VEHICLE JOURNEY from the CONNECTION LINK
        for the SERVICE JOURNEY INTERCHANGE. On a Feeder journey a
        Timetabled arrival time of the VEHICLE JOURNEY at the CONNECTION
        link for the SERVICE JOURNEY INTERCHANGE.
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
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
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
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
