import json
import os

from framework.config import Config


def restore_user_data_from_json():
    with open(os.path.join(Config.ASSETS_FOLDER.value, 'data.json')) as json_file:
        return json.load(json_file)
