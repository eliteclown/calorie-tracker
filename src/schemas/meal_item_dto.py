from pydantic import BaseModel

class MealItembase(BaseModel):
    food_id:int
    quantity:float

class MealItemCreate(MealItemBase):
    pass

class MealItem(MealItemBase):
    id:int
    calories:float
    protein:float
    carbs:float
    fat:float
    class Config:
        orm_mode=True