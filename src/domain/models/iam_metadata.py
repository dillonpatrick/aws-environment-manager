from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class IAMMetadata:
    Path: Optional[str] = None
    RoleName: str = None
    RoleId: str = None
    Arn: str = None
    CreateDate: datetime = None
    AssumeRolePolicyDocument: str = None
    Description: Optional[str] = None
    MaxSessionDuration: Optional[int] = None
    PermissionsBoundary: Optional[dict] = field(default_factory=dict)
    Tags: Optional[list[dict[str, any]]] = field(default_factory=list)
    RoleLastUsed: Optional[dict] = field(default_factory=dict)
