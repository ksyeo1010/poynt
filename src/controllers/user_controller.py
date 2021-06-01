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
    def bet_points(member, current_points, bet_amount):
        # new_amount = current_points - bet_amount
        # run update user point amount
        pass
