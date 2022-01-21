from dataclasses import dataclass, field
from typing import List, Optional
from siri.siri_utility.siri_types_v2_0 import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProductCategoryStructure:
    """
    Type for TYPE OF PRODUCT CATEGORY description.

    :ivar product_category_code: Identifier of TYPE OF PRODUCT CATEGORY
        classification. SIRI provides a recommended set of values
        covering most usages, intended to be TPEG compatible. See the
        SIRI facilities packaged.
    :ivar name: Name of classification  (Unbounded since SIRI 2.0)
    :ivar icon: Icon used to represent TYPE OF PRODUCT CATEGORY.
    """

    product_category_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class ServiceFeatureStructure:
    """
    Type for Service Feature description.

    :ivar service_feature_code: Identifier of classification. SIRI
        provides a recommended set of values covering most usages,
        intended to be TPEG compatible. See the SIRI facilities
        packaged.
    :ivar name: Name of classification.  (Unbounded since SIRI 2.0)
    :ivar icon: Icon associated with feature.
    """

    service_feature_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceFeatureCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
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
class VehicleFeaturesStructure:
    """
    Type for description of feature of VEHICLE.

    :ivar vehicle_feature_code: Identifier of feature of VEHICLE. SIRI
        provides a recommended set of values covering most usages,
        intended to be TPEG compatible. See the SIRI facilities
        packaged.
    :ivar name: Name of feature of VEHICLE.  (Unbounded since SIRI 2.0)
    :ivar icon: Icon used to represent feature of VEHICLE.
    """

    vehicle_feature_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleFeatureCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
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
class ProductCategory(ProductCategoryStructure):
    """
    Category for classification of a journey as a Product.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeature(ServiceFeatureStructure):
    """
    Service Feature description.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class VehicleFeature(VehicleFeaturesStructure):
    """
    Vehicle Feature description.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
