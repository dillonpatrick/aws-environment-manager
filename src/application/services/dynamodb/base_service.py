from typing import Optional

from src.application.services.data_services.dynamo_data_service import (
    DynamoDataService,
)
from src.infra.dynamodb.dynamodb_repository import DynamoDBRepository


class BaseService:
    def __init__(self, repository: Optional[DynamoDBRepository] = None):
        self.repository = (
            repository if repository is not None else DynamoDBRepository()
        )
        self.table_listing_service = DynamoDataService(self.repository)
