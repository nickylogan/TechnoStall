from django.test import TestCase
from django.db.utils import IntegrityError
from tsmanager.models import Item

# Create your tests here.


class ItemTestCase(TestCase):
    def setUp(self):
        self.no_desc = Item.objects.create(name="Item A", item_price=1_000)
        self.with_desc = Item.objects.create(
            name="Item B", item_price=2_000, description="this is a description")

    def test_item_creation(self):
        try:
            Item.objects.get(name="Item A")
            Item.objects.get(name="Item B")
        except Item.DoesNotExist:
            self.fail(
                "Unexpected DoesNotExist: Item should be created successfully!")

    def test_name(self):
        try:
            self.assertEqual(self.no_desc.name, "Item A", "Wrong name!")
            self.assertEqual(self.with_desc.name, "Item B", "Wrong name!")
        except AttributeError:
            self.fail(
                "Unexpected AttributeError for name: Item should have name attribute")

    def test_item_price(self):
        try:
            self.assertEqual(self.no_desc.item_price, 1_000,
                             "Wrong item item_price!")
            self.assertEqual(self.with_desc.item_price,
                             2_000, "Wrong item item_price!")
        except AttributeError:
            self.fail(
                "Unexpected AttributeError for item_price: Item should have item_price attribute")

    def test_item_description(self):
        try:
            self.assertEqual(self.no_desc.description, None,
                             "Description should be blank!")
            self.assertEqual(self.with_desc.description,
                             "this is a description", "Wrong item description!")
        except AttributeError:
            self.fail(
                "Unexpected AttributeError for description: Item should have description attribute")

    # def test_item_unqiueness(self):
    #   self.assertRaises(IntegrityError,
    #     Item.objects.create(name="Item A", item_price=1_000))
