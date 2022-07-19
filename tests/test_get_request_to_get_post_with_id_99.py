from framework.classes.api import API
from framework.classes.post import Post
from framework.config import Config
from framework.testdata import TestData


def test_get_request_to_get_post_with_id_99():
    res = API.get_post_by_id(TestData.TESTING_POST_ID_99.value)
    assert res.response_status == TestData.STATUS_CODE_200.value
    post = Post(res.data)
    assert post.is_id_equal(TestData.TESTING_POST_ID_99.value) == Config.TRUE_VALUE.value
    assert post.is_user_id_equal(TestData.TESTING_POST_99_USER_ID.value) == Config.TRUE_VALUE.value
    assert post.is_body_equal(TestData.STRING_EMPTY.value) != Config.TRUE_VALUE.value
    assert post.is_title_equal(TestData.STRING_EMPTY.value) != Config.TRUE_VALUE.value
