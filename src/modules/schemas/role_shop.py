import pymongo
from dataclasses import dataclass, asdict

from .common import Common


@dataclass
class Role:
    """The RoleShop class for the guild.

    :name: a string representing the name of the item.
    :privilege: an integer representing the privilege of the item.
    :cost: the cost of item.
    """
    name: str
    privilege: int
    cost: int

    @property
    def to_dict(self):
        """Returns the dataclass as a key-value dictionary."""
        return asdict(self)

    @staticmethod
    def get_validator() -> Common:
        """Represents the unique index of a role shop document and the schema validator.

        :return: a dictionary containing bson properties.
        """
        return Common(
            unique_index=[('privilege', pymongo.ASCENDING)],
            schema={
                '$jsonSchema': {
                    'bsonType': 'object',
                    'required': ['name', 'item_type', 'hierarchy', 'cost'],
                    'properties': {
                        'name': {
                            'bsonType': 'string',
                            'description': 'must be a string and is required'
                        },
                        'privilege': {
                            'bsonType': 'int',
                            'minimum': 1,
                            'description': 'must be an unique integer greater than 1 and is required'
                        },
                        'cost': {
                            'bsonType': 'int',
                            'minimum': 0,
                            'description': 'must be an integer greater than 0 and is required'
                        }
                    }
                }
            }
        )
