# Python program to show working with crud operations in FastAPI
# We shall now use a database dialect as database, instead of built in List
from typing import List
from fastapi import FastAPI, Depends
from pydantic import BaseModel, constr
from sqlalchemy import create_engine
from sqlalchemy.dialects import sqlite
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

DB_URL = "sqlite:///./test.db"
engine = create_engine(url=DB_URL, connect_args={"check_same_thread": False})
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


app = FastAPI()


class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    author = Column(String(50))
    publisher = Column(String(50))


Base.metadata.create_all(bind=engine)


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str

    class Config:
        # Note the use of orm_mode=True in the config class
        # indicating that it ismapped with the ORM class of SQLAlchemy
        orm_mode = True


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.post("/add_book", response_model=Book)
async def add_book(book: Book, db: Session = Depends(get_db)):
    bk = Books(id=book.id, title=book.title,
               author=book.title, publisher=book.publisher)

    db.add(bk)
    db.commit()
    db.refresh(bk)

    return Books(**book.model_dump())


@app.get("/all", response_model=List[Book])
async def get_all_books(db: Session = Depends(get_db)):
    recs = db.query(Books).all()

    return recs


@app.get("/book/{id}", response_model=Book)
async def get_one_book(id, db: Session = Depends(get_db)):
    rec = db.query(Books).filter(Books.id == id).first()


@app.put("/update/{id}", response_model=Book)
async def update_one_book(id : int, book: Book, db : Session = Depends(get_db)):
    b1  = db.query(Books).filter(Books.id == id).first()
    b1.id = book.id
    b1.title = book.title
    b1.author = book.author
    b1.publisher = book.publisher
    
    db.commit()
    
    return db.query(Books).filter(Books.id == id).first()


@app.delete("/book/{id}")
async def delete_one_book(id : int, db : Session = Depends(get_db)):
    try:
        db.query(Books).filter(Books.id == id).delete()
        db.commit()
        
    except Exception as e:
        raise Exception(e)
    
    return {"delete status" : "success"}