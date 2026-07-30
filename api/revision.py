from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from crud.revision import (create_revision, get_all_revisions, get_due_revisions, update_revision, delete_revision,)
from schemas.revision import (RevisionCreate, RevisionUpdate, RevisionResponse,)

router = APIRouter(
    prefix="/revisions",
    tags=["Revisions"]
)

@router.post("/", response_model=RevisionResponse)
def create_new_revision(
    revision: RevisionCreate,
    db: Session = Depends(get_db)
):
    return create_revision(db, revision)

@router.get("/", response_model=list[RevisionResponse])
def get_revisions(
    db: Session = Depends(get_db)
):
    return get_all_revisions(db)

@router.get("/due", response_model=list[RevisionResponse])
def due_revisions(
    db: Session = Depends(get_db)
):
    return get_due_revisions(db)

@router.put("/{revision_id}", response_model=RevisionResponse)
def update_existing_revision(
    revision_id: int,
    revision: RevisionUpdate,
    db: Session = Depends(get_db)
):
    return update_revision(
        db,
        revision_id,
        revision
    )
    
@router.delete("/{revision_id}")
def remove_revision(
    revision_id: int,
    db: Session = Depends(get_db)
):
    return delete_revision(
        db,
        revision_id
    )