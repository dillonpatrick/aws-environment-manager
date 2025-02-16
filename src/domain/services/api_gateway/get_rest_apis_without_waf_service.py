from os import getenv

from src.domain.models.api_gateway_v1_metadata import ApiGatewayV1Metadata
from src.infra.api_gateway.api_gateway_repository import ApiGatewayRepository


class GetRestApisWithoutWafService:
    @staticmethod
    def get_rest_apis_without_waf(
        apis_list: list[ApiGatewayV1Metadata],
    ) -> list[str]:
        rest_apis_without_waf = []

        for api in apis_list:
            if not GetRestApisWithoutWafService.has_replication(api.id):
                rest_apis_without_waf.append([api.name, api.id])

        return rest_apis_without_waf

    @staticmethod
    def has_replication(api_id) -> bool:
        api_arn = f"arn:aws:apigateway:{getenv('REGION')}::/restapis/{api_id}/stages/{getenv('PYTHON_ENV')}"
        response = ApiGatewayRepository().get_web_acls_for_api_v1(api_arn)
        return "WebACL" in response
