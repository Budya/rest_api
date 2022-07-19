from framework.classes.api import API
from framework.config import Config
from framework.testdata import TestData


def test_send_request_to_get_post_id_150():
    res = API.get_post_by_id(TestData.TESTING_POST_ID_150.value)
    assert res.response_status == TestData.STATUS_CODE_404.value
    assert res.is_response_body_empty() == Config.TRUE_VALUE.value
