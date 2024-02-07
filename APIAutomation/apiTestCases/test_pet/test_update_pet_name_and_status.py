from pageObjects.PetPage import PetPage
from utilities.JSONFixture import JSONFixture


class Test_005_Update_Pet_Name_And_Status:

    def test_update_pet_name_and_status(self):
        pet_data = JSONFixture.new_pet_data()
        pet_page = PetPage()
        response = pet_page.add_new_pet(pet_data)
        assert response.status_code == 200, 'Failed to add new pet'
        new_name = 'cooggie'
        new_status = 'pending'
        response = pet_page.update_pet_name_and_status(new_name, new_status)
        assert response.status_code == 200, 'Failed to update pet name and status'
