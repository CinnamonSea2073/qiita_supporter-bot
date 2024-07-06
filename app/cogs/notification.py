import discord
from discord.ext import commands, tasks
from discord.commands import Option, SlashCommandGroup
from model.view import OriginalEmbed, LoadingEmbed, ErrorEmbed
from repository.config import CONFIG
from model.article import Articles
from lib.send_discord import send_discord_message

class NotificationCog(commands.Cog):

    def __init__(self, bot: discord.AutoShardedBot):
        print(f"init -> {self.__class__}")
        self.bot = bot
        self.check_rss.start()

    @tasks.loop(seconds=CONFIG.interval)
    async def check_rss(self):
        for rss_url in CONFIG.rss_urls:
            rss_data = Articles(rss_url)
            filtered_data = rss_data.filter_during_interval()
            if filtered_data != []:
                title = f'{rss_data.title} に新しい記事が追加されました！'
                print(title)
                content = '\n\n'.join([str(data) for data in filtered_data])
                embed = OriginalEmbed(title=title, description=content)
                await send_discord_message(self.bot, title, embed)
            else:
                print('No new entries.')

    @check_rss.before_loop
    async def before_check_rss(self):
        print('waiting...')
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(NotificationCog(bot))