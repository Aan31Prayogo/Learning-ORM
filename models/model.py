from pydantic import BaseModel
from typing import Optional, Any, List, Dict, Union
from database.database import Base
from sqlalchemy import Column, Integer, String

class RequestModel(BaseModel):
    name : str
    age : int
    phone_number : str
    
class ResponseModel(BaseModel):
    status : bool
    data: Union[List[Dict[str, Any]], Any]
    
class Users(Base):
    __tablename__ = "Users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String(100))
    phone_number = Column(String(20))
    age = Column(Integer)
    
    def dict_format(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}
    