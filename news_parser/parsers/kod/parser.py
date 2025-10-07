from bs4 import BeautifulSoup
import httpx
from config import config
from adapter import adapter


def kodru_parser():
    news_dict = {}
    response = httpx.get(config.KODRU_URL, headers=config.HEADERS).text
    soup = BeautifulSoup(response, "lxml")
    all_hrefs_news = soup.find_all("a", class_="Post_link__bf86U")
    main_line = soup.find_all("a", class_="PostMain_grid__WQj4c")
    for news_main in main_line:
        news_name = news_main.get_text(strip=True)
        news_link = f'https://kod.ru/{news_main["href"]}'
        news_dict[news_name] = news_link
    for news in all_hrefs_news:
        news_name = news.get_text(strip=True)
        news_link = f'https://kod.ru/{news["href"]}'
        news_dict[news_name] = news_link
    first_key = list(news_dict.keys())[1]  # Мусорная строка в начале
    del news_dict[first_key]
    for title, link in news_dict.items():
        adapter.send_data(title, link, "kod")
