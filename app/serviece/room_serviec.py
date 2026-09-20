from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from app.model.room_modle import Room
from app.model.player_model import Player
import uuid
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
       return code
        
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

     return player
     

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