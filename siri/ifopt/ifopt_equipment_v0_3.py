from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from siri.ifopt.ifopt_administration_v0_3 import DataManagedObjectStructure
from siri.ifopt.ifopt_time_v0_2 import ValidityConditionsStructure
from siri.ifopt.ifopt_types_v0_2 import Extensions
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class EquipmentStatusEnumeration(Enum):
    """
    Availabilityload status of a EQUIPMENT.
    """

    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"


@dataclass
class AbstractEquipmentStructure(DataManagedObjectStructure):
    """
    Type for abstract EQUIPMENT.

    :ivar equipment_id: Identifer of EQUIPMENT.
    :ivar equipment_name: Name of EQUIPMENT.
    :ivar type_of_equipment: Type for reference to TYPE OF EQUIPMENT.
    """

    equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        },
    )
    equipment_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentName",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    type_of_equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )


@dataclass
class InstalledEquipmentStructure(AbstractEquipmentStructure):
    """
    Type for INSTALLED EQUIPMENT.
    """


@dataclass
class LocalServiceStructure(InstalledEquipmentStructure):
    """
    Type for LOCAL SERVICE.

    :ivar validity_conditions: Conditison governing availability of
        serevice.
    :ivar feature_refs: Classification of features.
    :ivar extensions:
    """

    validity_conditions: Optional[ValidityConditionsStructure] = field(
        default=None,
        metadata={
            "name": "ValidityConditions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    feature_refs: Optional["LocalServiceStructure.FeatureRefs"] = field(
        default=None,
        metadata={
            "name": "FeatureRefs",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class FeatureRefs:
        """
        :ivar feature_ref: Features of LOCAL SERVICe.
        """

        feature_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
            },
        )


@dataclass
class PlaceEquipmentStructure(InstalledEquipmentStructure):
    """
    Type for SITE EQUIPMENT.
    """

    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )


@dataclass
class LocalService(LocalServiceStructure):
    """
    LOCAL SERVICe.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"


@dataclass
class OtherPlaceEquipment(PlaceEquipmentStructure):
    """EQUIPMENT.

    that may be in a fixed within a SITe.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
