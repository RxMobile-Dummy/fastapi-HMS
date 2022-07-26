from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




engine = create_engine(url='postgresql://anirudh.chawla:123@localhost/department')


SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
