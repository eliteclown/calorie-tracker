from fastapi import APIRouter , Depends ,HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.models.user import User
from src.schemas import meal_dto
from src.services import meals_services
from src.db.session import get_db
from src.security.auth import get_current_user

router = APIRouter(prefix="/meals",tags=["meals"])



@router.post("/",response_model=meal_dto.Meal)
def create_meal(meal:meal_dto.MealCreate , db:Session=Depends(get_db) , current_user:User = Depends(get_current_user)):
    if not meal.items:
        raise HTTPException(status_code=400,detail="Meal must contain at least one item")
    return meals_services.create_meal(db,current_user.id,meal)

@router.get("/",response_model=List[meal_dto.Meal])
def list_meals(db:Session=Depends(get_db),current_user:User = Depends(get_current_user)):
    return meals_services.list_user_meals(db , current_user.id)