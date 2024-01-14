from sqlalchemy import Column, String, INTEGER
from db.config import Base

class Student(Base):

    __tablename__ = 'students'

    id = Column(INTEGER, primary_key = True, index = True)
    name = Column(String)
    grade = Column(String)
    section = Column(String)
    gender = Column(String)
    