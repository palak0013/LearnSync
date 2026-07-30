from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from crud.analytics import get_dashboard
from schemas.analytics import DashboardResponse

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard(
    db: Session = Depends(get_db)
):
    return get_dashboard(db)