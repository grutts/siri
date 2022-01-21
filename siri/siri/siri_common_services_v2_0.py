from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri.siri_request_error_conditions_v2_0 import (
    CapabilityNotSupportedError,
    OtherError,
    ServiceDeliveryErrorConditionStructure,
    ServiceNotAvailableError,
    UnknownSubscriberError,
    UnknownSubscriptionError,
)
from siri.siri.siri_requests_v2_0 import (
    AbstractNotificationStructure,
    AuthenticatedRequestStructure,
    ConsumerRequestEndpointStructure,
    ConsumerResponseEndpointStructure,
    ProducerRequestEndpointStructure,
    RequestStructure,
    ResponseEndpointStructure,
    ResponseStructure,
)
from siri.siri_utility.siri_utility_v1_1 import (
    EmptyType,
    Extensions,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataNameSpacesStructure:
    """
    Name spaces.

    :ivar stop_point_name_space: Name space for STOP POINTs.
    :ivar line_name_space: Name space for LINE names and DIRECTIONss.
    :ivar product_category_name_space: Name space for Product
        Categories.
    :ivar service_feature_name_space: Name space for service features.
    :ivar vehicle_feature_name_space: Name space for VEHICLE features.
    """

    stop_point_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceFeatureNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_name_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleFeatureNameSpace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class DataSupplyRequestBodyStructure:
    """Type for Body of Data Supply Request.

    Used in WSDL.

    :ivar notification_ref: Reference to a specific notification message
        for which data is to be fetched. Can be used to distinguish
        between notfcatiosn for the same service and subscriber but for
        different filters.If none specified,
    :ivar all_data: Whether to return all data, or just new updates
        since the last delivery. Default false, i.e. just updates.
    """

    notification_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


class DeliveryMethodEnumeration(Enum):
    """
    Delivery Method: Fetched or Direct Delivery.
    """

    DIRECT = "direct"
    FETCHED = "fetched"


class PredictorsEnumeration(Enum):
    """
    Allowed values for predictors.
    """

    AVMS_ONLY = "avmsOnly"
    ANYONE = "anyone"


@dataclass
class CheckStatusRequestStructure(RequestStructure):
    """
    Type for check status request.
    """

    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class CheckStatusResponseBodyStructure:
    """Type for Body of Service Status Check Response.

    Used in WSDL. Same as CheckStatusResponseStructure, but without
    extension to be consistent with the other operation definition.

    :ivar status:
    :ivar data_ready: Whether data delivery is ready to be fetched SIRI
        v 2.0
    :ivar error_condition: Description of any error or warning condition
        that applies to the status check.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar service_started_time: Time at which current instantiation of
        service started.
    """

    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_ready: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DataReady",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["CheckStatusResponseBodyStructure.ErrorCondition"] = field(
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
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar service_not_available_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        service_not_available_error: Optional[ServiceNotAvailableError] = field(
            default=None,
            metadata={
                "name": "ServiceNotAvailableError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class CheckStatusResponseStructure(ResponseStructure):
    """
    Type for Service Status Check Response.

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
    :ivar status:
    :ivar data_ready: Whether data delivery is ready to be fetched SIRI
        v 2.0
    :ivar error_condition: Description of any error or warning condition
        that applies to the status check.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar service_started_time: Time at which current instantiation of
        service started.
    :ivar extensions:
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
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_ready: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DataReady",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["CheckStatusResponseStructure.ErrorCondition"] = field(
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
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
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
    class ErrorCondition:
        """
        :ivar service_not_available_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        service_not_available_error: Optional[ServiceNotAvailableError] = field(
            default=None,
            metadata={
                "name": "ServiceNotAvailableError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class DataReadyRequestStructure(AbstractNotificationStructure):
    """Type for Request from Producer to Consumer to notify that data update is
    ready to fetch.

    Answered with a DataReadyResponse.
    """


@dataclass
class DataReadyResponseStructure(ConsumerResponseEndpointStructure):
    """
    Type for Data ready Acknowledgement Response.

    :ivar status:
    :ivar error_condition: Description of any error or warning condition
        as to why Consumer cannot fetch data.
    """

    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["DataReadyResponseStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar unknown_subscription_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriptionError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class DataReceivedResponseStructure(ConsumerResponseEndpointStructure):
    """
    Type for Data received Acknowledgement Response.

    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    """

    status: bool = field(
        default=True,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    error_condition: Optional["DataReceivedResponseStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar unknown_subscription_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriptionError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class DataSupplyRequestStructure(ConsumerRequestEndpointStructure):
    """
    Type for Data supply Request.

    :ivar notification_ref: Reference to a specific notification message
        for which data is to be fetched. Can be used to distinguish
        between notfcatiosn for the same service and subscriber but for
        different filters.If none specified,
    :ivar all_data: Whether to return all data, or just new updates
        since the last delivery. Default false, i.e. just updates.
    """

    notification_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class HeartbeatNotificationStructure(ProducerRequestEndpointStructure):
    """
    Type for Service Heartbeat Notification.

    :ivar status:
    :ivar data_ready: Whether data delivery is ready to be fetched SIRI
        v 2.0
    :ivar error_condition: Description of any error or warning condition
        that applies to the status check.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    :ivar service_started_time: Time at which current instantiation of
        service started.
    :ivar extensions:
    """

    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_ready: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DataReady",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["HeartbeatNotificationStructure.ErrorCondition"] = field(
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
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
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
    class ErrorCondition:
        """
        :ivar service_not_available_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        service_not_available_error: Optional[ServiceNotAvailableError] = field(
            default=None,
            metadata={
                "name": "ServiceNotAvailableError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class ServiceRequestContextStructure:
    """Configurable context for requests.

    Intended Primarily as a documentation mechanism.

    :ivar check_status_address: Address to which CheckStatus requests
        are to be sent.
    :ivar subscribe_address: Address to which subscription requests are
        to be sent.
    :ivar manage_subscription_address: Address to which subscription
        requests are to be sent. If absent, same as SubscribeAddress.
    :ivar get_data_address: Address to which requests are to return
        data.
    :ivar status_response_address: Address to which CheckStatus
        responses and heartbeats are to be sent. If absent, same as
        SubscriberAddress.
    :ivar subscriber_address: Address to which subscription responses
        are to be sent.
    :ivar notify_address: Address to which notifcations requests are to
        be sent. If absent, same as SubscriberAddress.
    :ivar consumer_address: Address to which data is to be sent. If
        absent, same as NotifyAddress.
    :ivar data_name_spaces: Default names pace used to scope data
        identifiers.
    :ivar language: Preferred language in which to return text values.
    :ivar wgs_decimal_degrees: Geospatial coordinates are given as Wgs
        84 Latiude and longitude, decimial degrees of arc.
    :ivar gml_coordinate_format: Name of GML Coordinate format used for
        Geospatial points in responses.
    :ivar distance_units: Units for Distance Type. Default is metres.
        +SIRI v2.0
    :ivar velocity_units: Units for Distance Type. Default is metres per
        second. +SIRI v2.0
    :ivar data_horizon: Maximum data horizon for requests.
    :ivar request_timeout: Timeout for requests. [Should this be
        separate for each type?]
    :ivar delivery_method: Whether Delivery is fetched or retrieved.
    :ivar multipart_despatch: Whether multi-part delivery is allowed,
        i.e. the breaking up of updates into more than one delivery
        messages with a MoreData flag,
    :ivar confirm_delivery: Whether Consumers should issue an
        acknowledgement on successful receipt of a delivery. Default is
        ' false'.
    :ivar maximimum_number_of_subscriptions: Maximum Number of
        subscriptions that can be sustained by the subscriber. If absent
        no limit.
    :ivar allowed_predictors: Who may make a prediction.
    :ivar prediction_function: Name of prediction method used.
    """

    check_status_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "CheckStatusAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscribe_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscribeAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    manage_subscription_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManageSubscriptionAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    get_data_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "GetDataAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status_response_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "StatusResponseAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscriber_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotifyAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consumer_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_name_spaces: Optional[DataNameSpacesStructure] = field(
        default=None,
        metadata={
            "name": "DataNameSpaces",
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
    wgs_decimal_degrees: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "WgsDecimalDegrees",
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
    distance_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    velocity_units: Optional[str] = field(
        default=None,
        metadata={
            "name": "VelocityUnits",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_horizon: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_timeout: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RequestTimeout",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delivery_method: Optional[DeliveryMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "DeliveryMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    multipart_despatch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MultipartDespatch",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    confirm_delivery: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConfirmDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximimum_number_of_subscriptions: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximimumNumberOfSubscriptions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    allowed_predictors: Optional[PredictorsEnumeration] = field(
        default=None,
        metadata={
            "name": "AllowedPredictors",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "PredictionFunction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class StatusResponseStructure(ResponseStructure):
    """
    Type for Response Status.

    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
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
class TerminateSubscriptionRequestBodyStructure:
    """Type for Body of Terminate Subscription Request content.

    Used in WSDL.

    :ivar subscriber_ref: Participant identifier of Subscriber.
        Subscription ref will be unique within this.
    :ivar all: Terminate all subscriptions for the requestor.
    :ivar subscription_ref: Terminate the subscription identfiied by the
        reference.
    """

    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class TerminateSubscriptionRequestStructure(AuthenticatedRequestStructure):
    """
    Type for request to terminate a subscription or subscriptions.

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
    :ivar subscriber_ref: Participant identifier of Subscriber.
        Subscription ref will be unique within this.
    :ivar all: Terminate all subscriptions for the requestor.
    :ivar subscription_ref: Terminate the subscription identfiied by the
        reference.
    :ivar extensions:
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
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "All",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
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
class TerminationResponseStatusStructure:
    """
    Type for Status of termination response.

    :ivar response_timestamp:
    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar subscriber_ref: Unique identifier of Subscriber - reference to
        a Participant.
    :ivar subscription_filter_ref: Unique identifier of Subscription
        filter to which this subscription is assigned. If there is onlya
        single filter, then can be omitted.
    :ivar subscription_ref: Reference to a service subscription: unique
        within Service and Subscriber.
    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    """

    response_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
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
    status: bool = field(
        default=True,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    error_condition: Optional["TerminationResponseStatusStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar capability_not_supported_error:
        :ivar unknown_subscriber_error:
        :ivar unknown_subscription_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
            default=None,
            metadata={
                "name": "CapabilityNotSupportedError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        unknown_subscriber_error: Optional[UnknownSubscriberError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriberError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriptionError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class CheckStatusRequest(CheckStatusRequestStructure):
    """Request from Consumer to Producer to check whether services is working.

    Answers a CheckStatusRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusResponse(CheckStatusResponseStructure):
    """Response from Producer to Consumer to inform whether services is
    working.

    Answers a CheckStatusRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ContextualisedRequestStructure:
    """
    Type for General SIRI Request.

    :ivar service_request_context: General request properties -
        typically configured rather than repeated on request.
    :ivar request_timestamp:
    :ivar account_id: Account Identifier. May be used to attribute
        requests to a particular application provider and authentication
        key. The account  may be common to all users of an application,
        or to an individual user. Note that to identify an individual
        user the  RequestorRef can be used with an anonymised token.  .
        +SIRI v2.0
    :ivar account_key: Authentication key for request. May be used to
        authenticate requests from a particular account. +SIRI v2.0
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

    service_request_context: Optional[ServiceRequestContextStructure] = field(
        default=None,
        metadata={
            "name": "ServiceRequestContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
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
class DataReadyAcknowledgement(DataReadyResponseStructure):
    """
    Response from Consumer to Producer to acknowledge to Producer that a
    DataReadyRequest has been received.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyNotification(DataReadyRequestStructure):
    """Request from Producer to Consumer to notify that data update is ready to
    fetch.

    Answered with a DataReadyResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DataReceivedAcknowledgement(DataReceivedResponseStructure):
    """Response from Consumer to Producer to acknowledge that data hase been
    received.

    Used as optioanl extra step if reliable delivery is needed. Answers
    a ServiceDelivery.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class DataSupplyRequest(DataSupplyRequestStructure):
    """Request from Consumer to Producer to fetch update previously notified by
    a Data ready message.

    Answered with a Service Delivery.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class HeartbeatNotification(HeartbeatNotificationStructure):
    """
    Notification from Producer to Consumer to indicate that the service is
    running normally.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ResponseStatus(StatusResponseStructure):
    """Contains infromation about the processing of a an individual service subscription - either success info or an error condition. (VDV Acknowledgement)."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionRequest(TerminateSubscriptionRequestStructure):
    """Request from Subscriber to Subscription Manager to terminate a
    subscription.

    Answered with a TerminateSubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class TerminateSubscriptionResponseStructure(ResponseEndpointStructure):
    """
    Type for Response to a request to terminate a subscription or
    subscriptions.

    :ivar termination_response_status: Status of each subscription
        termnination response.
    """

    termination_response_status: List[TerminationResponseStatusStructure] = field(
        default_factory=list,
        metadata={
            "name": "TerminationResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SubscriptionResponseBodyStructure:
    """Type for Body of Subscription Response.

    Used in WSDL.

    :ivar response_status:
    :ivar subscription_manager_address: Endpoint address of subscription
        manager if different from that of the Producer or known default.
    :ivar service_started_time: Time at which service providing the
        subscription was last started. Can be used to detect restarts.
        If absent, unknown.
    """

    response_status: List[ResponseStatus] = field(
        default_factory=list,
        metadata={
            "name": "ResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    subscription_manager_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionManagerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SubscriptionResponseStructure(ResponseEndpointStructure):
    """
    Type for Subscription Response.

    :ivar response_status:
    :ivar subscription_manager_address: Endpoint address of subscription
        manager if different from that of the Producer or known default.
    :ivar service_started_time: Time at which service providing the
        subscription was last started. Can be used to detect restarts.
        If absent, unknown.
    :ivar extensions:
    """

    response_status: List[ResponseStatus] = field(
        default_factory=list,
        metadata={
            "name": "ResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    subscription_manager_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionManagerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
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
class TerminateSubscriptionResponse(TerminateSubscriptionResponseStructure):
    """Request from Subscriber to Subscription Manager to terminate a
    subscription.

    Answered with a TerminateSubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionResponse(SubscriptionResponseStructure):
    """Response from Producer to Consumer to inform whether subscriptions have
    been created.

    Answers a previous SubscriptionRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
