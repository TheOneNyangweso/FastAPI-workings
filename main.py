from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hi There"}


# Using variable param in path i.e path parameter
# and then passing it to path operation func as a formal param
@app.get("/hello/{name}/{age}")
async def hello(name: str, age: int):
    return {"Hello": name, "age": age}


# Using query parameter now...
@app.get("/hello")
async def hello(name: str, age: int):
    return {"Hello": name, "age": age}


# COmbining path and query parameter now...
@app.get("/hello/{name}")
async def hello(name: str, age: int):
    return {"Hello": name, "age": age}
