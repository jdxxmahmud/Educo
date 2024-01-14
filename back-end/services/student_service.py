from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.student_model import Student
from schemas.student_schema import *

#CREATE students - POST OPERATION
def add_students(db: Session, student: StudentIn):
    new_student = Student(
        name = student.name,
        grade = student.grade,
        section = student.section, 
        gender = student.gender
        )
    
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
#READ students - GET OPERATION
def read_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

#UPDATE students - PUT OPERATION
def update_student(student_id: int, updated_student: StudentIn, db: Session):
    with db:
        db_student = db.get(Student, student_id)

        for attribute in vars(updated_student):
            setattr(db_student, attribute, getattr(updated_student, attribute))

        db.add(db_student)
        db.commit()
        db.refresh(db_student)

        return db_student
#DELETE students - DELETE OPERATION 
def delete_student(student_id: int, db: Session):
    with db:
        student = db.query(Student).filter(Student.id == student_id).first()

        db.delete(student)
        db.commit()

        return student