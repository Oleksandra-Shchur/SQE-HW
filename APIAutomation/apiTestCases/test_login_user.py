import requests
import json
import pytest

api_url = "https://petstore.swagger.io/v2/user/login?username=username&password=password1"


def test_login_user():
    response = requests.get(api_url)
    assert response.status_code == 200