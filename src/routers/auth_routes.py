from fastapi import Depends,APIRouter,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.services import users_services
from src.models.user import User
from src.schemas import user_dto , auth_dto
from src.db.session import get_db
from src.security.auth import get_password_hash,verify_password,create_access_token

router = APIRouter(prefix="/auth",tags=["authentication"])




@router.post("/register",response_model=user_dto.User)
def register(user:user_dto.UserCreate , db:Session=Depends(get_db)):
    new_user = users_services.register(user,db)
    return new_user


@router.post("/login", response_model=auth_dto.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return users_services.login(form_data, db)