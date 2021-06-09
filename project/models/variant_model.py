from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .poll_model import Poll

class Variant(Base):
    __tablename__ = 'variants'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship("Poll", back_populates="variants")
