from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class RevisionBase(BaseModel):
    revision_date: date


class RevisionCreate(RevisionBase):
    resource_id: int


class RevisionUpdate(BaseModel):
    revision_date: date | None = None
    is_completed: bool | None = None


class RevisionResponse(RevisionBase):
    id: int
    is_completed: bool
    created_at: datetime
    resource_id: int

    model_config = ConfigDict(from_attributes=True)