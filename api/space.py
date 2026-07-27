from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.database import get_db
from api.auth import get_current_user
from crud.space import create_space
from schemas.space import (SpaceCreate, SpaceResponse,)
from models.user import User


router = APIRouter(
    prefix="/spaces",
    tags=["Learning Spaces"]
)

@router.post(
    "",
    response_model=SpaceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_space(
    space: SpaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_space(
        db=db,
        space=space,
        current_user=current_user
    )