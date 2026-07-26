from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate
from utils.security import hash_password

def create_user(db: Session, user: UserCreate):
    existing_user=(
        db.query(User).filter(User.email == user.email).first()
    )
    
    if existing_user:
        return None
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
