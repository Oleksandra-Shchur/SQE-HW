import requests
import json
import pytest
import os

filepath = os.path.expanduser('~/SQE-HW/APIAutomation/Data/image.jpeg')
api_url = "https://petstore.swagger.io/v2/pet/1/uploadImage"


def test_update_pet_image():
    with open(filepath, 'rb') as file:
        files = {'file': file}
        response = requests.post(api_url, files=files)
    assert response.status_code == 200