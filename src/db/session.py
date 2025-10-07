from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.core.config import settings

#creates a sqlalchemy engine to connect to the database
engine = create_engine(settings.DATABASE_URL,future=True,echo=True)

#creates a sessionmaker to create sessions to the database
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#creates a declarative base to create the database models
Base = declarative_base()


#dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
