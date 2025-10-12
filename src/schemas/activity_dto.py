from pydantic import BaseModel
from datetime import datetime

class ActivityBase(BaseModel):
    name:str
    activity_time:datetime
    calories_burned:float



class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id:int
    class Config:
        orm_mode=True

