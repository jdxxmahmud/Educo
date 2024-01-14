from fastapi import FastAPI
from routers import book, student

app = FastAPI()
app.include_router(book.router)
app.include_router(student.router)


@app.get('/')
def root_page():
    return {'message : Hello this is Educo'} 

