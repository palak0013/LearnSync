from datetime import datetime
from pydantic import BaseModel, ConfigDict

class NoteBase(BaseModel):
    title: str
    content: str
    
class NoteCreate(NoteBase):
    space_id: int
    
class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    
class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    space_id: int

    model_config = ConfigDict(from_attributes=True)