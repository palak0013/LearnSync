from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.tag import (create_tag, get_all_tags, add_tag_to_resource, get_resource_tags)
from database.database import get_db
from schemas.tag import TagCreate, TagResponse

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)

@router.post("/", response_model=TagResponse)
def create_new_tag(
    tag: TagCreate,
    db: Session = Depends(get_db)
):
    return create_tag(db, tag)


@router.get("/", response_model=list[TagResponse])
def get_tags(
    db: Session = Depends(get_db)
):
    return get_all_tags(db)


@router.post("/resources/{resource_id}/tags/{tag_id}")
def attach_tag(
    resource_id: int,
    tag_id: int,
    db: Session = Depends(get_db)
):

    add_tag_to_resource(
        db,
        resource_id,
        tag_id
    )

    return {
        "message": "Tag added successfully"
    }
    

@router.get("/resources/{resource_id}/tags")
def get_tags_of_resource(
    resource_id: int,
    db: Session = Depends(get_db)
):

    resource = get_resource_tags(db, resource_id)

    return {
        "resource_id": resource.id,
        "title": resource.title,
        "tags": [   # list comprehension concept
            {
                "id": tag.id,
                "name": tag.name
            }
            for tag in resource.tags
        ]
    }