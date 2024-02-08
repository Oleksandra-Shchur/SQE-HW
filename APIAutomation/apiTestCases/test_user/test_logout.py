import logging
from pageObjects.UserPage import UserPage
from utilities.readProperties import ReadConfig


class Test_003_Logout:
    def test_logout_user(self):
        logger = logging.getLogger(__name__)
        user_name = ReadConfig.get_user_name()
        password = ReadConfig.get_password()
        user_page = UserPage()
        user_page.login_user(user_name, password)
        response = user_page.logout_user()
        assert response.status_code == 200, 'Failed to logout user'
