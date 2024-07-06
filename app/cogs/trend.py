import discord
from discord.ext import commands 
from discord.commands import Option, OptionChoice, SlashCommandGroup

class TrendCog(commands.Cog):

    def __init__(self, bot:commands.bot):
        print(f"init -> {self.__class__}")
        self.bot = bot

    # nameは全て小文字
    group = SlashCommandGroup(name="trend", description="トレンドを参照します。")

    # コマンド名は全て小文字。関数名の重複に注意。
    @group.command(name="today", description="トレンドから本日中に投稿された記事を取得します。")
    async def command_trend_today(self, ctx: discord.ApplicationContext):
        await ctx.response.send_message(content="pong!")

def setup(bot: commands.bot):
    bot.add_cog(TrendCog(bot))