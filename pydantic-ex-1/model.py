# model.py defines a Pydantic model
from pydantic import BaseModel, constr, Field


class Creature(BaseModel):
    # name: constr(min_length=2)
    # the ellipsis (...) within name: str = Field(..., min_length=2) means 
    # that a value is required, and that there’s no default value.
    name: str = Field(..., min_length=2)
    description: str
    location: str
