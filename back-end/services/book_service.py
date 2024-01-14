from sqlalchemy.orm import Session 
from fastapi import HTTPException

from models.book_model import Book
from schemas.book_schema import *

#CREATE  books - POST OPERATION
def add_books(db: Session, book: BookIn):
    new_book = Book(
        genre = book.genre, 
        name = book.name, 
        publish_date = book.publish_date, 
        price =  book.price
        )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

#READ books - GET OPERATION
def read_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()

#UPDATE books - PUT OPERATION
def update_book(book_id: int, updated_book: BookIn, db: Session):
    with db:
        db_book = db.get(Book, book_id)

        for attribute in vars(updated_book):
            setattr(db_book, attribute, getattr(updated_book, attribute))

        db.add(db_book)
        db.commit()
        db.refresh(db_book)

        return db_book

#DELETE books - DELETE  OPERATION
def delete_book(book_id: int, db: Session):
    with db:
        book = db.query(Book).filter(Book.id == book_id).first()
        
        db.delete(book)
        db.commit()

        return book 