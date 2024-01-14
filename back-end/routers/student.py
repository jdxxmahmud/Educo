from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session 
from schemas.student_schema import *
from models import student_model

from db.config import engine, get_db
from services.student_service import *

student_model.Base.metadata.create_all(bind = engine)

router = APIRouter(
    prefix = '/students', 
    tags =['/students'],
    responses = {404: {'description' : 'Not found'}} 
)

#CREATE students
@router.post('/add-student')
def create_student(student: StudentIn, db: Session = Depends(get_db)):
    return add_students(db, student)

#READ students
@router.get('/read-students')
def read_all_students(db: Session = Depends(get_db)):
    return read_students(db)

#UPDATE students
@router.put('/{student_id}')
def edit_student(student_id: int, updated_student: StudentIn, db: Session = Depends(get_db)):
    return update_student(student_id, updated_student, db)

#DELETE students
@router.delete('/{student_id}')
def remove_student(student_id: int, db: Session = Depends(get_db)):
    return delete_student(student_id, db)