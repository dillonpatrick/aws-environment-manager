from typing import Optional

from src.application.services.data_services.secret_data_service import (
    SecretDataService,
)
from src.infra.secrets_manager.secrets_manager_repository import (
    SecretsManagerRepository,
)


class BaseService:
    def __init__(self, repository: Optional[SecretsManagerRepository] = None):
        self.repository = (
            repository
            if repository is not None
            else SecretsManagerRepository()
        )
        self.secret_listing_service = SecretDataService(self.repository)
