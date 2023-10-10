from fastapi import FastAPI, Path, Query

app = FastAPI()


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
