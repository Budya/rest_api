from framework.classes.user import User
from framework.config import Config


class Users:
    def __init__(self, list_of_users):
        self.users = list_of_users

    def get_user_by_id(self, id_):
        for i in range(len(self.users)):
            if self.users[i][Config.USER_OBJECT_FIELD_ID.value] == id_:
                return User(self.users[i])

        print("No users found")
