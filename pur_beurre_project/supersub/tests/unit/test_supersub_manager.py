from django.test import TestCase
from supersub.manager.supersub_manager import SupersubManager

# Create your tests here.

class SupersubManagerTest(TestCase):
    """
    """
    def setUp(self):
        self.data = SupersubManager()._get_data()

    def test__get_data(self):
        """
        """
        data = {
            'ctxt': {},
            'render':"",
            'redirect':""
        }
        self.assertEqual(self.data, data)