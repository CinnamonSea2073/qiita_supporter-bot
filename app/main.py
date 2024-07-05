from calendar import c
import time
from repository.config import CONFIG
from model.article import Articles
from lib.send_discord import send_discord_message

def main():
    if CONFIG.first_message:
        for url in CONFIG.discord_urls:
            send_discord_message(url, 'BOTが起動しました。\n以下のURLから新しい記事を取得します。\n\n' + '\n'.join(CONFIG.rss_urls))
    while True:
        for rss_url in CONFIG.rss_urls:
            rss_data = Articles(rss_url)
            filtered_data = rss_data.filter_during_interval()
            if filtered_data != []:
                content = f"**{rss_data.title}** に新しい記事が追加されました！\n\n"+'\n'.join([str(data) for data in filtered_data])
                print(content)
                for url in CONFIG.discord_urls:
                    send_discord_message(url, content)
            else:
                print('No new entries.')
            time.sleep(CONFIG.interval)

if __name__ == '__main__':
    main()