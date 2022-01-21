from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from siri.ifopt.ifopt_modification_v0_3 import (
    ModificationEnumeration,
    StatusEnumeration,
)
from siri.ifopt.ifopt_types_v0_2 import InfoLinksStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AdministrativeAreaVersionedRefStructure:
    """
    Type for a versioned reference to anADMINISTRATIVE ZONE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
        },
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AdministratorVersionedRefStructure:
    """
    Type for a versioned reference to an ORGANISATION with administrative
    responsibility.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
        },
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VersionedObjectStructure:
    """
    Abstract Type for a versioned object.
    """

    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
            "required": True,
        },
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AdministrativeAreaRefsStructure:
    """
    Type for a collection of one or more references to ADMINISTRATIVE ZONEs.

    :ivar administrative_area_ref: Reference to the identifier of an
        ADMINISTRATIVE ZONE.
    """

    administrative_area_ref: List[AdministrativeAreaVersionedRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "AdministrativeAreaRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )


@dataclass
class DataManagedObjectStructure(VersionedObjectStructure):
    """
    Abstract Type for DATA MANAGED OBJECT, that is an object that may be
    assigned a RESPONSIBILITY SET dictating a responsbile ORGANISATION and/or
    ADMINISTRATIVE ZONE.

    :ivar managed_by_area_ref: ADMINISTRATIVE ZONEthat manages object.
        If absent then manager same as for containing parent of object.
    :ivar info_links: Collection of URL's associated with object.
    """

    managed_by_area_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ManagedByAreaRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "pattern": r"[0-9]{3}",
        },
    )
    info_links: Optional[InfoLinksStructure] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
