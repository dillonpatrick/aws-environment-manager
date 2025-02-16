from abc import ABC, abstractmethod


class ISecretsManagerRepository(ABC):

    @abstractmethod
    def list_secrets(self, sort_order: str) -> list[dict]:
        pass

    @abstractmethod
    def describe_secret(self, secret_id: str) -> dict:
        pass

    @abstractmethod
    def delete_secret(
        self, secret_id: str, force_delete_without_recovery: bool
    ) -> dict:
        pass

    @abstractmethod
    def tag_secret(self, secret_id: str, tags: list[dict]) -> None:
        pass

    @abstractmethod
    def replicate_secret(
        self,
        secret_id: str,
        add_replica_regions: list[dict],
        force_overwrite_replica_secret: bool,
    ) -> dict:
        pass
