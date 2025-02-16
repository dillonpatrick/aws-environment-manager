from src.application.services.log_group.base_service import BaseService
from src.domain.services.log_group.get_log_group_without_tag_service import (
    GetLogGroupWithoutTagService,
)
from src.utils.params_logger import logger


class TagLogGroupService(BaseService):
    def add_name_tag(self):
        logger.info("Starting process...")

        log_group_tag_list = self.repository.list_tags_for_all_log_groups()
        log_group_without_tag = (
            GetLogGroupWithoutTagService.get_log_group_without_name_tag(
                log_group_tag_list
            )
        )

        if not log_group_without_tag:
            logger.info("No log groups without 'Name' tag.")

        try:
            for log_group_name, log_group_arn, _ in log_group_without_tag:
                tag_name = {"Name": log_group_name}
                self.repository.tag_log_group(
                    resource_arn=log_group_arn,
                    tags=tag_name,
                )
                logger.info(
                    f"The 'Name' tag has been added to the log group '{log_group_name}'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
