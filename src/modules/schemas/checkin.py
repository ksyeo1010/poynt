from datetime import datetime, timedelta
from dataclasses import dataclass, field

from .common import Document


@dataclass
class Checkin(Document):
    """The Checkin class in a guild.

    :username: a string representing the username of a user.
    :date: the date checked in by the user.
    """
    username: str
    checkin_at: datetime = field(default=datetime.utcnow())
    expire_at: datetime = field(default=datetime.utcnow() + timedelta(seconds=24 * 59 * 60))

    @classmethod
    def get_validator(cls) -> dict:
        """Get the schema validator for a UserCheckin.

        :return: a dictionary containing bson properties.
        """
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['username', 'checkin_at', 'expire_at'],
                'properties': {
                    'username': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'checkin_at': {
                        'bsonType': 'date',
                        'description': 'must be a date and is required'
                    },
                    'expire_at': {
                        'bsonType': 'date',
                        'description': 'must be a date and is required'
                    }
                }
            }
        }

    @classmethod
    def create_index(cls, collection):
        """Create the indexes for Checkin collection."""
        collection.create_index([('username', 1)], unique=True)
        collection.create_index('expire_at', expiresAfterSeconds=0)
