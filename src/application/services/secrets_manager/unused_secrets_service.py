from datetime import datetime, timezone

from src.application.services.secrets_manager.base_service import BaseService
from src.domain.services.secrets_manager.get_unused_secret_service import (
    GetUnusedSecretService,
)
from src.utils.params_logger import logger


class UnusedSecretsServices(BaseService):
    def delete_unused_secrets(self):
        logger.info("Starting process...")

        secret_list = self.secret_listing_service.list_all_secrets()
        today = datetime.now(timezone.utc)
        unused_secrets = GetUnusedSecretService.get_unused_secrets(
            secret_list, today
        )

        if not unused_secrets:
            logger.info("No secrets unused.")

        try:
            for secret_name, days_unused in unused_secrets:
                self.repository.delete_secret(secret_id=secret_name)
                logger.info(
                    f"The secret {secret_name} has been deleted because it wasn't accessed for {days_unused} days."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
