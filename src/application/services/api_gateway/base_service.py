from typing import Optional

from src.application.services.data_services.api_gateway_v1_data_service import (
    ApiGatewayV1DataService,
)
from src.application.services.data_services.api_gateway_v2_data_service import (
    ApiGatewayV2DataService,
)
from src.infra.api_gateway.api_gateway_repository import ApiGatewayRepository


class BaseServiceV1:
    def __init__(self, repository: Optional[ApiGatewayV1DataService] = None):
        self.repository = (
            repository if repository is not None else ApiGatewayRepository()
        )
        self.api_v1_listing_service = ApiGatewayV1DataService(self.repository)


class BaseServiceV2:
    def __init__(self, repository: Optional[ApiGatewayV2DataService] = None):
        self.repository = (
            repository if repository is not None else ApiGatewayRepository()
        )
        self.api_v2_listing_service = ApiGatewayV2DataService(self.repository)
