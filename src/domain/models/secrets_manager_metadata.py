from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RotationRule:
    AutomaticallyAfterDays: Optional[int] = None
    Duration: Optional[str] = None
    ScheduleExpression: Optional[str] = None


@dataclass
class Tag:
    Key: str
    Value: str


@dataclass
class ReplicationStatusItem:
    Region: str
    KmsKeyId: str
    Status: str  # "InSync" | "Failed" | "InProgress"
    StatusMessage: str
    LastAccessedDate: Optional[datetime] = None


@dataclass
class SecretMetadata:
    ARN: str
    Name: str
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = False
    RotationLambdaARN: Optional[str] = None
    RotationRules: Optional[RotationRule] = None
    LastRotatedDate: Optional[datetime] = None
    LastChangedDate: Optional[datetime] = None
    LastAccessedDate: Optional[datetime] = None
    DeletedDate: Optional[datetime] = None
    NextRotationDate: Optional[datetime] = None
    Tags: list[Tag] = field(default_factory=list)
    VersionIdsToStages: dict[str, list[str]] = field(default_factory=dict)
    OwningService: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    PrimaryRegion: Optional[str] = None
    ReplicationStatus: list[ReplicationStatusItem] = field(
        default_factory=list
    )
