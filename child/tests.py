from django.test import TestCase
from .models import Child


# Create your tests here.
class TestChildClass(TestCase):
    """
    Child model test class that holds all test cases for the class
    """

    # Setup
    def setUp(self) -> None:
        """
        setup method to be ran before each test case
        :return:
        """
        self.new_child = Child(first_name='Pius', middle_name='Ben', surname='Bill', age=10, gender='male',
                               talent='artist', joined_at='01/02/2011')

    # Teardown
    def tearDown(self) -> None:
        """
        Teardown method to be ran before each test case
        :return:
        """
        children = Child.objects.all()
        children.delete()

    # Test instance
    def test_instance(self):
        """
        Test to check the instance of the child as defined in the setup
        :return:
        """
        self.assertTrue(isinstance(self.new_child, Child))

    # Test save child
    def test_save_child(self):
        """
        Test to check if a child id saved correctly
        :return:
        """
        self.new_child.save_child()
        children = Child.objects.all()

        self.assertTrue(len(children) > 0)

    # Test save multiple children
    def test_save_multiple_children(self):
        """
        Test to check if multiple children are saved correctly
        :return:
        """
        self.new_child.save_child()

        test_child = Child(first_name='Test', middle_name='Child', age=5, gender='female',
                           talent='singer', joined_at='01/02/2016')
        test_child.save_child()

        children = Child.objects.all()
        self.assertTrue(len(children) > 1)

    # Test delete a child
    def test_delete_child(self):
        """
        Test to check id a child can be deleted successfully
        :return:
        """
        self.new_child.save_child()
        self.new_child.delete_child()

        children = Child.objects.all()
        self.assertTrue(len(children) < 1)
