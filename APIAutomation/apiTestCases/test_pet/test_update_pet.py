from APIAutomation.pageObjects.PetAPIActions import PetAPIActions
from APIAutomation.utilities.JSONFixture import JSONFixture
import os


class Test_004_Update_Pet:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_of_parent_dir = os.path.dirname(os.path.dirname(current_dir))
    filepath = os.path.join(parent_of_parent_dir, 'TestData', 'image.jpeg')

    def test_update_pet_image(self):
        pet_data = JSONFixture.new_pet_data()
        pet_page = PetAPIActions()
        response = pet_page.add_new_pet(pet_data)
        assert response.status_code == 200, 'Failed to add new pet'
        pet_id = response.json()['id']
        with open(self.filepath, 'rb') as file:
            files = {'file': file}
            response = pet_page.update_pet_image(pet_id, files)
        assert response.status_code == 200, 'Failed to update pet image'

    def test_update_pet_name_and_status(self):
        pet_data = JSONFixture.new_pet_data()
        pet_page = PetAPIActions()
        response = pet_page.add_new_pet(pet_data)
        assert response.status_code == 200, 'Failed to add new pet'
        new_name = 'cooggie'
        new_status = 'pending'
        response = pet_page.update_pet_name_and_status(new_name, new_status)
        assert response.status_code == 200, 'Failed to update pet name and status'
