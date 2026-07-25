from fastapi import FastAPI
from database.database import Base, engine
from models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to LearnSync API 🚀"}