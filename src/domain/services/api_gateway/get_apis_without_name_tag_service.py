from src.infra.api_gateway.api_gateway_repository import ApiGatewayRepository


class GetApisWithoutNameTagService:
    @staticmethod
    def get_api_v1_without_name_tag() -> list[str]:
        apis_without_name_tag = []

        tags = ApiGatewayRepository().get_all_tags_v1()

        for api_name, tags, api_arn in tags:
            if not GetApisWithoutNameTagService.has_tag_name(tags):
                apis_without_name_tag.append([api_name, api_arn])

        return apis_without_name_tag

    @staticmethod
    def get_api_v2_without_name_tag() -> list[str]:
        apis_without_name_tag = []

        tags = ApiGatewayRepository().get_all_tags_v2()

        for api_name, tags, api_arn in tags:
            if not GetApisWithoutNameTagService.has_tag_name(tags):
                apis_without_name_tag.append([api_name, api_arn])

        return apis_without_name_tag

    @staticmethod
    def has_tag_name(tags) -> bool:
        if "Name" in tags:
            return True
        return False
