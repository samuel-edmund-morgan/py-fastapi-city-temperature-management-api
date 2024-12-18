from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class DBCity(Base):
    __tablename__ = "City"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    additional_info = Column(String(512), index=True)
