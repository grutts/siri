from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CommunicationsTransportMethodEnumeration(Enum):
    """
    Enumeration of communications transport method usage.
    """

    HTTP_POST = "httpPost"
    OTHER = "other"
    WSDL_SOAP = "wsdlSoap"
    WSDL_SOAP_DOCUMENT_LITERAL = "wsdlSoapDocumentLiteral"
    HTTP_URL_JSON = "httpUrlJSON"
    HTTP_URL_PROTO_BUFFERS = "httpUrlProtoBuffers"


class CompressionMethodEnumeration(Enum):
    """
    Enumeration of compression usage.
    """

    GZIP = "gzip"
    NONE = "none"
    OTHER = "other"


@dataclass
class IncludeTranslations:
    """Whether additional translations of text names are to be included in
    elements.

    If false, then only one element should be returned.  Defaukt is
    false. Where multiple values are returned The first element returned
    ill be used as the defaukt value
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class RequestTimestamp:
    """
    Timestamp on request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class RequestorRef:
    """Reference to a requestor - Participant Code."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class ResponseTimestamp:
    """
    Time individual response element was created.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
