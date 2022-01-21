from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from siri.siri.siri_requests_v2_0 import (
    AbstractCapabilitiesStructure,
    AbstractFunctionalServiceRequestStructure,
    AbstractIdentifiedItemStructure,
    AbstractReferencingItemStructure,
    AbstractServiceCapabilitiesResponseStructure,
    AbstractServiceDeliveryStructure,
    AbstractSubscriptionStructure,
    CapabilityRequestPolicyStructure,
    ServiceCapabilitiesRequestStructure,
)
from siri.siri_model.siri_model_permissions_v2_0 import PermissionsStructure
from siri.siri_model.siri_situation_identity_v1_1 import SituationRef
from siri.siri_utility.siri_permissions_v2_0 import (
    AbstractPermissionStructure,
    AbstractTopicPermissionStructure,
    CapabilityAccessControlStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about General Message Service Capabilities.

    Answered with a GeneralMessageCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageCapabilityAccessControlStructure(CapabilityAccessControlStructure):
    """
    Type for access control.

    :ivar check_info_channel_ref: If access control is supported,
        whether access control by LINE is supported. Default is 'true'.
    """

    check_info_channel_ref: bool = field(
        default=True,
        metadata={
            "name": "CheckInfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class GeneralMessageRequestStructure(AbstractFunctionalServiceRequestStructure):
    """
    Service Request for General Messages.

    :ivar info_channel_ref: Referenceto an Info Channel for which
        messages are to be returned.
    :ivar language: Preferred language in which to return text values.
    :ivar extensions:
    :ivar version: Version number of request. Fixed
    """

    info_channel_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InfoChannelRef",
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
class InfoChannelPermissionStructure(AbstractTopicPermissionStructure):
    """
    Type for Info Channel Permission.

    :ivar info_channel_ref: Reference to an Info Channel to which
        permission applies.
    """

    info_channel_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class InfoMessageCancellationStructure(AbstractReferencingItemStructure):
    """
    Type for Revocation of a previous message.

    :ivar info_message_identifier: Identifier of message. Unique within
        service and Producer participant.
    :ivar info_channel_ref: Info Channel to which message belongs.
    :ivar extensions:
    """

    info_message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    info_channel_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoChannelRef",
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
class InfoMessageStructure(AbstractIdentifiedItemStructure):
    """Type for an Info Message.

    @formatRef.

    :ivar info_message_identifier: Unique identifier of message.
    :ivar info_message_version: Optional version number of update to
        previosu message.
    :ivar info_channel_ref: Info Channel to which message belongs.
    :ivar valid_until_time: Time until when message is valid. If absent
        unopen ended.
    :ivar situation_ref:
    :ivar content: Message Content. Format is specified by Format Ref.
    :ivar extensions:
    :ivar format_ref: Reference to a format of the Content. If absent,
        free text.
    """

    info_message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    info_message_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "InfoMessageVersion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_channel_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: Optional[SituationRef] = field(
        default=None,
        metadata={
            "name": "SituationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    content: Optional[object] = field(
        default=None,
        metadata={
            "name": "Content",
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
    format_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatRef",
            "type": "Attribute",
        },
    )


@dataclass
class GeneralMessage(InfoMessageStructure):
    """
    An informative message.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageCancellation(InfoMessageCancellationStructure):
    """
    A revocation of a previous message.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageRequest(GeneralMessageRequestStructure):
    """
    Request for information about general information messages affecting stops,
    vehicles or services.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    """
    Type for General Message Capabilities.

    :ivar topic_filtering: Filtering Capabilities.
    :ivar request_policy: Request Policiy capabilities.
    :ivar access_control: Optional Access control capabilities.
    """

    topic_filtering: Optional["GeneralMessageServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional[CapabilityRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_control: Optional[GeneralMessageCapabilityAccessControlStructure] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class TopicFiltering:
        """
        :ivar default_preview_interval: Default preview interval.
            Default is 60 minutes.
        :ivar filter_by_info_channel: Whether results can be filtered by
            InfoChannel, departures. Default is 'true'.
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
        filter_by_info_channel: Optional[bool] = field(
            default=None,
            metadata={
                "name": "FilterByInfoChannel",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class GeneralMessageServicePermissionStructure(AbstractPermissionStructure):
    """
    Type for General MessageService Permission.

    :ivar info_channel_permissions: The monitoring points that the
        participant may access.
    :ivar extensions:
    """

    info_channel_permissions: Optional["GeneralMessageServicePermissionStructure.InfoChannelPermissions"] = field(
        default=None,
        metadata={
            "name": "InfoChannelPermissions",
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
    class InfoChannelPermissions:
        """
        :ivar allow_all:
        :ivar info_channel_permission: Participant's permission for this
            InfoChannel.
        """

        allow_all: Optional[bool] = field(
            default=None,
            metadata={
                "name": "AllowAll",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        info_channel_permission: List[InfoChannelPermissionStructure] = field(
            default_factory=list,
            metadata={
                "name": "InfoChannelPermission",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class GeneralMessageDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Delivery for General Message.

    :ivar general_message:
    :ivar general_message_cancellation:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    general_message: List[GeneralMessage] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_cancellation: List[GeneralMessageCancellation] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageCancellation",
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
class GeneralMessagePermissions(PermissionsStructure):
    """
    Participant's permissions to use the service.

    :ivar general_message_permission: Permission or a single particpant
        or all participants.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    general_message_permission: List[GeneralMessageServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessagePermission",
            "type": "Element",
        },
    )


@dataclass
class GeneralMessageServiceCapabilities(GeneralMessageServiceCapabilitiesStructure):
    """
    Capabilities of General Message Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageSubscriptionStructure(AbstractSubscriptionStructure):
    """
    Subscription for General Message Service.
    """

    general_message_request: Optional[GeneralMessageRequest] = field(
        default=None,
        metadata={
            "name": "GeneralMessageRequest",
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
class GeneralMessageCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    """
    Type for Delivery for General MessageService.

    :ivar general_message_service_capabilities:
    :ivar general_message_permissions:
    :ivar extensions:
    :ivar version: Version number of response. Fixed
    """

    general_message_service_capabilities: Optional[GeneralMessageServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "GeneralMessageServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_permissions: Optional[GeneralMessagePermissions] = field(
        default=None,
        metadata={
            "name": "GeneralMessagePermissions",
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
class GeneralMessageDelivery(GeneralMessageDeliveryStructure):
    """
    Delivery for General Message Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageSubscriptionRequest(GeneralMessageSubscriptionStructure):
    """
    Request for a subscription to General Message Service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageCapabilitiesResponse(GeneralMessageCapabilitiesResponseStructure):
    """Capabilities for General Message Service.

    Answers a GeneralMessageCapabilitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class GeneralMessageDeliveriesStructure:
    """Type for Deliveries.

    Used in WSDL.

    :ivar general_message_delivery: Delivery for general Message
        service.
    """

    general_message_delivery: List[GeneralMessageDelivery] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
