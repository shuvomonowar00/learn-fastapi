from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# autocommit=False -> We want to manually say when a transaction is done.
# autoflush=False -> Prevent SQLAlchemy from automatically sending data before commit

Base = declarative_base()

# DB dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()