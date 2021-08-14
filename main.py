from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Model(str, Enum):
    abc = "abc"
    xyz = "xyz"


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/items/{model}")
async def items(model: Model):
    return {"model": model}
