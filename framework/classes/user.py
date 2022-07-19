import json
import os
from framework.config import Config


class User:
    def __init__(self, user_data):
        self.user = user_data
        self.user_data = dict(user_data)

    def __str__(self):
        return str(self.user_data)

    def store_user_data(self):
        with open(os.path.join(Config.ASSETS_FOLDER.value, 'data.json'), 'w') as f:
            json.dump(self.user, f)

    def compare_users_data(self, data):
        if self.user_data == data:
            return True
        else:
            return False
