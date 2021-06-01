from mongoengine import *

from src.modules.user.schema import User
from src.modules.round.schema import Round


class Guild(Document):
    guild_id = LongField(unique=True, required=True)
    users = EmbeddedDocumentListField(User, default=list, max_length=100)
    rounds = EmbeddedDocumentListField(Round, default=list, max_length=5)
