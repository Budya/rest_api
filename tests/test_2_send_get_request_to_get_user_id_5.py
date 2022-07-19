from framework.classes.api import API
from framework.classes.user import User
from framework.config import Config
from framework.testdata import TestData
from framework.utils.restore_user_util import restore_user_data_from_json


def test_2_send_get_request_to_get_user_id_5():
    user_response = API.get_user_by_id(TestData.GET_USER_FROM_USERS_ID.value)
    assert user_response.response_status == TestData.STATUS_CODE_200.value
    restored_user = restore_user_data_from_json()
    user = User(user_response.data)
    assert user.compare_users_data(restored_user) == Config.TRUE_VALUE.value
