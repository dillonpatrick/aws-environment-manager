from src.domain.models.dynamodb_metadata import TableMetaData


class GetTablesWithoutDeletionProtectionEnabledService:
    @staticmethod
    def get_tables_without_deletion_protection_enabled(
        tables_list: list[TableMetaData],
    ) -> list[str]:
        tables_without_deletion_protection = []
        for table in tables_list:
            if not GetTablesWithoutDeletionProtectionEnabledService.has_deletion_protection_enabled(
                table
            ):
                tables_without_deletion_protection.append(table.TableName)
        return tables_without_deletion_protection

    @staticmethod
    def has_deletion_protection_enabled(table: TableMetaData) -> bool:
        return table.DeletionProtectionEnabled is True
