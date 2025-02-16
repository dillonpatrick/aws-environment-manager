from datetime import datetime, timezone

from src.domain.models.secrets_manager_metadata import SecretMetadata
from src.utils.params_logger import logger


class GetUnusedSecretService:
    @staticmethod
    def get_unused_secrets(
        secrets: list[SecretMetadata], today: datetime
    ) -> list[tuple[str, int]]:
        unused_secrets = []

        for secret in secrets:
            if GetUnusedSecretService.is_secret_from_client(secret):
                days_unused = GetUnusedSecretService.calculate_days_unused(
                    secret, today
                )
                if GetUnusedSecretService.is_secret_unused(
                    days_unused, secret
                ):
                    unused_secrets.append((secret.Name, days_unused))
        if len(unused_secrets) == 0:
            logger.info("No secrets to delete today.")
        return unused_secrets

    @staticmethod
    def is_secret_unused(days_unused: int, secret: SecretMetadata) -> bool:
        if secret.LastAccessedDate != None and days_unused >= 30:
            logger.info(
                f"The secret '{secret.Name}' hasn't been used for {days_unused} days."
            )
            return True
        elif secret.LastAccessedDate == None and days_unused >= 7:
            logger.info(
                f"The secret '{secret.Name}' was created {days_unused} days ago, but has never been used."
            )
            return True

        return False

    @staticmethod
    def is_secret_from_client(secret: SecretMetadata) -> bool:

        return secret.Name.startswith("test_") and secret.Name.endswith(
            "/tokens"
        )

    @staticmethod
    def calculate_days_unused(secret: SecretMetadata, today: datetime) -> int:
        if secret.LastAccessedDate != None:
            return (
                today - secret.LastAccessedDate.replace(tzinfo=timezone.utc)
            ).days
        return (today - secret.CreatedDate.replace(tzinfo=timezone.utc)).days
