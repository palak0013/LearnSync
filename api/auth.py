from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from crud.user import create_user
from database.database import get_db
from schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user:UserCreate,
    db: Session = Depends(get_db),
):
    new_user = create_user(db,user)
    
    if new_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already registerd"
        )
    return new_user