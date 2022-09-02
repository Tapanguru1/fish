from sqlalchemy import Column,Integer, String, Float
from .database import Base
class Fish(Base):
    __tablename__='fish_table'
    Id=Column(Integer,primary_key=True,index=True)
    Species=Column(String(20))
    Weight=Column(Float)
    Length1=Column(Float)
    Length2=Column(Float)
    Length3=Column(Float)
    Height=Column(Float)
    Width=Column(Float)
