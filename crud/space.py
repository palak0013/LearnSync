from sqlalchemy.orm import Session

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