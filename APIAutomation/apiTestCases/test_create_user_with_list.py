import requests
import json
import pytest

data = [
    {
        'id': 1,
        'username': 'myname',
        'firstName': 'fname',
        'lastName': 'lname',
        'email': 'email@gmail.com',
        'password': 'password',
        'phone': '1234567890',
        'userStatus': 1
    },
    {
        'id': 2,
        'username': 'myname2',
        'firstName': 'fname2',
        'lastName': 'lname2',
        'email': 'email2@gmail.com',
        'password': 'password2',
        'phone': '21234567890',
        'userStatus': 0
    }
]
api_url = "https://petstore.swagger.io/v2/user/createWithList"


def test_create_users_with_list():
    response = requests.post(api_url, json=data)
    assert response.status_code == 200