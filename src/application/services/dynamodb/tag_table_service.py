from src.application.services.dynamodb.base_service import BaseService
from src.domain.services.dynamodb.get_tables_without_name_tag_service import (
    GetTablesWithoutNameTagService,
)
from src.utils.params_logger import logger


class TagTableService(BaseService):
    def add_name_tag(self):
        logger.info("Starting Process...")

        tables_tags_list = self.repository.list_tags_of_all_tables()
        tables_without_tag = (
            GetTablesWithoutNameTagService.get_tables_without_name_tag(
                tables_tags_list
            )
        )

        if not tables_without_tag:
            logger.info("All tables have the 'Name' tag.")

        try:
            for table_name, _ in tables_without_tag:
                self.repository.tag_table(
                    table_name, [{"Key": "Name", "Value": table_name}]
                )
                logger.info(
                    f"The 'Name' tag has been added to the table '{table_name}'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
