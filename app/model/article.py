import datetime
from repository.config import CONFIG
import time
from dateutil import parser
import feedparser

class Article:
    def __init__(self, entry):
        self.title: str = entry.title
        self.link: str = entry.link
        self.published: datetime = parser.parse(entry.published)

    def __str__(self) -> str:
        return f'**{self.title}**\n{self.link}\n{self.published.strftime("%Y/%m/%d %H:%M:%S")}'

    def is_during_interval(self) -> bool:
        current_time = time.time()
        return current_time - self.published.timestamp() <= CONFIG.interval
    
class Articles:
    def __init__(self, url: str):
        print(url)
        feed = feedparser.parse(url)
        self.articles: list[Article] = []
        self.title: str = feed.feed.title
        for entry in feed.entries:
            article = Article(entry)
            self.articles.append(article)

    def __str__(self) -> str:
        return "\n".join([str(article) for article in self.articles])

    def filter_during_interval(self):
        return [article for article in self.articles if article.is_during_interval()]