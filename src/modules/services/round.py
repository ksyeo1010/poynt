from src.modules.schemas import UserBet, Round, Choice
from src.modules.client import Client


class RoundService:
    """A class that deals with the round collection db."""
    @staticmethod
    def add_round(guild_id: int, title: str):
        """Adds a round to the guild_id db given the title.

        :param guild_id: the guild_id identifier.
        :param title: the unique title to add to.
        :return: None.
        """
        new_round = Round(title=title)

        col = Client().get_collection(guild_id, 'rounds')
        col.insert_one(new_round.to_dict)

    @staticmethod
    def add_choice(guild_id: int, title: str, option: str):
        """Adds a choice to a given round.

        :param guild_id: th guild_id to identify db.
        :param title: the title to identify round.
        :param option: the option to add to round.
        :return: None.
        """
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
        """ Adds a bet to a option of a round.

        :param guild_id: the id to identify the db.
        :param title: the title to identify the round.
        :param option: the option to add a bet.
        :param username: the username of the user who is adding a bet.
        :param amount: the amount to bet.
        :return: None.
        """
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

    @staticmethod
    def get_total_bets(guild_id: int, title: str) -> list:
        """Gets the total bet of each choice of a round.

        :param guild_id: the id to identify db.
        :param title: the title to identify round.
        :return: a list of dictionaries: {_id: <option>, total: <total_amount>}
        """
        pipeline = [
            {'$match': {'title': title}},
            {'$unwind': '$choices'},
            {'$unwind': {
                'path': '$choices.bets',
                'preserveNullAndEmptyArrays': True
            }},
            {'$group': {
                '_id': '$choices.option',
                'total': {'$sum': '$choices.bets.amount'}
            }}
        ]

        round_col = Client().get_collection(guild_id, 'rounds')
        res = round_col.aggregate(pipeline)

        return list(res)

    @staticmethod
    def get_round_bets(guild_id: id, title: str, option: str) -> list:
        """Gets all options and bets of a round.

        :param guild_id: the id to identify db.
        :param title: the title to identify round.
        :param option: the winning choice of a round.
        :return: a list of dictionaries containing user and total amount bet.
                 [{_id: <username>, total: <total_amount>}]
        """
        pipeline = [
            {'$match': {'title': title}},
            {'$unwind': {'path': '$choices'}},
            {'$match': {'choices.option': option}},
            {'$unwind': {'path': '$choices.bets'}},
            {'$group': {
                '_id': '$choices.bets.username',
                'total': {'$sum': '$choices.bets.amount'}
            }}
        ]

        round_col = Client().get_collection(guild_id, 'rounds')
        res = round_col.aggregate(pipeline)

        return list(res)
