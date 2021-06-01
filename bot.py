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
        UserController.add_users(ctx)

    @bot.event
    async def on_member_join(member):
        UserController.add_new_user(member)

    @bot.command()
    async def points(ctx):
        """Checks how many points you have right now"""
        user_points = UserController.get_user_points(ctx)
        await ctx.send("You currently have " + str(user_points))

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def predict(ctx, round_title: str, *args):
        """$predict <round_title> <options> ... <options>"""
        UserController.add_round(ctx, round_title)
        for choice in args:
            UserController.add_choice(ctx, round_title, choice)
        await ctx.send(f"Predictions have started!\n"
                       f"Place your points on either choice by typing "
                       f"$bet <round_title> <option_name> <bet_amount>: \n")
        counter = 0
        for choice in args:
            counter += 1
            message = UserController.print_predictions(choice, counter)
            await ctx.send(message)

    @bot.command()
    async def bet(ctx, round_title: str, bet_choice: str, bet_amount: int):
        """$bet <round_title> <option_name> <bet_amount>"""
        user_points = UserController.get_user_points(ctx)
        if user_points < bet_amount:
            await ctx.send("You dont have enough points")
        else:
            UserController.bet_points(ctx, round_title, bet_choice, str(ctx.message.author), bet_amount)

    @bot.command()
    async def multiplier(ctx, round_title: str, amount: int):
        """Return the multiplier for each option for the round"""
        # await ctx.send("This is the current multiplier for each choice!")
        # for each in range(1, RoundController.get_total_choices() + 1):
        #   for round in RoundController.get_round(ctx, round_title, each)
        #       multiplier = RoundController.get_multiplier(ctx, round_title, winning_choice)
        #       await ctx.send(f"The multiplier for option {each} is {multiplier}. "
        #                      f"This means if you bet {amount} points, you'll get back {amount * multiplier} plus the "
        #                      f"original bet amount of {amount}, with the total of {(amount * multiplier) + amount}")
        pass

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def payout(ctx, round_title: str, winning_choice: str):
        """$payout <round_title> <winning_choice>"""
        # winner_list = RoundController.get_round(ctx, round_title, winning_choice)
        # multiplier = RoundController.get_multiplier(ctx, round_title, winning_choice)
        # for player in winner_list:
        #   winnings = (player.bet_amount * multiplier) + player.bet_amount
        #    UserController.update_points(ctx, winnings)
        # await ctx.send("All the points have been distributed!")
        # RoundController.delete_round(ctx, round_id)
        pass

    @bot.command()
    async def ranking(ctx):
        # users = vars(UserController.get_all_users(ctx))
        #
        #
        # for user in range(len(users)):
        #
        pass

    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
