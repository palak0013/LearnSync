from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.note import (create_note, get_all_notes, get_note_by_id, update_note, delete_note)
from database.database import get_db
from schemas.note import (NoteCreate, NoteUpdate, NoteResponse)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post("/", response_model=NoteResponse)
def create_new_note(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db, note)

@router.get("/", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db)):
    return get_all_notes(db)

@router.get("/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = get_note_by_id(db, note_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note

@router.put("/{note_id}", response_model=NoteResponse)
def update_existing_note(
    note_id: int,
    note: NoteUpdate,
    db: Session = Depends(get_db)
):
    updated_note = update_note(db, note_id, note)

    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")

    return updated_note

@router.delete("/{note_id}", response_model=NoteResponse)
def delete_existing_note(note_id: int, db: Session = Depends(get_db)):
    deleted_note = delete_note(db, note_id)

    if not deleted_note:
        raise HTTPException(status_code=404, detail="Note not found")

    return deleted_note