from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.config.db import Base


class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True, index=True)

    round_number = Column(Integer, nullable=False)
    question = Column(Text, nullable=False)
    status = Column(String(20), default="pending")  # pending, active, finished

    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

  
    room = relationship("Room", back_populates="rounds")

    def __repr__(self):
        return f"<Round id={self.id} number={self.round_number} room_id={self.room_id}>"