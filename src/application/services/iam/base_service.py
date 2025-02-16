from typing import Optional

from src.application.services.data_services.iam_data_service import (
    IAMDataService,
)
from src.infra.iam.iam_repository import IAMRepository


class BaseService:
    def __init__(self, repository: Optional[IAMDataService] = None):
        self.repository = (
            repository if repository is not None else IAMRepository()
        )

        self.iam_listing_service = IAMDataService(self.repository)
