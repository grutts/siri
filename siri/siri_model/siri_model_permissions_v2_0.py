from dataclasses import dataclass, field
from typing import List, Optional
from siri.siri_utility.siri_permissions_v2_0 import (
    AbstractPermissionStructure,
    AbstractTopicPermissionStructure,
    CapabilityAccessControlStructure,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckConnectionLinkRef:
    """If access control is supported, whether access control by CONNECTION
    link is supported.

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
class CheckLineRef:
    """If access control is supported, whether access control by LINE is
    supported.

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
class CheckMonitoringRef:
    """If access control is supported, whether access control by monitoring
    point (LOGICAL DISPLAY) is supported.

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
class CheckOperatorRef:
    """If access control is supported, whether access control by OPERATOR is
    supported.

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
class FilterByConnectionLinkRef:
    """Whether results can be filtered by CONNECTION LINK.

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
class FilterByDestination:
    """Whether results can be filtered by DESTINATION.

    Default is 'false'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )


@dataclass
class FilterByDirectionRef:
    """
    Whether results can be filtered by DIRECTION Default is 'true'.
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
class FilterByFacilityRef:
    """Whether results can be filtered by Facility (EQUIPMENT).

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
class FilterByInterchangeRef:
    """Whether results can be filtered by SERVICE JOURNEY INTERCHANGE.

    Default is 'false'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )


@dataclass
class FilterByLineRef:
    """Whether results can be filtered by LINE.

    Default is 'true'
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
class FilterByMonitoringRef:
    """Whether results can be filtered by Monitoring point (LOGICAL DISPLAY).

    Fixed as 'true'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        init=False,
        default=True,
        metadata={
            "required": True,
        },
    )


@dataclass
class FilterByOperatorRef:
    """Whether results can be filtered by OPERATOR.

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
class FilterByStopPointRef:
    """Whether results can be filtered by SCHEDULED STOP POINT.

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
class FilterByValidityPeriod:
    """Whether results can be filtered by VALIDITY PERIOD.

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
class FilterByVehicleJourneyRef:
    """Whether results can be filtered by VEHICLE JOURNEY.

    Default is 'false'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )


@dataclass
class FilterByVehicleRef:
    """Whether results can be filtered by VEHICLE.

    Default is 'false'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )


@dataclass
class PermissionsStructure:
    """
    Type for abstract permissions.

    :ivar permission_version_ref: Version of permission set.
    """

    permission_version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PermissionVersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ConnectionCapabilityAccessControlStructure(CapabilityAccessControlStructure):
    """
    Abstract type for capability access control.

    :ivar check_operator_ref:
    :ivar check_line_ref:
    :ivar check_connection_link_ref: If access control is supported,
        whether access control by CONNECTION LINK is supported. Default
        is 'true'.
    """

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
    check_connection_link_ref: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CheckConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ConnectionLinkPermissionStructure(AbstractTopicPermissionStructure):
    """
    Type for CONNECTION link Permission.

    :ivar connection_link_ref: Reference to a CONNECTION link for which
        permission is made.
    """

    connection_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class LinePermissionStructure(AbstractTopicPermissionStructure):
    """
    Type for Line Permission.

    :ivar line_ref: Reference to a LINE. whose data participant is
        allowed to access.
    :ivar direction_ref: Reference to a DIRECTION of LINE. that
        participant is allowed to access.
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
    direction_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class MonitoringCapabilityAccessControlStructure(CapabilityAccessControlStructure):
    """
    Type for Monitoring Service Capability access control.
    """

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
    check_monitoring_ref: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CheckMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class OperatorPermissionStructure(AbstractTopicPermissionStructure):
    """
    Type for OPERATOR Permission.

    :ivar operator_ref: Reference to an OPERATOR whose data participant
        is allowed to access.
    """

    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class StopMonitorPermissionStructure(AbstractTopicPermissionStructure):
    """
    Type for Monitoring Point  (LOGICAL DISPLAY) Permission.

    :ivar monitoring_ref: Reference to a Stop Monitoring point (LOGICAL
        DISPLAY) to which permission applies.
    """

    monitoring_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class ConnectionLinkPermissions:
    """
    The CONNECTION links that the participant may access.

    :ivar allow_all:
    :ivar connection_link_permission: Participant's permission for this
        CONNECTION link.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    allow_all: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowAll",
            "type": "Element",
        },
    )
    connection_link_permission: List[ConnectionLinkPermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkPermission",
            "type": "Element",
        },
    )


@dataclass
class LinePermissions:
    """
    The LINEs that the participant may access.

    :ivar allow_all:
    :ivar line_permission: Participant's permission for this LINE.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    allow_all: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowAll",
            "type": "Element",
        },
    )
    line_permission: List[LinePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "LinePermission",
            "type": "Element",
        },
    )


@dataclass
class OperatorPermissions:
    """
    The OPERATOR data that the participant may access.

    :ivar allow_all:
    :ivar operator_permission: Participant's permission for this
        OPERATOR.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    allow_all: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowAll",
            "type": "Element",
        },
    )
    operator_permission: List[OperatorPermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorPermission",
            "type": "Element",
        },
    )


@dataclass
class ConnectionServicePermissionStructure(AbstractPermissionStructure):
    """
    Type for Monitoring Service Permission.
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
    connection_link_permissions: Optional[ConnectionLinkPermissions] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkPermissions",
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
class ProductionTimetablePermission(ConnectionServicePermissionStructure):
    """
    Permission for a single participant or all participants to use an aspect of
    the service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
