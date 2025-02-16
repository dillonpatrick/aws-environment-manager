from abc import ABC, abstractmethod


class IApiGatewayRepository(ABC):
    # Api Gateway V1
    @abstractmethod
    def get_apis_v1(self) -> dict:
        pass

    @abstractmethod
    def get_api_tags_v1(self, resource_arn: str) -> dict:
        pass

    @abstractmethod
    def get_all_tags_v1(self):
        pass

    @abstractmethod
    def tag_api_v1(self, resource_arn: str, tags=dict) -> None:
        pass

    # Api Gateway V2
    @abstractmethod
    def get_apis_v2(self) -> dict:
        pass

    @abstractmethod
    def get_api_tags_v2(self, resource_arn: str) -> dict:
        pass

    @abstractmethod
    def get_all_tags_v2(self) -> dict:
        pass

    @abstractmethod
    def tag_api_v2(self, resource_arn: str, tags=dict) -> dict:
        pass

    # WAF V2
    @abstractmethod
    def get_web_acls_for_api_v1(self, resource_arn) -> dict:
        pass

    @abstractmethod
    def enbable_waf_v2(self, web_acl_arn: str, resource_arn: str) -> dict:
        pass
