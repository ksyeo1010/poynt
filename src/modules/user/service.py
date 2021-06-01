from .schema import User


class UserService:
    @staticmethod
    def create_user(username: str):
        user = User(username=username)
        user.save()

    @staticmethod
    def get_user(username: str) -> User:
        return User.objects.get(username=username)
