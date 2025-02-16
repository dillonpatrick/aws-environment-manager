from os import getenv

import boto3

from src.domain.repositories.dynamodb_repository import IDynamoDBRepository


class DynamoDBRepository(IDynamoDBRepository):
    def __init__(self):
        self.client = boto3.client("dynamodb")

    def list_tables(self):
        paginator = self.client.get_paginator("list_tables")
        tables = []

        for response in paginator.paginate():
            tables.extend(response.get("TableNames", []))
        return tables

    def list_tags_of_table(self, table_name):
        return self.client.list_tags_of_resource(
            ResourceArn=f"arn:aws:dynamodb:{getenv('REGION')}:{getenv('AWS_ACCOUNT_ID')}:table/{table_name}"
        )

    def list_tags_of_all_tables(self):
        tables = self.list_tables()
        tables_tags = []

        for table_name in tables:
            tags_list = self.list_tags_of_table(table_name)
            tables_tags.append([table_name, tags_list.get("Tags", [])])
        return tables_tags

    def describe_table(self, table_name):
        return self.client.describe_table(TableName=table_name)["Table"]

    def describe_all_tables(self):
        tables = self.list_tables()
        detailed_tables = []

        for table in tables:
            detailed_tables.append(self.describe_table(table))
        return detailed_tables

    def tag_table(self, table_name, tags):
        return self.client.tag_resource(
            ResourceArn=f"arn:aws:dynamodb:{getenv('REGION')}:{getenv('AWS_ACCOUNT_ID')}:table/{table_name}",
            Tags=tags,
        )

    def enable_deletion_protection(self, table_name):
        return self.client.update_table(
            TableName=table_name,
            DeletionProtectionEnabled=True,
        )

    def scan_table(self, table_name, attributes_to_get):
        paginator = self.client.get_paginator("scan")
        scan_result = []
        params = {
            "TableName": table_name,
            "AttributesToGet": attributes_to_get,
        }

        for response in paginator.paginate(**params):
            scan_result.extend(response.get("Items", []))
        return scan_result
