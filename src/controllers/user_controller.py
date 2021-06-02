from src.modules.services import UserService


class UserController:

    @staticmethod
    def add_users(ctx):
        guild_id = ctx.owner.guild.id
        for member in ctx.members:
            UserService.add_user(guild_id, str(member))

    @staticmethod
    def add_new_user(ctx):
        guild_id = ctx.owner.guild.id
        UserService.add_user(guild_id, str(ctx))

    @staticmethod
    def get_user_points(ctx):
        guild_id = ctx.guild.id
        user = UserService.get_user(guild_id, str(ctx.author))
        return user.points

    @staticmethod
    def decrement_user_points(ctx, username, amount):
        guild_id = ctx.guild.id
        UserService.decrement_bet(guild_id, username, amount)

    # @staticmethod
    # def payout_round(ctx, round_title, winning_choice):

    # @staticmethod
    # def multiplier(ctx, round_title):
    #     return RoundService.get_total_bets(ctx.guild.id, round_title)

