from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException

from app.core.config import settings
from app.schemas.user import UserCreate
from app.schemas.auth import Token

# In-memory fake DB (replace with real DB or CRUD later)
fake_users_db = {}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(email: str) -> Optional[dict]:
    return fake_users_db.get(email)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def register_user(user: UserCreate) -> dict:
    if get_user(user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)
    fake_users_db[user.email] = {
        "email": user.email,
        "hashed_password": hashed_password
    }

    return {"email": user.email}


def authenticate_user(email: str, password: str) -> str:
    user = get_user(email)
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return create_access_token(data={"sub": user["email"]})
