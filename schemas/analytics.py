from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_spaces: int
    total_resources: int
    completed_resources: int
    in_progress_resources: int
    not_started_resources: int
    total_notes: int
    total_tags: int
    pending_revisions: int
    completion_percentage: float