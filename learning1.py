from sqlalchemy import create_engine, Column, Integer, String, inspect
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


#inspect if engine already has a table 
table_exist = inspect(engine).has_table("MasterDataStudents")
if not table_exist:
    Base.metadata.create_all(engine)

# #buat session untuk koneksi ke database
Session = sessionmaker(bind= engine)
session = Session()


# create User
# new_user = MasterDataStudents(id="3110161054", name="Yulian SUrya PRayogo", class_name="Mekatronika")
# session.add(new_user)
# session.commit()

#making query
# master_data = session.query(MasterDataStudents).all()
# for data in master_data:
#     if data.id == '3110161054':
#         data.name = 'aan'
#         session.commit()
