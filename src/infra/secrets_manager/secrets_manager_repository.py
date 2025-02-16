import boto3

from src.domain.repositories.secrets_manager_repository import (
    ISecretsManagerRepository,
)


class SecretsManagerRepository(ISecretsManagerRepository):
    def __init__(self):
        self.client = boto3.client("secretsmanager")

    def list_secrets(self, sort_order="asc"):
        paginator = self.client.get_paginator("list_secrets")
        secrets = []

        for response in paginator.paginate(
            SortOrder=sort_order, MaxResults=100
        ):
            secrets.extend(response.get("SecretList", []))
        return secrets

    def describe_secret(self, secret_id):
        return self.client.describe_secret(SecretId=secret_id)

    def describe_secrets(self):
        secrets = self.list_secrets()
        detailed_secrets = []

        for secret in secrets:
            secret_id = secret.get("Name", "")
            secret_described = self.describe_secret(secret_id)
            detailed_secrets.append(secret_described)

        return detailed_secrets

    def delete_secret(self, secret_id, force_delete_without_recovery=True):
        return self.client.delete_secret(
            SecretId=secret_id,
            ForceDeleteWithoutRecovery=force_delete_without_recovery,
        )

    def tag_secret(self, secret_id, tags):
        return self.client.tag_resource(SecretId=secret_id, Tags=tags)

    def replicate_secret(
        self,
        secret_id,
        add_replica_regions,
        force_overwrite_replica_secret=False,
    ):
        return self.client.replicate_secret_to_regions(
            SecretId=secret_id,
            AddReplicaRegions=add_replica_regions,
            ForceOverwriteReplicaSecret=force_overwrite_replica_secret,
        )
