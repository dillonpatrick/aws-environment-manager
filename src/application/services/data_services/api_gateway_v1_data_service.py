from src.domain.models.api_gateway_v1_metadata import (
    ApiGatewayV1Metadata,
    EndpointConfiguration,
)
from src.infra.api_gateway.api_gateway_repository import ApiGatewayRepository


class ApiGatewayV1DataService:
    def __init__(self, repository: ApiGatewayRepository):
        self.repository = repository

    def list_all_apis_v1(self):
        apis = self.repository.get_apis_v1()
        return [
            ApiGatewayV1Metadata(
                id=api.get("id"),
                name=api.get("name"),
                description=api.get("description"),
                createdDate=api.get("createdDate"),
                version=api.get("version"),
                warnings=api.get("warnings"),
                binaryMediaTypes=api.get("binaryMediaTypes"),
                minimumCompressionSize=api.get("minimumCompressionSize"),
                apiKeySource=api.get("apiKeySource"),
                endpointConfiguration=(
                    EndpointConfiguration(
                        types=api.get("endpointConfiguration", {}).get(
                            "types"
                        ),
                        vpcEndpointIds=api.get(
                            "endpointConfiguration", {}
                        ).get("vpcEndpointIds"),
                    )
                    if api.get("endpointConfiguration")
                    else None
                ),
                policy=api.get("policy"),
                tags=api.get("tags"),
                disableExecuteApiEndpoint=api.get("disableExecuteApiEndpoint"),
                rootResourceId=api.get("rootResourceId"),
            )
            for api in apis
        ]
