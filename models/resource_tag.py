#acts as an association table b/w the tags and resources

from sqlalchemy import Table, Column, ForeignKey
from database.database import Base

resource_tags = Table(
    "resource_tags",
    Base.metadata,

    Column("resource_id", ForeignKey("resources.id"), primary_key=True),

    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)