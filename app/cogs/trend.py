from math import e
from uu import Error
import discord
from discord.ext import commands 
from discord.commands import Option, OptionChoice, SlashCommandGroup
from model.view import OriginalEmbed, ErrorEmbed
from model.article import Articles

class TrendCog(commands.Cog):

    def __init__(self, bot:commands.bot):
        print(f"init -> {self.__class__}")
        self.bot = bot

    # nameは全て小文字
    group = SlashCommandGroup(name="trend", description="トレンドを参照します。")

    # コマンド名は全て小文字。関数名の重複に注意。
    @group.command(name="today", description="24時間以内に投稿されトレンド入りした記事を取得します。")
    async def command_trend_today(self, ctx: discord.ApplicationContext):
        rss_data = Articles("https://qiita.com/popular-items/feed")
        filtered_data = rss_data.filter_during_interval(24*60*60)
        if filtered_data != []:
            title = "以下の記事が24時間以内に投稿され、トレンド入りしました。"
            content = '\n\n'.join([str(data) for data in filtered_data])
            embed = OriginalEmbed(title=title, description=content)
            await ctx.response.send_message(embed=embed)
        else:
            embed = ErrorEmbed(description="24時間以内に投稿され、トレンド入りした記事はありません。")
            await ctx.response.send_message(embed=embed)

def setup(bot: commands.bot):
    bot.add_cog(TrendCog(bot))