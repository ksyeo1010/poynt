from mongoengine import *

from src.modules.user.schema import User


class Guild(Document):
    guild_id: IntField(required=True)
    users: ListField(ReferenceField(User), max_length=100)
