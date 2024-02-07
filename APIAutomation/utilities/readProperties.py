import configparser
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
config_file = os.path.join(project_dir, 'Configuration', 'config.ini')
config = configparser.RawConfigParser()
config.read(config_file)


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_user_name():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password
