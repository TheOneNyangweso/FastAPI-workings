from fastapi import FastAPI, Path, Query, Body
import uvicorn
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(None, title="Name of Student", max_length=10)
    subjects: List[str] = []


# Populating request body using pydantic model object
@app.post("/students/{college}")
async def student_data(college: str, age: int, s1: Student):
    res = {"college": college, "age": age, **s1.model_dump()}
    return res


# You can also populate request body using Body class of fastapi
@app.post("/students/add/marks")
async def student_marks(name: str = Body(...), marks: float = Body(ge=0, le=100)):
    return {"name": name, "marks": marks}


@app.get("/")
async def index():
    return {"message": "Hi There"}


# Using variable param in path i.e path parameter while applying parameter validation
# and then passing it to path operation func as a formal param
@app.get("/hello/{name}/{age}")
async def hello(
    *,
    name: str = Path(..., min_length=3, max_length=10),
    age: int = Path(..., ge=1, le=100)
):
    return {"Hello": name, "age": age}


# Using query parameter now...
@app.get("/hello")
async def hello(name: str, age: int):
    return {"Hello": name, "age": age}


# Combining path and query parameter now, while applying query and also path parameters validation
@app.get("/hello/{name}")
async def hello(
    *,
    age: int,
    name: str = Path(..., min_length=3, max_length=10),
    percent: float = Query(..., ge=0, le=100)
):
    return {"Hello": name, "age": age, "percentage": percent}
