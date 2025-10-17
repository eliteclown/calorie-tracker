from sqlalchemy import Integer,String,Float,ForeignKey,Column,DateTime
from sqlalchemy.orm import relationship
from src.db.session import Base
from datetime import datetime,date

class Activity(Base):
    __tablename__="activities"

    id = Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    name=Column(String(50),nullable=False)
    calories_burned=Column(Float,nullable=False)
    activity_time=Column(DateTime,default=datetime.ctime)

    user = relationship("User",back_populates="activities")