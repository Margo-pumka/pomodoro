from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    username: Mapped[Optional[str]]
    password: Mapped[Optional[str]]
    google_access_token: Mapped[Optional[str]]
    yandex_access_token: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    name: Mapped[Optional[str]]
