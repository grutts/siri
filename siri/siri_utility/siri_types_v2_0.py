from dataclasses import dataclass, field
from typing import Optional
from siri.xml.xml import LangValue

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class NaturalLanguagePlaceNameStructure:
    """@lang. ISO language code (default is 'en')
    A string containing a phrase in a natural language name that requires at least one character of text and forbids certain reserved characters."""

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "pattern": r"[^,\[\]\{\}\?$%\^=@#;:]+",
        },
    )
    lang: Optional[LangValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class NaturalLanguageStringStructure:
    """
    Tyoe for a string in a specified language.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    lang: Optional[LangValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
