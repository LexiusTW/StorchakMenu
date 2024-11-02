from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Wish(BaseModel):
    id: int
    wishName: str
    description: str
    price: int

