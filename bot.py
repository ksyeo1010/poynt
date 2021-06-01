import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

from src.modules import client
from src.controllers.user_controller import UserController

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


def main():
    client.connect()

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    @bot.event
    async def on_guild_join(ctx):
        # print(ctx.owner.guild.id)
        UserController.add_users(ctx.members)

    @bot.event
    async def on_member_join(member):
        UserController.add_new_user(member)

    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
