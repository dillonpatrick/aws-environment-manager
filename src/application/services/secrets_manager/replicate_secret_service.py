from src.domain.services.secrets_manager.get_secret_without_replication_service import (
    GetSecretWithoutReplicationService,
)
from src.infra.secrets_manager.secrets_manager_repository import (
    SecretsManagerRepository,
)
from src.utils.params_logger import logger


class ReplicateSecretService:
    def replicate_secrets(self):
        logger.info("Starting process...")

        repository = SecretsManagerRepository()
        detailed_secrets_list = repository.describe_secrets()
        add_replica_regions = [{"Region": "us-west-2"}]
        secrets_without_replication = (
            GetSecretWithoutReplicationService.get_secrets_without_replication(
                detailed_secrets_list
            )
        )

        if not secrets_without_replication:
            logger.info("No secrets without replication.")

        try:
            for secret_name in secrets_without_replication:
                # remove this comment to enable the replication
                # repository.replicate_secret(
                #     secret_id=secret_name,
                #     add_replica_regions=add_replica_regions,
                #     force_overwrite_replica_secret=False,
                # )
                logger.info(
                    f"The secret '{secret_name}' has been replicated to the region 'us-west-2'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing Process...")
