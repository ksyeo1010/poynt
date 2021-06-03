from datetime import datetime

from src.modules.schemas import Checkin
from src.modules.client import Client


class CheckinService:
    """A class that deals with the checkin collection db."""
    @staticmethod
    def checkin_user(guild_id: int, username: str):
        """Checks in the user.

        :param guild_id: the id to identify the db.
        :param username: the username to add to the users collection.
        :return: None
        """
        checkin = Checkin(username=username)

        col = Client().get_collection(guild_id, 'checkin')
        col.insert_one(checkin.to_dict)

    @staticmethod
    def check_time(guild_id: int, username: str) -> int:
        """Checks the remaining time a user can checkin again.

        :param guild_id: the id to identify the db.
        :param username: the username to add to the users collection.
        :return: a integer representing total time left.
        """
        col = Client().get_collection(guild_id, 'checkin')
        res = col.find_one({'username': username}, {'_id': False})

        time_left = res['expire_at'] - datetime.utcnow()

        return int(time_left.total_seconds())
