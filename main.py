from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Wish(BaseModel):
    id: int
    wishName: str
    description: str
    price: int


wishRepo = [Wish(id = 1, wishName = "Карбонара", description = "Сливочные спагетти с хрустящим беконом под сыром моцарелла", price = 299)]


@app.get("/")
def get_menu():
    return wishRepo