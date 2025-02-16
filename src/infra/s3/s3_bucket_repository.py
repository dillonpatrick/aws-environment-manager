import boto3

from src.domain.repositories.s3_bucket_repository import IS3BucketRepository


class S3BucketRepository(IS3BucketRepository):
    def __init__(self):
        self.client = boto3.client("s3")

    def list_buckets(self):
        paginator = self.client.get_paginator("list_buckets")
        bucket_list = []
        response = paginator.paginate()
        for page in response:
            for bucket in page["Buckets"]:
                bucket_list.append(bucket["Name"])
        return bucket_list

    def get_bucket_tagging(self, bucket_name):
        return self.client.get_bucket_tagging(Bucket=bucket_name)

    def put_bucket_tagging(self, bucket_name, tags):
        # TODO - implement the put_bucket_tagging method
        pass

    def upload_file(self, filename, bucket, key):
        return self.client.upload_file(
            Filename=filename, Bucket=bucket, Key=key
        )
