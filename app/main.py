from repository.config import CONFIG
from lib.send_discord import send_discord_message
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.AutoShardedBot(intents=intents)
TOKEN = CONFIG.token
path = "./cogs"

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond(content="BOT管理者限定コマンドです", ephemeral=True)
    else:
        raise error

@bot.event
async def on_guild_join(guild: discord.Guild):
    print(f"Bot was installed on: {guild.name}")

@bot.event
async def on_ready():
    print(f"{bot.user} On ready")
    if CONFIG.first_message:
        await send_discord_message(bot, "Botが起動しました。")


bot.load_extensions(
    'cogs.trend',
    'cogs.notification',
    store=True
)
# store=Falseにすると、Cogでエラーが発生していた際にクリティカル警告となる

bot.run(TOKEN)