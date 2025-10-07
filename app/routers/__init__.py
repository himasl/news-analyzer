from fastapi import APIRouter

from app.routers.news import news_router

router = APIRouter(prefix="/v1")

router.include_router(news_router)
