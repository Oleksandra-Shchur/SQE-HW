import configparser
import requests
from utilities.readProperties import ReadConfig


class PetPage:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    base_api_url = ReadConfig.get_application_url()

    def add_new_pet(self, pet_data):
        api_url = self.base_api_url + "/pet"
        response = requests.post(api_url, json=pet_data)
        return response

    def delete_pet(self, pet_id):
        delete_url = f"{self.base_api_url}/pet/{pet_id}"
        response = requests.delete(delete_url)
        return response

    def update_pet_name_and_status(self, name, status):
        api_url = f"{self.base_api_url}/pet/"
        update_data = {"name": name, "status": status}
        response = requests.put(api_url, json=update_data)
        return response

    def update_pet_image(self, pet_id, file):
        api_url = f"{self.base_api_url}/pet/{pet_id}/uploadImage"
        response = requests.post(api_url, files=file)
        return response
