import boto3

from src.domain.repositories.iam_repository import IIAMReposoty


class IAMRepository(IIAMReposoty):
    def __init__(self):
        self.client = boto3.client("iam")

    def list_roles(self):
        paginator = self.client.get_paginator("list_roles")
        roles_list = []
        response = paginator.paginate()

        for roles in response:
            for role in roles["Roles"]:
                roles_list.append(role)

        return roles_list

    def list_role_tags(self, role_name):
        response = self.client.list_role_tags(RoleName=role_name)
        return response["Tags"]

    def list_tags_for_all_roles(self):
        list_roles = self.list_roles()
        tags = []

        for role in list_roles:
            tags.append(
                [
                    role["RoleName"],
                    self.list_role_tags(role["RoleName"]),
                ]
            )

        return tags

    def tag_role(self, role_name, tags):
        return self.client.tag_role(RoleName=role_name, Tags=tags)
