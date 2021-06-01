from .schema import Guild
from src.modules.user.schema import User


class GuildService:
    @staticmethod
    def init_guild(guild_id: int):
        guild = Guild(guild_id=guild_id)
        guild.save()

    @staticmethod
    def add_user(guild_id: int, username: str):
        user = User(username=username)
        user.save()

        guild = Guild.objects.get(guild_id=guild_id)
        guild.users.append(user)
        guild.save()

    @staticmethod
    def get_user(guild_id: int, username: str) -> User:
        user = Guild.objects.get(guild_id=guild_id, user__username=username)
        return user

