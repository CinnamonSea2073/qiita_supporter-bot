class Config:
    def __init__(self, data):
        self.interval: int = data['INTERVAL']
        self.rss_urls: list[str] = data['QIITA_RSS_URL']
        self.discord_urls: list[str] = data['DISCORD_WEBHOOK_URL']
        self.first_message: bool = data['FIRST_MESSAGE']
