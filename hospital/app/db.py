"""File to connect fastAPI WITH POSTGRESQL DATABASE"""
import sys,os
sys.path.append(os.getcwd())
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import hospital.config

DATABASE_URL = hospital.config.Config.DATABASE_URL
engine = create_engine(url='postgresql+psycopg2://akash.kareliya:123@localhost:54321/hospital')

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    """Function to get db details"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
