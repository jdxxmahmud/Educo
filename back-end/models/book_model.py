from sqlalchemy import Column, INTEGER, String
from db.config import Base

class Book(Base):
    
    __tablename__ = 'books'
    
    id = Column(INTEGER, primary_key = True, index = True)
    genre = Column(String)
    name = Column(String)
    publish_date = Column(String)
    price = Column(INTEGER)
    
    
    

