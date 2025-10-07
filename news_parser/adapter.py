from config import config
import httpx


class BackendAdapter:
    def __init__(self):
        self.backend_url = config.BACKEND_URL
        self.endpoint = config.BACKEND_ADD_NEWS_PATH

    def send_data(self, title: str, link: str, source: str):
        response = httpx.post(
            "http://project_name_app:8888/news",
            json={"news_title": title, "news_link": link, "news_source": source},
        )
        print(response.status_code)


adapter = BackendAdapter()
