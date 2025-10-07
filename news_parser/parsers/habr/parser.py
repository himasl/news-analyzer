from bs4 import BeautifulSoup
import httpx
from config import config
from adapter import adapter


def habr_parser():
    news_dict = {}
    response = httpx.get(config.HABR_URL, headers=config.HEADERS).text
    soup = BeautifulSoup(response, "lxml")
    all_hrefs_news = soup.find_all("a", class_="tm-title__link")
    for news in all_hrefs_news:
        news_name = news.find("span").text
        news_link = f'https://habr.com{news.get("href")}'
        news_dict[news_name] = news_link
    for title, link in news_dict.items():
        adapter.send_data(title, link, "habr")
