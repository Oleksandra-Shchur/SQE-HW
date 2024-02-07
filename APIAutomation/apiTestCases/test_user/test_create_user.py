import logging
from pageObjects.UserPage import UserPage
from utilities.JSONFixture import JSONFixture


class Test_001_Create_User:

    def test_create_single_user(self):
        logger = logging.getLogger(__name__)
        user_data = JSONFixture.single_user_data()
        user_page = UserPage()
        response = user_page.create_user(user_data)
        assert response.status_code == 200, 'Failed to add new user'

    def test_create_multiple_users(self):
        logger = logging.getLogger(__name__)
        user_data = JSONFixture.multiple_user_data()
        user_page = UserPage()
        response = user_page.create_users_with_list(user_data)
        assert response.status_code == 200, 'Failed to add multiple users'
