from APIAutomation.pageObjects.UserAPIActions import UserAPIActions
from APIAutomation.utilities.JSONFixture import JSONFixture


class Test_001_Create_User:

    def test_create_single_user(self):
        user_data = JSONFixture.single_user_data()
        user_page = UserAPIActions()
        response = user_page.create_user(user_data)
        assert response.status_code == 200, 'Failed to add new user'

    def test_create_multiple_users(self):
        user_data = JSONFixture.multiple_user_data()
        user_page = UserAPIActions()
        response = user_page.create_users_with_list(user_data)
        assert response.status_code == 200, 'Failed to add multiple users'
