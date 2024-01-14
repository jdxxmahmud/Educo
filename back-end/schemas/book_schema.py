from pydantic import BaseModel

class BookBase(BaseModel):
    genre : str
    name : str 
    publish_date : str
    price : int

class BookIn(BookBase):
    pass

class BookOut(BookBase):
    pass 

class BookDB(BookBase):
    id : int 