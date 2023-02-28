import pytest

from api_helpers.base_api_helper import BaseAPI


@pytest.fixture(scope="function")
def t_data(request):
    api_data = {}
    test_name = request.node.name

    if test_name == "test_successful_register":
        api_data["header"] = {"Content-Type": "application/json"}
        api_data["payload"] = {"email": "eve.holt@reqres.in", "password": "pistol"}
        api_data["path"] = "/register"
    elif test_name == "test_successful_login":
        api_data["header"] = {"Content-Type": "application/json"}
        api_data["payload"] = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        api_data["path"] = "/login"
    elif test_name == "test_list_resource":
        api_data["path"] = "/unknown"
    return api_data


@pytest.fixture(scope="class")
def api_config():
    base_url = "https://reqres.in/api"
    api_config = {"api_helper": BaseAPI(base_url), "base_url": base_url}
    return api_config
