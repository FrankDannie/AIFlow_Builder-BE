from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.session import SessionLocal
from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import Token
from app.services import auth as auth_service

router = APIRouter(prefix="/api/v1", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register_user(db, user)

@router.post("/auth/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = auth_service.authenticate_user(db, form_data.username, form_data.password)
    token = auth_service.create_access_token(data={"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
