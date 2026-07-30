from datetime import date
from sqlalchemy.orm import Session
from models.note import Note
from models.resource import Resource
from models.revision import Revision
from models.space import Space
from models.tag import Tag

def get_dashboard(db: Session):

    total_spaces = db.query(Space).count()

    total_resources = db.query(Resource).count()

    completed_resources = db.query(Resource).filter(
        Resource.status == "Completed"
    ).count()

    in_progress_resources = db.query(Resource).filter(
        Resource.status == "In Progress"
    ).count()

    not_started_resources = db.query(Resource).filter(
        Resource.status == "Not Started"
    ).count()

    total_notes = db.query(Note).count()

    total_tags = db.query(Tag).count()

    pending_revisions = db.query(Revision).filter(
        Revision.revision_date <= date.today(),
        Revision.is_completed == False
    ).count()

    if total_resources == 0:
        completion_percentage = 0

    else:
        completion_percentage = (
            completed_resources / total_resources
        ) * 100

    return {
        "total_spaces": total_spaces,
        "total_resources": total_resources,
        "completed_resources": completed_resources,
        "in_progress_resources": in_progress_resources,
        "not_started_resources": not_started_resources,
        "total_notes": total_notes,
        "total_tags": total_tags,
        "pending_revisions": pending_revisions,
        "completion_percentage": round(completion_percentage, 2)
    }