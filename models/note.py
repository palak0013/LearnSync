from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    content = Column(Text, nullable=False) # text is used for larger content

    created_at = Column(DateTime, default=datetime.utcnow)

    space_id = Column(Integer, ForeignKey("spaces.id"), nullable=False)

    space = relationship("Space", back_populates="notes")