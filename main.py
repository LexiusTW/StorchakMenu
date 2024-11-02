from typing import Annotated
from fastapi import FastAPI, Form, HTTPException
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

@app.put("/")
def update_wish(wish: Annotated[Wish, Form()]):
    for ws in wishRepo:
        if ws.id == wish.id:
            ws.wishName = wish.wishName
            ws.description = wish.description
            ws.price = wish.price
        return "Данные успешно обновлены =)"
    raise HTTPException(status_code=404, detail="wish not found")

@app.delete("/")
def delete_wish(id: int):
    for ws in wishRepo:
        if id == ws.id:
            wishRepo.remove(ws)
        return "Блюдо успешно удалено =)"
    raise HTTPException(status_code = 404, detail = "wish not found")