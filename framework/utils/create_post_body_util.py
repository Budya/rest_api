from framework.utils.random_string_util import randstring


def create_post_body_util():
    return {
        "title": randstring(),
        "body": randstring()
    }
