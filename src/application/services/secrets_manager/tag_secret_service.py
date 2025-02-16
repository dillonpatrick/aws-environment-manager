from src.application.services.secrets_manager.base_service import BaseService
from src.domain.services.secrets_manager.get_secret_without_tag_service import (
    GetSecretWithoutTagService,
)
from src.utils.params_logger import logger


class TagSecretService(BaseService):
    def add_name_tag(self):
        logger.info("Starting process...")

        secret_list = self.secret_listing_service.list_all_secrets()
        secrets_without_tag = (
            GetSecretWithoutTagService.get_secrets_without_name_tag(
                secret_list
            )
        )

        if not secrets_without_tag:
            logger.info("No secrets without 'Name' tag.")

        try:
            for secret_name, _ in secrets_without_tag:
                tag_name = {"Key": "Name", "Value": secret_name}
                self.repository.tag_secret(
                    secret_id=secret_name, tags=[tag_name]
                )
                logger.info(
                    f"The 'Name' tag has been added to the secret '{secret_name}'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
