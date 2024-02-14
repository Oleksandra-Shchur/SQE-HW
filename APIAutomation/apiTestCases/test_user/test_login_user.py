import logging
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig


class Test_002_Login:
    def test_login_user(self):
        # logger is not used
        logger = logging.getLogger(__name__)
        user_name = ReadConfig.get_user_name()
        password = ReadConfig.get_password()
        user_page = UserPage()
        response = user_page.login_user(user_name, password)
        assert response.status_code == 200, 'Failed to login user'
