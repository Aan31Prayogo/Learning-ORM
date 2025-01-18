from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#buat class template dari baseClase
Base = declarative_base()

#buat class yang nanti dijadikan template untuk buat tabel
class MasterDataStudents(Base):
    __tablename__ = "MasterDataStudents"
    
    #buat column
    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_number = Column(String)
    name = Column(String, nullable=False)
    class_name = Column(String)
    
    # def __repr___(self):
    #     return f"<User(id={self.id}, name={self.name}, email={self.email})>"
    
    def dict_format(self):
        return {column.name : getattr(self, column.name) for column in self.__table__.columns}
    
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
# new_user = MasterDataStudents(reg_number="3110161021", name="sasuke", class_name="Mekatronika")
# session.add(new_user)
# session.commit()

#making query
try:
    students = session.query(MasterDataStudents).filter_by(name='sasuke').all()
    students_dicts = [student.dict_format() for student in students]
    print(students_dicts)
except Exception as e:
    print(f"error with {e}")
    