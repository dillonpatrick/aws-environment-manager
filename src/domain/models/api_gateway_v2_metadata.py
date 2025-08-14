from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ApiGatewayV2Metadata:
    ApiEndpoint: str
    ApiGatewayManaged: Optional[bool] = False
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[dict] = None
    CreatedDate: Optional[datetime] = None
    Description: Optional[str] = None
    DisableSchemaValidation: Optional[bool] = False
    DisableExecuteApiEndpoint: Optional[bool] = False
    ImportInfo: Optional[list[str]] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    Tags: Optional[dict[str, str]] = None
    Version: Optional[str] = None
    Warnings: Optional[list[str]] = None
