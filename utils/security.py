from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import jwt
from database.database import (SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)
from jose import JWSError, JWTError
from fastapi import HTTPException, status

pwd_contect = CryptContext(  #creates password manager which is used everywhere
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_contect.hash(password) #return encrytped password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_contect.verify(
        plain_password,
        hashed_password
    )

def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )
    
def verify_access_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return user_id

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )