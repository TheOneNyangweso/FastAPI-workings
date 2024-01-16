# web.py defines FastAPI web endpoint(s) that returns the fake data
from model import Creature
from fastapi import FastAPI

app = FastAPI()


@app.get('/creature')
async def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()
