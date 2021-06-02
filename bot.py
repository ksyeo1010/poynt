import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

from src.modules.client import Client
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
    # init db
    Client()

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

    @bot.command(name="predict")
    @commands.has_permissions(administrator=True)
    async def _predict(ctx, round_title: str, *args):
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

    @_predict.error
    async def predict_error(ctx, error):
        # move this to a UserController.no_permission_error
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")

    @bot.command()
    async def bet(ctx, round_title: str, bet_choice: str, bet_amount: int):
        """$bet <round_title> <option_name> <bet_amount>"""
        user_points = UserController.get_user_points(ctx)
        if user_points < bet_amount:
            await ctx.send("You dont have enough points")
        else:
            UserController.bet_points(ctx, round_title, bet_choice, str(ctx.message.author), bet_amount)

    @bot.command()
    async def activerounds(ctx):
        # which rounds are active right now
        pass

    @bot.command()
    async def multiplier(ctx, round_title: str, amount: int):
        """Return the multiplier for each option for the round"""
        # await ctx.send("This is the current multiplier for each choice!")
        # multiplier_message = UserController.multipliers_for_round(ctx, round_title, amount)
        # await ctx.send(multiplier_message)
        pass

    @bot.command(name="payout")
    @commands.has_permissions(administrator=True)
    async def _payout(ctx, round_title: str, winning_choice: str):
        """$payout <round_title> <winning_choice>"""
        # multiplier = UserController.multiplier(ctx, round_title)
        # UserController.payout_round(ctx, round_title, winning_choice)
        # winner_list = RoundController.get_winners(ctx, round_title, winning_choice)
        # await ctx.send(winner_list)
        # UserController.delete_round(ctx, round_title)
        pass

    @_payout.error
    async def payout_error(ctx, error):
        # move this to a UserController.no_permission_error
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")

    @bot.command(name="goodbyepoynt")
    @commands.has_permissions(administrator=True)
    async def _goodbyepoynt(ctx):
        # move code below to a UserController and call controller instead
        # await ctx.send(f"Are you sure you would kick poynt?\n"
        #                f"This will remove all data stored up to this point.\n"
        #                f"Type yes or no to confirm.")
        #
        # def check(message):
        #     return message.author == ctx.author and message.channel == ctx.channel \
        #            and message.content.lower() in ["yes", "no"]
        #
        # response = await bot.wait_for("message", check=check)
        # if response.content.lower() == "yes":
        #     This controller will kick poynt and delete the database and also send message for completion
        #     UserController.kick_poynt(guild_id)
        # elif response.content.lower() == "no":
        #     await ctx.send(f"Thanks for not kicking me! :)")
        # else:
        #     await ctx.send(f"That's not a valid input, run the command again!")
        pass

    @_goodbyepoynt.error
    async def goodbyepoynt_error(ctx, error):
        # move this to a UserController.no_permission_error
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")


    @bot.command()
    async def ranking(ctx, category: str):
        # category will be wins, losses, or points
        # controller will return the list of ranked players for a category
        # result = UserController.get_ranking(ctx, category)
        # await ctx.send(result)
        pass

    @bot.command()
    async def shop(ctx):
        # display shop for users
        # shop_list = UserController.display_shop(ctx)
        # await ctx.send(shop_list)
        pass

    @bot.command()
    async def use(ctx, item: str):
        # uses item from the user's list of items
        # if item count is less than 1, send error message
        # controller subtracts count from the user's items and announces to the text channel about the usage
        # message = UserController.use_item(ctx, item)
        # await ctx.send(message)
        pass

    @bot.command()
    async def cleaninventory(ctx):
        # cleans item list by deleting items that have 0 item count
        # UserController.clean_inventory(ctx)
        pass

    @bot.command()
    async def buy(ctx, item: str):
        # buys an item from the shop
        # removes inventory count from shop and places it into user items list with item and count
        # UserController.buy_item(ctx, item)
        # announce the inventory left for the item
        # message = UserController.announce_item_inventory(ctx, item)
        # await ctx.send(message)
        pass

    @bot.command(name="shopadd")
    @commands.has_permissions(administrator=True)
    async def _shopadd(ctx, item: str, inventory: int,  description: str, price: int):
        # able to add items to the shop
        # inventory has to be greater than 0
        # announce the item addition to server
        # message = UserController.add_shop_items(ctx, inventory, stock description, price)
        # await ctx.send(message)
        pass

    @_shopadd.error
    async def shopadd_error(ctx, error):
        # move this to a UserController.no_permission_error
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")

    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
