from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse

app = FastAPI()
# Creating a class to manage our dependencies


class Dependency:
    def __init__(self, id: str, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age

# You can use a function as an alternative
# async def dependency(id : str, name: str, age: int):
#    return {"id": id, "name": name, "age": age}


async def validate(dep: Dependency = Depends(Dependency)):
    if dep.age < 18:
        raise HTTPException(status_code=400, detail="You aren't eligible")


@app.get("/user/")
async def user(dep: Dependency = Depends(Dependency)):
    return dep


@app.get("/admin/")
async def admin(dep: Dependency = Depends(Dependency)):
    return dep


@app.get("/validate/", dependencies=[Depends(validate)])
def validate_user_age():
    return {"message": "You are eligible"}

# If you use a function to manage our dependencies instead of a class,
# The type of parameter in the user defined operation func will be a dict,
# and the param insiede of Depends class will be the name of the func managing the dependencies e.g

# @app.get("/user/")
# async def user(dep: dict = Depends(dependency)):
#    return dep
