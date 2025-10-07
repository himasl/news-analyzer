from fastapi import APIRouter, Depends
from app.schemаs.news import NewsRq
from app.services.news import NewsService


news_router = APIRouter()


@news_router.post("/news")
async def parse_news(data: NewsRq, news_service: NewsService = Depends()):
    return await news_service.create_news(data)


@news_router.get("/news/titles")
async def news_titles(news_service: NewsService = Depends()):
    return await news_service.get_news_titles()
