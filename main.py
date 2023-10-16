from fastapi import FastAPI, Request, Path, Query, Body, Form, UploadFile, File, Cookie
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import shutil
from typing import List
from pydantic import BaseModel, Field
import aiofiles

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str = Field(None, title="Name of Student", max_length=10)
    subjects: List[str] = []


class UserDetails(BaseModel):
    name: str
    password: str
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


templates = Jinja2Templates(
    directory="/home/nyangweso/Desktop/Ds_1/FastAPI-workings/Templates"
)
app.mount(
    path="/home/nyangweso/Desktop/Ds_1/FastAPI-workings/Static",
    app=StaticFiles(
        directory="/home/nyangweso/Desktop/Ds_1/FastAPI-workings/Static"),
    name="Static",  # name which will be used in the 'url_for' param in html file
)


# Rendering HTML response instead of JSON
# It also shows us how to use the Request object directly i.e (no need to pass it as a query or path param)
@app.get("/Greetings/{name}", response_class=HTMLResponse)
async def greet_the_world(request: Request, name: str = Path(min_length=1)):
    return templates.TemplateResponse(
        name="hello.html", context={"request": request, "name": name}
    )

# Functions to render login.html
# and access the html form data


@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/submit/")
async def submit(name: str = Form(...), pwd: str = Form(...)):
    return UserDetails(name=name, password=pwd)

# To render upload.html to client
@app.get("/upload/", response_class=HTMLResponse)
async def upload_file(request: Request):
    return templates.TemplateResponse("upload.html", {"request":request})

# To handle the upload operation to server
@app.post("/uploader"/)
async def create_upload_file(file: UploadFile = File(...)):
    with open("destination.png", "wb") as buffer: # Using any other name apart from destination.png brings up errors
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename}

@app.post("/cookie/")
def create_cookie():
    content = {"message":"cookie set"}
    response = JSONResponse(content = content)
    # Setting the cookie parameter on the response object
    response.set_cookie(key = "username", value="admin")
    
    return response

# Reading the cookie object on the subsequent visits
@app.get("/readcookie/")
async def read_cookie(username: str = Cookie(None)):
    return {"username": username}