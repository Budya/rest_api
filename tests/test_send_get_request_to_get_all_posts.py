from framework.classes.api import API
from framework.classes.posts import Posts
from framework.config import Config
from framework.testdata import TestData


def test_send_get_request_to_get_all_posts():
    response = API.get_posts()
    assert response.response_status == TestData.STATUS_CODE_200.value
    assert response.is_valid_json() == Config.TRUE_VALUE.value
    assert Posts(response.data).is_sorted_by_id() == Config.TRUE_VALUE.value
