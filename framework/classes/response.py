import json
from framework.config import Config


class Response:
    def __init__(self, response):
        self.response = response
        self.data = response.json()
        self.response_status = response.status_code

    def is_valid_json(self):
        try:
            json.loads(self.response.text)
        except Exception:
            return False
        return True

    def is_response_body_empty(self):
        if self.data == Config.RESPONSE_BODY_EMPTY.value:
            return True
        else:
            return False

    def is_response_contains_posting_data(self, post_body):
        keys_check_result = []

        for i in post_body:
            if post_body[i] == self.data[i]:
                keys_check_result.append(True)

        if False not in keys_check_result and Config.POST_OBJECT_FIELD_ID.value in self.data:
            return True
        else:
            return False
