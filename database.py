import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use environment variable for database URL, checking multiple common names
DB_URL = os.getenv('DATABASE_URL') or os.getenv('POSTGRES_URL') or 'postgresql://postgres:postgres@localhost:5432/spotify-clone'

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()