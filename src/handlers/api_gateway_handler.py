from src.application.services.api_gateway import (
    TagApiServiceV1,
    TagApiServiceV2,
    WafForApiService,
)


def enable_waf_for_api_v1(event, context):
    return WafForApiService().enable_waf_for_api_v1()


def api_v1_add_name_tag(event, context):
    return TagApiServiceV1().api_v1_add_name_tag()


def api_v2_add_name_tag(event, context):
    return TagApiServiceV2().api_v2_add_name_tag()
