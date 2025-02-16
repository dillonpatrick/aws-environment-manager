from src.infra.iam.iam_repository import IAMRepository


class GetRolesWithoutTagService:
    @staticmethod
    def get_roles_without_name_tag() -> list[str]:
        roles_without_tag = []

        roles_tags_list = IAMRepository().list_tags_for_all_roles()

        for role_name, tags in roles_tags_list:
            if not GetRolesWithoutTagService.has_tag_name(
                tags
            ) and not role_name.startswith(
                "AWSReservedSSO"
            ):  # this roles is only modifiable by AWS
                roles_without_tag.append(role_name)

        return roles_without_tag

    @staticmethod
    def has_tag_name(tags) -> bool:
        for tag in tags:
            if tag.get("Key") == "Name":
                return True
        return False
