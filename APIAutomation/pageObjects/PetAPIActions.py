import requests
import configparser
from APIAutomation.utilities.JSONFixture import JSONFixture
from APIAutomation.utilities.readProperties import ReadConfig


class PetAPIActions:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    base_api_url = ReadConfig.get_application_url()

    def add_new_pet(self, pet_data=None):
        api_url = self.base_api_url + "/pet"
        data = pet_data if pet_data else JSONFixture.new_pet_data()
        response = requests.post(api_url, json=data)
        return response

    def delete_pet(self, pet_id=None):
        pet_id = pet_id if pet_id else JSONFixture.new_pet_data()['id']
        delete_url = f"{self.base_api_url}/pet/{pet_id}"
        response = requests.delete(delete_url)
        return response

    def update_pet_name_and_status(self, name, status):
        api_url = f"{self.base_api_url}/pet/"
        data = {
            "name": name if name else JSONFixture.update_pet_data()['name'],
            "status": status if status else JSONFixture.update_pet_data()['status']
        }
        response = requests.put(api_url, json=data)
        return response

    def update_pet_image(self, pet_id, file):
        pet_id = pet_id if pet_id else JSONFixture.new_pet_data()['id']
        api_url = f"{self.base_api_url}/pet/{pet_id}/uploadImage"
        response = requests.post(api_url, files=file)
        return response
