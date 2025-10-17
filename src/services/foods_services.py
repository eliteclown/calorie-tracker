from sqlalchemy.orm import Session
from src.models.food import Food
from src.schemas import food_dto

def create_food(db:Session , food_input:food_dto.FoodCreate):
    db_food = Food(**food_input.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food




def list_foods(db:Session):
    return db.query(Food).all()