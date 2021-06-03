import os
import discord
import logging
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

from src.modules.client import Client
from src.controllers import CommonController, RoundController, UserController, ShopController

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

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)


def main():
    # init db
    Client()

    # class AdminCog(commands.Cog, name='ADMIN'):
    #     def __init__(self, bot):
    #         self.bot = bot
    #
    #     @commands.command(name='predict',
    #                       brief='Create a round of predictions.',
    #                       description='If you would like to close or open betting for the predictions, '
    #                                   'search for <$help closebets> or <$help openbets>.')
    #     async def predict(self, ctx):
    #         await ctx.send('predict')
    #
    #     @commands.command(name='closebets',
    #                       brief='Close betting for prediction round.',
    #                       description='If you would like to reopen prediction round, search for <$help openbets>. '
    #                                   'If you would like to end the round, search for <$help payout>.')
    #     async def closebets(self, ctx):
    #         await ctx.send('closebets')
    #
    #     @commands.command(name='openbets',
    #                       brief='Open betting for prediction round.',
    #                       description='If you would like to reclose prediction round, search for <$help closebets>. '
    #                                   'If you would like to end the round, search for <$help payout>.')
    #     async def openbets(self, ctx):
    #         await ctx.send('openbets')
    #
    #     @commands.command(name='payout',
    #                       brief='Conclude the prediction round by paying out users.',
    #                       description='Allocate winnings to players. '
    #                                   'Running this will delete the round.')
    #     async def payout(self, ctx):
    #         await ctx.send('payout')
    #
    #     @commands.command(name='shopadd',
    #                       brief='Add roles to the shop.',
    #                       description='Add roles to the shop with the specified name, cost, and role color.')
    #     async def shopadd(self, ctx):
    #         await ctx.send('shopadd')
    #
    # class GeneralCog(commands.Cog, name='GENERAL'):
    #     def __init__(self, bot):
    #         self.bot = bot
    #
    #     @commands.command(name='points',
    #                       brief='Check your points.',
    #                       description='Check how many points you have right now. '
    #                                   'You can only use this command every 15 seconds.')
    #     async def points(self, ctx):
    #         await ctx.send('points')
    #
    #     @commands.command(name='postprediction',
    #                       brief='Check accumulated bets for options.',
    #                       description='Check how many points are bet in each option for the prediction round. '
    #                                   'You can only use this command every 15 seconds.')
    #     async def postprediction(self, ctx):
    #         await ctx.send('postprediction')
    #
    #     @commands.command(name='bet',
    #                       brief='Place a bet on an option.',
    #                       description='Bet on an option for the specified prediction round. '
    #                                   'You will only be able to place a bet when the betting status is open for the '
    #                                   'specified prediction round. '
    #                                   'You will not be able to place more points than what you already have.')
    #     async def bet(self, ctx):
    #         await ctx.send('bet')
    #
    #     @commands.command(name='activerounds',
    #                       brief='Check rounds available to bet.',
    #                       description='Check which prediction rounds are open to vote.')
    #     async def activerounds(self, ctx):
    #         await ctx.send('activerounds')
    #
    #     @commands.command(name='multiplier',
    #                       brief='Check multiplier for each option.',
    #                       description='Check how much you will earn by putting in specified points into each option. '
    #                                   'You can only use this command every 15 seconds.')
    #     async def multiplier(self, ctx):
    #         await ctx.send('multiplier')
    #
    #     @commands.command(name='ranking',
    #                       brief='Check points ranking for top 10 users.',
    #                       description='Check top 10 player in the guild with the most points. '
    #                                   'You can only use this command every 15 seconds.')
    #     async def ranking(self, ctx):
    #         await ctx.send('ranking')
    #
    #     @commands.command(name='shop',
    #                       brief='Display roles you are able to purchase.',
    #                       description='Shows all the roles that are available to purchase. '
    #                                   'If you would like to purchase any of the roles, search for <$help shopbuy>.')
    #     async def shop(self, ctx):
    #         await ctx.send('shop')
    #
    #     @commands.command(name='shopbuy',
    #                       brief='Buy role from the shop.',
    #                       description='The role you purchase will be assigned to you on your discord server. '
    #                                   'Please refer to the admin to change the display name colour to the specified role. '
    #                                   'If you would like to view the roles on sale, search for <$help shop>.')
    #     async def shopbuy(self, ctx):
    #         await ctx.send('shopbuy')
    #
    #     @commands.command(name='checkin',
    #                       brief='Check-in to receive 100 points.',
    #                       description='Receive 100 points for checking-in. '
    #                                   'You will only be able to check-in again after 24 hours.')
    #     async def checkin(self, ctx):
    #         await ctx.send('checkin')
    #

    @bot.group(invoke_without_command=True)
    async def help(ctx):
        embed = discord.Embed(title="help",
                              description="Use $help <command> for more details on a command.",
                              color=0x0000ff)
        embed.add_field(name="Admin", value="predict\nclosebets\nopenbets\npayout\nshopadd")
        embed.add_field(name="General", value="points\npostprediction\nbet\nactiverounds\nmultiplier\nranking\nshop\n"
                                              "shopbuy\ncheckin")
        await ctx.send(embed=embed)

    @help.command()
    async def predict(ctx):
        embed = discord.Embed(title="predict",
                              description="Create a round of predictions. "
                                          "You can create as many options as you want, but the minimum is two. "
                                          "If you would like to close or open betting for "
                                          "the predictions, search for <$help closebets> or <$help openbets>.",
                              color=0x0000ff)
        embed.add_field(name="**Syntax**", value="$predict <round_title> <option> ... <option>")
        await ctx.send(embed=embed)

    @help.command()
    async def closebets(ctx):
        embed = discord.Embed(title="closebets",
                              description="Close betting for the specified prediction round. "
                                          "If you would like to reopen prediction round, search for "
                                          "<$help openbets>. "
                                          "If you would like to end the round, search for <$help payout>",
                              color=0x0000ff)
        embed.add_field(name="**Syntax**", value="$closebets <round_title>")
        await ctx.send(embed=embed)


    @help.command()
    async def openbets(ctx):
        embed = discord.Embed(title="openbets",
                              description="Open betting for the specified prediction round. "
                                          "If you would like to reclose prediction round, search for <$help closebets>. "
                                          "If you would like to end the round, search for <$help payout>",
                              color=0x0000ff)
        embed.add_field(name="**Syntax**", value="$openbets <round_title>")
        await ctx.send(embed=embed)

    @help.command()
    async def payout(ctx):
        embed = discord.Embed(title="payout",
                              description="Conclude the prediction round and payout users.",
                              color=0x0000ff)
        embed.add_field(name="**Syntax**", value="$payout <round_title> <winning_option>")
        await ctx.send(embed=embed)

    @help.command()
    async def shopadd(ctx):
        embed = discord.Embed(title="shopadd",
                              description="Add roles to the shop with the specified name, cost, and color.",
                              color=0x0000ff)
        embed.add_field(name="**Syntax**", value="$shopadd <role_name> <role_price> <role_color>")
        await ctx.send(embed=embed)

    @bot.event
    async def on_ready():
        """Print to console when bot is connected."""
        print(f'{bot.user.name} has connected to Discord!')

    @bot.event
    async def on_guild_join(ctx):
        """Create database for server using server id, and create users collection and user documents for users in the
           discord server."""
        # print(ctx.owner.guild.id)
        CommonController.initiate_guild(ctx)
        UserController.add_users(ctx)

    @bot.event
    async def on_member_join(member):
        """Create user document when a new user joins server."""
        UserController.add_new_user(member)
        # embed = discord.Embed(color=0x00ff00)
        # embed.title = f"Welcome {member}!"
        # embed.description = f"Here's 500 points to start predicting!\n" \
        #                     f"In order to see my commands, simply type $help to view commands!\n" \
        #                     f"Keep in mind that you can only check the help commands by DM, but actual commands" \
        #                     f"need to be made on the server you would like to participate in!"
        # await member.send(embed=embed)

    @bot.event
    async def on_command_error(ctx, error):
        """Send message to channel for errors.

        The function handles errors in different situations and gives messages for the error."""
        embed = discord.Embed(color=0xff0000)
        if isinstance(error, commands.CommandOnCooldown):
            embed.title = f"Cooldown!"
            embed.description = f"{error}"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()
        if isinstance(error, commands.MissingPermissions):
            embed.title = "Nice Try!"
            embed.description = f"Sorry {ctx.message.author}, you are not an admin!"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()
        if isinstance(error, commands.BadArgument):
            embed.title = f"Command Error!"
            embed.description = "Please type the correct command"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()
        if isinstance(error, commands.CommandNotFound):
            embed.title = f"Command Error!"
            embed.description = "There's no commanded named that!"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()

    @bot.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def points(ctx):
        """Check how many points you have right now.
        You can only use this command every 15 seconds."""
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Points"
        user_points = UserController.get_user_points(ctx)
        embed.description = f"You currently have {str(user_points)}"
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2.5)
        await msg.delete()

    @bot.command(name="predict")
    @commands.has_permissions(administrator=True)
    async def predict(ctx, round_title: str, *args):
        """ADMIN COMMAND: Create a round of predictions.
        If you would like to close or open betting for the predictions, search for <$help closebets> or <$help openbets>."""
        if len(args) > 1:
            RoundController.add_round(ctx, round_title)
            for choice in args:
                RoundController.add_choice(ctx, round_title, choice)
            counter = 0
            options_list = []
            for choice in args:
                counter += 1
                message = RoundController.print_predictions(choice, counter)
                options_list.append(message)
            embed = discord.Embed(color=0x00ff00)
            embed.title = "Predict Round Initiated!"
            options_string = '\n'.join(options_list)
            general_message = (f"Predictions have started for {round_title}!\n"
                               f"Place your points on either choice by typing "
                               f"$bet <round_title> <option_name> <bet_amount>: \n")
            embed.description = general_message + options_string
            await ctx.message.delete()
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0xff0000)
            embed.title = "Prediction Command Error!"
            embed.description = "You have to put in at least two options"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def closebets(ctx, round_title):
        """ADMIN COMMAND: Close betting for the specified prediction round.
        If you would like to reopen prediction round, search for <$help openbets>.
        If you would like to end the round, search for <$help payout>"""
        RoundController.change_prediction_status(ctx, round_title, False)
        embed = discord.Embed(color=0xff0000)
        embed.title = "Betting Status Changed!"
        embed.description = f"Betting has now concluded for {round_title}.\n" \
                            f"In order to initiate betting once more, please contact an admin."
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def openbets(ctx, round_title):
        """ADMIN COMMAND: Open betting for the specified prediction round.
        If you would like to reclose prediction round, search for <$help closebets>.
        If you would like to end the round, search for <$help payout>"""
        RoundController.change_prediction_status(ctx, round_title, True)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Betting Status Changed!"
        embed.description = f"Betting has be initiated for {round_title}.\n" \
                            f"For more support in placing a bet, type command '$help bet' for more information.\n" \
                            f"Bet away!"
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @bot.command(name="postprediction")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def postprediction(ctx, round_title):
        """Check how many points are bet in each option for the prediction round.
        You can only use this command every 15 seconds."""
        result = RoundController.post_predictions(ctx, round_title)
        embed = discord.Embed(color=0x00ff00)
        embed.title = f"{round_title} Status"
        embed.description = result
        # embed.add_field(name=f"Round: {round_title}", value=result, inline=False)
        # user = bot.get_user(ctx.author.id)
        await ctx.message.delete()
        await ctx.send(embed=embed)

        # embed_dict = embed.to_dict()
        # await msg.delete()

    @bot.command()
    async def bet(ctx, round_title: str, bet_choice: str, bet_amount: int):
        """Bet on an option for the specified prediction round.
           You will only be able to place a bet when the betting status is open for the specified prediction round.
           You will not be able to place more points than what you already have."""
        if UserController.get_user_points(ctx) < bet_amount:
            embed = discord.Embed(color=0xff0000)
            embed.title = f"Bet Error!"
            embed.description = "You dont have enough points"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()
        if RoundController.is_prediction_running(ctx, round_title):
            UserController.update_user_points(ctx, str(ctx.message.author), bet_amount, True)
            RoundController.place_user_bet(ctx, round_title, bet_choice, str(ctx.message.author), bet_amount)
            embed = discord.Embed(color=0x00ff00)
            embed.title = f"Betting Complete!"
            embed.description = f"You've successfully bet {bet_amount} points to '{bet_choice}'!"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()
        else:
            embed = discord.Embed(color=0xff0000)
            embed.title = f"Bet Error!"
            embed.description = "The Poll is closed right now!"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()

    @bot.command()
    async def activerounds(ctx):
        """Check which prediction rounds are open to vote."""
        # which rounds are active right now
        pass

    @bot.command(name="multiplier")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def multiplier(ctx, round_title: str, money: int):
        """Check how much you will earn by putting in specified points into each option.
        You can only use this command every 15 seconds."""
        multiplier_message = RoundController.multiplier_total_pool(ctx, round_title, money)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Potential Bet Returns"
        options_string = '\n'.join(multiplier_message)
        embed.description = options_string
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2.5)
        await msg.delete()

    @bot.command(name="payout")
    @commands.has_permissions(administrator=True)
    async def payout(ctx, round_title: str, winning_choice: str):
        """ADMIN COMMAND: Conclude the prediction round and payout users."""
        # list_of_dict = RoundController.get_options(ctx, round_title)
        # total_bets_made = RoundController.get_total_round_bets(list_of_dict)
        # winning_option_total_bets = RoundController.get_winning_option_total_bets(list_of_dict, winning_choice)
        option_multiplier = RoundController.get_option_multiplier(ctx, round_title, winning_choice)
        winning_option = RoundController.get_winning_option(ctx, round_title, winning_choice)
        for winner in winning_option:
            winner = RoundController.apply_multiplier(winner, option_multiplier)
            UserController.update_user_points(ctx, winner.username, winner.amount, False)
        RoundController.delete_round(ctx, round_title)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Prediction Round Over!"
        embed.description = "Everything has been allocated!"
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2.5)
        await msg.delete()

    # @bot.command(name="goodbyepoynt")
    # @commands.has_permissions(administrator=True)
    # async def goodbyepoynt(ctx):
    #     # move code below to a UserController and call controller instead
    #     # await ctx.send(f"Are you sure you would kick poynt?\n"
    #     #                f"This will remove all data stored up to this point.\n"
    #     #                f"Type yes or no to confirm.")
    #     #
    #     # def check(message):
    #     #     return message.author == ctx.author and message.channel == ctx.channel \
    #     #            and message.content.lower() in ["yes", "no"]
    #     #
    #     # response = await bot.wait_for("message", check=check)
    #     # if response.content.lower() == "yes":
    #     #     This controller will kick poynt and delete the database and also send message for completion
    #     #     UserController.kick_poynt(guild_id)
    #     # elif response.content.lower() == "no":
    #     #     await ctx.send(f"Thanks for not kicking me! :)")
    #     # else:
    #     #     await ctx.send(f"That's not a valid input, run the command again!")
    #     pass

    @bot.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ranking(ctx):
        """Check top 10 player in the guild with the most points.
        You can only use this command every 15 seconds."""
        result = UserController.get_ranking(ctx)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Ranking!"
        embed.description = f"{result}"
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()

    @bot.command()
    async def shop(ctx):
        """Display roles you are able to purchase.
        If you would like to purchase any of the roles, search for <$help shopbuy>."""
        # display shop for users
        message = ShopController.display_shop(ctx)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Points Shop!"
        embed.description = f"{message}"
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(15)
        await msg.delete()

    @bot.command()
    async def shopbuy(ctx, role_name: str):
        """Buy role from the shop.
        The role you purchase will be assigned to you on your discord server.
        Please refer to the admin to change the display name colour to the specified role.
        If you would like to view the roles on sale, search for <$help shop>."""
        role_cost = ShopController.get_role_from_name(ctx, role_name)
        # assign user to the role_name
        # subtract role_name cost from user
        if UserController.get_user_points(ctx) < role_cost:
            embed = discord.Embed(color=0xff0000)
            embed.title = f"Purchase Error!"
            embed.description = "You dont have enough points"
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await msg.delete()
        else:
            member = ctx.message.author
            role = discord.utils.get(member.server.roles, name=role_name)
            await member.addroles(member, role)
            embed = discord.Embed(color=0x00ff00)
            embed.title = "Purchased!"
            embed.description = f"{role_name} was purchased from the shop!" \
                                f"The role has been assigned to you on the server."
            await ctx.message.delete()
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(15)
            await msg.delete()

    @bot.command(name="shopadd")
    @commands.has_permissions(administrator=True)
    async def shopadd(ctx, role_name, role_cost, role_color):
        """ADMIN COMMAND: Add roles to the shop with the specified name, cost, and role color."""
        # able to add items to the shop
        role_color = int(role_color, 16)
        ShopController.add_role(ctx, role_name, role_cost)
        await ctx.guild.create_role(name=role_name, color=role_color)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "New Role!"
        embed.description = f"New role has been added to the shop!\n" \
                            f"Roll Name:{role_name}\n" \
                            f"Price: {role_cost} Points\n"
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(15)
        await msg.delete()

    @bot.command()
    @commands.cooldown(1, 86340, commands.BucketType.user)
    async def checkin(ctx):
        """Check-in to receive 100 points.
        You will only be able to check-in again after 24 hours."""
        UserController.update_user_points(ctx, ctx.message.author, 100, False)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "Check in!"
        embed.description = f"You have checked in!\n" \
                            f"We have given you 100 points.\n" \
                            f"You can check in again after 24 hours!"
        await ctx.message.delete()
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await msg.delete()

    # bot.add_cog(AdminCog(bot))
    # bot.add_cog(GeneralCog(bot))
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
