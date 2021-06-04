from dataclasses import dataclass

from .common import Document


@dataclass
class Role(Document):
    """The RoleShop class for the guild.

    :name: a string representing the name of the item.
    :cost: the cost of item.
    """
    name: str
    cost: int

    @classmethod
    def create_index(cls, collection):
        """Create the indexes for Role collection."""
        collection.create_index([('name', 1)], unique=True)

    @classmethod
    def get_validator(cls) -> dict:
        """Get the schema validator for a Role.

        :return: a dictionary containing bson properties.
        """
        return {
            '$jsonSchema': {
                'bsonType': 'object',
                'required': ['name', 'cost'],
                'properties': {
                    'name': {
                        'bsonType': 'string',
                        'description': 'must be a string and is required'
                    },
                    'cost': {
                        'bsonType': 'int',
                        'minimum': 0,
                        'description': 'must be an integer greater than 0 and is required'
                    }
                }
            }
        }
