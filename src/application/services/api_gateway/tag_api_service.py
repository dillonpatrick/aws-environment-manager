from src.application.services.api_gateway.base_service import (
    BaseServiceV1,
    BaseServiceV2,
)
from src.domain.services.api_gateway.get_apis_without_name_tag_service import (
    GetApisWithoutNameTagService,
)
from src.utils.params_logger import logger


class TagApiServiceV1(BaseServiceV1):
    def api_v1_add_name_tag(self):
        logger.info("Starting Process...")

        apis_without_name_tag = (
            GetApisWithoutNameTagService.get_api_v1_without_name_tag()
        )

        if not apis_without_name_tag:
            logger.info("All APIs have the 'Name' tag.")

        try:
            for api_name, api_arn in apis_without_name_tag:
                self.repository.tag_api_v1(
                    resource_arn=api_arn, tags={"Name": api_name}
                )
                logger.info(
                    f"The 'Name' tag has been added to the API '{api_name}'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")


class TagApiServiceV2(BaseServiceV2):
    def api_v2_add_name_tag(self):
        logger.info("Starting Process...")

        apis_without_name_tag = (
            GetApisWithoutNameTagService.get_api_v2_without_name_tag()
        )
        if not apis_without_name_tag:
            logger.info("All APIs have the 'Name' tag.")
        try:
            for api_name, api_arn in apis_without_name_tag:
                self.repository.tag_api_v2(
                    resource_arn=api_arn, tags={"Name": api_name}
                )
                logger.info(
                    f"The 'Name' tag has been added to the API '{api_name}'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
