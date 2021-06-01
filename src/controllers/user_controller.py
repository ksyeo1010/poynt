from src.modules.user.service import UserService


class UserController:
    @staticmethod
    def add_users(ctx_members):
        for member in ctx_members:
            UserService.create_user(str(member))

    @staticmethod
    def add_new_user(member):
        UserService.create_user(str(member))
