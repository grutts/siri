from dataclasses import dataclass, field
from typing import Optional
from siri.siri_utility.siri_utility_v1_1 import EmptyType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractTopicPermissionStructure:
    """
    Type for Abstract Permission Topic.

    :ivar allow: Whether the participant may access this topic. Default
        is 'true'.
    """

    allow: bool = field(
        default=True,
        metadata={
            "name": "Allow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AllowAll:
    """
    Allow access to all topics known to the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class CapabilityAccessControlStructure:
    """
    Type for Common Access control capabilities.

    :ivar request_checking: Whether access control of requests is
        supported. Default is 'false'.
    """

    request_checking: bool = field(
        default=False,
        metadata={
            "name": "RequestChecking",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class AbstractPermissionStructure:
    """
    Type for Abstract Permission.

    :ivar all_participants: Parmissions apply by default to All
        particpants. May be overidden by other separate permissions for
        individual.
    :ivar participant_ref: Permission applies to specified participant.
    :ivar general_capabilities: Permissions for general capabilities.
    """

    all_participants: Optional[EmptyType] = field(
        default=None,
        metadata={
            "name": "AllParticipants",
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
    general_capabilities: Optional["AbstractPermissionStructure.GeneralCapabilities"] = field(
        default=None,
        metadata={
            "name": "GeneralCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class GeneralCapabilities:
        """
        :ivar request_response: Participant may make direct requests for
            data. Default is 'true'.
        :ivar publish_subscribe: Participant may create subscriptions.
            Default True.
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
