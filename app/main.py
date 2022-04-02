from ensurepip import version
from turtle import title
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import characters, weapons


app = FastAPI(
    title="Starfinder API", description="An API for Starfinder data using FastAPI"
)

app.add_middleware(CORSMiddleware)
app.include_router(characters.router)
app.include_router(weapons.router)
