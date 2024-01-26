import requests
import json
import pytest

data = {
    'id': 1,
    'name': 'doggie',
    'status': 'available'
}
api_url = "https://petstore.swagger.io/v2/pet"


def test_add_new_pet():
    response = requests.post(api_url, json=data)
    assert response.status_code == 200