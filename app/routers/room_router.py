from fastapi import APIRouter, Depends, status
from app.serviece.room_serviec import roomcreate,join_room,question_service,inputquestion_service
from app.dependences.db_dependences import get_db
from sqlalchemy.orm import Session
from app.dto.inputs import User,Answer


room_router=APIRouter(prefix='/room')

@room_router.post('/createroom', status_code=status.HTTP_200_OK)
def roomcreate_router(name:str,db:Session=Depends(get_db)):
    return  roomcreate(name,db)

@room_router.post("/join/{code}",status_code=status.HTTP_200_OK)
def joinroom_router(code:str,name:str,db:Session=Depends(get_db)):
    return join_room(code,name,db)

@room_router.get("{code}/question",status_code=status.HTTP_200_OK)
def getquestion_router(code:str,db:Session=Depends(get_db)):
    return question_service (code,db) 

@room_router.post("{code}/inputquestion",status_code=status.HTTP_200_OK)
def inputquestion_router(code:str,user:User,db:Session=Depends(get_db)):
    return inputquestion_service (code,user,db)

@room_router.post("{code}/{questionid}/answer",status_code=status.HTTP_200_OK)
def inputanswer_router(code:str,qid:str,user:Answer,db:Session=Depends(get_db)):
    return