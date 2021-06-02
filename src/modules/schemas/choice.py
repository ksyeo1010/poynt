from dataclasses import dataclass, field, asdict
from typing import List

from .user import UserBet


@dataclass
class Choice:
    """The choice dataclass.

    option: the option name of choice.
    bets: a list of bets made by users.
    """
    option: str
    bets: List[UserBet] = field(default_factory=lambda: [])

    @property
    def to_dict(self):
        """Returns the class as a key-value dictionary."""
        return asdict(self)

    @staticmethod
    def get_sub_validator():
        """ The sub-validator field of the choice embedded document.

        :return: a dictionary containing bson properties.
        """
        return {
            'bsonType': 'array',
            'uniqueItems': True,
            'additionalProperties': False,
            'items': {
                'bsonType': 'object',
                'required': ['option'],
                'properties': {
                    'option': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'bets': UserBet.get_sub_validator()
                }
            }
        }
