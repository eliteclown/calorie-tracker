from pydantic import BaseModel
from typing import List,Optional
from datetime import date, datetime

class UserBase(BaseModel):
    username:str
    email:str

class UserCreate(UserBase):
    password:str
    age:int
    height:float
    weight:float
    gender:str
    activity_level:str
    goal:str

class User(UserBase):
    id:int
    age:int
    height:float
    weight:float
    gender:str
    activity_level:str
    goal:str
    class Config:
        orm_mode=True