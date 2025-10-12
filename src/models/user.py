from sqlalchemy import Integer , String , Float ,Column , DateTime , Boolean , ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.db.session import Base

class User(Base):

    __tablename__="users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50),unique=False,nullable=False)
    email = Column(String(60),unique=True,nullable=False)
    password = Column(string(255),nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    gender = Column(String(10))
    activity_level = Column(String(20))
    goal = Column(String(20))