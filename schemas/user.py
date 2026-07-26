from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel): #fields that are common in multiple schemas so we don't have to write again and again
    username: str
    email: EmailStr
    
class UserCreate(UserBase): #Register API
    password: str
    
class UserLogin(BaseModel):# used for login
    email:EmailStr
    password: str

class UserResponse(UserBase): #sends response back to client
    id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)