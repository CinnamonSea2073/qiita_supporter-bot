class Config:
    def __init__(self, data):
        self.interval: int = data['INTERVAL']
        self.rss_urls: list[str] = data['QIITA_RSS_URL']
        self.first_message: bool = data['FIRST_MESSAGE']
        self.token: str = data['DISCORD_BOT_TOKEN']
        self.theme_color: int = data['THEME_COLOR']
        self.channel_id: int = data['CHANNEL_ID']