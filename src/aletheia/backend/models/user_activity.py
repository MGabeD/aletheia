from __future__ import annotations

import datetime as _dt
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from aletheia.backend.models.base import Base

if TYPE_CHECKING:  
    from aletheia.backend.models.users import User


class UserActivity(Base):
    """Tracks the last login time for a user."""

    __tablename__ = "user_activity"

    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE", name="fk_user_activity_user_id"), primary_key=True
    )
    last_login_at: Mapped[_dt.datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: _dt.datetime.now(_dt.timezone.utc),
        nullable=False,
    )

    # ---------- Relationships --------------------------------------------------
    user: Mapped["User"] = relationship("User", back_populates="activity")