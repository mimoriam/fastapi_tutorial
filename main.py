from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None


@app.post('/')
async def create_item(item: Item):
    return {
        "item": item
    }


@app.post('/items/{id}/')
# http://localhost:8000/items/2/?query=hello
async def create_item2(id: int, item: Item, query: Optional[str] = None):
    return {
        "id": id,
        "item": item
    }
