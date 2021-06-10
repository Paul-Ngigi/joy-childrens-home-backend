from django.test import TestCase
from .models import Adopter


# Create your tests here.
class TestAdopterClass(TestCase):
    """
    Adopter model test class that holds all test cases for the class
    """

    # Setup
    def setUp(self) -> None:
        """
        setup method to be ran before each test case
        :return:
        """
        self.new_adopter = Adopter(passport_image='default.jpg', first_name='me', last_name='maw', surname='who',
                                   phone_number='0721212', id_number='57612', location='nai', marital_status='single')

    # Teardown
    def tearDown(self) -> None:
        """
        Teardown method to be ran before each test case
        :return:
        """
        adopters = Adopter.objects.all()
        adopters.delete()

    # Test instance
    def test_instance(self):
        """
        Test to check the instance of the adopter as defined in the setup
        :return:
        """
        self.assertTrue(isinstance(self.new_adopter, Adopter))

    # Test save adopter
    def test_save_adopter(self):
        """
        Test to check if a adopter id saved correctly
        :return:
        """
        self.new_adopter.save_adopter()
        adopters = Adopter.objects.all()

        self.assertTrue(len(adopters) > 0)

    # Test save multiple adopters
    def test_save_multiple_adopters(self):
        """
        Test to check if multiple adopters are saved correctly
        :return:
        """
        self.new_adopter.save_adopter()

        test_adopter = Adopter(first_name='Test', middle_name='Adopter', age=5, gender='female',
                               talent='singer', joined_at='01/02/2016')
        test_adopter.save_adopter()

        adopters = Adopter.objects.all()
        self.assertTrue(len(adopters) > 1)

    # Test delete a adopter
    def test_delete_adopter(self):
        """
        Test to check id a adopter can be deleted successfully
        :return:
        """
        self.new_adopter.save_adopter()
        self.new_adopter.delete_adopter()

        adopters = Adopter.objects.all()
        self.assertTrue(len(adopters) < 1)
