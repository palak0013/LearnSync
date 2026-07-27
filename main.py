from fastapi import FastAPI
from database.database import Base, engine
from models.user import User
from api.auth import router as auth_router
from models.user import User
from models.space import Space
from api.space import router as space_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to LearnSync API 🚀"}

app.include_router(auth_router)
app.include_router(auth_router)
app.include_router(space_router)