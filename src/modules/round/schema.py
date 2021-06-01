from mongoengine import *

from src.modules.choice.schema import Choice


class Round(EmbeddedDocument):
    title = StringField(required=True, unique=True)
    choices = EmbeddedDocumentListField(Choice, default=list)

    @property
    def total_amount(self) -> int:
        amount = 0
        for choice in self.choices:
            amount += choice.total_bet()
        return amount
