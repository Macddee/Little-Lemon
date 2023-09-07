from django.test import TestCase
from Restaurent.models import *

class MenuItemTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=0.8, inventory=200)
        self.assertEqual(item, 'IceCream')