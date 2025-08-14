from typing import Optional

from src.application.services.data_services.log_group_data_service import (
    LogGroupDataService,
)
from src.infra.log_group.log_group_repository import LogGroupRepository


class BaseService:
    def __init__(self, repository: Optional[LogGroupRepository] = None):
        self.repository = (
            repository if repository is not None else LogGroupRepository()
        )
        self.log_group_listing_service = LogGroupDataService(self.repository)
