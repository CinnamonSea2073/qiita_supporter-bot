import discord
from discord.ui import Select, View, Button
from discord.ext import commands, tasks
from discord import Option, SlashCommandGroup
from aiohttp import client_exceptions
from repository.config import CONFIG

class OriginalEmbed(discord.Embed):
    def __init__(self, color=CONFIG.theme_color, title: str = None, url: str = None, description: str = None):
        super().__init__(color=color, title=title, url=url, description=description)


class LoadingEmbed(OriginalEmbed):
    def __init__(self, description: str):
        super().__init__(
            title='<a:loading:919603348049657936> ローディング中',
            description=description)


class ErrorEmbed(OriginalEmbed):
    def __init__(self, url: str = None, description: str = None):
        super().__init__(
            color=0xff0000,
            title=':warning: エラー',
            url=url,
            description=description)