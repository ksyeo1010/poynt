from src.modules.services import CommonService, RoundService, UserService


class UserController:

    @staticmethod
    def add_users(ctx):
        guild_id = ctx.owner.guild.id
        CommonService.init_guild(guild_id)
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
    def bet_points(ctx, title, bet_choice, username, amount):
        guild_id = ctx.guild.id
        # UserService.decrement_bet(guild_id, username, amount)
        RoundService.add_bet(guild_id, title, bet_choice, username, amount)

    @staticmethod
    def add_round(ctx, round_title):
        guild_id = ctx.guild.id
        RoundService.add_round(guild_id, round_title)

    @staticmethod
    def add_choice(ctx, round_title, choice):
        guild_id = ctx.guild.id
        RoundService.add_choice(guild_id, round_title, choice)

    @staticmethod
    def print_predictions(choice, counter):
        return f"{counter}: {choice}"

    # @staticmethod
    # def payout_round(ctx, round_title, winning_choice):

    @staticmethod
    def multiplier(ctx, round_title):
        return RoundService.get_round_bets(ctx.guild.id, round_title, 'one')
        # UserService.increment_bets(ctx.guild.id)
        return 'done'
