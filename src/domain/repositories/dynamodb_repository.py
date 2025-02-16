from abc import ABC, abstractmethod


class IDynamoDBRepository(ABC):

    @abstractmethod
    def list_tables(self) -> list[str]:
        pass

    @abstractmethod
    def describe_table(self, table_name: str) -> dict:
        pass

    @abstractmethod
    def tag_table(self, table_name: str, tags: list[dict]) -> None:
        pass

    @abstractmethod
    def enable_deletion_protection(self, table_name: str) -> None:
        pass

    @abstractmethod
    def scan_table(
        self, table_name: str, attributes_to_get: list[str]
    ) -> list[dict]:
        pass
