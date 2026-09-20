from fastapi import FastAPI

from app.config.db import Base, engine
from app.config.settings import settings

from app.model.room_modle import Room
from app.model.player_model import Player
from app.model.round_model import Round

from app.routers.room_router import room_router

app = FastAPI()

app.include_router(room_router)