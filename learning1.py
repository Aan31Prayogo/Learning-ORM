from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#buat class template dari baseClase
Base = declarative_base()

#buat class yang nanti dijadikan template untuk buat tabel
class MasterDataStudents(Base):
    __tablename__ = "MasterDataStudents"
    
    #buat column
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    class_name = Column(String)
    
    def __repr___(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
    
    def dict_format(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'class_name' : self.class_name
        }

    
class ClassA1(Base):
    __tablename__ = "ClassA1"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    class_name = Column(String)
    
DB = 'sqlite:///learning.db'
engine = create_engine(DB, echo = True)
# print(engine)

#buat table di daatabase
Base.metadata.create_all(engine)

#buat session untuk koneksi ke database
Session = sessionmaker(bind= engine)
session = Session()


#create User
new_user = MasterDataStudents(id="3110161054", name="Yulian SUrya PRayogo", class_name="Mekatronika")
session.add(new_user)
session.commit()

