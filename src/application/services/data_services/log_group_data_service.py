from src.domain.models.log_group_metadata import LogGroupMetaData
from src.infra.log_groups.log_group_repository import LogGroupRepository


class LogGroupDataService:
    def __init__(self, repository: LogGroupRepository):
        self.repository = repository

    def list_all_log_groups(self) -> list[LogGroupMetaData]:
        log_groups = self.repository.describe_log_groups()
        return [
            LogGroupMetaData(
                logGroupName=log_group.get("logGroupName"),
                creationTime=log_group.get("creationTime"),
                retentionInDays=log_group.get("retentionInDays"),
                metricFilterCount=log_group.get("metricFilterCount"),
                arn=log_group.get("arn"),
                storedBytes=log_group.get("storedBytes"),
                kmsKeyId=log_group.get("kmsKeyId"),
                dataProtectionStatus=log_group.get("dataProtectionStatus"),
                inheritedProperties=log_group.get("inheritedProperties"),
                logGroupClass=log_group.get("logGroupClass"),
            )
            for log_group in log_groups
        ]
