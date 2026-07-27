from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SpaceBase(BaseModel):
    name: str
    description: str | None = None


class SpaceCreate(SpaceBase):  #POST/spaces
    pass


class SpaceUpdate(BaseModel): #PUT/spaces/{id}
    name: str | None = None
    description: str | None = None


class SpaceResponse(SpaceBase): #api will return this
    id: int
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)