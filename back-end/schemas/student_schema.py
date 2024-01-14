from pydantic import BaseModel

class StudentBase(BaseModel):
    name : str
    grade : str
    section : str
    gender : str

class StudentIn(StudentBase):
    pass 

class StudentOut(StudentBase):
    pass 

class StudentDB(StudentBase):
    id : int