from database.database import get_db
from models.model import Users
from sqlalchemy.orm import Session


def get_user(db:Session, user_name:str):
    return db.query(Users).filter_by(name = user_name).all()

def create_user(db: Session, user_data: dict):
    new_user = Users(name = user_data['name'], age=user_data['age'], phone_number = user_data['phone_number'])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)