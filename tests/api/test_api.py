import pytest

pytestmark = [pytest.mark.api, pytest.mark.all]

class TestApi:
    "Test class for API tests"
    def test_successful_register(self, t_data, api_config):
        """ Test verifies a successful register"""
        api_helper = api_config["api_helper"]
        result = api_helper.post(t_data["path"], t_data["header"], t_data["payload"])
        assert result.status_code == 200, f"Expected response code is 200. " \
                                          f"Actual response code is {result.status_code} {result.text}"

    def test_successful_login(self, t_data, api_config):
        """ Test verifies a successful login"""
        api_helper = api_config["api_helper"]
        result = api_helper.post(t_data["path"], t_data["header"], t_data["payload"])
        assert result.status_code == 200, f"Expected response code is 200. " \
                                          f"Actual response code is {result.status_code} {result.text}"

    def test_list_resource(self, t_data, api_config):
        """ Test verifies a resource"""
        api_helper = api_config["api_helper"]
        result = api_helper.get(t_data["path"])
        assert result.status_code == 200, f"Expected response code is 200. " \
                                          f"Actual response code is {result.status_code} {result.text}"
        resources = result.json()
        actual_data = resources["data"][0]
        expected_data = dict(id=1, name="cerulean", year=2000, color="#98B2D1", pantone_value="15-4020")
        _verify_resource_data(actual_data, expected_data)


def _verify_resource_data(actual_data, expected_data, keys_to_verify=None):
    keys_list = keys_to_verify if keys_to_verify else expected_data.keys()

    for key in keys_list:
        assert actual_data[key] == expected_data[key], \
            f"Value of '{key}' from api response doesn't match, Actual: {actual_data[key]}, " \
            f"Expected: {expected_data[key]}"

    return True
