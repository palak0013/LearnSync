from sqlalchemy.orm import Session
from typing import Optional
from models.resource import Resource
from schemas.resource import ResourceCreate, ResourceUpdate

def create_resource(db: Session, resource: ResourceCreate):

    db_resource = Resource(
        title=resource.title,
        description=resource.description,
        url=resource.url,
        resource_type=resource.resource_type.value, # .value is used as i used Enums
        status=resource.status.value,
        estimated_time=resource.estimated_time,
        space_id=resource.space_id
    )

    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)

    return db_resource


def get_all_resources(db: Session):
    return db.query(Resource).all()


def get_resource_by_id(db: Session, resource_id: int):
    return db.query(Resource).filter(Resource.id == resource_id).first()



def update_resource(db: Session, resource_id: int, resource: ResourceUpdate):
    db_resource = get_resource_by_id(db, resource_id)

    if not db_resource:
        return None

    db_resource.title = resource.title
    db_resource.description = resource.description
    db_resource.url = resource.url
    db_resource.resource_type = resource.resource_type.value
    db_resource.status = resource.status.value
    db_resource.estimated_time = resource.estimated_time

    db.commit()
    db.refresh(db_resource)

    return db_resource


def delete_resource(db: Session, resource_id: int):
    db_resource = get_resource_by_id(db, resource_id)

    if not db_resource:
        return None

    db.delete(db_resource)
    db.commit()

    return db_resource

def search_resources(
    db: Session,
    title: Optional[str] = None,
    resource_type: Optional[str] = None,
    status: Optional[str] = None,
    space_id: Optional[int] = None,
):

    query = db.query(Resource)

    if title:
        query = query.filter(
            Resource.title.ilike(f"%{title}%")
        )

    if resource_type:
        query = query.filter(
            Resource.resource_type.ilike(f"%{resource_type}%")
        )

    if status:
        query = query.filter(
            Resource.status.ilike(f"%{status}%")
        )

    if space_id:
        query = query.filter(
            Resource.space_id == space_id
        )

    return query.all()