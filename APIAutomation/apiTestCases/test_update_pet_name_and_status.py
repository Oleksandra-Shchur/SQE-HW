import requests
import json
import pytest

data = {
    'petId': '1',
    'name': 'cooggie',
    'status': 'pending'
}
api_url = "https://petstore.swagger.io/v2/pet/"


def test_update_pet_name_and_status():
    response = requests.put(api_url, json=data)
    assert response.status_code == 200