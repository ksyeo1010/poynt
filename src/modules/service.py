from .schemas.guild import Guild
from .schemas.user import User


class Service:
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

    @staticmethod
    def add_round(guild_id: int, title: str):
        guild = Guild.objects.get(guild_id=guild_id)
        guild.rounds.create(title=title)
        guild.save()

    @staticmethod
    def add_choice(guild_id: int, title: str, description: str):
        guild = Guild.objects.get(guild_id=guild_id)
        selected_round = guild.rounds.get(title=title)
        selected_round.choices.create(description=description)
        guild.save()

    @staticmethod
    def add_bet(guild_id: int, title: str, description: str, username: str, amount: int):
        guild = Guild.objects.get(guild_id=guild_id)
        user = guild.users.get(username=username)
        user.points -= amount

        choice = guild.rounds.get(title=title).choices.get(description=description)
        choice.bets.create(username=username, amount=amount)

        guild.save()
