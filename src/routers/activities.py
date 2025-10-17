from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import activity_dto
from src.models.user import User
from src.services import activities_services
from src.db.session import get_db
from src.security.auth import get_current_user

router = APIRouter(prefix="/activities",tags=["Actvities"])

@router.post("/",response_model = activity_dto.Activity)
def create_activity(activity:activity_dto.ActivityCreate , db:Session = Depends(get_db),current_user:User = Depends(get_current_user)):
    return activities_services.create_activity(db,current_user.id , activity)


@router.get("/",response_model=List[activity_dto.Activity])
def list_my_activities(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return activities_services.get_activities_for_user(db,current_user.id)