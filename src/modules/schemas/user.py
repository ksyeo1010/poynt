import pymongo
from typing import Optional
from dataclasses import dataclass, field, asdict

from .common import Common


@dataclass
class User:
    username: str
    points: Optional[int] = field(default=500)

    @property
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def get_validator() -> Common:
        return Common(
            unique_index=[('username', pymongo.ASCENDING)],
            schema={
                '$jsonSchema': {
                    'bsonType': 'object',
                    'required': ['username'],
                    'properties': {
                        'username': {
                            'bsonType': 'string',
                            'description': 'must be a string and is required'
                        },
                        'points': {
                            'bsonType': 'int',
                            'minimum': 0,
                            'description': 'must be an integer greater than 0'
                        }
                    }
                }
            }
        )


@dataclass
class UserBet:
    username: str
    amount: int

    @property
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def get_sub_validator() -> dict:
        return {
            'bsonType': 'array',
            'uniqueItems': False,
            'additionalProperties': False,
            'items': {
                'bsonType': 'object',
                'required': ['username', 'amount'],
                'properties': {
                    'username': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'amount': {
                        'bsonType': 'int',
                        'minimum': 1,
                        'description': 'must be an integer greater than 0'
                    }
                }
            }
        }
