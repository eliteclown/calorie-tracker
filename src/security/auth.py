from datetime import datetime , timedelta
from typing import Optional

from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError ,jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.models.user import User
from app.schemas import user_dto
from src.db.session import get_db
from src.db.session import settings

SECRET_KEY=settings.JWT_SECRET
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE = settings.ACCESS_TOKEN_EXPIRE_MINUTES


pwd_context = CryptContext(schemas=["bcrypt"],deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def verify_password(plain_password , hashed_passowrd):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(passwordre)