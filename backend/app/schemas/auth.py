from pydantic import BaseModel, EmailStr, Field
from datetime import time


class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
    interests: list[str]
    custom_sources: list[str] = []
    email_delivery_time: time


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    interests: list[str]
    custom_sources: list[str]
    email_delivery_time: time
    is_subscribed: bool

    model_config = {
        "from_attributes": True
    }