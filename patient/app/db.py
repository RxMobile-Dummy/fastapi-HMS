"""File to connect fastAPI WITH POSTGRESQL DATABASE"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import patient.config

DATABASE_URL = patient.config.Config.DATABASE_URL
patient_engine = create_engine(url='postgresql+psycopg2://akash.kareliya:123@host.docker.internal:54321/patient')

SessionLocal = sessionmaker(bind=patient_engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    """Function to get db details"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
