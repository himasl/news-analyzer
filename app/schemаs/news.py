from pydantic import BaseModel


class NewsRq(BaseModel):
    news_title: str
    news_link: str
    news_source: str
