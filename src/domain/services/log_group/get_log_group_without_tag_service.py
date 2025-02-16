from src.domain.models.log_group_metadata import LogGroupMetaData


class GetLogGroupWithoutTagService:
    @staticmethod
    def get_log_group_without_name_tag(
        log_groups: list,
    ) -> list[dict]:
        log_groups_without_tags = []

        for log_group in log_groups:
            if (
                GetLogGroupWithoutTagService.has_tag_name(log_group["tags"])
                == False
            ):
                log_groups_without_tags.append(
                    [
                        log_group["log_group_name"],
                        log_group["log_group_arn"],
                        log_group["tags"],
                    ]
                )
        return log_groups_without_tags

    @staticmethod
    def has_tag_name(tags) -> bool:
        has_name_tag = False
        for tag in tags:
            if tag == "Name":
                has_name_tag = True
                break

        return has_name_tag
