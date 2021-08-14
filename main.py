from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def index():
    return {"Hello": "World"}


@app.get("/items/")
async def items(wow: int = 0, limit: int = 10):
    # http://localhost:8000/items/?wow=4&limit=20
    return {wow: limit}  # This line would give {"4" : 20} response based on that query parameter


@app.get("/items/a")
async def items(wow: Optional[str] = None):
    # http://localhost:8000/items/a?wow
    return {wow}  # This would give nothing because wow is now optional
