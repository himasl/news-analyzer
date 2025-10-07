from uuid import uuid4

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseDB


class NewsDB(BaseDB):
    __tablename__ = "news"  # noqa
    news_uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    news_title: Mapped[str] = mapped_column(index=True, unique=True)
    news_link: Mapped[str] = mapped_column(nullable=False)
    news_source: Mapped[str] = mapped_column(nullable=False)
