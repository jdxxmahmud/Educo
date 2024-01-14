from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.book_schema import *
from models import book_model

from db.config import engine, get_db
from services.book_service import *

book_model.Base.metadata.create_all(bind = engine)

router = APIRouter(
    prefix ='/books', 
    tags =['/books'], 
    responses = {404: {'description' : 'Not found'}}
)


#CREATE  books
@router.post('/add-book')
def create_book(book: BookIn, db: Session = Depends(get_db)):
    return add_books(db, book)

#READ books
@router.get('/read-books')
def read_all_books(db: Session = Depends(get_db)):
    return read_books(db)

#UPDATE books
@router.put('/{book_id}')
def edit_book(book_id: int, updated_book: BookIn, db: Session = Depends(get_db)):
    return update_book(book_id, updated_book, db)

#DELETE books
@router.delete("/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    return delete_book(book_id, db)