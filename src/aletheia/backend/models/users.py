from __future__ import annotations

from sqlalchemy.orm import Mapped, relationship
import uuid
from typing import TYPE_CHECKING, List, Optional

from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
)
from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from aletheia.backend.models.base import Base


if TYPE_CHECKING:
    from aletheia.backend.models.resume import Resume
    from aletheia.backend.models.linkedin_snapshot import LinkedInSnapshot
    from aletheia.backend.models.interview import Interview
    from aletheia.backend.models.user_activity import UserActivity


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE", name="fk_oauth_account_user_id"), primary_key=True
    )
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    """Core user record.

    The table name stays singular (``users``) to match existing FKs.
    """

    __tablename__ = "users"

    # ---------- Profile fields -------------------------------------------------
    full_name: Mapped[Optional[str]] = mapped_column(String(100))

    email: Mapped[Optional[str]] = mapped_column(String(255), unique=True)
    picture: Mapped[Optional[str]] = mapped_column(String(512))
    given_name: Mapped[Optional[str]] = mapped_column(String(100))
    family_name: Mapped[Optional[str]] = mapped_column(String(100))
    locale: Mapped[Optional[str]] = mapped_column(String(20))

    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    oauth_provider: Mapped[Optional[str]] = mapped_column(String(50), default="google")

    # ---------- Default asset references --------------------------------------
    default_resume_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("resume.id", ondelete="SET NULL", name="fk_user_default_resume_id")
    )
    default_linkedin_snapshot_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("linkedin_snapshot.id", ondelete="SET NULL", name="fk_user_default_linkedin_snapshot_id")
    )

    # ---------- Relationships --------------------------------------------------
    resumes: Mapped[List["Resume"]] = relationship(
        "Resume", 
        back_populates="user", 
        foreign_keys="[Resume.user_id]",
        # cascade="all, delete-orphan"
    )
    linkedin_snapshots: Mapped[List["LinkedInSnapshot"]] = relationship(
        "LinkedInSnapshot", 
        back_populates="user", 
        foreign_keys="[LinkedInSnapshot.user_id]",
        # cascade="all, delete-orphan"
    )
    interviews: Mapped[List["Interview"]] = relationship(
        "Interview", 
        back_populates="user", 
        foreign_keys="[Interview.user_id]",
        # cascade="all, delete-orphan"
    )
    activity: Mapped["UserActivity"] = relationship(
        "UserActivity", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )

    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )