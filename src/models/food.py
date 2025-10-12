from sqlalchemy import Integer,String,Float
from sqlalchemy.orm import relationship
from src.db.session import Base

class Food(Base):
    __tablename__="foods"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100),index=True)
    calories=Column(Float)
    protein=Column(Float)
    carbs=Column(Float)
    fat=Column(Float)