from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class AttributeDefinition:
    AttributeName: str
    AttributeType: str


@dataclass
class KeySchema:
    AttributeName: str
    KeyType: str


@dataclass
class ProvisionedThroughput:
    LastIncreaseDateTime: Optional[datetime]
    LastDecreaseDateTime: Optional[datetime]
    NumberOfDecreasesToday: int
    ReadCapacityUnits: int
    WriteCapacityUnits: int


@dataclass
class BillingModeSummary:
    BillingMode: str
    LastUpdateToPayPerRequestDateTime: Optional[datetime]


@dataclass
class Projection:
    ProjectionType: str
    NonKeyAttributes: Optional[List[str]]


@dataclass
class LocalSecondaryIndex:
    IndexName: str
    KeySchema: List[KeySchema]
    Projection: Projection
    IndexSizeBytes: int
    ItemCount: int
    IndexArn: str


@dataclass
class GlobalSecondaryIndex:
    IndexName: str
    KeySchema: List[KeySchema]
    Projection: Projection
    IndexStatus: str
    Backfilling: bool
    ProvisionedThroughput: Optional[ProvisionedThroughput]
    IndexSizeBytes: int
    ItemCount: int
    IndexArn: str


@dataclass
class StreamSpecification:
    StreamEnabled: bool
    StreamViewType: str


@dataclass
class ReplicaGlobalSecondaryIndex:
    IndexName: str
    ProvisionedThroughputOverride: Optional[ProvisionedThroughput]


@dataclass
class Replica:
    RegionName: str
    ReplicaStatus: str
    ReplicaStatusDescription: Optional[str]
    ReplicaStatusPercentProgress: Optional[str]
    KMSMasterKeyId: Optional[str]
    ProvisionedThroughputOverride: Optional[ProvisionedThroughput]
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndex]]


@dataclass
class RestoreSummary:
    SourceBackupArn: str
    SourceTableArn: str
    RestoreDateTime: datetime
    RestoreInProgress: bool


@dataclass
class SSEDescription:
    Status: str
    SSEType: str
    KMSMasterKeyArn: Optional[str]
    InaccessibleEncryptionDateTime: Optional[datetime]


@dataclass
class ArchivalSummary:
    ArchivalDateTime: datetime
    ArchivalReason: str
    ArchivalBackupArn: str


@dataclass
class TableClassSummary:
    TableClass: str
    LastUpdateDateTime: datetime


@dataclass
class TableMetaData:
    TableName: str
    AttributeDefinitions: List[AttributeDefinition]
    KeySchema: List[KeySchema]
    TableStatus: str
    CreationDateTime: datetime
    ProvisionedThroughput: ProvisionedThroughput
    TableSizeBytes: int
    ItemCount: int
    TableArn: str
    TableId: str
    BillingModeSummary: Optional[BillingModeSummary]
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndex]]
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndex]]
    StreamSpecification: Optional[StreamSpecification]
    LatestStreamLabel: Optional[str]
    LatestStreamArn: Optional[str]
    GlobalTableVersion: Optional[str]
    Replicas: Optional[List[Replica]]
    RestoreSummary: Optional[RestoreSummary]
    SSEDescription: Optional[SSEDescription]
    ArchivalSummary: Optional[ArchivalSummary]
    TableClassSummary: Optional[TableClassSummary]
    DeletionProtectionEnabled: Optional[bool]
    MultiRegionConsistency: Optional[bool]
