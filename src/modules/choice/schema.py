from mongoengine import *

from src.modules.user.schema import UserBet


class Choice(EmbeddedDocument):
    description = StringField(required=True, unique=True)
    bets = EmbeddedDocumentListField(UserBet, default=list)

    @property
    def total_bet(self) -> int:
        amount = 0
        for bet in self.bets:
            amount += bet.get_amount()
        return amount
