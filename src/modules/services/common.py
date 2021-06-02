from src.modules.schemas import User, Round
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
                           users=User.get_validator(),
                           rounds=Round.get_validator())