from os import getenv

from src.application.services.api_gateway.base_service import BaseServiceV1
from src.domain.services.api_gateway.get_rest_apis_without_waf_service import (
    GetRestApisWithoutWafService,
)
from src.utils.params_logger import logger


class WafForApiService(BaseServiceV1):
    def enable_waf_for_api_v1(self):
        logger.info("Starting process...")

        apis_list = self.api_v1_listing_service.list_all_apis_v1()
        apis_without_waf = (
            GetRestApisWithoutWafService.get_rest_apis_without_waf(apis_list)
        )

        if not apis_without_waf:
            logger.info("There are no APIs without WAF")

        try:
            for api_name, api_id in apis_without_waf:
                api_arn = f"arn:aws:apigateway:{getenv('REGION')}::/restapis/{api_id}/stages/{getenv('PYTHON_ENV')}"
                self.repository.enbable_waf_v2(getenv("WEB_ACL_ARN"), api_arn)
                logger.info(f"WAF has been enabled for API {api_name}")
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing process...")
