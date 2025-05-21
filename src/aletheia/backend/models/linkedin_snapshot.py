from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from aletheia.backend.models.base import Base

if TYPE_CHECKING:  
    from aletheia.backend.models.users import User
    from aletheia.backend.models.interview import Interview


class LinkedInSnapshot(Base):
    __tablename__ = "linkedin_snapshot"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE", name="fk_linkedin_snapshot_user_id")
    )
    profile_url: Mapped[str] = mapped_column(String(255))
    pulled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    profile_data: Mapped[dict] = mapped_column(JSONB)

    # relationships ------------------------------------------------------------
    user: Mapped["User"] = relationship(
        "User", 
        back_populates="linkedin_snapshots", 
        foreign_keys="[LinkedInSnapshot.user_id]"
    )
    interviews: Mapped[List["Interview"]] = relationship(
        "Interview", 
        back_populates="linkedin_snapshot",
        foreign_keys="[Interview.linkedin_snapshot_id]"
    )
