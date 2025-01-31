from database.database import get_db
from models.model import Users
from sqlalchemy.orm import Session
import uuid

async def get_user(db:Session, user_name:str):
    users = db.query(Users).filter_by(name = user_name).all()
    if users:
        return [user.dict_format() for user in users]
    else:
        return False

async def create_user(db: Session, user_data: dict):
    try:
        new_user = Users(id= str(uuid.uuid4()), 
                         name = user_data['name'], 
                         age=user_data['age'], 
                         phone_number = user_data['phone_number'])
        db.add(new_user)
        db.commit()
        # db.refresh(new_user)
        return True
    except Exception as e:
        print(f"error with {e}")
        return False
        
async def update_user_by_name(db: Session, user_name:str, user_data: dict):
    try:
        user = db.query(Users).filter_by(name=user_name).first()
        if user:
            user.age = user_data['age']
            db.commit()
            return True
        else:
            return False
    except Exception as e:
        print(f"error with {e}")
        return False

async def delete_user_by_name(db: Session, user_name:str):
    try:
        user = db.query(Users).filter_by(name=user_name).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        else:
            return False
    
    except Exception as e:
        print(f"error with {e}")
        return False