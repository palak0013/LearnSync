from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from crud.user import create_user
from crud.user import authenticate_user
from database.database import get_db
from schemas.user import UserCreate, UserResponse
from schemas.user import UserLogin, Token
from utils.security import create_access_token
from utils.security import verify_access_token
from models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
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

@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    authenticated_user = authenticate_user(
        db,
        user.email,
        user.password,
    )

    if authenticated_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": str(authenticated_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
    
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):

    user_id = verify_access_token(token)

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):

    return current_user