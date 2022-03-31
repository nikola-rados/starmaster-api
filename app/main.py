from fastapi import FastAPI
from app.api import api

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Fast API in Python"}


@app.get("/characters")
async def read_characters():
    return api.read_characters()


@app.get("/character/{id}")
async def character_by_id(id: int):
    return api.read_character_by_id(id)


@app.put("/character/{id}/rest")
async def rest_character(id: int):
    return api.rest_character(id)