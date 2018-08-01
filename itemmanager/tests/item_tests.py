from django.test import TestCase
from django.db.utils import IntegrityError
from itemmanager.models import Item


class ItemTestCase(TestCase):
    def setUp(self):
        self.no_desc = Item.objects.create(
            item_name="Item A", item_price=1_000)
        self.with_desc = Item.objects.create(
            item_name="Item B", item_price=2_000, description="this is a description")

    def test_item_creation(self):
        try:
            Item.objects.get(item_name="Item A")
            Item.objects.get(item_name="Item B")
        except Item.DoesNotExist:
            self.fail(
                "Unexpected DoesNotExist: Item should be created successfully!")

    def test_item_name(self):
        try:
            self.assertEqual(self.no_desc.item_name,
                             "Item A", "Wrong item_name!")
            self.assertEqual(self.with_desc.item_name,
                             "Item B", "Wrong item_name!")
        except AttributeError:
            self.fail(
                "Unexpected AttributeError for item_name: Item should have item_name attribute")

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

    def test_item_unqiueness(self):
        with self.assertRaises(IntegrityError):
            Item.objects.create(item_name="Item A", item_price=1_000)
