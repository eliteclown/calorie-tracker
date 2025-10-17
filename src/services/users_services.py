from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.models.user import User
from src.schemas import user_dto
from src.db.session import get_db
from src.security.auth import get_password_hash , verify_password , create_access_token

def register(user:user_dto.UserCreate , db:Session):

    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400 , detail = "email already registered")
    hashed_pw = get_password_hash(user.password)
    new_user = User(
        username = user.username,
        email = user.email,
        password = hashed_pw,
        age = user.age,
        height = user.height,
        weight = user.weight,
        gender = user.gender,
        activity_level = user.activity_level,
        goal = user.goal
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(form_data:OAuth2PasswordRequestForm , db:Session):
    user = db.query(User).filter(User.email==form_data.username).first()
    if not user or not verify_password(form_data.password , user.password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = "Incorrect email or password")
    token = create_access_token({"sub":str(user.id)})
    return {"access_token":token , "token_type":"bearer"}