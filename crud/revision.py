from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import date
from models.resource import Resource
from models.revision import Revision
from schemas.revision import RevisionCreate, RevisionUpdate


def create_revision(
    db: Session,
    revision: RevisionCreate
):

    resource = db.query(Resource).filter(
        Resource.id == revision.resource_id
    ).first()

    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    db_revision = Revision(
        revision_date=revision.revision_date,
        resource_id=revision.resource_id
    )

    db.add(db_revision)
    db.commit()
    db.refresh(db_revision)

    return db_revision


def get_all_revisions(db: Session):
    return db.query(Revision).all()

def get_due_revisions(db: Session):

    today = date.today()

    return db.query(Revision).filter(
        Revision.revision_date <= today,
        Revision.is_completed == False
    ).all()
    
def update_revision(
    db: Session,
    revision_id: int,
    revision: RevisionUpdate
):

    db_revision = db.query(Revision).filter(
        Revision.id == revision_id
    ).first()

    if not db_revision:
        raise HTTPException(
            status_code=404,
            detail="Revision not found"
        )

    if revision.revision_date is not None:
        db_revision.revision_date = revision.revision_date

    if revision.is_completed is not None:
        db_revision.is_completed = revision.is_completed

    db.commit()
    db.refresh(db_revision)

    return db_revision


def delete_revision(
    db: Session,
    revision_id: int
):

    db_revision = db.query(Revision).filter(
        Revision.id == revision_id
    ).first()

    if not db_revision:
        raise HTTPException(
            status_code=404,
            detail="Revision not found"
        )

    db.delete(db_revision)
    db.commit()

    return {
        "message": "Revision deleted successfully"
    }