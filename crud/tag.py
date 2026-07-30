from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.tag import Tag
from models.resource import Resource
from schemas.tag import TagCreate

def create_tag(db: Session, tag: TagCreate):

    existing_tag = db.query(Tag).filter(Tag.name == tag.name).first()

    if existing_tag:
        raise HTTPException(
            status_code=400,
            detail="Tag already exists"
        )

    db_tag = Tag(name=tag.name)

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)

    return db_tag


def get_all_tags(db: Session):
    return db.query(Tag).all()


def add_tag_to_resource(
    db: Session,
    resource_id: int,
    tag_id: int
):

    resource = db.query(Resource).filter(
        Resource.id == resource_id
    ).first()

    tag = db.query(Tag).filter(
        Tag.id == tag_id
    ).first()

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    if not tag:
        raise HTTPException(
            status_code=404,
            detail="Tag not found"
        )

    if tag in resource.tags:
        raise HTTPException(
            status_code=400,
            detail="Tag already added"
        )

    resource.tags.append(tag)

    db.commit()

    return resource


def get_resource_tags(db: Session, resource_id: int):

    resource = db.query(Resource).filter(Resource.id == resource_id).first()

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    return resource