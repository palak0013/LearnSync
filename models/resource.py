from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from database.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String, nullable=True)

    url = Column(String, nullable=False)

    resource_type = Column(String, nullable=False)

    status = Column(String, nullable=False)

    estimated_time = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    space_id = Column(Integer, ForeignKey("spaces.id"), nullable=False)

    space = relationship("Space", back_populates="resources")