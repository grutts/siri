from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorCodeStructure:
    """
    Type for Error Code.

    :ivar error_text: Addtional Description of error. This allows a
        descripotion to be supplied when the Error code is used in a
        specific WSDL fault, rather than within a general error
        condition.
    :ivar number: Error code number assoicated with error.
    """

    error_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AccessNotAllowedErrorStructure(ErrorCodeStructure):
    """
    Type forError:Access Not Allowed.
    """


@dataclass
class AllowedResourceUsageExceededErrorStructure(ErrorCodeStructure):
    """Type for error.

    AllowedResourceUsageExceeded
    """


@dataclass
class BeyondDataHorizonErrorStructure(ErrorCodeStructure):
    """
    Type for error.
    """


@dataclass
class CapabilityNotSupportedErrorStructure(ErrorCodeStructure):
    """
    Type for Error: Service does not support requested capability.

    :ivar capability_ref: Id of capabiliuty that is noit supported.
    """

    capability_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CapabilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class EndpointDeniedAccessStructure(ErrorCodeStructure):
    """
    Type for Error: EndpointDeniedAccess +SIRI v2.0.

    :ivar endpoint: Endpoint that was denied access  + SIRI v2.0
    """

    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class EndpointNotAvailableAccessStructure(ErrorCodeStructure):
    """
    Type for Error: EndpointNotAvailable +SIRI v2.0.

    :ivar endpoint: Endpoint that is noit available. + SIRI v2.0
    """

    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class InvalidDataReferencesErrorStructure(ErrorCodeStructure):
    """Type for InvalidDataReferencesError:.

    +SIRI v2.0.
    """


@dataclass
class NoInfoForTopicErrorStructure(ErrorCodeStructure):
    """
    Type for Error: No Info for Topic.
    """


@dataclass
class OtherErrorStructure(ErrorCodeStructure):
    """
    Type for error.
    """


@dataclass
class ParametersIgnoredErrorStructure(ErrorCodeStructure):
    """Type for Parameters Ignored Error:.

    +SIRI v2.0.
    """


@dataclass
class ServiceNotAvailableErrorStructure(ErrorCodeStructure):
    """
    Type for Service Not Available error.

    :ivar expected_restart_time: Expected time fro reavailability of
        servcie.  +SIRI v2.0
    """

    expected_restart_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedRestartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class UnapprovedKeyAccessStructure(ErrorCodeStructure):
    """
    Type for Error: UnapprovedKey +SIRI v2.0.

    :ivar key: User key.
    """

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class UnknownEndpointErrorStructure(ErrorCodeStructure):
    """
    Type for Error: Unknown Endpoint +SIRI v2.0.

    :ivar endpoint: Endpoint that is noit known. + SIRI v2.0
    """

    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class UnknownExtensionsErrorStructure(ErrorCodeStructure):
    """Type for Unknown Extensions Error:.

    +SIRI v2.0.
    """


@dataclass
class UnknownParticipantErrorStructure(ErrorCodeStructure):
    """Type for Error: Unknown Participant.

    +SIRI v2.0

    :ivar participant_ref: Reference to  Participant who is unknown. +
        SIRI v2.0
    """

    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class UnknownSubscriberErrorStructure(ErrorCodeStructure):
    """
    Type for Error: Subscriber not found.

    :ivar subscriber_ref: Id of capabiliuty that is noit supported. +
        SIRI v2.0
    """

    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class UnknownSubscriptionErrorStructure(ErrorCodeStructure):
    """
    Type for Error: Subscription not found.

    :ivar subscription_code: Ubscription code that could not be found. +
        SIRI v2.0
    """

    subscription_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AccessNotAllowedError(AccessNotAllowedErrorStructure):
    """Error: Requestor is not authorised to the service or data requested."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class AllowedResourceUsageExceededError(AllowedResourceUsageExceededErrorStructure):
    """Error: Valid request was made but request would exceed the permitted resource usage of the client."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class BeyondDataHorizon(BeyondDataHorizonErrorStructure):
    """Error: Data period or subscription period is outside of period covered by service."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityNotSupportedError(CapabilityNotSupportedErrorStructure):
    """Error: Service does not support the requested capability."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EndpointDeniedAccessError(EndpointDeniedAccessStructure):
    """Error:Endpoint to which a message is to be distributed did not allow
    access by the cloient.

    +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class EndpointNotAvailableAccessError(EndpointNotAvailableAccessStructure):
    """Error:Recipient of a message to be distributed is not available.

    +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class InvalidDataReferencesError(InvalidDataReferencesErrorStructure):
    """Error: Request contains references to  identifiers that are not known.  +SIRI v2.0."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class NoInfoForTopicError(NoInfoForTopicErrorStructure):
    """Error: Valid request was made but service does not hold any data for the requested topic. expression."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class OtherError(OtherErrorStructure):
    """Error: Error type other than the well defined codes."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ParametersIgnoredError(ParametersIgnoredErrorStructure):
    """Error: Request contained parameters that were not supported by the producer. A response has been provided but some parameters have been ignored. +SIRI v2.0."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceNotAvailableError(ServiceNotAvailableErrorStructure):
    """Error: Functional service is not available to use (but it is still capable of giving this response)."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class UnapprovedKeyAccessError(UnapprovedKeyAccessStructure):
    """Error:Recipient of a message to be distributed is not available.

    +SIRI v2.0
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class UnknownEndpointError(UnknownEndpointErrorStructure):
    """Error: Recipient for a message to be distributed is unknown. +SIRI v2.0"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class UnknownExtensionsError(UnknownExtensionsErrorStructure):
    """Error: Request contained extensions that were not supported by the producer. A response has been provided but some or all extensions have been ignored..  +SIRI v2.0."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class UnknownParticipantError(UnknownParticipantErrorStructure):
    """Error: Recipient for a message to be distributed is unknown. +SIRI v2.0"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriberError(UnknownSubscriberErrorStructure):
    """Error: Subscriber not found."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriptionError(UnknownSubscriptionErrorStructure):
    """Error: Subscription not found."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ErrorConditionElementStructure:
    """
    Type for Standard ErrorConditions for Service request.

    :ivar unapproved_key_access_error:
    :ivar unknown_participant_error: Error: Recipient for a message to
        be distributed is unknown. I.e. delegatior is found, but  +SIRI
        v2.0
    :ivar unknown_endpoint_error:
    :ivar endpoint_denied_access_error:
    :ivar endpoint_not_available_access_error:
    :ivar service_not_available_error:
    :ivar capability_not_supported_error:
    :ivar access_not_allowed_error:
    :ivar invalid_data_references_error:
    :ivar beyond_data_horizon: Error: Data period or subscription period
        is outside of period covered by service.   +SIRI v2.0.
    :ivar no_info_for_topic_error:
    :ivar parameters_ignored_error:
    :ivar unknown_extensions_error: Error: Request contained extensions
        that were not supported by the producer. A response has been
        provided but some or all extensions have been ignored.  +SIRI
        v2.0.
    :ivar allowed_resource_usage_exceeded_error:
    :ivar other_error:
    :ivar unknown_subscription_error:
    :ivar description: Text description of error.
    """

    unapproved_key_access_error: Optional[UnapprovedKeyAccessError] = field(
        default=None,
        metadata={
            "name": "UnapprovedKeyAccessError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_participant_error: Optional[UnknownParticipantError] = field(
        default=None,
        metadata={
            "name": "UnknownParticipantError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_endpoint_error: Optional[UnknownEndpointError] = field(
        default=None,
        metadata={
            "name": "UnknownEndpointError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    endpoint_denied_access_error: Optional[EndpointDeniedAccessError] = field(
        default=None,
        metadata={
            "name": "EndpointDeniedAccessError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    endpoint_not_available_access_error: Optional[EndpointNotAvailableAccessError] = field(
        default=None,
        metadata={
            "name": "EndpointNotAvailableAccessError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_not_available_error: Optional[ServiceNotAvailableError] = field(
        default=None,
        metadata={
            "name": "ServiceNotAvailableError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
        default=None,
        metadata={
            "name": "CapabilityNotSupportedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_not_allowed_error: Optional[AccessNotAllowedError] = field(
        default=None,
        metadata={
            "name": "AccessNotAllowedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    invalid_data_references_error: Optional[InvalidDataReferencesError] = field(
        default=None,
        metadata={
            "name": "InvalidDataReferencesError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    beyond_data_horizon: Optional[BeyondDataHorizon] = field(
        default=None,
        metadata={
            "name": "BeyondDataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    no_info_for_topic_error: Optional[NoInfoForTopicError] = field(
        default=None,
        metadata={
            "name": "NoInfoForTopicError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    parameters_ignored_error: Optional[ParametersIgnoredError] = field(
        default=None,
        metadata={
            "name": "ParametersIgnoredError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_extensions_error: Optional[UnknownExtensionsError] = field(
        default=None,
        metadata={
            "name": "UnknownExtensionsError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    allowed_resource_usage_exceeded_error: Optional[AllowedResourceUsageExceededError] = field(
        default=None,
        metadata={
            "name": "AllowedResourceUsageExceededError",
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
    unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
        default=None,
        metadata={
            "name": "UnknownSubscriptionError",
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
class ErrorConditionStructure:
    """
    Type for RequestErrorCondition.

    :ivar service_not_available_error:
    :ivar capability_not_supported_error:
    :ivar access_not_allowed_error:
    :ivar invalid_data_references_error:
    :ivar beyond_data_horizon: Error: Data period or subscription period
        is outside of period covered by service.   +SIRI v2.0.
    :ivar no_info_for_topic_error:
    :ivar parameters_ignored_error:
    :ivar unknown_extensions_error: Error: Request contained extensions
        that were not supported by the producer. A response has been
        provided but some or all extensions have been ignored.  +SIRI
        v2.0.
    :ivar allowed_resource_usage_exceeded_error:
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
    capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
        default=None,
        metadata={
            "name": "CapabilityNotSupportedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_not_allowed_error: Optional[AccessNotAllowedError] = field(
        default=None,
        metadata={
            "name": "AccessNotAllowedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    invalid_data_references_error: Optional[InvalidDataReferencesError] = field(
        default=None,
        metadata={
            "name": "InvalidDataReferencesError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    beyond_data_horizon: Optional[BeyondDataHorizon] = field(
        default=None,
        metadata={
            "name": "BeyondDataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    no_info_for_topic_error: Optional[NoInfoForTopicError] = field(
        default=None,
        metadata={
            "name": "NoInfoForTopicError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    parameters_ignored_error: Optional[ParametersIgnoredError] = field(
        default=None,
        metadata={
            "name": "ParametersIgnoredError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_extensions_error: Optional[UnknownExtensionsError] = field(
        default=None,
        metadata={
            "name": "UnknownExtensionsError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    allowed_resource_usage_exceeded_error: Optional[AllowedResourceUsageExceededError] = field(
        default=None,
        metadata={
            "name": "AllowedResourceUsageExceededError",
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
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ServiceDeliveryErrorConditionStructure:
    """
    Type for Standard ErrorConditiosn for Service request.

    :ivar unapproved_key_access_error:
    :ivar unknown_participant_error: Error: Recipient for a message to
        be distributed is unknown. I.e. delegatior is found, but  +SIRI
        v2.0
    :ivar unknown_endpoint_error:
    :ivar endpoint_denied_access_error:
    :ivar endpoint_not_available_access_error:
    :ivar service_not_available_error:
    :ivar capability_not_supported_error:
    :ivar access_not_allowed_error:
    :ivar invalid_data_references_error:
    :ivar beyond_data_horizon: Error: Data period or subscription period
        is outside of period covered by service.   +SIRI v2.0.
    :ivar no_info_for_topic_error:
    :ivar parameters_ignored_error:
    :ivar unknown_extensions_error: Error: Request contained extensions
        that were not supported by the producer. A response has been
        provided but some or all extensions have been ignored.  +SIRI
        v2.0.
    :ivar allowed_resource_usage_exceeded_error:
    :ivar other_error:
    :ivar description: Text description of error.
    """

    unapproved_key_access_error: Optional[UnapprovedKeyAccessError] = field(
        default=None,
        metadata={
            "name": "UnapprovedKeyAccessError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_participant_error: Optional[UnknownParticipantError] = field(
        default=None,
        metadata={
            "name": "UnknownParticipantError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_endpoint_error: Optional[UnknownEndpointError] = field(
        default=None,
        metadata={
            "name": "UnknownEndpointError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    endpoint_denied_access_error: Optional[EndpointDeniedAccessError] = field(
        default=None,
        metadata={
            "name": "EndpointDeniedAccessError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    endpoint_not_available_access_error: Optional[EndpointNotAvailableAccessError] = field(
        default=None,
        metadata={
            "name": "EndpointNotAvailableAccessError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_not_available_error: Optional[ServiceNotAvailableError] = field(
        default=None,
        metadata={
            "name": "ServiceNotAvailableError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
        default=None,
        metadata={
            "name": "CapabilityNotSupportedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_not_allowed_error: Optional[AccessNotAllowedError] = field(
        default=None,
        metadata={
            "name": "AccessNotAllowedError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    invalid_data_references_error: Optional[InvalidDataReferencesError] = field(
        default=None,
        metadata={
            "name": "InvalidDataReferencesError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    beyond_data_horizon: Optional[BeyondDataHorizon] = field(
        default=None,
        metadata={
            "name": "BeyondDataHorizon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    no_info_for_topic_error: Optional[NoInfoForTopicError] = field(
        default=None,
        metadata={
            "name": "NoInfoForTopicError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    parameters_ignored_error: Optional[ParametersIgnoredError] = field(
        default=None,
        metadata={
            "name": "ParametersIgnoredError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_extensions_error: Optional[UnknownExtensionsError] = field(
        default=None,
        metadata={
            "name": "UnknownExtensionsError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    allowed_resource_usage_exceeded_error: Optional[AllowedResourceUsageExceededError] = field(
        default=None,
        metadata={
            "name": "AllowedResourceUsageExceededError",
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
class ErrorCondition(ErrorConditionStructure):
    """
    Description of error or warning condition associated with response.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ErrorConditionElement(ErrorConditionElementStructure):
    """
    Element fror an erroc condition  (for use in WSDL.)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDeliveryErrorConditionElement(ServiceDeliveryErrorConditionStructure):
    """
    Element fror an erroc condition for use in WSDL.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
