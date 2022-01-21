from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri.siri_request_error_conditions_v2_0 import ServiceDeliveryErrorConditionStructure
from siri.siri.siri_request_support_v2_0 import (
    CommunicationsTransportMethodEnumeration,
    CompressionMethodEnumeration,
)
from siri.siri_utility.siri_utility_v1_1 import (
    EmptyType,
    Extensions,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractItemStructure:
    """
    Type for an Activity.

    :ivar recorded_at_time: Time at which data was recorded.
    """

    recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AbstractRequestStructure:
    """
    Type for General SIRI Request.
    """

    request_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AbstractSubscriptionStructure:
    """
    Type for SIRI Service subscriptions.

    :ivar subscriber_ref: Participant identifier of Subscriber. Normally
        this will be given by context, i.e. be the same as on the
        Subscription Request.
    :ivar subscription_identifier: Identifier to be given to
        Subscription.
    :ivar initial_termination_time: Requested end time for subscription.
    """

    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    initial_termination_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "InitialTerminationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class CapabilityGeneralInteractionStructure:
    """
    Type for Common Request Policy capabilities.

    :ivar interaction: Interaction capabilities.
    :ivar delivery: Delivery capabilities.
    :ivar multipart_despatch: Whether the service supports multiple part
        despatch with MoreData flag. Default is 'true'.
    :ivar multiple_subscriber_filter: Whether the service supports
        multiple Subscriber Filters. Default is ' false'.
    :ivar has_confirm_delivery: Whether the service supports Delivery
        confirm.
    :ivar has_heartbeat: Whether the service has a heartbeat message.
        Default is 'false'.
    :ivar visit_numberis_order: Whether VisitNumber can be used as a
        strict order number within JOURNEY PATTERN. Default is 'false'.
    """

    interaction: Optional["CapabilityGeneralInteractionStructure.Interaction"] = field(
        default=None,
        metadata={
            "name": "Interaction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    delivery: Optional["CapabilityGeneralInteractionStructure.Delivery"] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    multipart_despatch: bool = field(
        default=True,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    multiple_subscriber_filter: bool = field(
        default=False,
        metadata={
            "name": "MultipleSubscriberFilter",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    has_confirm_delivery: bool = field(
        default=False,
        metadata={
            "name": "HasConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    has_heartbeat: bool = field(
        default=False,
        metadata={
            "name": "HasHeartbeat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    visit_numberis_order: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisitNumberisOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Interaction:
        """
        :ivar request_response: Whether the service supports Request
            Response Interaction. Default is 'true'.
        :ivar publish_subscribe: Whether the service supports Publish
            Subscribe Interaction. Default is 'true'.
        """

        request_response: bool = field(
            default=True,
            metadata={
                "name": "RequestResponse",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        publish_subscribe: bool = field(
            default=True,
            metadata={
                "name": "PublishSubscribe",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )

    @dataclass
    class Delivery:
        """
        :ivar direct_delivery: Whether the service supports Direct
            delivery.
        :ivar fetched_delivery: Whether the service supports Fetched
            delivery (VDV Style)
        """

        direct_delivery: Optional[bool] = field(
            default=None,
            metadata={
                "name": "DirectDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        fetched_delivery: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FetchedDelivery",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )


@dataclass
class CapabilitySubscriptionPolicyStructure:
    """
    Type for Common Subscription capabilities.

    :ivar has_incremental_updates: Whether incremental updates can be
        specified for updates Default is ' true'.
    :ivar has_change_sensitivity: Whether change threshold can be
        specified for updates. Default is 'true'.
    """

    has_incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasIncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_change_sensitivity: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasChangeSensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ResponseStructure:
    """
    General Type for General SIRI Response.
    """

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class Status:
    """Whether the request was processed successfully or not.

    Default is 'true'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        },
    )


@dataclass
class SubscriptionContextStructure:
    """Type for Subscription context - Configuration parameters which may be evrriden.

    :ivar heartbeat_interval: Interval for heartbeat.
    """

    heartbeat_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "HeartbeatInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractDiscoveryDeliveryStructure(ResponseStructure):
    """
    Abstract supertype fro discovery responses.

    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    """

    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractIdentifiedItemStructure(AbstractItemStructure):
    """
    Type for an Activity that can be referenced.

    :ivar item_identifier: Identifier of item.
    """

    item_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractReferencingItemStructure(AbstractItemStructure):
    """
    Type for an Activity that references a previous Activity.

    :ivar item_ref: Reference to an Activity Element of  a delivery.
    """

    item_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractRequiredIdentifiedItemStructure(AbstractItemStructure):
    """
    Type for an Activity that can be referenced.

    :ivar item_identifier: Identifier of item.
    """

    item_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AbstractRequiredReferencingItemStructure(AbstractItemStructure):
    """
    Type for an Activity that references a previous Activity.

    :ivar item_ref: Reference to an Activity Element of  a delivery.
    """

    item_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AbstractServiceCapabilitiesResponseStructure(ResponseStructure):
    """
    Type for capabilities response.

    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    """

    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractServiceDeliveryStructure(ResponseStructure):
    """
    Type for Common elementd for a SIRI service delivery of the Form
    xxxDelivery.

    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar default_language: Default language for text elements.
    """

    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
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


@dataclass
class AbstractServiceRequestStructure(AbstractRequestStructure):
    """
    Abstract Service Request for SIRI Service request.

    :ivar message_identifier: Arbitrary unique reference to this
        message.
    """

    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AuthenticatedRequestStructure(AbstractRequestStructure):
    """
    Type for Authticated SIRI Request.

    :ivar account_id: Account Identifier. May be used to attribute
        requests to a particular application provider and authentication
        key. The account  may be common to all users of an application,
        or to an individual user. Note that to identify an individual
        user the  RequestorRef can be used with an anonymised token.  .
        +SIRI v2.0
    :ivar account_key: Authentication key for request. May be used to
        authenticate requests from a particular account. +SIRI v2.0
    """

    account_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountId",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    account_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountKey",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class CapabilityRequestPolicyStructure:
    """
    Type for Common Request Policy capabilities.

    :ivar national_language: National languages supported by service.
    :ivar translations: Whether producer can provide multiple
        translations of NL text elements  +SIRI 2.0
    :ivar gml_coordinate_format: Name of GML Coordinate format used for
        Geospatial points in responses.
    :ivar wgs_decimal_degrees: Geospatial coordinates are given as Wgs
        84 Latiude and longitude, decimial degrees of arc.
    """

    national_language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "NationalLanguage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    translations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Translations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    gml_coordinate_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "GmlCoordinateFormat",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    wgs_decimal_degrees: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "WgsDecimalDegrees",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ConsumerResponseEndpointStructure(ResponseStructure):
    """Type for Unique reference to this response created by Consumer.

    May be used to reference the request in subsequent interactions.
    Used by WSDL.

    :ivar consumer_ref: Unique identifier of Consumer - a Participant
        reference.
    :ivar request_message_ref: Reference to an arbitrary unique
        idenitifer associated with the request which gave rise to this
        response.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    consumer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ProducerResponseEndpointStructure(ResponseStructure):
    """Type for Unique reference to reponse from producer.

    May be used to reference request in subsequent interactions. Used
    for WSDL.

    :ivar producer_ref: Unique identifier of Producer - Participant
        reference.
    :ivar address: Endpoint Address to which acknowledgements to confirm
        delivery are to be sent.
    :ivar response_message_identifier: An arbitrary unique reference
        associated with the response which may be used to reference it.
    :ivar request_message_ref: Reference to an arbitrary unique
        identifier associated with the request which gave rise to this
        response.
    """

    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ProducerResponseStructure(ResponseStructure):
    """
    Type for General SIRI Producer Response.

    :ivar producer_ref: Unique identifier of Producer - Participant
        reference.
    :ivar address: Endpoint Address to which acknowledgements to confirm
        delivery are to be sent.
    :ivar response_message_identifier: An arbitrary unique reference
        associated with the response which may be used to reference it.
    :ivar request_message_ref: Reference to an arbitrary unique
        identifier associated with the request which gave rise to this
        response.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ResponseEndpointStructure(ResponseStructure):
    """Type for Unique reference to reponse.

    May be used to reference request in subsequent interactions. Used
    for WSDL

    :ivar address: Address for further interaction.
    :ivar responder_ref: Participant reference that identifies
        responder.
    :ivar request_message_ref: Reference to an arbitrary unique
        reference associated with the request which gave rise to this
        response.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    responder_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponderRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class TransportDescriptionStructure:
    """
    Type for implementation structure.

    :ivar communications_transport_method: Communications Transport
        method used to exchange messages. Default is 'httpPost'.
    :ivar compression_method: Compression method used to compress
        messages for transmission. Default is 'none'.
    """

    communications_transport_method: CommunicationsTransportMethodEnumeration = field(
        default=CommunicationsTransportMethodEnumeration.HTTP_POST,
        metadata={
            "name": "CommunicationsTransportMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    compression_method: CompressionMethodEnumeration = field(
        default=CompressionMethodEnumeration.NONE,
        metadata={
            "name": "CompressionMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AbstractCapabilitiesStructure:
    """
    Type for Capabilities of StopMonitopring Service.

    :ivar general_interaction: General capabilities common to all SIRI
        service request types.
    :ivar transport_description: Implementation properties common to all
        request types.
    """

    general_interaction: Optional[CapabilityGeneralInteractionStructure] = field(
        default=None,
        metadata={
            "name": "GeneralInteraction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    transport_description: Optional[TransportDescriptionStructure] = field(
        default=None,
        metadata={
            "name": "TransportDescription",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractDiscoveryRequestStructure(AuthenticatedRequestStructure):
    """
    Requests for stop reference data for use in service requests.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message. n subsequent interactions.
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AbstractFunctionalServiceRequestStructure(AbstractServiceRequestStructure):
    """
    Abstract Service Request for SIRI Service request.
    """


@dataclass
class ConsumerRequestEndpointStructure(AuthenticatedRequestStructure):
    """Type for Unique reference to this request, created by Consumer.

    May be used to reference the request in subsequent interactions.
    Used by WSDL.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar consumer_ref: Unique identifier of Consumer - a Participant
        reference.
    :ivar message_identifier: Arbitrary unique reference to this
        message. Some systems may use just timestamp for this.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consumer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ProducerRequestEndpointStructure(AuthenticatedRequestStructure):
    """Type for Unique reference to request to the producer.

    May be used to reference request in subsequent interactions. Used
    for WSDL.

    :ivar address: Address to which response is to be sent. This may
        also be determined from ProducerRef and preconfigured data.
    :ivar producer_ref: Unique identifier of Producer - Participant
        reference.
    :ivar message_identifier: Arbitrary unique reference to this
        message. Some systems may use just timestamp for this. Where
        there are multiple SubscriptionFilters, this can be used to
        distinguish between different notifications for different
        filters.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class RequestStructure(AuthenticatedRequestStructure):
    """
    Type for General SIRI Request.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message. n subsequent interactions.
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ServiceCapabilitiesRequestStructure(AbstractServiceRequestStructure):
    """
    Type for ServcieCapabilities request.

    :ivar participant_permissions: Whether to include the requestors
        permissions in the response. Only applies if Access control
        capability supported. Default is 'false'.
    :ivar extensions:
    :ivar version: Version number of request. Fixed.
    """

    participant_permissions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ParticipantPermissions",
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
class AbstractNotificationStructure(ProducerRequestEndpointStructure):
    """
    Type for Notification Request.
    """


@dataclass
class AbstractSubscriptionRequestStructure(RequestStructure):
    """
    Type for COmmon Subscription Request.

    :ivar consumer_address: Address to which data is to be sent, if
        different from Address. This may also be determined from
        RequestorRef and preconfigured data.
    :ivar subscription_filter_identifier: Reference to a Subscription
        Filter with which this subscription is to be aggregated for
        purposes of notification and delivery. If absent, use the
        default filter. If present, use any existing filter with that
        identifier, if none found, create a new one. Optional SIRI
        feature.
    :ivar subscription_context: General values that apply to
        subscription. Usually set by configuration.
    """

    consumer_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionFilterIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_context: Optional[SubscriptionContextStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
