from src.domain.models.dynamodb_metadata import TableMetaData
from src.infra.dynamodb.dynamodb_repository import DynamoDBRepository


class DynamoDataService:
    def __init__(self, repository: DynamoDBRepository):
        self.repository = repository

    def list_all_tables(self):
        tables = self.repository.describe_all_tables()
        return [
            TableMetaData(
                AttributeDefinitions=table["AttributeDefinitions"],
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                TableStatus=table["TableStatus"],
                CreationDateTime=table["CreationDateTime"],
                ProvisionedThroughput=table["ProvisionedThroughput"],
                TableSizeBytes=table["TableSizeBytes"],
                ItemCount=table["ItemCount"],
                TableArn=table["TableArn"],
                TableId=table["TableId"],
                BillingModeSummary=table.get("BillingModeSummary"),
                LocalSecondaryIndexes=table.get("LocalSecondaryIndexes"),
                GlobalSecondaryIndexes=table.get("GlobalSecondaryIndexes"),
                StreamSpecification=table.get("StreamSpecification"),
                LatestStreamLabel=table.get("LatestStreamLabel"),
                LatestStreamArn=table.get("LatestStreamArn"),
                GlobalTableVersion=table.get("GlobalTableVersion"),
                Replicas=table.get("Replicas"),
                RestoreSummary=table.get("RestoreSummary"),
                SSEDescription=table.get("SSEDescription"),
                ArchivalSummary=table.get("ArchivalSummary"),
                TableClassSummary=table.get("TableClassSummary"),
                DeletionProtectionEnabled=table.get(
                    "DeletionProtectionEnabled"
                ),
                MultiRegionConsistency=table.get("MultiRegionConsistency"),
            )
            for table in tables
        ]
