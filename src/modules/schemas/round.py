import pymongo

from dataclasses import dataclass, field, asdict
from typing import List

from .common import Common
from .choice import Choice


@dataclass
class Round:
    title: str
    choices: List[Choice] = field(default_factory=lambda: [])

    @property
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def get_validator():
        return Common(
            unique_index=[('title', pymongo.ASCENDING)],
            schema={
                '$jsonSchema': {
                    'bsonType': 'object',
                    'required': ['title'],
                    'properties': {
                        'title': {
                            'bsonType': 'string',
                            'description': 'must be a string and is required'
                        },
                        'choices': Choice.get_sub_validator()
                    }
                }
            }
        )


