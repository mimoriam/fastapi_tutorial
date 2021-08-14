from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


class Item(BaseModel):
    name: str
    description: Optional[str] = None


@app.post("/items/{id}/")
# http://localhost:8000/items/2/?query=hello
# async def create_item2(id: int, item: Item, query: Optional[str] = Query(None, max_length=25)):
# This is only for optional parameters. What if we want required ones for the query but also validation? Simple:
async def create_item2(id: int, item: Item, query: str = Query(..., max_length=25)):
    # Now query is required and ENFORCED to be of max_length = 25
    return {
        "id": id,
        "item": item
    }

# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
# This goes waaaaay into detail but not doing most of the code here so check it out ^^
