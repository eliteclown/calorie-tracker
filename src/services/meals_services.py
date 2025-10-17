from sqlalchemy.orm import Session
from src.models.food import Food
from src.models.meal import Meal 
from src.models.meal_item import MealItem 
from src.schemas import meal_dto

def create_meal(db:Session , user_id:int , meal:meal_dto.MealCreate):

    db_meal = Meal(
        user_id=user_id,
        log_date= meal.log_date,
        meal_type = meal.meal_type
    )


    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)

    for item in meal.items:
        food = db.query(Food).get(item.food_id)
        factor = item.quantity/100.0
        db_item = MealItem(
            meal_id = db_meal.id,
            food_id = item.food_id,
            quantity = item.quantity,
            calories = food.calories * factor,
            protein = food.protein * factor,
            carbs = food.carbs * factor,
            fat = food.fat * factor
        )

        db.add(db_item)
    db.commit()
    db.refresh(db_meal)
    return db_meal



def list_user_meals(db:Session,user_id:int):
    return db.query(Meal).filter(Meal.user_id == user_id).all()