from framework.classes.api import API
from framework.config import Config
from framework.testdata import TestData
from framework.utils.create_post_body_util import create_post_body_util


def test_send_post_request_with_data():
    post_body = create_post_body_util()
    res = API.add_post_by_id(TestData.ADD_POST_ID.value, post_body)
    assert res.response_status == TestData.STATUS_CODE_201.value
    assert res.is_response_contains_posting_data(post_body) == Config.TRUE_VALUE.value
