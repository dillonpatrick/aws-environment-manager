from src.application.services.dynamodb.base_service import BaseService
from src.domain.services.dynamodb.get_tables_without_replication_service import (
    GetTablesWithoutReplicationService,
)
from src.utils.params_logger import logger


class ListTablesInfoService(BaseService):
    def list_tables_without_replication(self):
        logger.info("Starting Process...")

        tables_list = self.table_listing_service.list_all_tables()
        tables_without_replication = (
            GetTablesWithoutReplicationService.get_tables_without_replication(
                tables_list
            )
        )

        if not tables_without_replication:
            logger.info("All tables have replication enabled")
        try:
            logger.info(
                f"Tables without replication: {tables_without_replication}"
            )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
