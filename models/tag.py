from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.resource_tag import resource_tags
from database.database import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, unique=True, nullable=False)

    resources = relationship("Resource", secondary="resource_tags", back_populates="tags")