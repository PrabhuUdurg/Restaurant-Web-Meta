from django.test import TestCase
from web.models import Menu

class MenuItemTest(TestCase):
 def test_get_item(self):
    item = Menu.objects.create(title="IceCream", price=80, inventory=100)
    self.assertEqual(item, "IceCream : 80")