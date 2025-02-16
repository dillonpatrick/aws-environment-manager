from src.application.services.dynamodb.base_service import BaseService
from src.domain.services.dynamodb.get_tables_without_deletion_protection_enabled_service import (
    GetTablesWithoutDeletionProtectionEnabledService,
)
from src.utils.params_logger import logger


class DeletionProtectionService(BaseService):
    def enable_protection(self):
        logger.info("Starting Process...")

        tables_list = self.table_listing_service.list_all_tables()
        tables_without_deletion_protection = GetTablesWithoutDeletionProtectionEnabledService.get_tables_without_deletion_protection_enabled(
            tables_list
        )

        if not tables_without_deletion_protection:
            logger.info("All tables have deletion protection enabled")

        try:
            for table_name in tables_without_deletion_protection:
                self.repository.enable_deletion_protection(table_name)
                logger.info(
                    f"Enabled deletion protection for table {table_name}"
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
