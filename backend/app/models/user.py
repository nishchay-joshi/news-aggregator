from sqlalchemy import Boolean, Integer, String, Time
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    interests: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False, default=list)
    custom_sources: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False, default=list)
    email_delivery_time: Mapped[Time] = mapped_column(Time, nullable=False)
    is_subscribed: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)