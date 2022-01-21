from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ActionStatusEnumeration(Enum):
    """
    Values for Progress Status.
    """

    OPEN = "open"
    PUBLISHED = "published"
    CLOSED = "closed"


@dataclass
class ActionDataStructure:
    """
    Type for list of SITUATIONs.

    :ivar name: Name of action data Element.
    :ivar type: Data type of action data.
    :ivar value: Value for action.
    :ivar prompt: Display prompt for presenting action to user.
        (Unbounded since SIRI 2.0)
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    value: List[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    prompt: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Prompt",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SimpleActionStructure:
    """
    Type for list of SITUATIONs.

    :ivar action_status: Processing Status of action at time of
        SITUATION publication.
    """

    action_status: Optional[ActionStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ParameterisedActionStructure(SimpleActionStructure):
    """
    Type for parameterised, i.e. user definable, actions.

    :ivar description: Description of action.
    :ivar action_data: Data associated with action.
    """

    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    action_data: List[ActionDataStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActionData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ManualActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION ManuallyWeb.
    """


@dataclass
class PublishToDisplayActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION To Web.

    :ivar on_place: Include in SITUATION lists on station displays.
    :ivar on_board: Include onboard displays.
    """

    on_place: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnPlace",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    on_board: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnBoard",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PublishToMobileActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION To Displays.

    :ivar incidents: Include in SITUATION lists on mobile site. Default
        is 'true'.
    :ivar home_page: Include in home page on mobile site. Default is
        'false'.
    """

    incidents: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incidents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    home_page: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomePage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PublishToTvActionStructure(ParameterisedActionStructure):
    """
    Type for Notify SITUATION to Tv.

    :ivar ceefax: Publish to Teltext. Default is 'true'.
    :ivar teletext: Publish to Ceefax. Default is 'true'.
    """

    ceefax: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ceefax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    teletext: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Teletext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PublishToWebActionStructure(ParameterisedActionStructure):
    """
    Type for Action Publish SITUATION To Web.

    :ivar incidents: Include in SITUATION lists on web site. Default is
        'true'.
    :ivar home_page: Include on home page on web site. Default is
        'false'.
    :ivar ticker: Include in moving ticker band. Default is 'false'.
    """

    incidents: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Incidents",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    home_page: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HomePage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ticker: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ticker",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PushedActionStructure(ParameterisedActionStructure):
    """
    Type for publication action.

    :ivar before_notices: Whether reminders should be sent.
    :ivar clear_notice: Whether a clearing notice should be displayed.
    """

    before_notices: Optional["PushedActionStructure.BeforeNotices"] = field(
        default=None,
        metadata={
            "name": "BeforeNotices",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    clear_notice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClearNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class BeforeNotices:
        """
        :ivar interval: Intervals before validity start date to send
            reminders.
        """

        interval: List[XmlDuration] = field(
            default_factory=list,
            metadata={
                "name": "Interval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class ManualAction(ManualActionStructure):
    """Action: Publish SITUATION Manually. i.e. a procedure must be carried out."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByEmailActionStructure(PushedActionStructure):
    """
    Type for Notify user by Email.

    :ivar email: Email address to which notice should be sent.
    """

    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class NotifyByPagerActionStructure(PushedActionStructure):
    """
    Type for Notify user by Pager.

    :ivar pager_group_ref: Reference to a pager group to be notfied.
    :ivar pager: Pager number of pager to be notfied.
    """

    pager_group_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PagerGroupRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    pager: Optional[str] = field(
        default=None,
        metadata={
            "name": "Pager",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class NotifyBySmsActionStructure(PushedActionStructure):
    """
    Type for Notify user by SMS.

    :ivar phone: MSISDN of user to which to send messages.
    :ivar premium: Whether content is flagged as subject to premium
        charge.
    """

    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    premium: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Premium",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class NotifyUserActionStructure(PushedActionStructure):
    """
    Type for Notify user by other means.

    :ivar workgroup_ref: Workgroup of user to be notified.
    :ivar user_name: Name of user to be notified.
    :ivar user_ref: Reference to a user to be notified.
    """

    workgroup_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkgroupRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    user_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PublishToAlertsActionStructure(PushedActionStructure):
    """
    Type for Action Publish SITUATION To Alert Service.

    :ivar by_email: Send as email alert.
    :ivar by_mobile: Send as mobile alert by SMS or WAP push.
    """

    by_email: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ByEmail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    by_mobile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ByMobile",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class PublishToDisplayAction(PublishToDisplayActionStructure):
    """Action: Publish SITUATION To Displays."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class PublishToMobileAction(PublishToMobileActionStructure):
    """Action: Publish SITUATION To WAP and PDA."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class PublishToTvAction(PublishToTvActionStructure):
    """Action: Publish SITUATION To TvService."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class PublishToWebAction(PublishToWebActionStructure):
    """Action: Publish SITUATION To Web."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByEmailAction(NotifyByEmailActionStructure):
    """Action: Publish SITUATION to a named workgroup or individual by email."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class NotifyByPagerAction(NotifyByPagerActionStructure):
    """Action: Publish SITUATION To pager."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class NotifyBySmsAction(NotifyBySmsActionStructure):
    """Action: Publish SITUATION to an individual by SMS."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class NotifyUserAction(NotifyUserActionStructure):
    """Action: Publish SITUATION To User."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class PublishToAlertsAction(PublishToAlertsActionStructure):
    """Action: Publish SITUATION To Alert Service."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ActionsStructure:
    """
    Type for list of actions.

    :ivar publish_to_web_action:
    :ivar publish_to_mobile_action:
    :ivar publish_to_tv_action:
    :ivar publish_to_alerts_action:
    :ivar manual_action:
    :ivar notify_by_email_action:
    :ivar notify_by_sms_action:
    :ivar notify_by_pager_action:
    :ivar notify_user_action:
    :ivar extensions: Extension point.
    """

    publish_to_web_action: List[PublishToWebAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToWebAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_mobile_action: List[PublishToMobileAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToMobileAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_tv_action: Optional[PublishToTvAction] = field(
        default=None,
        metadata={
            "name": "PublishToTvAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_alerts_action: List[PublishToAlertsAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToAlertsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    manual_action: List[ManualAction] = field(
        default_factory=list,
        metadata={
            "name": "ManualAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_email_action: List[NotifyByEmailAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByEmailAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_sms_action: Optional[NotifyBySmsAction] = field(
        default=None,
        metadata={
            "name": "NotifyBySmsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_pager_action: List[NotifyByPagerAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByPagerAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_user_action: List[NotifyUserAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyUserAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
