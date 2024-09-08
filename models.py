from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Artists(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
  
class Records(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    title = Column(String)
    description = Column(String)
    year = Column(Integer)
    artistname = Column(String)
    worth = Column(String)
    damage = Column(String)
    serial_nr = Column(String)
    cover_image = Column(String)
  