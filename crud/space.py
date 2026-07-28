from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.space import Space
from models.user import User
from schemas.space import SpaceCreate


def create_space(
    db: Session,
    space: SpaceCreate,
    current_user: User
):
    new_space = Space(
        name=space.name,
        description=space.description,
        owner_id=current_user.id
    )

    db.add(new_space)
    db.commit()
    db.refresh(new_space)

    return new_space

def get_spaces(
    db: Session,
    current_user: User,
):
    return(
        db.query(Space).filter(Space.owner_id == current_user.id).all()
    )
    
def get_space_by_id(
    db: Session,
    space_id: int,
    current_user: User,
):
    space = (
    db.query(Space).filter(Space.id == space_id, Space.owner_id == current_user.id).first()
    )
    if space is None:
        raise HTTPException(
            status_code=404,
            detail="Space not found"
        )
    return space


def update_space(
    db: Session,
    space_id: int,
    space: SpaceCreate,
    current_user: User,
):
    existing_space = (
        db.query(Space).filter(Space.id == space_id, Space.owner_id == current_user.id).first()
    )

    if existing_space is None:
        raise HTTPException(
            status_code=404,
            detail="Space not found"
        )

    existing_space.name = space.name
    existing_space.description = space.description

    db.commit()
    db.refresh(existing_space)

    return existing_space


def delete_space(
    db: Session,
    space_id: int,
    current_user: User,
):
    space = (
        db.query(Space)
        .filter(
            Space.id == space_id,
            Space.owner_id == current_user.id
        )
        .first()
    )

    if space is None:
        raise HTTPException(
            status_code=404,
            detail="Space not found"
        )

    db.delete(space)
    db.commit()

    return {"message": "Space deleted successfully"}