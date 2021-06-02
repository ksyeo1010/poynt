from dataclasses import dataclass, field, asdict
from typing import List

from .common import Common
from .user import UserBet


@dataclass
class Choice:
    option: str
    bets: List[UserBet] = field(default_factory=lambda: [])

    @property
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def get_sub_validator():
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
