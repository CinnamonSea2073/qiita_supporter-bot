from repository.config import CONFIG
import discord
from typing import Optional

async def send_discord_message(
        bot: discord.AutoShardedBot, 
        message: str = None, 
        embed: Optional[discord.Embed] = None
    ) -> None:
    channel = bot.get_partial_messageable(id=CONFIG.channel_id)
    try:
        await channel.send(content=message, embed=embed)
    except discord.errors.HTTPException as e:
        print(e)
        print('Failed to send message.')
        return