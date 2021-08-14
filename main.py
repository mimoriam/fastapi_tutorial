from fastapi import FastAPI, Path, Query, Body
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None, max_length=255)


@app.post("/items/{id}/")
# http://localhost:8000/items/2/?query=Hello
# Note that Path(), Body()/Field() & Query() have the same optional parameters
async def create_item(
        id: int = Path(..., lt=3, gt=0, title="Id of item"),
        item: Item = Body(...),
        query: str = Query(..., max_length=25)):
    return {
        "id": id,
        "item": item
    }

# https://fastapi.tiangolo.com/tutorial/body-fields/
# Body validation using Fields() ^^
