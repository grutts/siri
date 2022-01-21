from dataclasses import dataclass, field
from typing import List, Optional
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AnnotatedConnectionLinkStructure:
    """
    View of a SCHEDULED CONNECTION LINK description.

    :ivar connection_link_ref: Identifer of the connection link.
        DetailLevel=minimum
    :ivar feeder_stop_point_ref: Identifer of the feeder's stop.
        DetailLevel=normal
    :ivar distributor_stop_point_ref: Identifer of the distributor's
        stop. DetailLevel=normal
    :ivar monitored: Whether real-time data is available for the
        connection link. Default is 'true'. DetailLevel=minimum
    :ivar connection_link_name: Name of SCHEDULED CONNECTION LINK.
        DetailLevel=minimum
    :ivar feeder_stop_point_name: Name of the feeder's stop.
        DetailLevel=full
    :ivar distributor_stop_point_name: Name of the distributor's stop.
        DetailLevel=full
    :ivar url: Web page associated with connection link.
        DetailLevel=full
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
    feeder_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeederStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DistributorStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "FeederStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DistributorStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class AnnotatedConnectionLinkRef(AnnotatedConnectionLinkStructure):
    """
    SCHEDULED CONNECTION LINK definition.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
