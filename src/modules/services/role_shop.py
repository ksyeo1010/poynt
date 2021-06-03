from src.modules.schemas import Role
from src.modules.client import Client


class RoleShopService:
    """A class that deals with the role shop collection db."""
    @staticmethod
    def add_role(guild_id: int, name: str, cost: int):
        """Add a role to the role shop.

        :param guild_id: the id to identify the db.
        :param name: the name of the role.
        :param cost: the cost of the role.
        :return: None.
        """
        role = Role(name=name, cost=cost)

        col = Client().get_collection(guild_id, 'role_shop')
        col.insert_one(role.to_dict)

    @staticmethod
    def get_role(guild_id: int, name: str) -> Role:
        """Gets a role by its privilege number.

        :param guild_id: the id to identify the db.
        :param name: the name of the role to get.
        :return: a Role object. Role(name, privilege, cost)
        """
        col = Client().get_collection(guild_id, 'role_shop')
        res = col.find_one({'name': name})

        return Role(**res)

    @staticmethod
    def get_roles(guild_id: int) -> list:
        """Get all roles.

        :param guild_id: the id to identify the db.
        :return: list of roles of roles.
                 [Role(name, cost)]
        """
        col = Client().get_collection(guild_id, 'role_shop')
        res = col.find({}, {'_id': False}).sort([('cost', -1)])

        return list(map(lambda r: Role(r['name'], r['cost']), list(res)))

    @staticmethod
    def delete_role(guild_id: int, name: str):
        col = Client().get_collection(guild_id, 'role_shop')
        col.find_one_and_delete({
            'name': name
        })
