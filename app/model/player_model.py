from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.config.db import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(50), nullable=False)
    is_host = Column(Boolean, default=False)
    is_connected = Column(Boolean, default=True)

    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

  
    room = relationship("Room", back_populates="players")
    
    def __repr__(self):
        return f"<Player id={self.id} name={self.name} room_id={self.room_id}>"