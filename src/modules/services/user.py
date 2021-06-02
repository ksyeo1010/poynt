from src.modules.schemas import User
from src.modules.client import Client


class UserService:
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
    def decrement_bet(guild_id: int, username: str, amount: int):
        user_col = Client().get_collection(guild_id, 'users')
        user_col.update({
            'username': username
        }, {
            '$inc': {
                'points': -amount
            }
        })