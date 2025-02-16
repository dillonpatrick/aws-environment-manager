from src.domain.models.secrets_manager_metadata import SecretMetadata


class GetSecretWithoutTagService:
    @staticmethod
    def get_secrets_without_name_tag(
        secrets: list[SecretMetadata],
    ) -> list[dict]:
        secrets_without_tags = []

        for secret in secrets:
            if GetSecretWithoutTagService.has_tag_name(secret) == False:
                secrets_without_tags.append((secret.Name, secret.Tags))
        return secrets_without_tags

    @staticmethod
    def has_tag_name(secret):
        if secret.Tags is None:
            return False
        for tag in secret.Tags:
            if tag.get("Key") == "Name":
                return True
        return False
