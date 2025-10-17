from pydantic import BaseModel
from typing import List
from datetime import date
from src.schemas.meal_item_dto import MealItemCreate,MealItem

class MealBase(BaseModel):
    log_date:date
    meal_type:str

class MealCreate(MealBase):
    items:List[MealItemCreate]


class Meal(MealBase):
    id:int
    items:List[MealItem]
    class Config:
        orm_mode=True