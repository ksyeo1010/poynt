from src.modules.schemas import User, Round, Role, Checkin
from src.modules.client import Client


class CommonService:
    """A class that deals with common functions for the db."""
    @staticmethod
    def init_guild(guild_id: int):
        """Initializes the db and collections needed for a guild.

        :param guild_id: the guild_id is the name of the db.
        :return: None.
        """
        Client().create_db(guild_id,
                           users=User,
                           rounds=Round,
                           role_shop=Role,
                           checkin=Checkin)

    @staticmethod
    def delete_guild(guild_id: int):
        """Deletes a guid from the database.

        :param guild_id: the guild_id is the name of the db.
        :return: None.
        """
        Client().delete_db(guild_id)
