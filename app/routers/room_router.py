from fastapi import APIRouter, Depends, status
from app.serviece.room_serviec import roomcreate,join_room
from app.dependences.db_dependences import get_db
from sqlalchemy.orm import Session


room_router=APIRouter(prefix='/room')

@room_router.post('/createroom', status_code=status.HTTP_200_OK)
def roomcreate_router(name:str,db:Session=Depends(get_db)):
    return  roomcreate(name,db)

@room_router.post("/join/{code}",status_code=status.HTTP_200_OK)
def joinroom_router(code:str,name:str,db:Session=Depends(get_db)):
    return join_room(code,name,db)

