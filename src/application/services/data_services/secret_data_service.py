from src.domain.models.secrets_manager_metadata import SecretMetadata
from src.infra.secrets_manager.secrets_manager_repository import (
    SecretsManagerRepository,
)


class SecretDataService:
    def __init__(self, repository: SecretsManagerRepository):
        self.repository = repository

    def list_all_secrets(self) -> list[SecretMetadata]:
        secrets = self.repository.list_secrets()
        return [
            SecretMetadata(
                ARN=secret.get("ARN"),
                Name=secret.get("Name"),
                Tags=secret.get("Tags"),
                CreatedDate=secret.get("CreatedDate"),
                LastAccessedDate=secret.get("LastAccessedDate"),
                PrimaryRegion=secret.get("PrimaryRegion"),
            )
            for secret in secrets
        ]
