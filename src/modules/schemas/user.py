import pymongo
from typing import Optional
from dataclasses import dataclass, field, asdict

from .common import Common


@dataclass
class User:
    """The User class in a guild.

    :username: a string representing the username of a user.
    :points: an integer representing the total amount of points of a user.
    """
    username: str
    points: Optional[int] = field(default=500)

    @property
    def to_dict(self):
        """Returns the dataclass as a key-value dictionary."""
        return asdict(self)

    @staticmethod
    def get_validator() -> Common:
        """Represents the unique index of a user document and the schema validator.

        :return: a dictionary containing bson properties.
        """
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
    """The user betting class.

    :username: a string representing the username of a user.
    :amount: the amount bet by the user.
    """
    username: str
    amount: int

    @property
    def to_dict(self):
        """Returns the class as a key-value dictionary."""
        return asdict(self)

    @staticmethod
    def get_sub_validator() -> dict:
        """ The sub-validator field of the choice embedded document.

        :return: a dictionary containing bson properties.
        """
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
