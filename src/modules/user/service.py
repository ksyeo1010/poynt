from schema import User


class UserService:
    @staticmethod
    def create_user(self, username: str):
        user = User(username)
        user.save()

    @staticmethod
    def get_user(self, username: str) -> User:
        return User.objects.get(username=username)
