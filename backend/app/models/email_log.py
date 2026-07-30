from datetime import datetime
from sqlalchemy import Enum

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.enums import EmailStatus


class EmailLog(Base):
    __tablename__ = "email_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[EmailStatus] = mapped_column(Enum(EmailStatus), nullable=False)
    sent_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)