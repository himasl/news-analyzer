class Config:
    HEADERS = {
        "accept": "application/json, text/plain, */*",
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    }
    HABR_URL = f"https://habr.com/ru/news/"
    HI_TECH_URL = f"https://hi-tech.mail.ru/search/?utm_partner_id=&q=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B5+%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8"
    RBC_URL = f"https://www.rbc.ru/technology_and_media/"
    KODRU_URL = f"https://kod.ru/tag/news"

    BACKEND_URL = "http://127.0.0.1:8000"
    BACKEND_ADD_NEWS_PATH = "/api/news"


config = Config()
