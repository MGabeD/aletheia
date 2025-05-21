from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from aletheia.backend.models.base import Base

if TYPE_CHECKING:  
    from aletheia.backend.models.users import User
    from aletheia.backend.models.resume import Resume
    from aletheia.backend.models.linkedin_snapshot import LinkedInSnapshot


class Interview(Base):
    __tablename__ = "interview"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE", name="fk_interview_user_id")
    )
    resume_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("resume.id", ondelete="CASCADE", name="fk_interview_resume_id")
    )
    linkedin_snapshot_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("linkedin_snapshot.id", ondelete="CASCADE", name="fk_interview_linkedin_snapshot_id")
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    summary_data: Mapped[dict] = mapped_column(JSONB)

    # relationships ------------------------------------------------------------
    user: Mapped["User"] = relationship("User", back_populates="interviews", foreign_keys="[Interview.user_id]")
    resume: Mapped["Resume"] = relationship("Resume", back_populates="interviews", foreign_keys="[Interview.resume_id]")
    linkedin_snapshot: Mapped["LinkedInSnapshot"] = relationship(
        "LinkedInSnapshot", back_populates="interviews", foreign_keys="[Interview.linkedin_snapshot_id]"
    )
