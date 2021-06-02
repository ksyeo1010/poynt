import os
from pymongo import MongoClient


class Client:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._client = MongoClient(
            f'mongodb://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/?authSource=admin'
        )

    def create_db(self, guild_id: int, **kwargs):
        db = self._client[str(guild_id)]
        for key, value in kwargs.items():
            db.create_collection(key, validator=value.schema)
            db[key].create_index(value.unique_index, unique=True)

    def get_collection(self, guild_id: int, collection: str):
        return self._client[str(guild_id)][collection]
