import requests
import json
import pytest

data = {
    "id": 1,
    "username": "username",
    "firstName": "fname",
    "lastName": "lname",
    "email": "email@example.com",
    "password": "password1",
    "phone": "12345678901",
    "userStatus": 0
}
api_url = "https://petstore.swagger.io/v2/user"


def test_create_user():
    response = requests.post(api_url, json=data)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    print(json_response)