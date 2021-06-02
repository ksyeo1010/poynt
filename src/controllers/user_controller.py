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
    def update_user_points(ctx, username, amount, is_decrement):
        guild_id = ctx.guild.id
        UserService.update_bet(guild_id, username, amount, is_decrement)
