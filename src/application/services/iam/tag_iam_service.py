from src.application.services.iam.base_service import BaseService
from src.domain.services.iam.get_roles_without_tag_service import (
    GetRolesWithoutTagService,
)
from src.utils.params_logger import logger


class TagIamService(BaseService):
    def add_name_tag(self):
        logger.info("Starting process...")

        roles_without_tag = (
            GetRolesWithoutTagService.get_roles_without_name_tag()
        )

        if not roles_without_tag:
            logger.info("All roles have the 'Name' tag.")

        try:
            for role_name in roles_without_tag:
                self.repository.tag_role(
                    role_name=role_name,
                    tags=[
                        {"Key": "Name", "Value": role_name},
                    ],
                )
                logger.info(
                    f"The 'Name' tag has been added to the role '{role_name}'."
                )
        except Exception as e:
            logger.error(str(e))

        logger.info("Finishing process...")
