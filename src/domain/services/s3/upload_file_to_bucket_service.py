from src.infra.s3.s3_bucket_repository import S3BucketRepository


class UploadFileToBucketService:
    @staticmethod
    def upload_file(
        repository: S3BucketRepository,
        bucket: str,
        filename: str,
        key: str,
    ):
        return repository.upload_file(
            bucket=bucket, filename=filename, key=key
        )
