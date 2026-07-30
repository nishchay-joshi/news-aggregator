from datetime import datetime
from sqlalchemy import Enum

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.enums import ContentType


class Content(Base):
    __tablename__ = "content"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    image_url: Mapped[str | None] = mapped_column(String)
    source_name: Mapped[str] = mapped_column(String(100), nullable=False)
    content_type: Mapped[ContentType] = mapped_column(Enum(ContentType), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)