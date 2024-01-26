import requests
import json
import pytest

api_url = "https://petstore.swagger.io/v2/user/logout"

def test_logout_user():
    response = requests.get(api_url)
    assert response.status_code == 200