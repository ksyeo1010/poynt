from mongoengine import *

from .user import User
from .round import Round


class Guild(Document):
    guild_id = LongField(unique=True, required=True)
    users = EmbeddedDocumentListField(User, default=list, max_length=100)
    rounds = EmbeddedDocumentListField(Round, default=list, max_length=5)
