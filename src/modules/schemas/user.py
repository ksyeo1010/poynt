from typing import Optional
from dataclasses import dataclass, field

from .common import Document, EmbeddedDocument


@dataclass
class User(Document):
    """The User class in a guild.

    :username: a string representing the username of a user.
    :points: an integer representing the total amount of points of a user.
    """
    username: str
    points: Optional[int] = field(default=500)

    @classmethod
    def create_index(cls, collection):
        """Create the indexes for User collection."""
        collection.create_index([('username', 1)], unique=True)

    @classmethod
    def get_validator(cls) -> dict:
        """Get the schema validator for a User.

        :return: a dictionary containing bson properties.
        """
        return {
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


@dataclass
class UserBet(EmbeddedDocument):
    """The user betting class.

    :username: a string representing the username of a user.
    :amount: the amount bet by the user.
    """
    username: str
    amount: int

    @classmethod
    def get_sub_validator(cls) -> dict:
        """Get the schema embedded validator for a UserBet.

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
