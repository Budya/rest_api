from enum import Enum
from framework.assets.dir_path import assets_folder


class Config(Enum):
    BASE_URL = "https://jsonplaceholder.typicode.com"
    GET_POSTS = "/posts"
    ADD_POST = "/posts"
    GET_USERS = "/users"
    RANDOM_STRING_UTIL_LINE = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    RANDOM_STRING_UTIL_LENGTH = 10
    RESPONSE_BODY_EMPTY = {}
    POST_OBJECT_FIELD_ID = "id"
    USER_OBJECT_FIELD_ID = "id"
    TRUE_VALUE = True
    ASSETS_FOLDER = assets_folder
