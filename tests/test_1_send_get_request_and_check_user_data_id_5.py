from framework.classes.api import API
from framework.classes.users import Users
from framework.config import Config
from framework.testdata import TestData


def test_send_get_request_and_check_user_data_id_5():
    users_res = API.get_users()
    assert users_res.is_valid_json() == Config.TRUE_VALUE.value
    assert users_res.response_status == TestData.STATUS_CODE_200.value
    users_list = Users(users_res.data)
    user = users_list.get_user_by_id(TestData.GET_USER_FROM_USERS_ID.value)
    assert user.compare_users_data(TestData.USER_DATA_FOR_VALIDATION.value) == Config.TRUE_VALUE.value

    user.store_user_data()
