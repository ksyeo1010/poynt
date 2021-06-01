from mongoengine import *


class User(EmbeddedDocument):
    username = StringField(unque=True, max_length=256, required=True)
    points = IntField(min_value=0, default=500)


class UserBet(EmbeddedDocument):
    username = StringField(max_length=256, required=True)
    amount = IntField(min_value=0, required=True)

    @property
    def get_amount(self):
        return self.amount
