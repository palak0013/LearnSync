from datetime import datetime

from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.database import Base


class Revision(Base):
    __tablename__ = "revisions"

    id = Column(Integer, primary_key=True, index=True)

    revision_date = Column(Date, nullable=False)

    is_completed = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    resource_id = Column(
        Integer,
        ForeignKey("resources.id"),
        nullable=False
    )

    resource = relationship(
        "Resource",
        back_populates="revisions"
    )