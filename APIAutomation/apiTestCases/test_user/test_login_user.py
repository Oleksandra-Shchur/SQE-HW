from APIAutomation.pageObjects.UserAPIActions import UserAPIActions
from APIAutomation.utilities.readProperties import ReadConfig


class Test_002_Login:
    def test_login_user(self):
        user_name = ReadConfig.get_user_name()
        password = ReadConfig.get_password()
        user_page = UserAPIActions()
        response = user_page.login_user(user_name, password)
        assert response.status_code == 200, 'Failed to login user'
