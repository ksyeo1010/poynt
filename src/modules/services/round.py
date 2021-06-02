from src.modules.schemas import UserBet, Round, Choice
from src.modules.client import Client


class RoundService:
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

        round_col = Client().get_collection(guild_id, 'rounds')
        round_col.update({
            'title': title,
            'choices.option': option
        }, {
            '$push': {
                'choices.$.bets': bet.to_dict
            }
        })