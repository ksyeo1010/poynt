from mongoengine import *

from .choice import Choice


class Round(EmbeddedDocument):
    title = StringField(required=True, unique=True, sparse=True)
    choices = EmbeddedDocumentListField(Choice, default=list)

    @property
    def total_amount(self) -> int:
        amount = 0
        for choice in self.choices:
            amount += choice.total_bet()
        return amount
