from fastapi import HTTPException
from sqlalchemy.orm import Session
from jose import jwt
from datetime import datetime, timedelta

from app.core.config import settings
from app.db.crud import user as user_crud
from app.schemas.user import UserCreate

def authenticate_user(db: Session, email: str, password: str):
    db_user = user_crud.get_user_by_email(db, email)
    if not db_user or not user_crud.verify_password(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return db_user

def register_user(db: Session, user: UserCreate):
    existing = user_crud.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return user_crud.create_user(db, user)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
