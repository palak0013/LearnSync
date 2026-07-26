from passlib.context import CryptContext

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