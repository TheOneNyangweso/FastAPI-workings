from fastapi import FastAPI
from typing import Tuple
from pydantic import BaseModel

app = FastAPI()


class Supplier(BaseModel):
    supplier_ID: int
    supplier_name: str


class Product(BaseModel):
    product_ID: int
    product_name: str
    price: float
    supplier: Supplier


class Customer(BaseModel):
    cust_ID: int
    cust_name: str
    product: Tuple[Product]


@app.post('/invoice/')
async def get_invoice(c1: Customer):
    return c1
