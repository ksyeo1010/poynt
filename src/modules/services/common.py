from src.modules.schemas import User, Round
from src.modules.client import Client


class CommonService:
    @staticmethod
    def init_guild(guild_id: int):
        Client().create_db(guild_id,
                           users=User.get_validator(),
                           rounds=Round.get_validator())