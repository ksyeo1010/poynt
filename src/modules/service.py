# from .schemas.guild import Guild
from .schemas.user import User
from .schemas.round import Round
from .schemas.choice import Choice
from .schemas.user import UserBet

from .client import Client


class Service:
    @staticmethod
    def init_guild(guild_id: int):
        Client().create_db(guild_id,
                           users=User.get_validator(),
                           rounds=Round.get_validator())

    @staticmethod
    def add_user(guild_id: int, username: str):
        user = User(username=username)

        col = Client().get_collection(guild_id, 'users')
        col.insert_one(user.to_dict)

    @staticmethod
    def get_user(guild_id: int, username: str) -> User:
        col = Client().get_collection(guild_id, 'users')
        user = col.find_one({'username': username}, {'_id': False})
        return User(user)

    @staticmethod
    def add_round(guild_id: int, title: str):
        new_round = Round(title=title)

        col = Client().get_collection(guild_id, 'rounds')
        col.insert_one(new_round.to_dict)

    @staticmethod
    def add_choice(guild_id: int, title: str, option: str):
        choice = Choice(option=option)

        col = Client().get_collection(guild_id, 'rounds')
        col.update({
            'title': title
        }, {
            '$push': {
                'choices': choice.to_dict
            }
        })

    @staticmethod
    def add_bet(guild_id: int, title: str, option: str, username: str, amount: int):
        bet = UserBet(username=username, amount=amount)

        user_col = Client().get_collection(guild_id, 'users')
        user_col.update({
            'username': username
        }, {
            '$inc': {
                'points': -amount
            }
        })

        round_col = Client().get_collection(guild_id, 'rounds')
        round_col.update({
            'title': title,
            'choices.option': option
        }, {
            '$push': {
                'choices.$.bets': bet.to_dict
            }
        })
