from dataclasses import dataclass, field
from typing import Optional
from siri.ifopt.ifopt_countries_v0_2 import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationNumber:
    """Identifier of SITUATION within a Participant.

    Excldue versionr.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SituationSimpleRef:
    """
    Reference to a SITUATION associated with the element.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class SituationFullRefStructure:
    """
    Type for reference to a SITUATION.

    :ivar version_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar participant_ref: Unique identifier of a Participant. Provides
        namespace for SITUATION.
    :ivar situation_number: Unique identifier of SITUATION within a
        Participant. Excludes any version number.
    :ivar update_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar update_participant_ref: Unique identifier of a Participant.
        Provides namespace for SITUATION. If absent provdied from
        context.
    :ivar version: Unique identifier of update version within a
        SITUATION Number Omit if reference to the base SITUATION.
    """

    version_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "VersionCountryRef",
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
            "required": True,
        },
    )
    situation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    update_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "UpdateCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    update_participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpdateParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SituationSharedRefStructure:
    """Type for reference to a SITUATION or an update to a SITUATION.

    Participant ref is optional and may be supplied from context.

    :ivar country_ref: Unique identifier of a Country of a Participant
        who created SITUATION. Provides namespace for Participant If
        absent proided from context.
    :ivar participant_ref: Unique identifier of a Participant. Provides
        namespace for SITUATION. If absent provdied from context.
    :ivar situation_number: Unique identifier of SITUATION within a
        Participant. Excludes any version number.
    :ivar update_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar update_participant_ref: Unique identifier of a Participant.
        Provides namespace for SITUATION. If absent provdied from
        context.
    :ivar version: Unique identifier of update version within a
        SITUATION Number Omit if reference to the base SITUATION.
    """

    country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "CountryRef",
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
    situation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    update_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "UpdateCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    update_participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpdateParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SituationFullRef(SituationFullRefStructure):
    """Reference to a SITUATION.

    Elements are retained as atomic elements.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SituationRefStructure:
    """
    Type for reference to a SITUATION.

    :ivar situation_simple_ref:
    :ivar situation_full_ref: Reference to a SITUATION. Elements of
        SITUATION identfier are expressed as atomic elements.
    """

    situation_simple_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationSimpleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_full_ref: Optional[SituationFullRef] = field(
        default=None,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SituationRef(SituationRefStructure):
    """
    Reference to a SITUATION associated with the element.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
