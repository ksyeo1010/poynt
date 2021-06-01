from mongoengine import *


class User(Document):
    username = StringField(max_length=256, required=True)
    points = IntField(min_value=0, default=500)
