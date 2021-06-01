from mongoengine import *


class User(EmbeddedDocument):
    username = StringField(max_length=256, required=True)
    points = IntField(min_value=0, default=500)
