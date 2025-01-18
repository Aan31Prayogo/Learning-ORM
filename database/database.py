from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base


DB = 'sqlite:///learning.db'
engine = create_engine(DB, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def check_table():
    table_exist = inspect(engine).has_table("Users")
    if not table_exist:
        Base.metadata.create_all(engine)
    else:
        print("table users already exists")