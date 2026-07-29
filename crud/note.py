from sqlalchemy.orm import Session
from models.note import Note
from schemas.note import NoteCreate, NoteUpdate

def create_note(db: Session, note: NoteCreate):
    db_note = Note(
        title=note.title,
        content=note.content,
        space_id=note.space_id
    )

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

def get_all_notes(db: Session):
    return db.query(Note).all()

def get_note_by_id(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()

def update_note(db: Session, note_id: int, note: NoteUpdate):
    db_note = get_note_by_id(db, note_id)

    if not db_note:
        return None

    db_note.title = note.title
    db_note.content = note.content

    db.commit()
    db.refresh(db_note)

    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note_by_id(db, note_id)

    if not db_note:
        return None

    db.delete(db_note)
    db.commit()

    return db_note