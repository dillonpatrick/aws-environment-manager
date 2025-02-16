from os import getenv

import boto3

from src.domain.repositories.api_gateway_repository import (
    IApiGatewayRepository,
)


class ApiGatewayRepository(IApiGatewayRepository):
    _api_gateway_v1 = boto3.client("apigateway")
    _api_gateway_v2 = boto3.client("apigatewayv2")
    _wafv2 = boto3.client("wafv2", region_name=getenv("REGION"))

    def __init__(self):
        self.api_gateway_v1 = self._api_gateway_v1
        self.api_gateway_v2 = self._api_gateway_v2
        self.wafv2 = self._wafv2

    # Api Gateway V1
    def get_apis_v1(self):
        paginator = self.api_gateway_v1.get_paginator("get_rest_apis")
        apis_v1 = []
        for response in paginator.paginate():
            apis_v1.extend(response.get("items", []))
        return apis_v1

    def get_api_tags_v1(self, resource_arn):
        return self.api_gateway_v1.get_tags(resourceArn=resource_arn)

    def get_all_tags_v1(self):
        apis_v1 = self.get_apis_v1()
        tags_list = []
        for api in apis_v1:
            api_arn = f"arn:aws:apigateway:{getenv('REGION')}::/restapis/{api.get('id')}/stages/{getenv('PYTHON_ENV')}"
            get_tags = self.get_api_tags_v1(api_arn)
            tags_list.append([api.get("name"), get_tags.get("tags"), api_arn])
        return tags_list

    def tag_api_v1(self, resource_arn, tags):
        return self.api_gateway_v1.tag_resource(
            resourceArn=resource_arn, tags=tags
        )

    # Api Gateway V2
    def get_apis_v2(self):
        paginator = self.api_gateway_v2.get_paginator("get_apis")
        apis_v2 = []
        for response in paginator.paginate():
            apis_v2.extend(response.get("Items", []))
        return apis_v2

    def get_api_tags_v2(self, resource_arn):
        return self.api_gateway_v2.get_tags(ResourceArn=resource_arn)

    def get_all_tags_v2(self):
        apis_v2 = self.get_apis_v2()
        tags_list = []
        for api in apis_v2:
            api_arn = f"arn:aws:apigateway:{getenv('REGION')}::/apis/{api.get('ApiId')}"
            api_tags = self.get_api_tags_v2(api_arn)
            tags_list.append([api.get("Name"), api_tags.get("Tags"), api_arn])
        return tags_list

    def tag_api_v2(self, resource_arn, tags):
        return self.api_gateway_v2.tag_resource(
            ResourceArn=resource_arn, Tags=tags
        )

    # WAF V2
    def get_web_acls_for_api_v1(self, resource_arn):
        return self.wafv2.get_web_acl_for_resource(ResourceArn=resource_arn)

    def enbable_waf_v2(self, web_acl_arn, resource_arn):
        return self.wafv2.associate_web_acl(
            WebACLArn=web_acl_arn, ResourceArn=resource_arn
        )
