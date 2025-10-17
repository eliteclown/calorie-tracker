from datetime import datetime , timedelta
from typing import Optional

from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError , jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.models.user import User
# Removed unused import to avoid linter errors
from src.db.session import get_db
from src.db.session import settings

SECRET_KEY=settings.JWT_SECRET
# Normalize and validate algorithm from settings; default to HS256 if blank/invalid
_alg = (settings.JWT_ALGORITHM or "").strip().upper()
_allowed_algs = {"HS256","HS384","HS512"}
ALGORITHM = _alg if _alg in _allowed_algs else "HS256"
ACCESS_TOKEN_EXPIRE = settings.ACCESS_TOKEN_EXPIRE_MINUTES


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE))
    to_encode.update({
        "exp":expire
    })
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="could not validate credentials",
                                          headers={"WWW-Authenticate":"Bearer"},
                                          )
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user