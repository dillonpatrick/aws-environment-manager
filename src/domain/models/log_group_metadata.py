from dataclasses import dataclass
from typing import Optional


@dataclass
class LogGroupMetaData:
    logGroupName: str = None
    creationTime: int = None
    retentionInDays: int = None
    metricFilterCount: int = None
    arn: str = None
    storedBytes: int = None
    kmsKeyId: Optional[str] = None
    dataProtectionStatus: Optional[str] = None
    inheritedProperties: Optional[list[str]] = None
    logGroupClass: Optional[str] = None
    tags: Optional[list[dict]] = None
