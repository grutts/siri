from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from siri.siri.siri_common_services_v2_0 import (
    CheckStatusRequest,
    CheckStatusResponse,
    ContextualisedRequestStructure,
    DataReadyAcknowledgement,
    DataReadyNotification,
    DataReceivedAcknowledgement,
    DataSupplyRequest,
    HeartbeatNotification,
    SubscriptionResponse,
    TerminateSubscriptionRequest,
    TerminateSubscriptionResponse,
)
from siri.siri.siri_request_error_conditions_v2_0 import (
    CapabilityNotSupportedError,
    OtherError,
)
from siri.siri.siri_requests_v2_0 import (
    AbstractSubscriptionRequestStructure,
    AuthenticatedRequestStructure,
    ProducerResponseStructure,
)
from siri.siri_connection_monitoring_service import (
    ConnectionMonitoringCapabilitiesRequest,
    ConnectionMonitoringCapabilitiesResponse,
    ConnectionMonitoringDistributorDelivery,
    ConnectionMonitoringFeederDelivery,
    ConnectionMonitoringRequest,
    ConnectionMonitoringSubscriptionRequest,
)
from siri.siri_connection_timetable_service import (
    ConnectionTimetableCapabilitiesRequest,
    ConnectionTimetableCapabilitiesResponse,
    ConnectionTimetableDelivery,
    ConnectionTimetableRequest,
    ConnectionTimetableSubscriptionRequest,
)
from siri.siri_discovery import (
    ConnectionLinksDelivery,
    ConnectionLinksRequest,
    FacilityDelivery,
    FacilityRequest,
    InfoChannelDelivery,
    InfoChannelRequest,
    LinesDelivery,
    LinesRequest,
    ProductCategoriesDelivery,
    ProductCategoriesRequest,
    ServiceFeaturesDelivery,
    ServiceFeaturesRequest,
    StopPointsDelivery,
    StopPointsRequest,
    VehicleFeaturesDelivery,
    VehicleFeaturesRequest,
)
from siri.siri_estimated_timetable_service import (
    EstimatedTimetableCapabilitiesRequest,
    EstimatedTimetableCapabilitiesResponse,
    EstimatedTimetableDelivery,
    EstimatedTimetableRequest,
    EstimatedTimetableSubscriptionRequest,
)
from siri.siri_facility_monitoring_service import (
    FacilityMonitoringCapabilitiesRequest,
    FacilityMonitoringCapabilitiesResponse,
    FacilityMonitoringDelivery,
    FacilityMonitoringRequest,
    FacilityMonitoringSubscriptionRequest,
)
from siri.siri_general_message_service import (
    GeneralMessageCapabilitiesRequest,
    GeneralMessageCapabilitiesResponse,
    GeneralMessageDelivery,
    GeneralMessageRequest,
    GeneralMessageSubscriptionRequest,
)
from siri.siri_production_timetable_service import (
    ProductionTimetableCapabilitiesRequest,
    ProductionTimetableCapabilitiesResponse,
    ProductionTimetableDelivery,
    ProductionTimetableRequest,
    ProductionTimetableSubscriptionRequest,
)
from siri.siri_situation_exchange_service import (
    SituationExchangeCapabilitiesRequest,
    SituationExchangeCapabilitiesResponse,
    SituationExchangeDelivery,
    SituationExchangeRequest,
    SituationExchangeSubscriptionRequest,
)
from siri.siri_stop_monitoring_service import (
    StopMonitoringCapabilitiesRequest,
    StopMonitoringCapabilitiesResponse,
    StopMonitoringDelivery,
    StopMonitoringMultipleRequest,
    StopMonitoringRequest,
    StopMonitoringSubscriptionRequest,
)
from siri.siri_stop_timetable_service import (
    StopTimetableCapabilitiesRequest,
    StopTimetableCapabilitiesResponse,
    StopTimetableDelivery,
    StopTimetableRequest,
    StopTimetableSubscriptionRequest,
)
from siri.siri_utility.siri_utility_v1_1 import Extensions
from siri.siri_vehicle_monitoring_service import (
    VehicleMonitoringCapabilitiesRequest,
    VehicleMonitoringCapabilitiesResponse,
    VehicleMonitoringDelivery,
    VehicleMonitoringRequest,
    VehicleMonitoringSubscriptionRequest,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesRequestStructure(AuthenticatedRequestStructure):
    """
    Type for Requests for capabilities of the current system.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar delegator_address: Address of original Consumer, ie requesting
        system to which delegating response is to be  returned. +SIRI
        2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    :ivar production_timetable_capabilities_request:
    :ivar estimated_timetable_capabilities_request:
    :ivar stop_timetable_capabilities_request:
    :ivar stop_monitoring_capabilities_request:
    :ivar vehicle_monitoring_capabilities_request:
    :ivar connection_timetable_capabilities_request:
    :ivar connection_monitoring_capabilities_request:
    :ivar general_message_capabilities_request:
    :ivar facility_monitoring_capabilities_request:
    :ivar situation_exchange_capabilities_request:
    :ivar version:
    """

    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    requestor_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    production_timetable_capabilities_request: Optional[ProductionTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_capabilities_request: Optional[EstimatedTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_capabilities_request: Optional[StopTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "StopTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_capabilities_request: Optional[StopMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "StopMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_capabilities_request: Optional[VehicleMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_capabilities_request: Optional[ConnectionTimetableCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_capabilities_request: Optional[ConnectionMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_capabilities_request: Optional[GeneralMessageCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "GeneralMessageCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_capabilities_request: Optional[FacilityMonitoringCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_capabilities_request: Optional[SituationExchangeCapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "SituationExchangeCapabilitiesRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CapabilitiesResponseStructure(ProducerResponseStructure):
    """
    Type for the capabilities of an implementation.
    """

    production_timetable_capabilities_response: Optional[ProductionTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_capabilities_response: Optional[EstimatedTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_capabilities_response: Optional[StopTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "StopTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_capabilities_response: Optional[StopMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "StopMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_capabilities_response: Optional[VehicleMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_capabilities_response: Optional[ConnectionTimetableCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "ConnectionTimetableCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_capabilities_response: Optional[ConnectionMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_capabilities_response: Optional[GeneralMessageCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "GeneralMessageCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_capabilities_response: Optional[FacilityMonitoringCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_capabilities_response: Optional[SituationExchangeCapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "SituationExchangeCapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ServiceDeliveryBodyStructure:
    """
    Type for SIRI Service Delivery Body..

    :ivar status: Whether the complerte request could be processed
        successfully or not. Default is 'true'. If any of the individual
        requests within the delivery failed, should be set to ' false'.
    :ivar error_condition: Description of any error or warning
        conditions that appluy to the overall request. More Specific
        error conditions should be included on each request that fails.
    :ivar more_data: Whether there is a further delvery message with
        more current updates that follows this one. Default is 'false'.
    :ivar production_timetable_delivery:
    :ivar estimated_timetable_delivery:
    :ivar stop_timetable_delivery:
    :ivar stop_monitoring_delivery: Delivery for Stop Event service.
    :ivar vehicle_monitoring_delivery: Delivery for Vehicle Activity
        Service.
    :ivar connection_timetable_delivery:
    :ivar connection_monitoring_feeder_delivery: Delivery for Connection
        Protection Fetcher Service.
    :ivar connection_monitoring_distributor_delivery: Delivery for
        Connection Protection Fetcher Service.
    :ivar general_message_delivery: Delivery for general Message
        service.
    :ivar facility_monitoring_delivery:
    :ivar situation_exchange_delivery:
    :ivar srs_name: Default gml coordinate format for eny location
        elements in response; applies if Coordinates element is used to
        specify points. May be overridden on individual points.
    """

    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["ServiceDeliveryBodyStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    more_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    production_timetable_delivery: List[ProductionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_delivery: List[EstimatedTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_delivery: List[StopTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_delivery: List[StopMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_delivery: List[VehicleMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_delivery: List[ConnectionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_feeder_delivery: List[ConnectionMonitoringFeederDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringFeederDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_distributor_delivery: List[ConnectionMonitoringDistributorDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringDistributorDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_delivery: List[GeneralMessageDelivery] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_delivery: List[FacilityMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_delivery: List[SituationExchangeDelivery] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar capability_not_supported_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
            default=None,
            metadata={
                "name": "CapabilityNotSupportedError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class ServiceDeliveryStructure(ProducerResponseStructure):
    """
    Type for SIRI Service Delivery.

    :ivar status: Whether the complerte request could be processed
        successfully or not. Default is 'true'. If any of the individual
        requests within the delivery failed, should be set to ' false'.
    :ivar error_condition: Description of any error or warning
        conditions that appluy to the overall request. More Specific
        error conditions should be included on each request that fails.
    :ivar more_data: Whether there is a further delvery message with
        more current updates that follows this one. Default is 'false'.
    :ivar production_timetable_delivery:
    :ivar estimated_timetable_delivery:
    :ivar stop_timetable_delivery:
    :ivar stop_monitoring_delivery: Delivery for Stop Event service.
    :ivar vehicle_monitoring_delivery: Delivery for Vehicle Activity
        Service.
    :ivar connection_timetable_delivery:
    :ivar connection_monitoring_feeder_delivery: Delivery for Connection
        Protection Fetcher Service.
    :ivar connection_monitoring_distributor_delivery: Delivery for
        Connection Protection Fetcher Service.
    :ivar general_message_delivery: Delivery for general Message
        service.
    :ivar facility_monitoring_delivery:
    :ivar situation_exchange_delivery:
    :ivar srs_name: Default gml coordinate format for eny location
        elements in response; applies if Coordinates element is used to
        specify points. May be overridden on individual points.
    """

    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional["ServiceDeliveryStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    more_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    production_timetable_delivery: List[ProductionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_delivery: List[EstimatedTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_delivery: List[StopTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_delivery: List[StopMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_delivery: List[VehicleMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_delivery: List[ConnectionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_feeder_delivery: List[ConnectionMonitoringFeederDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringFeederDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_distributor_delivery: List[ConnectionMonitoringDistributorDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringDistributorDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_delivery: List[GeneralMessageDelivery] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_delivery: List[FacilityMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_delivery: List[SituationExchangeDelivery] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar capability_not_supported_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        capability_not_supported_error: Optional[CapabilityNotSupportedError] = field(
            default=None,
            metadata={
                "name": "CapabilityNotSupportedError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )


@dataclass
class ServiceRequestStructure(ContextualisedRequestStructure):
    """
    SIRI Service Request.
    """

    production_timetable_request: List[ProductionTimetableRequest] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_request: List[EstimatedTimetableRequest] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_request: List[StopTimetableRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_multiple_request: List[StopMonitoringMultipleRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringMultipleRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_request: List[StopMonitoringRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_request: List[VehicleMonitoringRequest] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_request: List[ConnectionTimetableRequest] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionTimetableRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_request: List[ConnectionMonitoringRequest] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_request: List[GeneralMessageRequest] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_request: List[FacilityMonitoringRequest] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_request: List[SituationExchangeRequest] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SiriServiceDeliveryStructure:
    """
    Type for a SIRI SIRI Functional Service Delivery types.Used for WSDL.

    :ivar production_timetable_delivery:
    :ivar estimated_timetable_delivery:
    :ivar stop_timetable_delivery:
    :ivar stop_monitoring_delivery: Delivery for Stop Event service.
    :ivar vehicle_monitoring_delivery: Delivery for Vehicle Activity
        Service.
    :ivar connection_timetable_delivery:
    :ivar connection_monitoring_feeder_delivery: Delivery for Connection
        Protection Fetcher Service.
    :ivar connection_monitoring_distributor_delivery: Delivery for
        Connection Protection Fetcher Service.
    :ivar general_message_delivery: Delivery for general Message
        service.
    :ivar facility_monitoring_delivery:
    :ivar situation_exchange_delivery:
    """

    production_timetable_delivery: List[ProductionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_delivery: List[EstimatedTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_delivery: List[StopTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_delivery: List[StopMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_delivery: List[VehicleMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_delivery: List[ConnectionTimetableDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionTimetableDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_feeder_delivery: List[ConnectionMonitoringFeederDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringFeederDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_distributor_delivery: List[ConnectionMonitoringDistributorDelivery] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringDistributorDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_delivery: List[GeneralMessageDelivery] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_delivery: List[FacilityMonitoringDelivery] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_delivery: List[SituationExchangeDelivery] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SiriSubscriptionRequestStructure:
    """Type for SIRI Functional Service Subscription types.

    Used for WSDL exchanges.
    """

    production_timetable_subscription_request: List[ProductionTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_subscription_request: List[EstimatedTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_subscription_request: List[StopTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_subscription_request: List[StopMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_subscription_request: List[VehicleMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_subscription_request: List[ConnectionTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_subscription_request: List[ConnectionMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_subscription_request: List[GeneralMessageSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_subscription_request: List[FacilityMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_subscription_request: List[SituationExchangeSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class SubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    """
    Type for SIRI Subscription Request.
    """

    production_timetable_subscription_request: List[ProductionTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_subscription_request: List[EstimatedTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "EstimatedTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_subscription_request: List[StopTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_subscription_request: List[StopMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "StopMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_subscription_request: List[VehicleMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_timetable_subscription_request: List[ConnectionTimetableSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionTimetableSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_subscription_request: List[ConnectionMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_message_subscription_request: List[GeneralMessageSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "GeneralMessageSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_subscription_request: List[FacilityMonitoringSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMonitoringSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_exchange_subscription_request: List[SituationExchangeSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangeSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )


@dataclass
class CapabilitiesRequest(CapabilitiesRequestStructure):
    """Requests a the current capabilities of the server.

    Answred with a CpabailitiesResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesResponse(CapabilitiesResponseStructure):
    """
    Responses with the capabilities of an implementation.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDelivery(ServiceDeliveryStructure):
    """Response from Producer to Consumer to deliver payload data.

    Either answers a direct ServiceRequest, or asynchronously satisfies
    a subscription. May be sent directly in one step, or fetched in
    response to a DataSupply Request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequest(ServiceRequestStructure):
    """Request from Consumer to Producer for immediate delivery of data.

    Answered with a ServiceDelivery (or a DataReadyRequest)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionRequest(SubscriptionRequestStructure):
    """Request from Subscriber to Producer for a subscription.

    Answered with a SubscriptionResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"


@dataclass
class Siri:
    """
    SIRI Service Interface for Real-time  Operation.

    :ivar service_request:
    :ivar subscription_request:
    :ivar terminate_subscription_request:
    :ivar data_ready_notification:
    :ivar data_supply_request:
    :ivar check_status_request:
    :ivar heartbeat_notification:
    :ivar capabilities_request:
    :ivar stop_points_request:
    :ivar lines_request:
    :ivar service_features_request:
    :ivar product_categories_request:
    :ivar vehicle_features_request:
    :ivar info_channel_request:
    :ivar facility_request:
    :ivar connection_links_request:
    :ivar subscription_response:
    :ivar terminate_subscription_response:
    :ivar data_ready_acknowledgement:
    :ivar service_delivery:
    :ivar data_received_acknowledgement:
    :ivar check_status_response:
    :ivar capabilities_response: Responses with the capabilities of an
        implementation. Answers a CapabilityRequest.
    :ivar stop_points_delivery:
    :ivar lines_delivery:
    :ivar product_categories_delivery:
    :ivar service_features_delivery:
    :ivar vehicle_features_delivery:
    :ivar info_channel_delivery:
    :ivar facility_delivery:
    :ivar connection_links_delivery:
    :ivar extensions:
    :ivar version:
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    service_request: Optional[ServiceRequest] = field(
        default=None,
        metadata={
            "name": "ServiceRequest",
            "type": "Element",
        },
    )
    subscription_request: Optional[SubscriptionRequest] = field(
        default=None,
        metadata={
            "name": "SubscriptionRequest",
            "type": "Element",
        },
    )
    terminate_subscription_request: Optional[TerminateSubscriptionRequest] = field(
        default=None,
        metadata={
            "name": "TerminateSubscriptionRequest",
            "type": "Element",
        },
    )
    data_ready_notification: Optional[DataReadyNotification] = field(
        default=None,
        metadata={
            "name": "DataReadyNotification",
            "type": "Element",
        },
    )
    data_supply_request: Optional[DataSupplyRequest] = field(
        default=None,
        metadata={
            "name": "DataSupplyRequest",
            "type": "Element",
        },
    )
    check_status_request: Optional[CheckStatusRequest] = field(
        default=None,
        metadata={
            "name": "CheckStatusRequest",
            "type": "Element",
        },
    )
    heartbeat_notification: Optional[HeartbeatNotification] = field(
        default=None,
        metadata={
            "name": "HeartbeatNotification",
            "type": "Element",
        },
    )
    capabilities_request: Optional[CapabilitiesRequest] = field(
        default=None,
        metadata={
            "name": "CapabilitiesRequest",
            "type": "Element",
        },
    )
    stop_points_request: Optional[StopPointsRequest] = field(
        default=None,
        metadata={
            "name": "StopPointsRequest",
            "type": "Element",
        },
    )
    lines_request: Optional[LinesRequest] = field(
        default=None,
        metadata={
            "name": "LinesRequest",
            "type": "Element",
        },
    )
    service_features_request: Optional[ServiceFeaturesRequest] = field(
        default=None,
        metadata={
            "name": "ServiceFeaturesRequest",
            "type": "Element",
        },
    )
    product_categories_request: Optional[ProductCategoriesRequest] = field(
        default=None,
        metadata={
            "name": "ProductCategoriesRequest",
            "type": "Element",
        },
    )
    vehicle_features_request: Optional[VehicleFeaturesRequest] = field(
        default=None,
        metadata={
            "name": "VehicleFeaturesRequest",
            "type": "Element",
        },
    )
    info_channel_request: Optional[InfoChannelRequest] = field(
        default=None,
        metadata={
            "name": "InfoChannelRequest",
            "type": "Element",
        },
    )
    facility_request: Optional[FacilityRequest] = field(
        default=None,
        metadata={
            "name": "FacilityRequest",
            "type": "Element",
        },
    )
    connection_links_request: Optional[ConnectionLinksRequest] = field(
        default=None,
        metadata={
            "name": "ConnectionLinksRequest",
            "type": "Element",
        },
    )
    subscription_response: Optional[SubscriptionResponse] = field(
        default=None,
        metadata={
            "name": "SubscriptionResponse",
            "type": "Element",
        },
    )
    terminate_subscription_response: Optional[TerminateSubscriptionResponse] = field(
        default=None,
        metadata={
            "name": "TerminateSubscriptionResponse",
            "type": "Element",
        },
    )
    data_ready_acknowledgement: Optional[DataReadyAcknowledgement] = field(
        default=None,
        metadata={
            "name": "DataReadyAcknowledgement",
            "type": "Element",
        },
    )
    service_delivery: Optional[ServiceDelivery] = field(
        default=None,
        metadata={
            "name": "ServiceDelivery",
            "type": "Element",
        },
    )
    data_received_acknowledgement: Optional[DataReceivedAcknowledgement] = field(
        default=None,
        metadata={
            "name": "DataReceivedAcknowledgement",
            "type": "Element",
        },
    )
    check_status_response: Optional[CheckStatusResponse] = field(
        default=None,
        metadata={
            "name": "CheckStatusResponse",
            "type": "Element",
        },
    )
    capabilities_response: Optional[CapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "CapabilitiesResponse",
            "type": "Element",
        },
    )
    stop_points_delivery: Optional[StopPointsDelivery] = field(
        default=None,
        metadata={
            "name": "StopPointsDelivery",
            "type": "Element",
        },
    )
    lines_delivery: Optional[LinesDelivery] = field(
        default=None,
        metadata={
            "name": "LinesDelivery",
            "type": "Element",
        },
    )
    product_categories_delivery: Optional[ProductCategoriesDelivery] = field(
        default=None,
        metadata={
            "name": "ProductCategoriesDelivery",
            "type": "Element",
        },
    )
    service_features_delivery: Optional[ServiceFeaturesDelivery] = field(
        default=None,
        metadata={
            "name": "ServiceFeaturesDelivery",
            "type": "Element",
        },
    )
    vehicle_features_delivery: Optional[VehicleFeaturesDelivery] = field(
        default=None,
        metadata={
            "name": "VehicleFeaturesDelivery",
            "type": "Element",
        },
    )
    info_channel_delivery: Optional[InfoChannelDelivery] = field(
        default=None,
        metadata={
            "name": "InfoChannelDelivery",
            "type": "Element",
        },
    )
    facility_delivery: Optional[FacilityDelivery] = field(
        default=None,
        metadata={
            "name": "FacilityDelivery",
            "type": "Element",
        },
    )
    connection_links_delivery: Optional[ConnectionLinksDelivery] = field(
        default=None,
        metadata={
            "name": "ConnectionLinksDelivery",
            "type": "Element",
        },
    )
    extensions: Optional[Extensions] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
        },
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        },
    )


def parse(file) -> Siri:
    """Parse an XML string, or a filename referring to an XML file, into a SIRI object"""
    context = XmlContext()
    parser = XmlParser(context=context)
    try:
        return parser.parse(file, Siri)
    except FileNotFoundError:
        return parser.from_string(file, Siri)


def serialize(obj: Siri) -> str:
    """Take a Siri (or other object from this library) and serialise it to XML"""
    context = XmlContext()
    serializer = XmlSerializer(context=context)
    return serializer.render(obj)
