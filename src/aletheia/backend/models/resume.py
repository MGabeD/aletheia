# resume.py
from __future__ import annotations
import datetime as _dt
import uuid
from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from aletheia.backend.models.base import Base

if TYPE_CHECKING:  
    from aletheia.backend.models.users import User
    from aletheia.backend.models.interview import Interview


class Resume(Base):
    """Uploaded resumes belonging to users."""

    __tablename__ = "resume"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE", name="fk_resume_user_id")
    )

    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(String(512))
    uploaded_at: Mapped[_dt.datetime] = mapped_column(
        default=lambda: _dt.datetime.now(_dt.timezone.utc)
    )
    archived: Mapped[bool] = mapped_column(Boolean, default=False)

    # relationships ------------------------------------------------------------
    user: Mapped["User"] = relationship(
        "User", 
        back_populates="resumes", 
        foreign_keys="[Resume.user_id]",
        lazy="joined"
        )

    interviews: Mapped[List["Interview"]] = relationship(
        "Interview", 
        back_populates="resume",
        foreign_keys="[Interview.resume_id]"
    )
