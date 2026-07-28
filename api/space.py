from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.database import get_db
from api.auth import get_current_user
from crud.space import create_space, update_space, delete_space
from crud.space import get_spaces, get_space_by_id
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
    

@router.get(
    "",
    response_model=list[SpaceResponse]
)
def get_all_spaces(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_spaces(
        db=db,
        current_user=current_user
    )
    

@router.get(
    "/{space_id}",
    response_model=SpaceResponse
)
def get_space(
    space_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_space_by_id(
        db=db,
        space_id=space_id,
        current_user=current_user
    )
    

@router.put(
    "/{space_id}",
    response_model=SpaceResponse
)
def update_space_api(
    space_id: int,
    space: SpaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return update_space(
        db=db,
        space_id=space_id,
        space=space,
        current_user=current_user
    )
    
    
@router.delete("/{space_id}")
def delete_space_api(
    space_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return delete_space(
        db=db,
        space_id=space_id,
        current_user=current_user
    )