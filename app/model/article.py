import datetime
from model.qiita import QiitaInfo
from typing import Optional
from repository.qiita import load_qiita_info
from repository.config import CONFIG
import time
from dateutil import parser
import feedparser

class Article:
    def __init__(self, entry) -> None:
        self.title: str = entry.title
        self.link: str = entry.link
        self.published: datetime = parser.parse(entry.published)
        self.author: str = entry.author
        self.qiita_info_data: Optional[QiitaInfo] = None

    def __str__(self) -> str:
        return f'**[{self.title}]({self.link})**\n{self.published.strftime("%Y/%m/%d %H:%M:%S")}\n**User: **{self.author}'

    def is_during_interval(self, interval_time: int = CONFIG.interval) -> bool:
        current_time = time.time()
        return current_time - self.published.timestamp() <= interval_time
    
    def get_qiita_info(self) -> QiitaInfo:
        self._qiita_info_data = load_qiita_info(self.link.split('/')[-1])
        return self.qiita_info
    
    @property
    def qiita_info(self) -> QiitaInfo:
        if self._qiita_info_data is None:
            self.get_qiita_info()
        return self._qiita_info_data
    
    @qiita_info.setter
    def qiita_info_data(self, value: QiitaInfo):
        self._qiita_info_data = value
    
class Articles:
    def __init__(self, url: str) -> None:
        print(url)
        feed = feedparser.parse(url)
        self.articles: list[Article] = []
        self.title: str = feed.feed.title
        for entry in feed.entries:
            article = Article(entry)
            self.articles.append(article)

    def __str__(self) -> str:
        return "\n\n".join([str(article) for article in self.articles])

    def filter_during_interval(self, interval_time: int = CONFIG.interval) -> list[Article]:
        return [article for article in self.articles if article.is_during_interval(interval_time=interval_time)]
    
    def get_qiita_info(self) -> list[Article]:
        for article in self.articles:
            article.get_qiita_info()
        return self.articles