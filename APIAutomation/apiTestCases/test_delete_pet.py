import requests
import json
import pytest

api_key = '1'
pet_id = 1
api_url = f"https://petstore.swagger.io/v2/pet/{pet_id}"


def test_delete_pet():
    headers = {'api_key': api_key}
    response = requests.delete(api_url, headers=headers)
    assert response.status_code == 200