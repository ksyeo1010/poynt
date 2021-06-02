import pymongo

from dataclasses import dataclass, field, asdict
from typing import List

from .common import Common
from .choice import Choice


@dataclass
class Round:
    """The Round dataclass, representing a game round.

    title: a string representing the round string.
    running: a boolean representing if the prediction is running.
    choices: a list of choices for a given round.
    """
    title: str
    running: bool = field(default=True)
    choices: List[Choice] = field(default_factory=lambda: [])

    @property
    def to_dict(self):
        """Returns the class as a key-value dictionary."""
        return asdict(self)

    @staticmethod
    def get_validator():
        """Represents the unique index of a user document and the schema validator.

        :return: a dictionary containing bson properties.
        """
        return Common(
            unique_index=[('title', pymongo.ASCENDING)],
            schema={
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
        )


