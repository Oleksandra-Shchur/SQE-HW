class JSONFixture:
    @staticmethod
    def single_user_data():
        return {
            "id": 1,
            "username": "username",
            "firstName": "fname",
            "lastName": "lname",
            "email": "email@example.com",
            "password": "password1",
            "phone": "12345678901",
            "userStatus": 0
        }

    @staticmethod
    def multiple_user_data():
        return [
            {
                'id': 1,
                'username': 'myname',
                'firstName': 'fname',
                'lastName': 'lname',
                'email': 'email@gmail.com',
                'password': 'password',
                'phone': '1234567890',
                'userStatus': 1
            },
            {
                'id': 2,
                'username': 'myname2',
                'firstName': 'fname2',
                'lastName': 'lname2',
                'email': 'email2@gmail.com',
                'password': 'password2',
                'phone': '21234567890',
                'userStatus': 0
            }
        ]

    @staticmethod
    def new_pet_data():
        return {
            'id': 1,
            'name': 'doggie',
            'status': 'available'
        }

    @staticmethod
    def update_pet_data():
        return {
            'petId': '1',
            'name': 'cooggie',
            'status': 'pending'
        }
