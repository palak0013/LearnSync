from sqlalchemy import create_engine #connection to postgreSql
from sqlalchemy.orm import declarative_base, sessionmaker #session maker creates sessions for us and base lets sqlalchemy know these tables

from dotenv import load_dotenv #loads variables from .env
import os #allows to read DATABASE_URL from .env

load_dotenv() #read everythin inside .env
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #bridge b/w FASTAPI & PostgreSql

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base() #all classes will inherit from this base

