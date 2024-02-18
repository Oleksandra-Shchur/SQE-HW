from APIAutomation.pageObjects.PetAPIActions import PetAPIActions
from APIAutomation.utilities.JSONFixture import JSONFixture


class Test_002_Delete_Pet:
    def test_delete_pet(self):
        pet_data = JSONFixture.new_pet_data()
        pet_page = PetAPIActions()
        response = pet_page.add_new_pet(pet_data)
        assert response.status_code == 200, 'Failed to add new pet'
        pet_id = response.json()['id']
        response = pet_page.delete_pet(pet_id)
        assert response.status_code == 200, 'Failed to delete pet'
