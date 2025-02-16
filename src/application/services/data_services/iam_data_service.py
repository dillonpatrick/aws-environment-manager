from src.domain.models.iam_metadata import IAMMetadata
from src.infra.iam.iam_repository import IAMRepository


class IAMDataService:
    def __init__(self, repository: IAMRepository):
        self.repository = repository

    def list_all_roles(self):
        roles = self.repository.list_roles()
        return [
            IAMMetadata(
                Path=role.get("Path"),
                RoleName=role.get("RoleName"),
                RoleId=role.get("RoleId"),
                Arn=role.get("Arn"),
                CreateDate=role.get("CreateDate"),
                AssumeRolePolicyDocument=role.get("AssumeRolePolicyDocument"),
                Description=role.get("Description"),
                MaxSessionDuration=role.get("MaxSessionDuration"),
                PermissionsBoundary=role.get("PermissionsBoundary"),
                Tags=role.get("Tags"),
                RoleLastUsed=role.get("RoleLastUsed"),
            )
            for role in roles
        ]
