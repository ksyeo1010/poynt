from dataclasses import dataclass, field, asdict
from typing import List

from .user import UserBet
from .common import Common, EmbeddedDocument


@dataclass
class Choice(EmbeddedDocument):
    """The choice dataclass.

    option: the option name of choice.
    winner: a boolean representing if the choice is a winner.
    bets: a list of bets made by users.
    """
    option: str
    winner: bool = field(default=False)
    bets: List[UserBet] = field(default_factory=lambda: [])

    @classmethod
    def get_sub_validator(cls):
        """ The sub-validator field of the choice embedded document.

        :return: a dictionary containing bson properties.
        """
        return {
            'bsonType': 'array',
            'uniqueItems': True,
            'additionalProperties': False,
            'items': {
                'bsonType': 'object',
                'required': ['option', 'winner'],
                'properties': {
                    'option': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'winner': {
                        'bsonType': 'bool',
                        'description': 'must be a boolean and is required'
                    },
                    'bets': UserBet.get_sub_validator()
                }
            }
        }


@dataclass
class ChoiceTotal(Common):
    """The ChoiceTotal dataclass representing the total amount in an choice."""
    option: str
    total: int
