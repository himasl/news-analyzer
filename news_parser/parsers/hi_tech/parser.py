from bs4 import BeautifulSoup
import httpx
from config import config
from adapter import adapter


def hi_tech_parser():
    news_dict = {}
    response = httpx.get(config.HI_TECH_URL, headers=config.HEADERS).text
    soup = BeautifulSoup(response, "lxml")
    all_hrefs_news = soup.find_all("a", class_="da2727fca3 cbde347509 e65bdf6865")
    for news in all_hrefs_news:
        news_name = news.get_text(strip=True)
        news_link = f'https://hi-tech.mail.ru/{news["href"]}'
        news_dict[news_name] = news_link

    for title, link in news_dict.items():
        adapter.send_data(title, link, "hi_tech")
