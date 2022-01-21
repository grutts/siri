from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.acsb.acsb_passenger_mobility_v0_3 import SuitabilityStructure
from siri.datex2.datexiischema_2_0_rc1_2_0 import (
    AreaOfInterestEnum,
    Cause,
    Comment,
    DelayBandEnum,
    DelaysTypeEnum,
    ExtensionType,
    GroupOfLocations,
    Impact,
    InformationStatusEnum,
    Management,
    ProbabilityOfOccurrenceEnum,
    PublicEventTypeEnum,
    RoadsideReferencePointLinear,
    SituationRecord,
    Source,
    SourceTypeEnum,
    Validity,
)
from siri.ifopt.ifopt_countries_v0_2 import IanaCountryTldEnumeration
from siri.ifopt.ifopt_location_v0_3 import LinkProjectionStructure
from siri.siri_model.siri_journey_support_v2_0 import (
    ArrivalBoardingActivityEnumeration,
    DepartureBoardingActivityEnumeration,
)
from siri.siri_model.siri_situation_actions_v1_0 import ActionsStructure
from siri.siri_model.siri_situation_affects_v2_0 import (
    AffectedNetworkStructure,
    AffectedOperatorStructure,
    AffectedPlaceStructure,
    AffectedStopPlaceStructure,
    AffectedStopPointStructure,
    AffectedVehicleJourneyStructure,
    CasualtiesStructure,
    OffsetStructure,
)
from siri.siri_model.siri_situation_classifiers_v1_1 import (
    ServiceConditionEnumeration,
    SeverityEnumeration,
    VerificationStatusEnumeration,
)
from siri.siri_model.siri_situation_reasons_v1_1 import (
    EnvironmentReasonEnumeration,
    EquipmentReasonEnumeration,
    MiscellaneousReasonEnumeration,
    PersonnelReasonEnumeration,
)
from siri.siri_model.siri_situation_service_types_v1_0 import (
    ReportTypeEnumeration,
    TicketRestrictionEnumeration,
)
from siri.siri_model.siri_time_v1_2 import (
    DayTypeEnumeration,
    HalfOpenTimestampRangeStructure,
)
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import (
    EmptyType,
    Extensions,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AudienceEnumeration(Enum):
    """
    Values for Audience.
    """

    PUBLIC = "public"
    EMERGENCY_SERVICES = "emergencyServices"
    STAFF = "staff"
    STATION_STAFF = "stationStaff"
    MANAGEMENT = "management"
    INFO_SERVICES = "infoServices"


@dataclass
class BlockingStructure:
    """
    Type for blocking.

    :ivar journey_planner: Whether information about parts of the
        network identified by Affects should be blocked from computation
        made by a Journey Planner that has a real-tiem feed of the
        SITUATIONs. Default is 'false'; do not suppress.
    :ivar real_time: Whether information about parts of the network
        identified by Affects should be blocked from real-time
        departureinfo systems. Default is 'false'; do not suppress.
    """

    journey_planner: Optional[bool] = field(
        default=None,
        metadata={
            "name": "JourneyPlanner",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    real_time: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RealTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


class ImageContentEnumeration(Enum):
    """
    Values for image content.
    """

    MAP = "map"
    GRAPHIC = "graphic"
    LOGO = "logo"


class LinkContentEnumeration(Enum):
    """
    Values for image content.
    """

    TIMETABLE = "timetable"
    RELATED_SITE = "relatedSite"
    DETAILS = "details"
    ADVICE = "advice"
    OTHER = "other"


class QualityEnumeration(Enum):
    """
    Type for Quality of data indication.
    """

    CERTAIN = "certain"
    VERY_RELIABLE = "veryReliable"
    RELIABLE = "reliable"
    PROBABLY_RELIABLE = "probablyReliable"
    UNCONFIRMED = "unconfirmed"


class RelatedToEnumeration(Enum):
    """
    Values for Type of Source.
    """

    CAUSE = "cause"
    EFFECT = "effect"
    UPDATE = "update"
    SUPERCEDES = "supercedes"
    SUPERCEDED_BY = "supercededBy"
    ASSOCIATED = "associated"


class ScopeTypeEnumeration(Enum):
    """
    Values for ScopeType.
    """

    GENERAL = "general"
    OPERATOR = "operator"
    NETWORK = "network"
    ROUTE = "route"
    LINE = "line"
    PLACE = "place"
    STOP_PLACE = "stopPlace"
    STOP_PLACE_COMPONENT = "stopPlaceComponent"
    STOP_POINT = "stopPoint"
    VEHICLE_JOURNEY = "vehicleJourney"
    DATED_VEHICLE_JOURNEY = "datedVehicleJourney"
    CONNECTION_LINK = "connectionLink"
    INTERCHANGE = "interchange"
    ROAD = "road"


class SensitivityEnumeration(Enum):
    """
    Values for Sensitivity.
    """

    VERY_HIGH = "veryHigh"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "veryLow"


class SituationSourceTypeEnumeration(Enum):
    """
    Values for Type of Source.
    """

    DIRECT_REPORT = "directReport"
    EMAIL = "email"
    PHONE = "phone"
    FAX = "fax"
    POST = "post"
    FEED = "feed"
    RADIO = "radio"
    TV = "tv"
    WEB = "web"
    PAGER = "pager"
    TEXT = "text"
    OTHER = "other"


class WorkflowStatusEnumeration(Enum):
    """
    Values for Entry Status.
    """

    DRAFT = "draft"
    APPROVED_DRAFT = "approvedDraft"
    OPEN = "open"
    PUBLISHED = "published"
    CLOSING = "closing"
    CLOSED = "closed"


@dataclass
class AbstractSituationElementStructure:
    """
    Type for abstract EntryAbstract type.

    :ivar creation_time: Time of creation of SITUATION.
    :ivar country_ref: Unique identifier of a Country of a Participant
        who created SITUATION. Provides namespace for Participant If
        absent proided from context.
    :ivar participant_ref: Unique identifier of a Participant. Provides
        namespace for SITUATION. If absent provdied from context.
    :ivar situation_number: Unique identifier of SITUATION within a
        Participant. Excludes any version number.
    :ivar update_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar update_participant_ref: Unique identifier of a Participant.
        Provides namespace for SITUATION. If absent provdied from
        context.
    :ivar version: Unique identifier of update version within a
        SITUATION Number Omit if reference to the base SITUATION.
    """

    creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    update_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "UpdateCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    update_participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpdateParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AffectedRoadStructure:
    """
    Type for Raod scope for scope of SITUATION or effect.

    :ivar road:
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    """

    road: Optional[RoadsideReferencePointLinear] = field(
        default=None,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class BoardingStructure:
    """
    Type for boarding restrictions.

    :ivar arrival_boarding_activity: Type of boarding and alighting
        allowed at stop. Default is 'Alighting'.
    :ivar departure_boarding_activity: Type of alighting allowed at
        stop. Default is 'Boarding'.
    """

    arrival_boarding_activity: Optional[ArrivalBoardingActivityEnumeration] = field(
        default=None,
        metadata={
            "name": "ArrivalBoardingActivity",
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


@dataclass
class DefaultedTextStructure(NaturalLanguageStringStructure):
    """
    Type for a text that may be overridden.

    :ivar overridden: Whether the text value has been overridden from
        the generated default. Default is 'true'.
    """

    overridden: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DelaysStructure:
    """
    Type for easement info.

    :ivar delay_band: Time band into which delay will fall.
    :ivar delay_type: Category of delay.
    :ivar delay: Additional journey time needed to overcome disruption.
    """

    delay_band: Optional[DelayBandEnum] = field(
        default=None,
        metadata={
            "name": "DelayBand",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay_type: Optional[DelaysTypeEnum] = field(
        default=None,
        metadata={
            "name": "DelayType",
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


@dataclass
class EasementsStructure:
    """
    Type for easement info.

    :ivar ticket_restrictions: Ticket restriction conditiosn in effect.
        TPEG pti table pti25.
    :ivar easement: Description of fare exceptions allowed because of
        disruption.  (Unbounded since SIRI 2.0)
    :ivar easement_ref: Refernce to a fare exceptions code that is
        allowed because of the disruption. An easement may relax a fare
        condition, for exampel "You may use your metro ticket on the
        bus', or 'You may use your bus ticket in teh metro between these
        two stops'.
    """

    ticket_restrictions: Optional[TicketRestrictionEnumeration] = field(
        default=None,
        metadata={
            "name": "TicketRestrictions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easement: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easement_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EasementRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ImageStructure:
    """
    Type for image.

    :ivar image_ref: Reference to an image.
    :ivar image_binary: Embedded image.
    :ivar image_content: Categorisation of image content.
    """

    image_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    image_binary: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "ImageBinary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "format": "base64",
        },
    )
    image_content: Optional[ImageContentEnumeration] = field(
        default=None,
        metadata={
            "name": "ImageContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class OptionalTrafficElementStructure:
    """An event which is not planned by the traffic OPERATOR, which is
    affecting, or has the potential to affect traffic flow.

    This SIRI-SX element embeds the Datex2 TrafficElement, making all
    elements optional because they may alternatvielky be specified by
    common SIRI-SRX SITUATION elements.

    :ivar situation_record_creation_reference: A unique alphanumeric
        reference (either an external reference or GUID) of the
        SITUATIONRecord object (the first version of the record) that
        was created by the original supplier.
    :ivar situation_record_creation_time: The date/time that the
        SITUATIONRecord object (the first version of the record) was
        created by the original supplier.
    :ivar situation_record_observation_time: The date/time that the
        information represented by the current version of the
        SITUATIONRecord was observed by the original (potentially
        external) source of the information.
    :ivar situation_record_version: Each record within a SITUATION may
        iterate through a series of versions during its life time. The
        SITUATION record version uniquely identifies the version of a
        particular record within a SITUATION. It is generated and used
        by systems external to DATEX 2.
    :ivar situation_record_version_time: The date/time that this current
        version of the SITUATIONRecord was written into the database of
        the supplier which is involved in the data exchange.
    :ivar situation_record_first_supplier_version_time: The date/time
        that the current version of the SITUATION Record was written
        into the database of the original supplier in the supply chain.
    :ivar probability_of_occurrence: An assessment of the degree of
        likelihood that the reported event will occur.
    :ivar source:
    :ivar validity:
    :ivar impact: Impact of Road SITUATION as specified by Datex2.
    :ivar cause: Impact of Road SITUATION as specified by Datex2 model.
    :ivar general_public_comment: Datex 2 comments for public use.
    :ivar non_general_public_comment: Ccomments not for public use.
    :ivar group_of_locations: Datex 2 model of where event ois taking
        place on the road.
    :ivar management:
    :ivar situation_record_extension:
    :ivar traffic_element_extension:
    """

    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
            "max_length": 1024,
        },
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationRecordVersion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    non_general_public_comment: List[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PtAdviceStructure:
    """
    Type for advice.

    :ivar advice_ref: Reference to a standardis advisory NOTICE to be
        given to passengers if a particular condition arises .
    :ivar details: Further Textual advice to passengers.  (Unbounded
        since SIRI 2.0)
    """

    advice_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdviceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    details: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class RelatedSituationStructure:
    """
    Type for a reference.

    :ivar creation_time: Time of creation of 'related to' assocation.
    :ivar country_ref: Unique identifier of a Country of a Participant
        who created SITUATION. Provides namespace for Participant If
        absent proided from context.
    :ivar participant_ref: Unique identifier of a Participant. Provides
        namespace for SITUATION. If absent provdied from context.
    :ivar situation_number: Unique identifier of SITUATION within a
        Participant. Excludes any version number.
    :ivar update_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar update_participant_ref: Unique identifier of a Participant.
        Provides namespace for SITUATION. If absent provdied from
        context.
    :ivar version: Unique identifier of update version within a
        SITUATION Number Omit if reference to the base SITUATION.
    :ivar external_reference: A single string that identifiers the
        referenced SITUATION.
    :ivar related_as: Relationship of refercence to the referncing
        SITUATION e.
    :ivar extensions:
    """

    creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    update_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "UpdateCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    update_participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpdateParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    related_as: Optional[RelatedToEnumeration] = field(
        default=None,
        metadata={
            "name": "RelatedAs",
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
class SituationSourceStructure:
    """
    Type for a source, i.e. provider of information.

    :ivar country: Country of origin of source element.
    :ivar source_type: Nature of Source.
    :ivar email: Email of Supplier of information.
    :ivar phone: Phone number of Supplier of information.
    :ivar fax: Fax number of Supplier of information.
    :ivar web: Information was obtained from a web site URL of site
        and/or page.
    :ivar other: Other information about source.
    :ivar source_method: Nature of method used to get Source.
    :ivar agent_reference: Reference to an Agent, i.e. Capture client
        user who input an SITUATION. Available for use in intranet
        exchange of SITUATIONs.
    :ivar name: Name of for source.
    :ivar source_role: Job title of Source.
    :ivar time_of_communication: Time of communication of message, if
        different from creation time.
    :ivar external_code: External system reference to SITUATION.
    :ivar source_file: Electronic file / attachment containing
        information about SITUATION.
    :ivar extensions:
    """

    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_type: Optional[SituationSourceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SourceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    web: Optional[str] = field(
        default=None,
        metadata={
            "name": "Web",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "name": "Other",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_method: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "SourceMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    agent_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_role: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceRole",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    time_of_communication: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeOfCommunication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceFile",
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
class AffectedRoadsStructure:
    """
    Type for Location model for scope of SITUATION or effect.

    :ivar datex2_locations: Refereences to road network locations
        affected by the SITUATION.
    :ivar affected_road: Description of affected road.
    """

    datex2_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "Datex2Locations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_road: List[AffectedRoadStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedRoad",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class InfoLinkStructure:
    """
    Type for a general hyperlink.

    :ivar uri: URI for link.
    :ivar label: Label for Link.  (Unbounded since SIRI 2.0)
    :ivar image: Image to use when presenting hyperlink.
    :ivar link_content: Categorisation of link content.
    """

    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uri",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    label: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    image: Optional[ImageStructure] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_content: Optional[LinkContentEnumeration] = field(
        default=None,
        metadata={
            "name": "LinkContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ReferencesStructure:
    """
    Type for references.

    :ivar related_to_ref: A reference to another SITUATION with an
        indication of the nature of the association, e.g. a cause, a
        result, an update. Note that a Entry that is an update, i.e. has
        the same IdentifierNumber but a later version number as a
        previous Entry alway has a supercedes relationship and this does
        not need to be expliciitly coded.
    """

    related_to_ref: List[RelatedSituationStructure] = field(
        default_factory=list,
        metadata={
            "name": "RelatedToRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class AffectsScopeStructure:
    """
    Type for Location model for scope of SITUATION or effect.

    :ivar area_of_interest: Affected overall Geographic scope.
    :ivar operators: Affected OPERATORs, If absent, taken from context.
        If present, any OPERATORs stated completely replace those from
        context.
    :ivar networks: Networks affected by SITUATION.
    :ivar stop_points: STOP POINTs affected by SITUATION.
    :ivar stop_places: Places other than STOP POINTs affected by
        SITUATION.
    :ivar places: Places other than STOP POINTs affected by SITUATION.
    :ivar vehicle_journeys: Specific journeys affected by SITUATION.
    :ivar roads: Roads affected by.
    :ivar extensions:
    """

    area_of_interest: Optional[AreaOfInterestEnum] = field(
        default=None,
        metadata={
            "name": "AreaOfInterest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operators: Optional["AffectsScopeStructure.Operators"] = field(
        default=None,
        metadata={
            "name": "Operators",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    networks: Optional["AffectsScopeStructure.Networks"] = field(
        default=None,
        metadata={
            "name": "Networks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_points: Optional["AffectsScopeStructure.StopPoints"] = field(
        default=None,
        metadata={
            "name": "StopPoints",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_places: Optional["AffectsScopeStructure.StopPlaces"] = field(
        default=None,
        metadata={
            "name": "StopPlaces",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    places: Optional["AffectsScopeStructure.Places"] = field(
        default=None,
        metadata={
            "name": "Places",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journeys: Optional["AffectsScopeStructure.VehicleJourneys"] = field(
        default=None,
        metadata={
            "name": "VehicleJourneys",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    roads: Optional[AffectedRoadsStructure] = field(
        default=None,
        metadata={
            "name": "Roads",
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
    class Operators:
        """
        :ivar all_operators: All OPERATORs.
        :ivar affected_operator: Operators of services affected by
            SITUATION.
        """

        all_operators: Optional[EmptyType] = field(
            default=None,
            metadata={
                "name": "AllOperators",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        affected_operator: List[AffectedOperatorStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedOperator",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class Networks:
        """
        :ivar affected_network: Nrtworks and Route(s) affected by
            SITUATION.
        """

        affected_network: List[AffectedNetworkStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedNetwork",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPoints:
        """
        :ivar affected_stop_point: Stop affected by SITUATION.
        """

        affected_stop_point: List[AffectedStopPointStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPoint",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class StopPlaces:
        """
        :ivar affected_stop_place: Stop affected by SITUATION.
        """

        affected_stop_place: List[AffectedStopPlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedStopPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Places:
        """
        :ivar affected_place: Stop affected by SITUATION.
        """

        affected_place: List[AffectedPlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedPlace",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class VehicleJourneys:
        """
        :ivar affected_vehicle_journey: Journeys affected by the
            SITUATIONj
        """

        affected_vehicle_journey: List[AffectedVehicleJourneyStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedVehicleJourney",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class SituationElementStructure(AbstractSituationElementStructure):
    """
    Type for loggable Entry.

    :ivar references: Associations with other SITUATIONs.
    :ivar source: Information about source of information, that is,
        where the agent using the capture client obtained an item of
        information, or in the case of an automated feed, an identifier
        of the specific feed. Can be used to obtain updates, verify
        details or otherwise assess relevance.
    :ivar versioned_at_time: Time at which SITUATION element was
        versioned. Once versioned, no furtr changes can be made.
    """

    references: Optional[ReferencesStructure] = field(
        default=None,
        metadata={
            "name": "References",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source: Optional[SituationSourceStructure] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    versioned_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VersionedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PtConsequenceStructure:
    """
    Type for disruption.

    :ivar period: Period of effect of disruption, if different from that
        of SITUATION.
    :ivar condition:
    :ivar severity: Severity of disruption if different from that of
        SITUATION. TPEG pti26
    :ivar affects: Parts of transport network affected by disruption if
        different from that of SITUATION.
    :ivar suitabilities: Effect on different passenger needs.
    :ivar advice: Advice to passengers.
    :ivar blocking: How Disruption should be handled in Info systems.
    :ivar boarding: Change to normal boarding activity allowed at stop.
    :ivar delays:
    :ivar casualties: Information on casualties.
    :ivar easements: Description of fare exceptions allowed because of
        disruption.
    :ivar extensions:
    """

    period: Optional[HalfOpenTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    condition: Optional[ServiceConditionEnumeration] = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suitabilities: Optional["PtConsequenceStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: Optional[PtAdviceStructure] = field(
        default=None,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    blocking: Optional[BlockingStructure] = field(
        default=None,
        metadata={
            "name": "Blocking",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding: Optional[BoardingStructure] = field(
        default=None,
        metadata={
            "name": "Boarding",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delays: Optional[DelaysStructure] = field(
        default=None,
        metadata={
            "name": "Delays",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    casualties: Optional[CasualtiesStructure] = field(
        default=None,
        metadata={
            "name": "Casualties",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easements: List[EasementsStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easements",
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
    class Suitabilities:
        """
        :ivar suitability: Effect on a passenger need.
        """

        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class PtConsequencesStructure:
    """
    Type for list of effects.

    :ivar consequence: Nature of the effect to disrupt (or restore)
        service, and further details.
    """

    consequence: List[PtConsequenceStructure] = field(
        default_factory=list,
        metadata={
            "name": "Consequence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class PtSituationElementStructure(SituationElementStructure):
    """
    Type for individual PT SITUATION.

    :ivar verification: Whether the SITUATION has been verified.
    :ivar progress: ProgressStatus. One of a specified set of overall
        processing states assigned to SITUATION. For example, 'Draft'
        for not yet published; 'Published' for live SITUATIONs; 'Closed'
        indicates a completed SITUATION.
    :ivar quality_index: Assessement of likely correctness of data.
    :ivar reality: Whether SITUATION is real or a test.
    :ivar likelihood: Likellihoo of a future sutuation happening.
    :ivar publication: Publishing status one of a specified set of
        substates to which an SITUATION can be assigned.
    :ivar validity_period: Overall inclusive Period of applicability of
        SITUATION.
    :ivar repetitions: situation applies only on the repeated day types
        within the overall validity period(s). For example Sunday.
    :ivar publication_window: Publication Window for SITUATION if
        different from validity period.
    :ivar unknown_reason:
    :ivar miscellaneous_reason:
    :ivar personnel_reason: Personnel reason.
    :ivar equipment_reason:
    :ivar environment_reason: Environment reason.
    :ivar undefined_reason:
    :ivar public_event_reason: Classifier of Pub;ic Event.
    :ivar reason_name: Text explanation of SITUATION reason. Not
        normally needed.  (Unbounded since SIRI 2.0)
    :ivar severity:
    :ivar priority: Arbitrary rating of priority 1-High.
    :ivar sensitivity: Confidentiality of SITUATION.
    :ivar audience: Intended audience of SITUATION.
    :ivar scope_type: Nature of scope, e.g. general, network.
    :ivar report_type:
    :ivar planned: Whether the SITUATION was planned (eg engineering
        works) or unplanned (eg service alteration). Default is 'false',
        i.e. unplanned.
    :ivar keywords: Arbitrary application specific classifiers.
    :ivar secondary_reasons: additioanl reasons.
    :ivar language: Default language.
    :ivar summary: Summary of SITUATION. If absent should be generated
        from structure elements / and or by condensing Description.
        (Unbounded since SIRI 2.0)
    :ivar description: Description of SITUATION. Should not repeat any
        strap line included in Summary.  (Unbounded since SIRI 2.0)
    :ivar detail: Additional descriptive details about the SITUATION
        (Unbounded since SIRI 2.0).
    :ivar advice: Further advice to passengers.  (Unbounded since SIRI
        2.0)
    :ivar internal: Further advice to passengers.
    :ivar images: Any images associated with SITUATION.
    :ivar info_links: Hyperlinks to other resources associated with
        SITUATION.
    :ivar affects: Structured model identifiying parts of transport
        network affected by SITUATION. OPERATOR and NETWORK values will
        be defaulted to values in general Context unless explicitly
        overridden.
    :ivar consequences: Structured model describing effect of the
        SITUATION on PT system.
    :ivar publishing_actions: Structured model describing distribution
        actions to handle SITUATION. Any actions stated completely
        replace those from Context. If no actions are stated, any
        actions from general Context are used.
    :ivar extensions:
    """

    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress: Optional[WorkflowStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    quality_index: Optional[QualityEnumeration] = field(
        default=None,
        metadata={
            "name": "QualityIndex",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reality: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "Reality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    likelihood: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "Likelihood",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: List[HalfOpenTimestampRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    repetitions: Optional["PtSituationElementStructure.Repetitions"] = field(
        default=None,
        metadata={
            "name": "Repetitions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication_window: Optional[HalfOpenTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnknownReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    miscellaneous_reason: Optional[MiscellaneousReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "MiscellaneousReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    personnel_reason: Optional[PersonnelReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "PersonnelReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_reason: Optional[EquipmentReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EquipmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    environment_reason: Optional[EnvironmentReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EnvironmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    undefined_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndefinedReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    public_event_reason: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "PublicEventReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sensitivity: Optional[SensitivityEnumeration] = field(
        default=None,
        metadata={
            "name": "Sensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    audience: Optional[AudienceEnumeration] = field(
        default=None,
        metadata={
            "name": "Audience",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    scope_type: Optional[ScopeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopeType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    report_type: Optional[ReportTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ReportType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    secondary_reasons: Optional["PtSituationElementStructure.SecondaryReasons"] = field(
        default=None,
        metadata={
            "name": "SecondaryReasons",
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
    summary: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Summary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    detail: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    internal: Optional[DefaultedTextStructure] = field(
        default=None,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    images: Optional["PtSituationElementStructure.Images"] = field(
        default=None,
        metadata={
            "name": "Images",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_links: Optional["PtSituationElementStructure.InfoLinks"] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consequences: Optional[PtConsequencesStructure] = field(
        default=None,
        metadata={
            "name": "Consequences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publishing_actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "PublishingActions",
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
    class Repetitions:
        day_type: List[DayTypeEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "DayType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class SecondaryReasons:
        """
        :ivar reason: Reason.
        """

        reason: List["PtSituationElementStructure.SecondaryReasons.Reason"] = field(
            default_factory=list,
            metadata={
                "name": "Reason",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Reason:
            """
            :ivar unknown_reason:
            :ivar miscellaneous_reason:
            :ivar personnel_reason: Personnel reason.
            :ivar equipment_reason:
            :ivar environment_reason: Environment reason.
            :ivar undefined_reason:
            :ivar public_event_reason: Classifier of Pub;ic Event.
            :ivar reason_name: Text explanation of SITUATION reason. Not
                normally needed.  (Unbounded since SIRI 2.0)
            """

            unknown_reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UnknownReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            miscellaneous_reason: Optional[MiscellaneousReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "MiscellaneousReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            personnel_reason: Optional[PersonnelReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "PersonnelReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            equipment_reason: Optional[EquipmentReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EquipmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            environment_reason: Optional[EnvironmentReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EnvironmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            undefined_reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UndefinedReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            public_event_reason: Optional[PublicEventTypeEnum] = field(
                default=None,
                metadata={
                    "name": "PublicEventReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            reason_name: List[NaturalLanguageStringStructure] = field(
                default_factory=list,
                metadata={
                    "name": "ReasonName",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )

    @dataclass
    class Images:
        """
        :ivar image: Image description.
        """

        image: List[ImageStructure] = field(
            default_factory=list,
            metadata={
                "name": "Image",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class InfoLinks:
        """
        :ivar info_link: Hyperlink description.
        """

        info_link: List[InfoLinkStructure] = field(
            default_factory=list,
            metadata={
                "name": "InfoLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class RoadSituationElementStructure(SituationElementStructure):
    """
    Type for individual PT SITUATION.

    :ivar verification: Whether the SITUATION has been verified.
    :ivar progress: ProgressStatus. One of a specified set of overall
        processing states assigned to SITUATION. For example, 'Draft'
        for not yet published; 'Published' for live SITUATIONs; 'Closed'
        indicates a completed SITUATION.
    :ivar quality_index: Assessement of likely correctness of data.
    :ivar reality: Whether SITUATION is real or a test.
    :ivar likelihood: Likellihoo of a future sutuation happening.
    :ivar publication: Publishing status one of a specified set of
        substates to which an SITUATION can be assigned.
    :ivar validity_period: Overall inclusive Period of applicability of
        SITUATION.
    :ivar repetitions: situation applies only on the repeated day types
        within the overall validity period(s). For example Sunday.
    :ivar publication_window: Publication Window for SITUATION if
        different from validity period.
    :ivar unknown_reason:
    :ivar miscellaneous_reason:
    :ivar personnel_reason: Personnel reason.
    :ivar equipment_reason:
    :ivar environment_reason: Environment reason.
    :ivar undefined_reason:
    :ivar public_event_reason: Classifier of Pub;ic Event.
    :ivar reason_name: Text explanation of SITUATION reason. Not
        normally needed.  (Unbounded since SIRI 2.0)
    :ivar severity:
    :ivar priority: Arbitrary rating of priority 1-High.
    :ivar sensitivity: Confidentiality of SITUATION.
    :ivar audience: Intended audience of SITUATION.
    :ivar scope_type: Nature of scope, e.g. general, network.
    :ivar report_type:
    :ivar planned: Whether the SITUATION was planned (eg engineering
        works) or unplanned (eg service alteration). Default is 'false',
        i.e. unplanned.
    :ivar keywords: Arbitrary application specific classifiers.
    :ivar secondary_reasons: additioanl reasons.
    :ivar language: Default language.
    :ivar summary: Summary of SITUATION. If absent should be generated
        from structure elements / and or by condensing Description.
        (Unbounded since SIRI 2.0)
    :ivar description: Description of SITUATION. Should not repeat any
        strap line included in Summary.  (Unbounded since SIRI 2.0)
    :ivar detail: Additional descriptive details about the SITUATION
        (Unbounded since SIRI 2.0).
    :ivar advice: Further advice to passengers.  (Unbounded since SIRI
        2.0)
    :ivar internal: Further advice to passengers.
    :ivar images: Any images associated with SITUATION.
    :ivar info_links: Hyperlinks to other resources associated with
        SITUATION.
    :ivar affects: Structured model identifiying parts of transport
        network affected by SITUATION. Operator and Network values will
        be defaulted to values in general Context unless explicitly
        overridden.
    :ivar consequences: Structured model describing effect of the
        SITUATION on PT system.
    :ivar publishing_actions: Structured model describing distribution
        actions to handle SITUATION. Any actions stated completely
        replace those from Context. If no actions are stated, any
        actions from general Context are used.
    :ivar situation_record: Datex2 SITUATION Record.
    :ivar extensions:
    """

    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress: Optional[WorkflowStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    quality_index: Optional[QualityEnumeration] = field(
        default=None,
        metadata={
            "name": "QualityIndex",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reality: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "Reality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    likelihood: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "Likelihood",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: List[HalfOpenTimestampRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    repetitions: Optional["RoadSituationElementStructure.Repetitions"] = field(
        default=None,
        metadata={
            "name": "Repetitions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication_window: Optional[HalfOpenTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnknownReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    miscellaneous_reason: Optional[MiscellaneousReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "MiscellaneousReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    personnel_reason: Optional[PersonnelReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "PersonnelReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_reason: Optional[EquipmentReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EquipmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    environment_reason: Optional[EnvironmentReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EnvironmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    undefined_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndefinedReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    public_event_reason: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "PublicEventReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sensitivity: Optional[SensitivityEnumeration] = field(
        default=None,
        metadata={
            "name": "Sensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    audience: Optional[AudienceEnumeration] = field(
        default=None,
        metadata={
            "name": "Audience",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    scope_type: Optional[ScopeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopeType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    report_type: Optional[ReportTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ReportType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    secondary_reasons: Optional["RoadSituationElementStructure.SecondaryReasons"] = field(
        default=None,
        metadata={
            "name": "SecondaryReasons",
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
    summary: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Summary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    detail: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    internal: Optional[DefaultedTextStructure] = field(
        default=None,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    images: Optional["RoadSituationElementStructure.Images"] = field(
        default=None,
        metadata={
            "name": "Images",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_links: Optional["RoadSituationElementStructure.InfoLinks"] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consequences: Optional[PtConsequencesStructure] = field(
        default=None,
        metadata={
            "name": "Consequences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publishing_actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "PublishingActions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record: Optional[SituationRecord] = field(
        default=None,
        metadata={
            "name": "SituationRecord",
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
    class Repetitions:
        day_type: List[DayTypeEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "DayType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class SecondaryReasons:
        """
        :ivar reason: Reason.
        """

        reason: List["RoadSituationElementStructure.SecondaryReasons.Reason"] = field(
            default_factory=list,
            metadata={
                "name": "Reason",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Reason:
            """
            :ivar unknown_reason:
            :ivar miscellaneous_reason:
            :ivar personnel_reason: Personnel reason.
            :ivar equipment_reason:
            :ivar environment_reason: Environment reason.
            :ivar undefined_reason:
            :ivar public_event_reason: Classifier of Pub;ic Event.
            :ivar reason_name: Text explanation of SITUATION reason. Not
                normally needed.  (Unbounded since SIRI 2.0)
            """

            unknown_reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UnknownReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            miscellaneous_reason: Optional[MiscellaneousReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "MiscellaneousReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            personnel_reason: Optional[PersonnelReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "PersonnelReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            equipment_reason: Optional[EquipmentReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EquipmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            environment_reason: Optional[EnvironmentReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EnvironmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            undefined_reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UndefinedReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            public_event_reason: Optional[PublicEventTypeEnum] = field(
                default=None,
                metadata={
                    "name": "PublicEventReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            reason_name: List[NaturalLanguageStringStructure] = field(
                default_factory=list,
                metadata={
                    "name": "ReasonName",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )

    @dataclass
    class Images:
        """
        :ivar image: Image description.
        """

        image: List[ImageStructure] = field(
            default_factory=list,
            metadata={
                "name": "Image",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class InfoLinks:
        """
        :ivar info_link: Hyperlink description.
        """

        info_link: List[InfoLinkStructure] = field(
            default_factory=list,
            metadata={
                "name": "InfoLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class PtSituationElement(PtSituationElementStructure):
    """
    Type for individual IPT ncident.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class RoadSituationElement(RoadSituationElementStructure):
    """
    Type for individual IPT ncident.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
