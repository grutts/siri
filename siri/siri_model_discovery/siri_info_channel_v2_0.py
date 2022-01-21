from dataclasses import dataclass, field
from typing import Optional
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InfoChannelStructure:
    """
    Type for Info Channels description.

    :ivar info_channel_code: Identifier of classification.
    :ivar name: Name of Info Channel.
    :ivar icon: Icon associated with Info Channel.
    """

    info_channel_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoChannelCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )


@dataclass
class InfoChannel(InfoChannelStructure):
    """
    Info Channel supported by Producer service.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
