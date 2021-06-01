from mongoengine import *

from src.modules.user.schema import User


class Guild(Document):
    guild_id = LongField(unique=True, required=True)
    users = ListField(ReferenceField(User), default=list, max_length=100)
