from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt import create_access_token
from app.database.session import get_db
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
)
from app.auth.dependencies import get_current_user
from app.schemas.auth import UserResponse
from app.models.user import User

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    stmt = select(User).where(User.email == request.email)
    existing_user = db.scalar(stmt)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered.",
        )

    user = User(
        name=request.name,
        email=request.email,
        password_hash=hash_password(request.password),
        interests=request.interests,
        custom_sources=request.custom_sources,
        email_delivery_time=request.email_delivery_time,
    )

    db.add(user)
    db.commit()
    db.refresh(user)


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db),
):
    stmt = select(User).where(User.email == request.email)
    user = db.scalar(stmt)

    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    access_token = create_access_token(
        {"sub": str(user.id)}
    )

    return TokenResponse(access_token=access_token)


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user