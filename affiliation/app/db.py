from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




engine = create_engine(url='postgresql+psycopg2://akash.kareliya:123@localhost:5432/affiliation')


SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
