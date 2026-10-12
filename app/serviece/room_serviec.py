from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.model.room_modle import Room
from app.model.player_model import Player
from app.model.round_model import Round
from app.dto.inputs import User
import random
import string
import logging

logger=logging.getLogger(__name__)



def generate_room_code(length: int = 6):
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choices(characters, k=length))

def roomcreate(name:str,db:Session):
     try:
       code=generate_room_code()

        
       room = Room(
            code=code,
            name=name
        )

       db.add(room)
       db.commit()
       db.refresh(room)
       return {"status":200,
               "code":code}
        
     except HTTPException:
        raise    

     except Exception as e:
        db.rollback()
        logger.error(" error for api rooms: %s", e, exc_info=True) 
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail={
            "success": False,
            "error": "SERVER_ERROR",
            "message": "Server failure"
        }
    )


def join_room(code:str,name:str,db:Session):
   try:
     room = db.query(Room).filter(Room.code == code).first()
     if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )
     player = Player(
        name=name,
        room_id=room.id,
        is_host=False,
        is_connected=True
    )

     db.add(player)
     db.commit()
     db.refresh(player)

     return {"status":200,
               "player":player}
     

   except HTTPException:
        raise
   except Exception as e:
           db.rollback()
           logger.error(" error for api join rooms: %s", e, exc_info=True) 
           raise HTTPException(
           status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
           detail={
               "success": False,
               "error": "SERVER_ERROR",
               "message": "Server failure"
           }
       )


def question_service(code:str,db:Session):
    try:
      room=db.query(Room).filter(Room.code==code).first()
      if not room:
              raise HTTPException(
                  status_code=404,
                  detail="Room not found"
              )
      round=db.query(Round).filter(Round.room_id==room.id).first()

      return{
          "status":200,
          "data":{"id":round.id,
                  "question":round.question}
      }
    except HTTPException:
        raise
    except Exception as e:
              
               logger.error(" error for api question get: %s", e, exc_info=True) 
               raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail={
                   "success": False,
                   "error": "SERVER_ERROR",
                   "message": "Server failure"
               }
           )


    
def inputquestion_service(code:str,user:User,db:Session):
    try:
        room=db.query(Room).filter(Room.code==code).first()
        if not room:
                      raise HTTPException(
                          status_code=404,
                          detail="Room not found")
       

        round=Round(
              
               question=user.question,
               room_id=room.id
             
        )

        db.add(round)
        db.commit()
        db.refresh(round)
        return {
             "status_code":200,
             "message":"question inputed"
        }

       


    except HTTPException:
            raise
    except Exception as e:
               db.rollback()
               logger.error(" error for api question input: %s", e, exc_info=True) 
               raise HTTPException(
               status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail={
                   "success": False,
                   "error": "SERVER_ERROR",
                   "message": "Server failure"
               }
           )
    