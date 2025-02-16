from src.domain.models.dynamodb_metadata import TableMetaData


class GetTablesWithoutReplicationService:
    @staticmethod
    def get_tables_without_replication(
        tables_list: list[TableMetaData],
    ) -> list[str]:
        tables_without_replication = []
        for table in tables_list:
            if not GetTablesWithoutReplicationService.has_replication(table):
                if table.TableName != "tfstate-dev":
                    tables_without_replication.append(table.TableName)
        return tables_without_replication

    @staticmethod
    def has_replication(table: TableMetaData) -> bool:
        if table.Replicas != None:
            return True
        return False
