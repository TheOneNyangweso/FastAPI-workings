from fastapi import FastAPI, Depends, HTTPException, params
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


def user_dep(name: str, pwd: str):  # -> dict[str, Any]:
    return {'name': name, 'valid': True}


@app.get('/new-user')
async def new_user(user: dict = Depends(user_dep)):  # -> dict[Any, Any]:
    return user


@app.get("/existing-user/")
async def existing_user(dep: Dependency = Depends(Dependency)) -> Dependency:
    return dep


@app.get("/admin/")
async def admin(dep: Dependency = Depends(Dependency)) -> Dependency:
    return dep


@app.get("/validate/", dependencies=[Depends(validate)])
def validate_user_age() -> dict[str, str]:
    return {"message": "You are eligible"}

# If you use a function to manage our dependencies instead of a class,
# The type of parameter in the user defined operation func will be a dict,
# and the param insiede of Depends class will be the name of the func managing the dependencies e.g

# @app.get("/user/")
# async def user(dep: dict = Depends(dependency)):
#    return dep
