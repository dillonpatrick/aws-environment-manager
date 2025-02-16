from abc import ABC, abstractmethod


class IIAMReposoty(ABC):
    @abstractmethod
    def list_roles(self) -> dict:
        pass

    @abstractmethod
    def list_role_tags(self, role_name: str) -> dict:
        pass

    @abstractmethod
    def list_tags_for_all_roles(self) -> list[dict]:
        pass

    @abstractmethod
    def tag_role(self, role_name: str, tags: list) -> None:
        pass
