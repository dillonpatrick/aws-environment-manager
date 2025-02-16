from src.application.services.dynamodb import (
    DeletionProtectionService,
    ExportCompaniesInfoService,
    ListTablesInfoService,
    TagTableService,
)
from src.infra.dynamodb.dynamodb_repository import DynamoDBRepository
from src.infra.s3.s3_bucket_repository import S3BucketRepository


def add_name_tag(event, context):
    return TagTableService().add_name_tag()


def list_tables_without_replication(event, context):
    return ListTablesInfoService().list_tables_without_replication()


def enable_protection(event, context):
    return DeletionProtectionService().enable_protection()


def export_companies_to_csv(event, context):
    dynamodb_repository = DynamoDBRepository()
    s3_repository = S3BucketRepository()

    export_service = ExportCompaniesInfoService(
        dynamodb_repository, s3_repository
    )
    export_service.export_infos_to_csv()
