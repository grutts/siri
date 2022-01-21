from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from siri.acsb.acsb_accessibility_v0_3 import AccessibilityAssessmentStructure
from siri.acsb.acsb_limitations_v0_2 import AccessibilityEnumeration
from siri.acsb.acsb_passenger_mobility_v0_3 import SuitabilityStructure
from siri.ifopt.ifopt_equipment_v0_3 import EquipmentStatusEnumeration
from siri.siri_model.siri_facilities_v1_2 import (
    AccessFacilityEnumeration,
    AllFacilitiesFeatureStructure,
)
from siri.siri_model.siri_situation_identity_v1_1 import SituationRef
from siri.siri_model.siri_time_v1_2 import (
    DaysOfWeekEnumerationx,
    HalfOpenTimeRangeStructure,
    HalfOpenTimestampRangeStructure,
    HolidayTypeEnumerationx,
)
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure
from siri.siri_utility.siri_utility_v1_1 import Extensions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class FacilityCategoryEnumeration(Enum):
    """
    Generic catégory of a facility.
    """

    UNKNOWN = "unknown"
    FIXED_EQUIPMENT = "fixedEquipment"
    SERVICE_PROVIDED_BY_INDIVIDUAL = "serviceProvidedByIndividual"
    SERVICE_FOR_PERSONAL_DEVICE = "serviceForPersonalDevice"
    RESERVED_AREA = "reservedArea"


@dataclass
class FacilityLocationStructure:
    """
    Location of the MONITORED FACILITY.

    :ivar line_ref:
    :ivar stop_point_ref:
    :ivar vehicle_ref:
    :ivar dated_vehicle_journey_ref:
    :ivar connection_link_ref:
    :ivar interchange_ref:
    :ivar stop_place_ref: Reference to a Stop Place.
    :ivar stop_place_component_id: System identifier of Stop Place
        component. Unique at least within Stop Place and concrete
        component type.
    :ivar operator_ref: OPERATOR of a VEHICLE JOURNEY.   Note that the
        operator may change over the course of a journey.  This shoudl
        show teh operator for the curent point in the journey.  Use
        Journey Parts tp record all the operators in the whole journeyh.
    :ivar product_category_ref: Product Classification of VEHICLE
        JOURNEY- subdivides a transport mode. e.g. express, loacl.
    :ivar service_feature_ref: Classification of service into arbitrary
        Service categories, e.g. school bus. Recommended SIRI values
        based on TPEG are given in SIRI documentation and enumerated in
        the siri_facilities package. Corresponds to NeTEX TYPE OF
        SERVICe.
    :ivar vehicle_feature_ref: Features of VEHICLE providing journey.
        Recommended SIRI values based on TPEG are given in SIRI
        documentation and enumerated in the siri_facilities package.
    """

    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_component_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPlaceComponentId",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
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
    vehicle_feature_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class FacilityRef:
    """
    Reference to a Facility.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class FacilityStatusEnumeration(Enum):
    """
    Allowed values for the status of a MONITORED FACILITY.
    """

    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
    PARTIALLY_AVAILABLE = "partiallyAvailable"
    ADDED = "added"
    REMOVED = "removed"


class MonitoringTypeEnumeration(Enum):
    """Allowed values for the types of monitoring: automatic or manual - describing the hardware transducer (video, GPS/Radio, in-road sensors, etc.) doesn't seeme useful for SIRi."""

    UNKNOWN = "unknown"
    MANUAL = "manual"
    AUTOMATIC = "automatic"


class RemedyTypeEnumeration(Enum):
    """
    Allowed values for actions to remedy a faclity change.
    """

    UNKNOWN = "unknown"
    REPLACE = "replace"
    REPAIR = "repair"
    REMOVE = "remove"
    OTHER_ROUTE = "otherRoute"
    OTHER_LOCATION = "otherLocation"


@dataclass
class EquipmentAvailabilityStructure:
    """
    Type for Availaibility Change of EQUIPMENT.

    :ivar equipment_ref: Reference to an EQUIPMENT.
    :ivar description: Description of EQUIPMENT.  (Unbounded since SIRI
        2.0)
    :ivar equipment_type_ref: Reference to a TYPE OF EQUIPMENT.r.
    :ivar validity_period: Period for which change to EQUIPMENT status
        applies applies. If omitted, indefinite period.
    :ivar equipment_status: Availability status of the EQUIPMENT.
        Default is 'notAvailable'.
    :ivar equipment_features: Service Features associated with
        equipment.
    :ivar extensions:
    """

    equipment_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentTypeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[HalfOpenTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_status: EquipmentStatusEnumeration = field(
        default=EquipmentStatusEnumeration.NOT_AVAILABLE,
        metadata={
            "name": "EquipmentStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    equipment_features: Optional["EquipmentAvailabilityStructure.EquipmentFeatures"] = field(
        default=None,
        metadata={
            "name": "EquipmentFeatures",
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
    class EquipmentFeatures:
        """
        :ivar feature_ref: Service or Stop features associated with
            equipment. Recommended values based on TPEG are given in
            SIRI documentation and enumerated in the siri_facilities
            package.
        """

        feature_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class FacilityStatusStructure:
    """
    Descriprion of the status of a MONITORED FACILITY.

    :ivar status: Status of the facility.
    :ivar description: Description of the facility Status.  (Unbounded
        since SIRI 2.0)
    :ivar accessibility_assessment: Accessibility of the facility.
    :ivar extensions:
    """

    status: Optional[FacilityStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
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
class MobilityDisruptionStructure:
    """
    Type for effect of EQUIPMENT availability change on impaired access users.

    :ivar mobility_impaired_access: Whether stop or service is
        accessible to mobility impaired users. This may be further
        qualified by one ore more MobilityFacility instances to specify
        which types of mobility access are available (true) or not
        available (false). For example suitableForWheelChair, or
        'tepFreeAccess.
    :ivar access_facility: Classification of Mobility Facility type -
        Based on Tpeg pti23.
    """

    mobility_impaired_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    access_facility: List[AccessFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFacility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class MonitoringValidityConditionStructure:
    """
    Allowed values for the type for Description of the monitoring conditions
    (frequency of mesurement, etc): an automatic monitoring of the satus of a
    lift with pushed alert in case of incident is very different from a daily
    manual/visual check.

    :ivar period: Date and tme range within which condition is
        available.
    :ivar timeband: Monitoring period within a single day (monitoring
        may not be available at night, or may ony occur at certain time
        of day for manual monitoring, etc.). Several periods can be
        defined.
    :ivar day_type: Days type for monitoring availability.
    :ivar holiday_type: Holiday type for monitoring availability.
    """

    period: List[HalfOpenTimestampRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timeband: List[HalfOpenTimeRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    day_type: List[DaysOfWeekEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    holiday_type: List[HolidayTypeEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class RemedyStructure:
    """
    Description of the remedy to the change of a facility status (mainly when
    it becomes partially or totally anavailable)

    :ivar remedy_type: Type of the remedy (repair/replacement/remove)
    :ivar description: Description of the set up remedy in natural
        language.  (Unbounded since SIRI 2.0)
    :ivar extensions:
    """

    remedy_type: Optional[RemedyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RemedyType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
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
class FacilityChangeStructure:
    """Type for change to equipment availability.

    Basic structure defined in the first 1.0 SIRI XSd.

    :ivar equipment_availability: Availability change for Equipment
        item.
    :ivar situation_ref:
    :ivar mobility_disruption: Effect of change on impaired access
        users.
    """

    equipment_availability: Optional[EquipmentAvailabilityStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentAvailability",
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
    mobility_disruption: Optional[MobilityDisruptionStructure] = field(
        default=None,
        metadata={
            "name": "MobilityDisruption",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class FacilityStructure:
    """
    Type for sescription the MONITORED FACILITY itself.

    :ivar facility_code: Identfier of Facility.
    :ivar description: Textual description of the facility.  (Unbounded
        since SIRI 2.0)
    :ivar facility_class: Type of facility (several types may be
        associated to a single facility)
    :ivar features: Features of service.
    :ivar owner_ref: Refererence to identifier of owner of facility.
    :ivar owner_name: Textual description of the owner of the facility.
    :ivar validity_condition: When Facility is normally avaialble. If
        not specified, default is 'always'. Values are Logically ANDed
        together.
    :ivar facility_location: Describes where the facility is located.
        The location is a Transmodel object reference or an IFOPT object
        reference.
    :ivar limitations: Limitation of facility.
    :ivar suitabilities: Suitabilities of facility for specific
        passenger needs.
    :ivar accessibility_assessment: Accessibility of the facility.
    :ivar extensions:
    """

    facility_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_class: List[FacilityCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    features: Optional["FacilityStructure.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "OwnerName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_condition: Optional[MonitoringValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_location: Optional[FacilityLocationStructure] = field(
        default=None,
        metadata={
            "name": "FacilityLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    limitations: Optional["FacilityStructure.Limitations"] = field(
        default=None,
        metadata={
            "name": "Limitations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suitabilities: Optional["FacilityStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
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
    class Features:
        """
        :ivar feature: Description of the feauture of the facility.
            Several features may be associated to a single facility.
        """

        feature: List[AllFacilitiesFeatureStructure] = field(
            default_factory=list,
            metadata={
                "name": "Feature",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Limitations:
        """
        :ivar wheelchair_access:
        :ivar step_free_access:
        :ivar escalator_free_access:
        :ivar lift_free_access:
        :ivar audible_signals_available: Whether a PLACE / SITE ELEMENT
            has Audible signals for the viusally impaired.
        :ivar visual_signs_available: Whether a PLACE / SITE ELEMENT has
            Visual signals for the hearing impaired.
        """

        wheelchair_access: AccessibilityEnumeration = field(
            default=AccessibilityEnumeration.FALSE,
            metadata={
                "name": "WheelchairAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "required": True,
            },
        )
        step_free_access: Optional[AccessibilityEnumeration] = field(
            default=None,
            metadata={
                "name": "StepFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        escalator_free_access: Optional[AccessibilityEnumeration] = field(
            default=None,
            metadata={
                "name": "EscalatorFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        lift_free_access: Optional[AccessibilityEnumeration] = field(
            default=None,
            metadata={
                "name": "LiftFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        audible_signals_available: Optional[AccessibilityEnumeration] = field(
            default=None,
            metadata={
                "name": "AudibleSignalsAvailable",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        visual_signs_available: Optional[AccessibilityEnumeration] = field(
            default=None,
            metadata={
                "name": "VisualSignsAvailable",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )

    @dataclass
    class Suitabilities:
        """
        :ivar suitability: Type of specific need for wich the facility
            is appropriate.
        """

        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )


@dataclass
class MonitoringInformationStructure:
    """
    Allowed values for the monitoring conditions (frequency of mesurement,
    etc): an automatic monitoring of the satus of a lift with pushed alert in
    case of incident is very different from a daily manual/visual check.

    :ivar monitoring_interval: Mean time interval between two
        measurements.
    :ivar monitoring_type: How monitoring is automatic, manual, etc..
    :ivar monitoring_period: When the monitoring is in effect. If absent
        always.
    :ivar extensions:
    """

    monitoring_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MonitoringInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_type: Optional[MonitoringTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MonitoringType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_period: Optional[MonitoringValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringPeriod",
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
class AnnotatedFacilityStructure:
    """Summary information about  Facility.

    Used in DISCOVERY used

    :ivar facility_ref:
    :ivar monitored: Whether real-time data is available for the stop.
        Default is 'true'.
    :ivar facility: Description of the facility (without its status)
    """

    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    facility: Optional[FacilityStructure] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class FacilityChangeElement(FacilityChangeStructure):
    """A change to the availaibility of EQUIPMENT.

    Basic structure defined in the first 1.0 SIRI XSd.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class FacilityConditionStructure:
    """
    Description of any change concerning a MONITORED FACILITY New structure
    defined in SIRI XSD 1.1 for Faclities Management.

    :ivar facility: Facility affected by condition.
    :ivar facility_ref:
    :ivar facility_status: Status of Facility.
    :ivar situation_ref:
    :ivar remedy: Setup action to remedy the change of the facility
        status (if partialy or totaly anavailable)
    :ivar monitoring_info: Description of the mechanism used to monitor
        the change of the facility status.
    :ivar validity_period: Period (duration) of the status change for
        the facility.
    :ivar extensions:
    """

    facility: Optional[FacilityStructure] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_status: Optional[FacilityStatusStructure] = field(
        default=None,
        metadata={
            "name": "FacilityStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
    remedy: Optional[RemedyStructure] = field(
        default=None,
        metadata={
            "name": "Remedy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_info: Optional[MonitoringInformationStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringInfo",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[HalfOpenTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
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
class FacilityConditionElement(FacilityConditionStructure):
    """
    Description of any change concerning a MONITORED FACILITY New structure
    defined in SIRI XSD 1.1 for Facilities Management.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
