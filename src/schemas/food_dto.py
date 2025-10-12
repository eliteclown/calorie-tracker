from pydantic import BaseModel


class FoodBase(BaseModel):
    name:str
    calories:float
    protein:float
    carbs:float
    fat:float

class FoodCreate(FoodBase):
    pass


class Food(FoodBase):
    id:int
    class Config:
        orm_mode=True

#tells pydantic to treat ORM objects (like SQLAlchemy models) as dictionaries
#This allows Fastapi to convert Sqlalchemy models to pydantic models seamlessly
