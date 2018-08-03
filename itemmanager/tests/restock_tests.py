from django.test import TestCase
from itemmanager.models import Restock, RestockItem, Item


class RestockTestCase(TestCase):
    def setUp(self):
        self.item_c = Item.objects.create(
            item_name="Item C", item_price=1_000)
        self.item_d = Item.objects.create(
            item_name="Item D", item_price=1_000, item_stock=5)

    # TODO: IMPLEMENT NEW TEST CASES!!!
