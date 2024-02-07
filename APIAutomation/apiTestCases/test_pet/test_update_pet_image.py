from pageObjects.PetPage import PetPage
from utilities.JSONFixture import JSONFixture
import os


class Test_004_Update_Pet_Image:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_of_parent_dir = os.path.dirname(os.path.dirname(current_dir))
    filepath = os.path.join(parent_of_parent_dir, 'TestData', 'image.jpeg')

    def test_update_pet_image(self):
        pet_data = JSONFixture.new_pet_data()
        pet_page = PetPage()
        response = pet_page.add_new_pet(pet_data)
        assert response.status_code == 200, 'Failed to add new pet'
        pet_id = response.json()['id']
        with open(self.filepath, 'rb') as file:
            files = {'file': file}
            response = pet_page.update_pet_image(pet_id, files)
        assert response.status_code == 200, 'Failed to update pet image'
