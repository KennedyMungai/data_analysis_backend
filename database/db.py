"""The file with the database connection logic"""
import os
import psycopg

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(find_dotenv())

DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """A simple function for getting access to the database

    Yields:
        db: SessionLocal instance
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
