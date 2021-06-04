from src.modules.services import RoleShopService


class ShopController:

    @staticmethod
    def add_role(ctx, role_name, role_cost):
        guild_id = ctx.guild.id
        RoleShopService.add_role(guild_id, role_name, role_cost)

    @staticmethod
    def display_shop(ctx):
        guild_id = ctx.guild.id
        list_of_roles = RoleShopService.get_roles(guild_id)
        string_list = []
        for role in list_of_roles:
            role_name = role.name
            role_cost = role.cost
            role_string = f"{role_name}: {role_cost} points."
            string_list.append(role_string)
        return '\n'.join(string_list)

    @staticmethod
    def get_role_from_name(ctx, role_name):
        guild_id = ctx.guild.id
        role_object = RoleShopService.get_role(guild_id, role_name)
        return role_object.cost



# the roles that admin adds -> save to db -> each time a user buys something in the flexshop
# -> save what they bought -> add command that changes the role name -> then they can change the colour of the role.