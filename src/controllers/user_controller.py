from src.modules.service import Service


class UserController:

    @staticmethod
    def add_users(ctx):
        guild_id = ctx.owner.guild.id
        Service.init_guild(guild_id)
        for member in ctx.members:
            Service.add_user(guild_id, str(member))

    @staticmethod
    def add_new_user(ctx):
        guild_id = ctx.owner.guild.id
        Service.add_user(guild_id, str(ctx))

    @staticmethod
    def get_user_points(ctx):
        guild_id = ctx.guild.id
        user = Service.get_user(guild_id, str(ctx.author))
        return user.points

    @staticmethod
    def bet_points(ctx, title, bet_choice, username, amount):
        guild_id = ctx.guild.id
        Service.add_bet(guild_id, title, bet_choice, username, amount)

    @staticmethod
    def add_round(ctx, round_title):
        guild_id = ctx.guild.id
        Service.add_round(guild_id, round_title)

    @staticmethod
    def add_choice(ctx, round_title, choice):
        guild_id = ctx.guild.id
        Service.add_choice(guild_id, round_title, choice)

    @staticmethod
    def print_predictions(choice, counter):
        return f"{counter}: {choice}"
