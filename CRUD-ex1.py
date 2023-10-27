# Python program to show working with crud operations in FastAPI
# We shall use a Python list an in-memory database

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = []


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str


@app.post("/book")
async def add_book(book: Book):
    data.append(book.model_dump())
    return data


@app.get("/all")
async def get_all_books():
    return data


@app.get("/book/{id}")
async def get_one_book(id):
    for val in data:
        if val['id'] == int(id):
            return val


@app.put("/book/{id}")
async def update_one_book(id, book: Book):
    for count, val in enumerate(data):
        if val['id'] == int(id):
            data[count] = book.model_dump()  # Convert pydantic object to dict
            return data[count]


@app.delete("/book/{id}")
async def delete_one_book(id):
    for count, val in enumerate(data):
        if val['id'] == int(id):
            del (data[count])
            return data
