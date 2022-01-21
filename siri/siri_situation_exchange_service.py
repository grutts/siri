from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.acsb.acsb_passenger_mobility_v0_3 import PassengerAccessibilityNeedsStructure
from siri.datex2.datexiischema_2_0_rc1_2_0 import (
    DirectionEnum,
    InformationStatusEnum,
)
from siri.ifopt.ifopt_countries_v0_2 import IanaCountryTldEnumeration
from siri.ifopt.ifopt_modes_v0_2 import AccessModesEnumeration
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
from siri.siri_model.siri_journey_support_v2_0 import FramedVehicleJourneyRefStructure
from siri.siri_model.siri_model_permissions_v2_0 import (
    LinePermissions,
    OperatorPermissions,
    PermissionsStructure,
)
from siri.siri_model.siri_modes_v1_1 import (
    AirSubmodesOfTransportEnumeration,
    BusSubmodesOfTransportEnumeration,
    CoachSubmodesOfTransportEnumeration,
    MetroSubmodesOfTransportEnumeration,
    RailSubmodesOfTransportEnumeration,
    TramSubmodesOfTransportEnumeration,
    VehicleModesOfTransportEnumeration,
    WaterSubmodesOfTransportEnumeration,
)
from siri.siri_model.siri_situation_actions_v1_0 import ActionsStructure
from siri.siri_model.siri_situation_affects_v2_0 import (
    AffectedOperatorStructure,
    NetworkStructure,
)
from siri.siri_model.siri_situation_classifiers_v1_1 import (
    PredictabilityEnumeration,
    SeverityEnumeration,
    VerificationStatusEnumeration,
)
from siri.siri_model.siri_situation_v2_0 import (
    PtSituationElementStructure,
    RoadSituationElement,
    ScopeTypeEnumeration,
    WorkflowStatusEnumeration,
)
from siri.siri_utility.siri_location_v2_0 import LocationStructure
from siri.siri_utility.siri_permissions_v2_0 import (
    AbstractPermissionStructure,
    CapabilityAccessControlStructure,
)
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NetworkContextStructure:
    """
    Type for shared context.

    :ivar operator: Default OPERATOR  for SITUATIONs.
    :ivar network: Default Network of affected LINEs. These values apply
        to all SITUATIONs unless overridden on individual instances.
    """

    operator: List[AffectedOperatorStructure] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network: Optional[NetworkStructure] = field(
        default=None,
        metadata={
            "name": "Network",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class RoadFilterStructure:
    """
    Type for Parameters to filter Situation Exchange Service requests, based on
    the SITUATION Road, Logically ANDed with other values.

    :ivar road_number: Identifier or number of the road on which the
        reference POINT is located.
    :ivar direction_bound: The DIRECTION at the reference point in terms
        of general destination DIRECTION. If absent both.
    :ivar reference_point_identifier: Road reference POINT identifier,
        unique on the specified road.
    """

    road_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "max_length": 1024,
        },
    )
    direction_bound: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "directionBound",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reference_point_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "referencePointIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "max_length": 1024,
        },
    )


@dataclass
class SituationExchangeCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about Situation Exchange Service Capabilities.

    Answered with a VehicleMontoringCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SituationExchangeServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for SItuation Exchange Service Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policy capabilities.
    :ivar subscription_policy: Subscription Policy capabilities.
    :ivar access_control: Optional Access control capabilities.
    :ivar response_features: Optional Response capabilities.
    :ivar extensions:
    """

    topic_filtering: Optional["SituationExchangeServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional["SituationExchangeServiceCapabilitiesStructure.RequestPolicy"] = field(
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
    access_control: Optional["SituationExchangeServiceCapabilitiesStructure.AccessControl"] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_features: Optional["SituationExchangeServiceCapabilitiesStructure.ResponseFeatures"] = field(
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
            Default is 'false'.
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
class SituationExchangeServicePermissionStructure(AbstractPermissionStructure):
    """
    Type for Situation Exchange Service Permissions.
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
class ContextStructure:
    """
    Common parameters for all SITUATIONs.

    :ivar country_ref: Reference to a Country of a Participant who
        published SITUATION.
    :ivar participant_ref: Reference to a system publishing SITUATIONs.
        If SITUATIONs from other participants are included in delivery,
        then ParticipantRef of immediate publisher must be given here.
    :ivar topographic_place_ref: Refrence to a TOPOGRAPHIC PLACE
        (locality). Also Derivable from an individual StopRef.
    :ivar topographic_place_name: Name of locality in which SITUATIONs
        apply. Derivable from LocalityRef.  (Unbounded since SIRI 2.0)
    :ivar default_language: Default language of text.
    :ivar network_context: Default context for common properties of
        Public Transport SITUATIONs.
    :ivar actions: Actions that apply to all SITUATIONs unless
        overridden.
    :ivar extensions:
    """

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
            "required": True,
        },
    )
    topographic_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    topographic_place_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "TopographicPlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_context: Optional[NetworkContextStructure] = field(
        default=None,
        metadata={
            "name": "NetworkContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "Actions",
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
class SituationExchangePermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    situation_exchange_permission: List[SituationExchangeServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangePermission",
            "type": "Element",
        },
    )


@dataclass
class SituationExchangeRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Type for Functional Service Request for Situation Exchange Service.

    :ivar preview_interval: Forward duration for which SITUATIONs should
        be included, that is, only SITUATIONs that start before the end
        of this window time will be included.
    :ivar start_time: Start time for for selecting SITUATIONs to be
        sent. Only SITUATIONs or updates created after this time will be
        sent. This enables a restart without resending everything.
    :ivar vehicle_mode:
    :ivar air_submode:
    :ivar bus_submode:
    :ivar coach_submode:
    :ivar metro_submode:
    :ivar rail_submode:
    :ivar tram_submode:
    :ivar water_submode:
    :ivar access_mode:
    :ivar severity: Severity filter value to apply: only SITUATIONs with
        a severity greater than or equal to the specified value will be
        returned. See TPEG severities. Default is 'all'.
    :ivar scope: Types of SITUATION to include.
    :ivar predictability: Whether just planned, unplanned or both
        SITUATIONs will be returned.
    :ivar keywords: Arbitrary application specific classifiers. Only
        SITUATIONs that match these keywords will be returned.
    :ivar verification: Whether incident has been verified or not If not
        specified return all.
    :ivar progress: Workflow Progress Status. One of a specified set of
        overall processing states assigned to SITUATION. For example,
        'Draft' for not yet published; 'Published' for live SITUATIONs;
        'Closed' indicates a completed SITUATION. If not specified
        return open, published closing and closed. l.
    :ivar reality: Whether SITUATION is real or a test. If not specified
        return all.
    :ivar operator_ref: Referance to an OPERATOR. If unspecified, all
        OPERATOR.s.
    :ivar operational_unit_ref: OPERATIONAL UNIT responsible for
        managing services.
    :ivar network_ref: Reference to a NETWORK.
    :ivar line_ref:
    :ivar stop_point_ref:
    :ivar connection_link_ref:
    :ivar facility_ref:
    :ivar stop_place_ref: Reference to a STOP PLACE.
    :ivar framed_vehicle_journey_ref: Refercence to a VEHICLE JOURENY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref:
    :ivar interchange_ref:
    :ivar vehicle_ref:
    :ivar country_ref: Reference to a COUNTRY where incident takes place
        If specified only incidents that affect this place country will
        be returned.
    :ivar place_ref: Reference to a TOPOGRAPHIC PLACE. Only incidents
        which are deemed to affect this place will be returned.
    :ivar location: Bounding box of an arbitrary area. Only incidents
        geocoded as falling within area will be included.
    :ivar situation_road_filter: Parameters to filter Situation Exchange
        Service requests, based on the SITUATION Road. Logically ANDed
        with other values.
    :ivar accessibility_need_filter: Parameters to filter Situation
        Exchange Service requests, based on specific needs .
    :ivar language: Preferred language in which to return text values.
    :ivar include_translations:
    :ivar maximum_number_of_situation_elements: The maximum number of
        SITUATION elements to return in a given delivery. The most
        recent n Events within the look ahead window are included.
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
    vehicle_mode: Optional[VehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    air_submode: Optional[AirSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bus_submode: Optional[BusSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    coach_submode: Optional[CoachSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    metro_submode: Optional[MetroSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    rail_submode: Optional[RailSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    tram_submode: Optional[TramSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    water_submode: Optional[WaterSubmodesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_mode: Optional[AccessModesEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessMode",
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
    scope: List[ScopeTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Scope",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    predictability: Optional[PredictabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "Predictability",
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
    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress: List[WorkflowStatusEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Progress",
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
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operational_unit_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationalUnitRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    network_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetworkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: List[str] = field(
        default_factory=list,
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
    connection_link_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkRef",
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
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
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
    country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "max_occurs": 2,
        },
    )
    situation_road_filter: Optional["SituationExchangeRequestStructure.SituationRoadFilter"] = field(
        default=None,
        metadata={
            "name": "SituationRoadFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_need_filter: List[PassengerAccessibilityNeedsStructure] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityNeedFilter",
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
    maximum_number_of_situation_elements: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfSituationElements",
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
    class SituationRoadFilter:
        road_filter: List[RoadFilterStructure] = field(
            default_factory=list,
            metadata={
                "name": "RoadFilter",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class SituationExchangeServiceCapabilities(SituationExchangeServiceCapabilitiesStructure):
    """Capabilities of Situation Exchange Service.

    Answers a SituationExchangeCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SituationExchangeCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for Situation Exchange Service.

    :ivar situation_exchange_service_capabilities:
    :ivar situation_exchange_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    situation_exchange_service_capabilities: Optional[SituationExchangeServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "SituationExchangeServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_permissions: Optional[SituationExchangePermissions] = field(
        default=None,
        metadata={
            "name": "SituationExchangePermissions",
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
class SituationExchangeDeliveryStructure(AbstractServiceDeliveryStructure):
    """Type for Delivery for Situation Exchange Service.

    Provides information about one or more vehicles; each has its own
    VEHICLE activity element.

    :ivar pt_situation_context: Default context for common properties of
        SITUATIONs, Values specified apply to all SITUATIONs unless
        overridden. Can be used optionally to reduce file bulk.
    :ivar situations: SITUATIONs in Delivery.
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    pt_situation_context: Optional[ContextStructure] = field(
        default=None,
        metadata={
            "name": "PtSituationContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situations: Optional["SituationExchangeDeliveryStructure.Situations"] = field(
        default=None,
        metadata={
            "name": "Situations",
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
    class Situations:
        """
        :ivar pt_situation_element: Description of an SITUATION.
        :ivar road_situation_element:
        """

        pt_situation_element: List[PtSituationElementStructure] = field(
            default_factory=list,
            metadata={
                "name": "PtSituationElement",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        road_situation_element: List[RoadSituationElement] = field(
            default_factory=list,
            metadata={
                "name": "RoadSituationElement",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class SituationExchangeRequest(SituationExchangeRequestStructure):
    """
    Request for information about Facilities status.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SituationExchangeCapabilitiesResponse(SituationExchangeCapabilitiesResponseStructure):
    """Capabilities for Situation Exchange Service.

    Answers a VehicleMontoringCapabilitiesRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SituationExchangeDelivery(SituationExchangeDeliveryStructure):
    """
    Delivery for Situation Exchange Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SituationExchangeSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Type for Subscription Request for Situation Exchange Service.

    :ivar situation_exchange_request:
    :ivar incremental_updates: Whether the producer will return the
        complete set of current data, or only provide updates to this
        data, i.e. additions, modifications and deletions. If false or
        omitted, each subscription response will contain the full
        information as specified in this request.
    :ivar extensions:
    """

    situation_exchange_request: Optional[SituationExchangeRequest] = field(
        default=None,
        metadata={
            "name": "SituationExchangeRequest",
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
class SituationExchangeDeliveriesStructure:
    """Type for Deliveries for Situation Exchange Service.

    Used in WSDL.

    :ivar situation_exchange_delivery: Delivery for Vehicle Activity
        Service.
    """

    situation_exchange_delivery: List[SituationExchangeDelivery] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )


@dataclass
class SituationExchangeSubscriptionRequest(SituationExchangeSubscriptionStructure):
    """
    Request for a subscription to the Situation Exchange Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
