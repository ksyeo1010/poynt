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
        user_points = UserController.get_user_points(ctx)
        await ctx.send("You currently have " + str(user_points))

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def predict(ctx, choice_one: str, choice_two: str):
        # Run controller to assign choices to document
        # GameController.option_one(str(choice_one))
        # GameController.option_two(str(choice_two))
        await ctx.send(f"Predictions have started!\n"
                       f"Place your points on either choice by typing the number: \n"
                       f"1: {choice_one}\n"
                       f"2: {choice_two}\n")

    @bot.command()
    async def bet(ctx, current_points: str, bet_amount: str):
        # create a new predictions round collection (are we going to allow the admin to access previous results?)
        # Add bet_amount to user's collection field
        # Add bet_choice to user's collection field
        # if the user's bet amount is not 0, they will not be able to use this command

        # run controller to place bet amount into correct choice field of predictions round
        # add username to the array of either choices

        # if str(ctx.message) == "1" or str(ctx.message) == "2":
        # Run controller to place bet amount in the current predictions round
        # if str(ctx.message) == "1":
        # GameController.place_points_first_option(bet_amount)
        # else:
        # GameController.place_points_second_option(bet_amount)
        # Run controller to take away bet amount from user
        # UserController.bet_points(str(ctx.author),current_points, bet_amount)
        # else:
        # ctx.send("that's not a correct choice, please choose between option 1 or option 2")
        pass

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def finish(ctx):
        # calculate payout multipliers based on amount of bets etc... add to collection field of predictions round
        # await ctx.send(f"Predictions have ended!")
        pass

    @bot.command()
    @commands.has_permissions()
    async def payout(ctx, winning_choice):
        # if the player's bet_choice is equal to winning_choice
        # multiply player's bet_amount to multiplier and update the result
        # clear all player_bet_amounts and bet_choice
        pass

    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
