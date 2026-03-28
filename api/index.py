import sys
import os

# Add the parent directory to sys.path so we can import from the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from models.base import Base
from routes import auth, song
from database import engine

app = FastAPI()
app.include_router(auth.router, prefix='/auth')
app.include_router(song.router, prefix='/song')

# Create tables only if a database is configured
if os.getenv('DATABASE_URL') or os.getenv('POSTGRES_URL'):
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Database initialization failed or skipped: {e}")
else:
    print("DATABASE_URL not set, skipping table creation.")

@app.get("/")
def hello():
    return {"message": "FastAPI on Vercel is live!"}
