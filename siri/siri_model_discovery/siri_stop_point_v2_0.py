from dataclasses import dataclass, field
from typing import List, Optional
from siri.siri_model.siri_reference_v2_0 import LineDirectionStructure
from siri.siri_model_discovery.siri_feature_v2_0 import ServiceFeatureStructure
from siri.siri_utility.siri_location_v2_0 import LocationStructure
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AnnotatedStopPointStructure:
    """
    View of a SCHEDULED STOP POINT description.

    :ivar stop_point_ref: Identifer of the stop.
    :ivar timing_point:
    :ivar monitored: Whether real-time data is available for the stop.
        Default is 'true'. Detail level is 'normal'.
    :ivar stop_name: Name of SCHEDULED STOP POINT. Detail level is
        'normal'.  (Unbounded since SIRI 2.0)
    :ivar stop_area_ref: Identifer of the sSTOP AREA to which SCHEDULED
        STOP POINT belongs. +SIRI.v2.0
    :ivar features: Service features of stop. Detail level is 'full'
    :ivar lines: LINEs that use stop. Detail level is 'full'
    :ivar location: Coordinates to use to show stop as a poitn on map.
        Detail level is 'normal'.+SIRI.v2.0
    :ivar url: Web page associated with Stop. Detail level is
        'full'+SIRI.v2.0
    """

    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    timing_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TimingPoint",
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
    stop_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_area_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    features: Optional["AnnotatedStopPointStructure.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["AnnotatedStopPointStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
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
    class Features:
        """
        :ivar service_feature: Description of Service features of stop.
        :ivar service_feature_ref:
        """

        service_feature: List[ServiceFeatureStructure] = field(
            default_factory=list,
            metadata={
                "name": "ServiceFeature",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        service_feature_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ServiceFeatureRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class Lines:
        """
        :ivar line_ref: Reference to a LINE that calls at stop.
        :ivar line_direction: Reference to a LINE  that calls at stop.
            and its direction  +SIRI V2.0
        """

        line_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "LineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        line_direction: List[LineDirectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "LineDirection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class AnnotatedStopPointRef(AnnotatedStopPointStructure):
    """
    SCHEDULED STOP POINT definition.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
