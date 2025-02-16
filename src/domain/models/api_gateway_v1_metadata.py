from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class EndpointConfiguration:
    types: list[str]
    vpcEndpointIds: Optional[list[str]] = None


@dataclass
class ApiGatewayV1Metadata:
    id: str
    name: str
    description: str
    createdDate: datetime
    version: str
    warnings: Optional[list[str]] = None
    binaryMediaTypes: Optional[list[str]] = None
    minimumCompressionSize: Optional[int] = None
    apiKeySource: Optional[str] = None
    endpointConfiguration: Optional[EndpointConfiguration] = None
    policy: Optional[str] = None
    tags: Optional[dict[str, str]] = None
    disableExecuteApiEndpoint: Optional[bool] = None
    rootResourceId: Optional[str] = None
