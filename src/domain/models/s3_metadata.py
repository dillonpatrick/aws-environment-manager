from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class BucketMetaData:
    Name: str
    CreationDate: Optional[datetime] = None
    BucketRegion: Optional[str] = None
