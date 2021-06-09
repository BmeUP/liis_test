from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Poll(Base):
    __tablename__ = 'polls'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    question = Column(String)
    variants = relationship("Variant", back_populates="poll")

    