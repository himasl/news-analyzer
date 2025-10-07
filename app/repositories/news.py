from sqlalchemy.dialects.postgresql import insert

from app.engines.postgres_storage import PostgresEngine
from app.models.news import NewsDB
from sqlalchemy import select


class NewsRepository:
    def __init__(self):
        self.db: PostgresEngine = PostgresEngine()

    async def create(self, news_data: dict) -> NewsDB | None:
        stmt = (
            insert(NewsDB)
            .values(**news_data)
            .on_conflict_do_nothing(index_elements=["news_title"])
            .returning(NewsDB)
        )
        return await self.db.execute(stmt)

    async def get_titles(self):
        stmt = select(NewsDB.news_title)
        titles = await self.db.execute(stmt, return_many=True)
        return titles
