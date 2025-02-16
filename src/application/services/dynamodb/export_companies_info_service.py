from os import getenv

from src.domain.services.dynamodb.fetch_companies_info_service import (
    FetchCompaniesInfoService,
)
from src.domain.services.s3.upload_file_to_bucket_service import (
    UploadFileToBucketService,
)
from src.infra.dynamodb.dynamodb_repository import DynamoDBRepository
from src.infra.s3.s3_bucket_repository import S3BucketRepository
from src.utils.params_logger import logger


class ExportCompaniesInfoService:
    def __init__(
        self, repository: DynamoDBRepository, s3Repository: S3BucketRepository
    ):
        self.repository = repository
        self.s3Repository = s3Repository

    def export_infos_to_csv(self):
        logger.info("Starting process...")

        csv_file_path = "/tmp/companies.csv"  # lambda temporary folder

        try:
            companies = FetchCompaniesInfoService.fetch_companies_with_scan(
                repository=self.repository,
                table_name=str(getenv("TABLE_NAME")),
                attributes_to_get=[
                    "id",
                    "companyName",
                    "skipMonitoring",
                    "status",
                ],
            )
            if not companies:
                logger.info("No companies found in the table.")
                return

            processed_data = FetchCompaniesInfoService.process_companies(
                companies
            )

            logger.info(f"Processed {len(processed_data)} companies.")
            FetchCompaniesInfoService.save_to_csv(
                processed_data, csv_file_path
            )

            logger.info(f"Data written successfully to {csv_file_path}")

            UploadFileToBucketService.upload_file(
                repository=self.s3Repository,
                bucket=str(getenv("BUCKET_DATADOG_REFERENCE_TABLES")),
                filename=csv_file_path,
                key="companies.csv",
            )

        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing process...")
