class GetTablesWithoutNameTagService:
    @staticmethod
    def get_tables_without_name_tag(tables_tags_list: list) -> list:
        tables_without_tag = []
        for table_name, tags in tables_tags_list:
            if not GetTablesWithoutNameTagService.has_tag_name(
                table_name, tags
            ):
                tables_without_tag.append([table_name, tags])
        return tables_without_tag

    @staticmethod
    def has_tag_name(table_name, tag_list: dict) -> bool:
        return {"Key": "Name", "Value": table_name} in tag_list
