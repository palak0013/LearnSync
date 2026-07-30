from fastapi import FastAPI
from database.database import Base, engine
from models.user import User
from api.auth import router as auth_router
from models.user import User
from models.space import Space
from api.space import router as space_router
from api import resource
from api.note import router as note_router
from models.tag import Tag
from api.tag import router as tag_router
from models.revision import Revision
from api.revision import router as revision_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to LearnSync API 🚀"}

app.include_router(auth_router)
app.include_router(space_router)
app.include_router(resource.router)
app.include_router(note_router)
app.include_router(tag_router)
app.include_router(revision_router)