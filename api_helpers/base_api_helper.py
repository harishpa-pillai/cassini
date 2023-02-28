import json

import requests


class BaseAPI:
    """API Base class, with basic Rest API methods"""

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, path, header, payload):
        """ Send API Post request, and returns the result object
        Args:
            path: API endpoint, String
            header: API header, Dict
            payload: API payload, Dict
        Returns:
            Result from API post request, if post is successful
        Raises:
            BaseAPIException
        """

        endpoint = f"{self.base_url}{path}"
        if header["Content-Type"] == "application/json":
            payload = json.dumps(payload)

        try:
            result = requests.post(endpoint, data=payload, headers=header)
        except Exception:
            raise BaseAPIException("Exception while executing API post request")
        return result

    def get(self, path, params=None):
        """ Send API Get request, and returns the result object
        Args:
            path: API endpoint, String
            params: API parameters, Dict
        Returns:
            Result from API get request, if get is successful
        Raises:
            BaseAPIException
        """

        endpoint = f"{self.base_url}{path}"
        try:
            result = requests.get(endpoint, params)
        except Exception:
            raise BaseAPIException("Exception while executing API get request")
        return result


class BaseAPIException(Exception):
    """Custom Exception class for BaseAPI"""
    pass
