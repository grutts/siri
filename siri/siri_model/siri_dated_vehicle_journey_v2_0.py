from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri_model.siri_journey_support_v2_0 import (
    ArrivalBoardingActivityEnumeration,
    ConnectingJourneyRefStructure,
    DepartureBoardingActivityEnumeration,
    FirstOrLastJourneyEnumeration,
    FramedVehicleJourneyRefStructure,
)
from siri.siri_model.siri_journey_v2_0 import (
    ArrivalPlatformName,
    DeparturePlatformName,
    JourneyNote,
    PlannedStopAssignmentStructure,
    SimpleContactStructure,
)
from siri.siri_model.siri_reference_v2_0 import (
    PublishedLineName,
    StopPointName,
    VehicleModesEnumeration,
)
from siri.siri_utility.siri_types_v2_0 import (
    NaturalLanguagePlaceNameStructure,
    NaturalLanguageStringStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceJourneyInterchangeStructure:
    """A planned SERVICE JOURNEY INTERCHANGE between two journeys.

    +SIRI v2.0

    :ivar interchange_code: Identifier of SERVICE JOURNEY INTERCHANGE.
        +SIRI v2.0
    :ivar connection_link_ref: Reference to a physical CONNECTION LINK
        over which the SERVICE JOURNEY INTERCHANGE takes place. +SIRI
        v2.0
    :ivar feeder_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI v2.0
    :ivar feeder_arrival_stop_ref: SCHEDULED STOP POINT at which feeder
        journey arrives. +SIRI v2.0
    :ivar feeder_visit_number: Sequence of visit to Feeder stop within
        Feeder JOURNEY PATTERN.
    :ivar distributor_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI
        v2.0
    :ivar distributor_departure_stop_ref: SCHEDULED STOP POINT at which
        distributor journet departs. +SIRI v2.0
    :ivar distributor_visit_number: Sequence of visit to Distributor
        stop within Distributor JOURNEY PATTERN.
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE. SIRI
        v2,0
    :ivar maximum_wait_time: Maximum time that Distributor will wait for
        Feeder for INTERCHANGE. SIRI v1.0
    :ivar maximum_automatic_wait_time: Maximum automatic wait time that
        Distributor will wait for Feeder for INTERCHANGE. +SIRI v2.0
    :ivar standard_transfer_time: Standard transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar minimum_transfer_time: Minimum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar extensions:
    """

    interchange_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
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
    feeder_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_arrival_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FeederVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_departure_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorDepartureStopRef",
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
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
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
class ContextualisedConnectionLinkStructure:
    """Connection between two stops within a connection area.

    Used within the context of one or other end.

    :ivar connection_link_code: Identifier of CONNECTION LINk.
    :ivar stop_point_ref:
    :ivar stop_point_name:
    :ivar default_duration: Default time (Duration) needeed to traverse
        SERVICE JOURNEY INTERCHANGE from feeder to distributor.
    :ivar frequent_traveller_duration: Time needeed by a traveller whis
        is familiar with SERVICE JOURNEY INTERCHANGE to traverse it. If
        absent, use DefaultDuration.
    :ivar occasional_traveller_duration: Time needeed by a traveller
        whis is not familiar with SERVICE JOURNEY INTERCHANGE to
        traverse it. If absent, use DefaultDuration and a standard
        weighting.
    :ivar impaired_access_duration: Time needeed by a traveller wos is
        mobility impaired to traverse SERVICE JOURNEY INTERCHANGE. If
        absent, use DefaultDuration and a standard impaired travel
        speed.
    """

    connection_link_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkCode",
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
    stop_point_name: Optional[StopPointName] = field(
        default=None,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DefaultDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    frequent_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FrequentTravellerDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occasional_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OccasionalTravellerDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    impaired_access_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ImpairedAccessDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class FromServiceJourneyInterchangeStructure:
    """A planned SERVICE JOURNEY INTERCHANGE from a journey.

    +SIRI v2.0

    :ivar interchange_code: Identifier of SERVICE JOURNEY INTERCHANGE.
        +SIRI v2.0
    :ivar connection_link_ref: Reference to a physical CONNECTION LINK
        over which the SERVICE JOURNEY INTERCHANGE takes place. +SIRI
        v2.0
    :ivar feeder_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI v2.0
    :ivar feeder_arrival_stop_ref: SCHEDULED STOP POINT at which feeder
        journey arrives. +SIRI v2.0
    :ivar feeder_visit_number: Sequence of visit to Feeder stop within
        Feeder JOURNEY PATTERN.
    :ivar distributor_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI
        v2.0
    :ivar distributor_departure_stop_ref: SCHEDULED STOP POINT at which
        distributor journet departs. +SIRI v2.0
    :ivar distributor_visit_number: Sequence of visit to Distributor
        stop within Distributor JOURNEY PATTERN.
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE. SIRI
        v2,0
    :ivar maximum_wait_time: Maximum time that Distributor will wait for
        Feeder for INTERCHANGE. SIRI v1.0
    :ivar maximum_automatic_wait_time: Maximum automatic wait time that
        Distributor will wait for Feeder for INTERCHANGE. +SIRI v2.0
    :ivar standard_transfer_time: Standard transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar minimum_transfer_time: Minimum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar extensions:
    """

    interchange_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
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
    feeder_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    feeder_arrival_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    feeder_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FeederVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_departure_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorDepartureStopRef",
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
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
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
class ServiceJourneyInterchangeStructure:
    """A planned SERVICE JOURNEY INTERCHANGE between two journeys.

    +SIRI v2.0

    :ivar interchange_code: Identifier of SERVICE JOURNEY INTERCHANGE.
        +SIRI v2.0
    :ivar connection_link_ref: Reference to a physical CONNECTION LINK
        over which the SERVICE JOURNEY INTERCHANGE takes place. +SIRI
        v2.0
    :ivar feeder_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI v2.0
    :ivar feeder_arrival_stop_ref: SCHEDULED STOP POINT at which feeder
        journey arrives. +SIRI v2.0
    :ivar feeder_visit_number: Sequence of visit to Feeder stop within
        Feeder JOURNEY PATTERN.
    :ivar distributor_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI
        v2.0
    :ivar distributor_departure_stop_ref: SCHEDULED STOP POINT at which
        distributor journet departs. +SIRI v2.0
    :ivar distributor_visit_number: Sequence of visit to Distributor
        stop within Distributor JOURNEY PATTERN.
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE. SIRI
        v2,0
    :ivar maximum_wait_time: Maximum time that Distributor will wait for
        Feeder for INTERCHANGE. SIRI v1.0
    :ivar maximum_automatic_wait_time: Maximum automatic wait time that
        Distributor will wait for Feeder for INTERCHANGE. +SIRI v2.0
    :ivar standard_transfer_time: Standard transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar minimum_transfer_time: Minimum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar extensions:
    """

    interchange_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
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
    feeder_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    feeder_arrival_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    feeder_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FeederVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    distributor_departure_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorDepartureStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
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
class ToServiceJourneyInterchangeStructure:
    """A planned SERVICE JOURNEY INTERCHANGE to a journey.

    +SIRI v2.0

    :ivar interchange_code: Identifier of SERVICE JOURNEY INTERCHANGE.
        +SIRI v2.0
    :ivar connection_link_ref: Reference to a physical CONNECTION LINK
        over which the SERVICE JOURNEY INTERCHANGE takes place. +SIRI
        v2.0
    :ivar feeder_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI v2.0
    :ivar feeder_arrival_stop_ref: SCHEDULED STOP POINT at which feeder
        journey arrives. +SIRI v2.0
    :ivar feeder_visit_number: Sequence of visit to Feeder stop within
        Feeder JOURNEY PATTERN.
    :ivar distributor_ref: Reference to a feeder VEHICLE JOURNEY. +SIRI
        v2.0
    :ivar distributor_departure_stop_ref: SCHEDULED STOP POINT at which
        distributor journet departs. +SIRI v2.0
    :ivar distributor_visit_number: Sequence of visit to Distributor
        stop within Distributor JOURNEY PATTERN.
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE. SIRI
        v2,0
    :ivar maximum_wait_time: Maximum time that Distributor will wait for
        Feeder for INTERCHANGE. SIRI v1.0
    :ivar maximum_automatic_wait_time: Maximum automatic wait time that
        Distributor will wait for Feeder for INTERCHANGE. +SIRI v2.0
    :ivar standard_transfer_time: Standard transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar minimum_transfer_time: Minimum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar extensions:
    """

    interchange_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
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
    feeder_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_arrival_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FeederVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_ref: Optional[ConnectingJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    distributor_departure_stop_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorDepartureStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
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
class TargetedInterchangeStructure:
    """
    Planned Connection between two VEHICLE JOURNEYs.

    :ivar interchange_code: Identifier of SERVICE JOURNEY INTERCHANGE.
    :ivar distributor_vehicle_journey_ref: Reference to a (dated)
        distributor VEHICLE JOURNEY.
    :ivar distributor_connection_link_ref: Reference to a physical
        CONNECTION LINK over which the SERVICE JOURNEY INTERCHANGE takes
        place.
    :ivar distributor_connection_link: Link to Interchange stop from
        which the distributor journey departs. If omitted: the
        distributor journey stop is the same as the feeder journey stop,
        i.e. that of theh dated call.
    :ivar distributor_visit_number: Sequence of visit to Distributor
        stop within Distributor JOURNEY PATTERN.
    :ivar distributor_order: For implementations for which Order is not
        used for VisitNumber, (i.e. if VisitNumberIsOrder is false) then
        Order can be used to associate the Order as well if useful for
        translation.
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE. SIRI
        v2,0
    :ivar maximum_wait_time: Maximum time that Distributor will wait for
        Feeder for INTERCHANGE. SIRI v1.0
    :ivar maximum_automatic_wait_time: Maximum automatic wait time that
        Distributor will wait for Feeder for INTERCHANGE. +SIRI v2.0
    :ivar standard_transfer_time: Standard transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar minimum_transfer_time: Minimum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE. SIRI v2,0
    """

    interchange_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    distributor_connection_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_connection_link: Optional[ContextualisedConnectionLinkStructure] = field(
        default=None,
        metadata={
            "name": "DistributorConnectionLink",
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
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class DatedCallStructure:
    """
    Type for Planned VEHICLE JOURNEY Stop (Production Timetable Service).

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    :ivar timing_point:
    :ivar boarding_stretch: Whether this is a Hail and Ride Stop.
        Default is 'false'.
    :ivar request_stop: Whether Vehicle stops only if requested
        explicitly by passenger. Default is 'false'.
    :ivar destination_display: Destination to show for the VEHICLE at
        the specific stop (vehicle signage), if different to the
        Destination Name for the full journey.
    :ivar call_note: Text annotation that applies to this call.
    :ivar aimed_arrival_time:
    :ivar arrival_platform_name:
    :ivar arrival_boarding_activity:
    :ivar arrival_stop_assignment: Assignment of arrival of Scheduled
        STOP POINT to a phsyical QUAY (platform). If not given, assume
        same as for departure +SIRI v2.0.
    :ivar arrival_operator_refs: OPERATORs of of servcie up until
        arrival.. May change for departure. +SIRI v2.0.
    :ivar aimed_departure_time:
    :ivar departure_platform_name:
    :ivar departure_boarding_activity:
    :ivar departure_stop_assignment:
    :ivar departure_operator_refs: OPERATORs of of service for
        departure and onwards.. May change from that for arrival. +SIRI
        v2.0.
    :ivar aimed_latest_passenger_access_time:
    :ivar aimed_headway_interval:
    :ivar targeted_interchange: Information on any planned distributor
        connections (deprecated from SIRI V2.0 ... see 2 next
        attributes)
    :ivar from_service_journey_interchange: Information on any planned
        feeder connections. SIRI 2.0
    :ivar to_service_journey_interchange: Information on any planned
        distributor connections. SIRI 2.0
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
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
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
    arrival_stop_assignment: Optional[PlannedStopAssignmentStructure] = field(
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
    departure_stop_assignment: Optional[PlannedStopAssignmentStructure] = field(
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
    aimed_latest_passenger_access_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedLatestPassengerAccessTime",
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
    targeted_interchange: List[TargetedInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "TargetedInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    from_service_journey_interchange: List[FromServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "FromServiceJourneyInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    to_service_journey_interchange: List[ToServiceJourneyInterchangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ToServiceJourneyInterchange",
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
class DatedCall(DatedCallStructure):
    """
    Complete sequence of stops along the route path, in calling order.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourneyStructure:
    """
    Type for Planned VEHICLE JOURNEY (Production Timetable Service).

    :ivar dated_vehicle_journey_code: Identifier for a VEHICLE JOURNEY.
    :ivar framed_vehicle_journey_ref: Refercence to a VEHICLE JOURENY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref:
    :ivar extra_journey: Whether this journey is an addition to the
        plan. Can only be used when both participants recognise the same
        schedule version. If omitted, defaults to false: the journey is
        not an addition.
    :ivar cancellation: Whether this journey is a deletion of a journey
        in the plan. Can only be used when both participants recognise
        the same schedule version. If omitted, defaults to 'false':
        Journey is not a deletion.
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
    :ivar vehicle_journey_name: For train services with named journeys.
        Train name, e.g. “West Coast Express”. If omitted: No train
        name. Inherited property.  (Unbounded since SIRI 2.0)
    :ivar journey_note:
    :ivar public_contact: Contact details for use by members of public.
        +SIRI v2.0
    :ivar operations_contact: Contact details for use by operational
        staff. +SIRI v2.0
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
    :ivar block_ref: BLOCK that VEHICLE is running.
    :ivar course_of_journey_ref: COURSE OF JOURNEY ('Run') that VEHICLE
        is running.
    :ivar dated_calls: Complete sequence of stops along the route path,
        in calling order.
    :ivar extensions:
    """

    dated_vehicle_journey_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyCode",
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
    vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
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
    dated_calls: Optional["DatedVehicleJourneyStructure.DatedCalls"] = field(
        default=None,
        metadata={
            "name": "DatedCalls",
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
    class DatedCalls:
        dated_call: List[DatedCall] = field(
            default_factory=list,
            metadata={
                "name": "DatedCall",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 2,
            },
        )


@dataclass
class DatedVehicleJourney(DatedVehicleJourneyStructure):
    """
    A planned VEHICLE JOURNEY taking place on a particular date.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
