from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    sub:int
    exp:Optional[datetime] = None


class UserLogin(BaseModel):
    email:str
    password:str