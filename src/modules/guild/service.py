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
        guild.users.save()

    @staticmethod
    def get_user(guild_id: int, username: str) -> User:
        guild = Guild.objects.get(guild_id=guild_id)
        user = guild.users.get(username=username)
        return user

    @staticmethod
    def add_round(guild_id: int, title: str):
        guild = Guild.objects.get(guild_id=guild_id)
        guild.rounds.create(title=title)
        guild.rounds.save()

    @staticmethod
    def add_choice(guild_id: int, title: str, choice: str):
        selected_round = Guild.objects.get(
            guild_id=guild_id,
            rounds__title=title
        )
        selected_round.create(choice=choice)
        selected_round.choices.save()

    @staticmethod
    def add_bet(guild_id: int, title: str, description: str, username: str, amount: int):
        guild = Guild.objects.get(guild_id=guild_id)
        user = guild.users.get(username=username)
        user.points -= amount

        guild.objects.get(
            rounds__title=title,
            rounds__choices__description=description
        ).create(
            username=username,
            amount=amount
        )
