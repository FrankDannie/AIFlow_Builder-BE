from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserOut
from app.schemas.auth import Token
from app.services import auth as auth_service

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate):
    return auth_service.register_user(user)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = auth_service.authenticate_user(
        email=form_data.username,
        password=form_data.password
    )
    return {"access_token": token, "token_type": "bearer"}
