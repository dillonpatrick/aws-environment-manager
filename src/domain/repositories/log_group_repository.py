from abc import ABC, abstractmethod


class ILogGroupRepository(ABC):

    @abstractmethod
    def describe_log_groups(self) -> dict:
        pass

    @abstractmethod
    def tag_log_group(self, resource_arn: str, tags: dict) -> None:
        pass

    @abstractmethod
    def list_tags_for_log_group(self, resource_arn: str) -> dict:
        pass
