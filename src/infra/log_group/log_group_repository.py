import boto3

from src.domain.repositories.log_group_repository import ILogGroupRepository


class LogGroupRepository(ILogGroupRepository):
    def __init__(self):
        self.client = boto3.client("logs")

    def describe_log_groups(self):
        paginator = self.client.get_paginator("describe_log_groups")
        log_groups_list = []
        response = paginator.paginate()

        for page in response:
            for log_group in page["logGroups"]:
                log_groups_list.append(log_group)
        return log_groups_list

    def list_tags_for_log_group(self, resource_arn):
        return self.client.list_tags_for_resource(resourceArn=resource_arn)

    def list_tags_for_all_log_groups(self):
        tags = []

        for log_group in self.describe_log_groups():
            log_group_arn = (log_group["arn"]).rstrip(":*")
            log_group_name = log_group["logGroupName"]
            tags.append(
                {
                    "log_group_name": log_group_name,
                    "log_group_arn": log_group_arn,
                    "tags": self.list_tags_for_log_group(log_group_arn)[
                        "tags"
                    ],
                }
            )
        return tags

    def tag_log_group(self, resource_arn, tags):
        return self.client.tag_resource(resourceArn=resource_arn, tags=tags)
