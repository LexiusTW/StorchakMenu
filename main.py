from typing import Annotated
from fastapi import FastAPI, Form
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

@app.post("/")
def add_wish(wish: Annotated[Wish, Form()]):
    wishRepo.append(wish)
    return "Данные успешно добавлены =)"