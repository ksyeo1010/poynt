from .schema import Guild
from src.modules.user.schema import User


class GuildService:
    @staticmethod
    def init_guild(guild_id: int):
        guild = Guild(guild_id=guild_id)
        guild.save()

    @staticmethod
    def add_user(guild_id: int, username: str):
        guild = Guild.objects.get(guild_id=guild_id)
        guild.users.create(username=username)
        guild.save()

    @staticmethod
    def get_user(guild_id: int, username: str) -> User:
        guild = Guild.objects.get(guild_id=guild_id)
        user = guild.users.get(username=username)
        return user

