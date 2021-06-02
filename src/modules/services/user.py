from src.modules.schemas import User
from src.modules.client import Client


class UserService:
    """A class that deals with the user's collection of a db."""
    @staticmethod
    def add_user(guild_id: int, username: str):
        """Adds a user given guild_id to identify a db.

        :param guild_id: the id to identify the db.
        :param username: the username to add to the users collection.
        :return: None.
        """
        user = User(username=username)

        col = Client().get_collection(guild_id, 'users')
        col.insert_one(user.to_dict)

    @staticmethod
    def get_user(guild_id: int, username: str) -> User:
        """Gets the user information given the username.

        :param guild_id: the id to identify the db.
        :param username: the username the get the user information.
        :return: A User object. User(<username>, <points>)
        """
        col = Client().get_collection(guild_id, 'users')
        user = col.find_one({'username': username}, {'_id': False})
        return User(**user)

    @staticmethod
    def update_bet(guild_id: int, username: str, amount: int, is_decrement: False):
        """Decrements the points of a user given the amount.

        :param guild_id: the id to identify the db.
        :param username: the username to decrement the points from.
        :param amount: the amount to decrement.
        :param is_decrement: decrement if true, increments otherwise.
        :return: None.
        """
        if is_decrement:
            amount *= -1

        user_col = Client().get_collection(guild_id, 'users')
        user_col.update({
            'username': username
        }, {
            '$inc': {
                'points': amount
            }
        })
