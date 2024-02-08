import configparser
from utilities.JSONFixture import JSONFixture
import requests
from utilities.readProperties import ReadConfig


class UserPage:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    base_api_url = ReadConfig.get_application_url()

    def create_user(self, user_data=None):
        api_url = self.base_api_url + "/user"

        # big plus for this approach
        data = user_data if user_data else JSONFixture.single_user_data()
        response = requests.post(api_url, json=data)
        return response

    def create_users_with_list(self, user_data):
        api_url = self.base_api_url + "/user/createWithList"
        response = requests.post(api_url, json=user_data)
        return response

    def login_user(self, username, password):
        url = f"{self.base_api_url}/user/login?"
        params = {
            "username": username,
            "password": password
        }
        response = requests.get(url, params=params)
        return response

    def logout_user(self):
        logout_url = f"{self.base_api_url}/user/logout"
        response = requests.get(logout_url)
        return response
