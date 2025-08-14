import unittest
from unittest.mock import Mock

from src.application.services.data_services.log_group_data_service import (
    LogGroupDataService,
)
from src.domain.models.log_group_metadata import LogGroupMetaData
from src.infra.log_group.log_group_repository import LogGroupRepository


class TestLogGroupDataService(unittest.TestCase):
    def setUp(self):
        self.mock_log_group_repository = Mock(spec=LogGroupRepository)
        self.log_group_data_service = LogGroupDataService(
            repository=self.mock_log_group_repository
        )

    def test_list_all_log_groups(self):
        # Arrange
        mock_log_groups = [
            {
                "logGroupName": "test-log-group-1",
                "creationTime": 1234567890,
                "retentionInDays": 7,
                "metricFilterCount": 1,
                "arn": "arn:aws:logs:us-east-1:123456789012:log-group:test-log-group-1",
                "storedBytes": 1024,
                "kmsKeyId": "test-kms-key-id",
                "dataProtectionStatus": "ACTIVATED",
                "inheritedProperties": [],
                "logGroupClass": "STANDARD",
            },
            {
                "logGroupName": "test-log-group-2",
                "creationTime": 1234567891,
                "retentionInDays": 14,
                "metricFilterCount": 0,
                "arn": "arn:aws:logs:us-east-1:123456789012:log-group:test-log-group-2",
                "storedBytes": 2048,
                "kmsKeyId": None,
                "dataProtectionStatus": "DISABLED",
                "inheritedProperties": [],
                "logGroupClass": "INFREQUENT_ACCESS",
            },
        ]
        self.mock_log_group_repository.describe_log_groups.return_value = (
            mock_log_groups
        )

        # Act
        result = self.log_group_data_service.list_all_log_groups()

        # Assert
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], LogGroupMetaData)
        self.assertEqual(result[0].logGroupName, "test-log-group-1")
        self.assertEqual(result[1].logGroupName, "test-log-group-2")


if __name__ == "__main__":
    unittest.main()
