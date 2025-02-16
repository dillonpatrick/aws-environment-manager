from src.domain.models.secrets_manager_metadata import SecretMetadata


class GetSecretWithoutReplicationService:
    @staticmethod
    def get_secrets_without_replication(
        secrets: list[SecretMetadata],
    ) -> list[dict]:
        secrets_without_replication = []

        for secret in secrets:
            if (
                GetSecretWithoutReplicationService.has_replication(secret)
                == False
            ):
                secrets_without_replication.append((secret["Name"]))
        return secrets_without_replication

    @staticmethod
    def has_replication(secret: SecretMetadata) -> bool:
        has_replication = False
        if "PrimaryRegion" in secret:
            has_replication = True
        return has_replication
