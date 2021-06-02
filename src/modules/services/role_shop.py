from src.modules.schemas.role_shop import Role
from src.modules.client import Client


class RoleShopService:
    """A class that deals with the role shop collection db."""
    @staticmethod
    def add_role(guild_id: int, name: str, privilege: int, cost: int):
        """Add a role to the role shop.

        :param guild_id: the id to identify the db.
        :param name: the name of the role.
        :param privilege: the privilege level of the role.
        :param cost: the cost of the role.
        :return: None.
        """
        role = Role(name=name, privilege=privilege, cost=cost)

        col = Client().get_collection(guild_id, 'role_shop')
        col.insert_one(role.to_dict)

    @staticmethod
    def get_role_by_privilege(guild_id: int, privilege: int) -> Role:
        """Gets a role by its privilege number.

        :param guild_id: the id to identify the db.
        :param privilege: the privilege to get.
        :return: a Role object. Role(name, privilege, cost)
        """
        col = Client().get_collection(guild_id, 'role_shop')
        res = col.find_one({'privilege': privilege})

        return Role(**res)

    @staticmethod
    def get_roles(guild_id: int) -> list:
        """Get all roles.

        :param guild_id: the id to identify the db.
        :return: list of roles of roles.
                 [Role(name, privilege, cost)]
        """
        col = Client().get_collection(guild_id, 'role_shop')
        res = col.find({}, {'_id': False})

        return list(map(lambda r: Role(r['name'], r['privilege'], r['cost']), list(res)))

    @staticmethod
    def delete_role(guild_id: int, privilege: int):
        col = Client().get_collection(guild_id, 'role_shop')
        col.find_one_and_delete({
            'privilege': privilege
        })
