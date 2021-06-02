import os
import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

from src.modules.client import Client
from src.controllers import CommonController, RoundController, UserController

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
        CommonController.initiate_guild(ctx)
        UserController.add_users(ctx)

    @bot.event
    async def on_member_join(member):
        UserController.add_new_user(member)

    @bot.command()
    async def points(ctx):
        """Checks how many points you have right now"""
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Points"
        user_points = UserController.get_user_points(ctx)
        embed.description = f"You currently have {str(user_points)}"
        await ctx.send(embed=embed)

    @bot.command(name="predict")
    @commands.has_permissions(administrator=True)
    async def predict(ctx, round_title: str, *args):
        """$predict <round_title> <options> ... <options>"""
        if len(args) > 1:
            RoundController.add_round(ctx, round_title)
            for choice in args:
                RoundController.add_choice(ctx, round_title, choice)
            await ctx.send(f"Predictions have started!\n"
                           f"Place your points on either choice by typing "
                           f"$bet <round_title> <option_name> <bet_amount>: \n")
            counter = 0
            for choice in args:
                counter += 1
                message = RoundController.print_predictions(choice, counter)
                await ctx.send(message)
        else:
            await ctx.send("You have to put in at least two options")
            return

    @predict.error
    async def predict_error(ctx, error):
        # move this to a UserController.no_permission_error
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")

    @bot.command()
    async def endpredict(ctx, round_title):
        RoundController.change_prediction_status(ctx, round_title, False)
        await ctx.send("Voting has ended!")

    @bot.command()
    async def startpredict(ctx, round_title):
        RoundController.change_prediction_status(ctx, round_title, True)
        await ctx.send("Voting has started again!")

    @bot.command()
    async def postprediction(ctx, round_title):
        result = RoundController.post_predictions(ctx, round_title)
        await ctx.send(result)

    @bot.command()
    async def bet(ctx, round_title: str, bet_choice: str, bet_amount: int):
        """$bet <round_title> <option_name> <bet_amount>"""
        if UserController.get_user_points(ctx) < bet_amount:
            await ctx.send("You dont have enough points")
        if RoundController.is_prediction_running(ctx, round_title):
            UserController.update_user_points(ctx, str(ctx.message.author), bet_amount, True)
            RoundController.place_user_bet(ctx, round_title, bet_choice, str(ctx.message.author), bet_amount)
        else:
            await ctx.send("The Poll is closed right now!")

    @bot.command()
    async def activerounds(ctx):
        # which rounds are active right now
        pass

    @bot.command()
    async def multiplier(ctx, round_title: str):
        """Return the multiplier for each option for the round"""
        await ctx.send("This is the current multiplier for each choice!")
        multiplier_message = RoundController.multiplier(ctx, round_title)
        await ctx.send(multiplier_message)
        pass

    @bot.command(name="payout")
    @commands.has_permissions(administrator=True)
    async def payout(ctx, round_title: str, winning_choice: str):
        """$payout <round_title> <winning_choice>"""
        list_of_dict = RoundController.get_options(ctx, round_title)
        total_bets_made = RoundController.get_total_round_bets(list_of_dict)
        winning_option_total_bets = RoundController.get_winning_option_total_bets(list_of_dict, winning_choice)
        option_multiplier = RoundController.get_option_multiplier(winning_option_total_bets, total_bets_made)
        winning_option = RoundController.get_winning_option(ctx, round_title, winning_choice)
        for winner in winning_option:
            winner = RoundController.apply_multiplier(winner, option_multiplier)
            UserController.update_user_points(ctx, winner["_id"], winner["total"], False)
            # await ctx.send(f"{winner['_id']} has gained {winner['total']}")
        await ctx.send("Everything has been allocated!")

    @payout.error
    async def payout_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")

    @bot.command(name="goodbyepoynt")
    @commands.has_permissions(administrator=True)
    async def goodbyepoynt(ctx):
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

    @goodbyepoynt.error
    async def goodbyepoynt_error(ctx, error):
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
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"Sorry {ctx.message.author}, you are not an admin!")

    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    bot.run(TOKEN)


if __name__ == '__main__':
    main()
