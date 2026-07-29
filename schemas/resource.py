from datetime import datetime
from pydantic import BaseModel, ConfigDict
from schemas.enums import ResourceType, ResourceStatus


class ResourceBase(BaseModel):
    title: str
    description: str | None = None
    url: str
    resource_type: ResourceType
    status: ResourceStatus
    estimated_time: int | None = None

class ResourceCreate(ResourceBase):
    space_id: int
    

class ResourceUpdate(ResourceBase):
    title: str | None = None
    description: str | None = None
    url: str | None = None
    resource_type: ResourceType | None = None
    status: ResourceStatus | None = None
    estimated_time: int | None = None
    
    
class ResourceResponse(ResourceBase):
    id: int
    created_at: datetime
    space_id: int

    model_config = ConfigDict(from_attributes=True)