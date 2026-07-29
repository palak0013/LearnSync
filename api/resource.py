from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from crud.resource import (create_resource, get_all_resources, get_resource_by_id, update_resource, delete_resource)
from schemas.resource import (ResourceCreate, ResourceUpdate, ResourceResponse)

router = APIRouter(
    prefix="/resources",
    tags=["Resources"]
)

@router.post("/", response_model=ResourceResponse)
def create_new_resource(
    resource: ResourceCreate,
    db: Session = Depends(get_db)
):
    return create_resource(db, resource)

@router.get("/", response_model=list[ResourceResponse])
def get_resources(
    db: Session = Depends(get_db)
):
    return get_all_resources(db)

@router.get("/{resource_id}", response_model=ResourceResponse)
def get_resource(
    resource_id: int,
    db: Session = Depends(get_db)
):
    resource = get_resource_by_id(db, resource_id)

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return resource

@router.put("/{resource_id}", response_model=ResourceResponse)
def update_existing_resource(
    resource_id: int,
    resource: ResourceUpdate,
    db: Session = Depends(get_db)
):
    updated_resource = update_resource(db, resource_id, resource)

    if not updated_resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return updated_resource

@router.delete("/{resource_id}", response_model=ResourceResponse)
def delete_existing_resource(
    resource_id: int,
    db: Session = Depends(get_db)
):
    deleted_resource = delete_resource(db, resource_id)

    if not deleted_resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return deleted_resource