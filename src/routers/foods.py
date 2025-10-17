from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from src.schemas import food_dto
from src.db.session import get_db
from src.services import foods_services
from typing import List

router = APIRouter(prefix="/foods",tags=["foods"])

@router.post("/",response_model=food_dto.Food)
def create_food(food:food_dto.FoodCreate , db:Session=Depends(get_db)):
    return foods_services.create_food(db,food)


@router.get("/",response_model=List[food_dto.Food])
def list_foods(db:Session = Depends(get_db)):
    return foods_services.list_foods(db)