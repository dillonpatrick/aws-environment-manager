from abc import ABC, abstractmethod


class IS3BucketRepository:
    @abstractmethod
    def list_buckets(self) -> list[str]:
        pass

    @abstractmethod
    def get_bucket_tagging(self, bucket_name: str) -> dict:
        pass

    @abstractmethod
    def put_bucket_tagging(self, bucket_name: str, tags: list[dict]) -> None:
        pass

    @abstractmethod
    def upload_file(self, file_path: str, bucket_name: str) -> None:
        pass
