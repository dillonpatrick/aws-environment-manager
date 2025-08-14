from src.domain.models.api_gateway_v2_metadata import ApiGatewayV2Metadata
from src.infra.api_gateway.api_gateway_repository import ApiGatewayRepository


class ApiGatewayV2DataService:
    def __init__(self, repository: ApiGatewayRepository):
        self.repository = repository

    def list_all_apis_v2(self):
        apis = self.repository.get_apis_v2()
        return [
            ApiGatewayV2Metadata(
                ApiEndpoint=api.get("ApiEndpoint"),
                ApiGatewayManaged=api.get("ApiGatewayManaged"),
                ApiId=api.get("ApiId"),
                ApiKeySelectionExpression=api.get("ApiKeySelectionExpression"),
                CorsConfiguration=api.get("CorsConfiguration"),
                CreatedDate=api.get("CreatedDate"),
                Description=api.get("Description"),
                DisableSchemaValidation=api.get("DisableSchemaValidation"),
                DisableExecuteApiEndpoint=api.get("DisableExecuteApiEndpoint"),
                ImportInfo=api.get("ImportInfo"),
                Name=api.get("Name"),
                ProtocolType=api.get("ProtocolType"),
                RouteSelectionExpression=api.get("RouteSelectionExpression"),
                Tags=api.get("Tags"),
                Version=api.get("Version"),
                Warnings=api.get("Warnings"),
            )
            for api in apis
        ]


if __name__ == "__main__":
    service = ApiGatewayV2DataService(ApiGatewayRepository())
    print(service.list_all_apis_v2())
