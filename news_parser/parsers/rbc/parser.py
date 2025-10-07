from bs4 import BeautifulSoup
import httpx
from config import config
from adapter import adapter


def rbc_parser():
    news_dict = {}
    response = httpx.get(config.RBC_URL, headers=config.HEADERS).text
    soup = BeautifulSoup(response, "lxml")
    all_hrefs_news = soup.find_all(
        "a", class_="item__link rm-cm-item-link js-rm-central-column-item-link"
    )
    for news in all_hrefs_news:
        news_name = news.get_text(strip=True)
        news_link = f'{news.get("href")}'
        news_dict[news_name] = news_link
    for title, link in news_dict.items():
        adapter.send_data(title, link, "rbc")
