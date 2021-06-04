from dataclasses import dataclass, field
from typing import List

from .common import Document
from .choice import Choice


@dataclass
class Round(Document):
    """The Round dataclass, representing a game round.

    title: a string representing the round string.
    running: a boolean representing if the prediction is running.
    choices: a list of choices for a given round.
    """
    title: str
    running: bool = field(default=True)
    choices: List[Choice] = field(default_factory=lambda: [])

    @classmethod
    def create_index(cls, collection):
        """Create the indexes for Round collection."""
        collection.create_index([('title', 1)], unique=True)

    @classmethod
    def get_validator(cls) -> dict:
        """Get the schema validator for a Round.

        :return: a dictionary containing bson properties.
        """
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['title', 'running'],
                'properties': {
                    'title': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'running': {
                        'bsonType': 'bool',
                        'description': 'must be a boolean and is required'
                    },
                    'choices': Choice.get_sub_validator()
                }
            }
        }
