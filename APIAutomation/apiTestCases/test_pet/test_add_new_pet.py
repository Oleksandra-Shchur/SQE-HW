from pageObjects.PetPage import PetPage
from utilities.JSONFixture import JSONFixture

# Why each test in separate class?
# What else could be verified except status code?
class Test_001_Add_Pet:
    def test_add_new_pet(self):
        pet_data = JSONFixture.new_pet_data()  # Get data for new pet from JSONFixture
        pet_page = PetPage()
        response = pet_page.add_new_pet(pet_data)
        assert response.status_code == 200, 'Failed to add new pet'
