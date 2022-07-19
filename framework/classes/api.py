import requests
from framework.config import Config
from framework.classes.response import Response


class API:
    @staticmethod
    def get_posts():
        return Response(requests.get(Config.BASE_URL.value + Config.GET_POSTS.value))

    @staticmethod
    def get_post_by_id(id_):
        return Response(requests.get(Config.BASE_URL.value + Config.GET_POSTS.value + f"/{id_}"))

    @staticmethod
    def add_post_by_id(id_, post_body):
        post_body["userId"] = str(id_)
        return Response(requests.post(Config.BASE_URL.value + Config.ADD_POST.value, data=post_body))

    @staticmethod
    def get_users():
        return Response(requests.get(Config.BASE_URL.value + Config.GET_USERS.value))

    @staticmethod
    def get_user_by_id(id_):
        return Response(requests.get(Config.BASE_URL.value + Config.GET_USERS.value + f"/{id_}"))
