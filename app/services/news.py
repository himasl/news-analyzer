from app.repositories.news import NewsRepository
from aiogram import Bot
from app.schemаs.news import NewsRq
from app.settings import settings
from aiogram.client.default import DefaultBotProperties


class NewsService:
    def __init__(self):
        self.news_repository: NewsRepository = NewsRepository()
        self.bot = Bot(
            token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML")
        )

    async def create_news(self, data: NewsRq):
        news = await self.news_repository.create(data.model_dump())
        if news:
            message = f"""Новая новость: {news.news_title}\n{news.news_link}\n{news.news_source}"""
            for user_id in settings.TELEGRAM_USERS:
                try:
                    await self.bot.send_message(chat_id=user_id, text=message)
                except Exception as e:
                    print(f"Ошибка при отправке пользователю {user_id}: {e}")
        return news

    async def get_news_titles(self):
        return await self.news_repository.get_titles()
