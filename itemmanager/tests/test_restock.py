from django.test import TestCase
from django.core.exceptions import ValidationError
from itemmanager.models import Restock, RestockItem, Item


class RestockTestCase(TestCase):
    def setUp(self):
        self.item_c = Item.objects.create(
            item_name="Item C", item_price=1_000)

    def test_restock(self):
        restock = Restock.objects.create(restock_PIC="personA")
        restock_item = RestockItem.objects.create(restock=restock, item=self.item_c, restock_item_amount=5, restock_item_total_cost=5000)
        self.assertEqual(self.item_c.item_stock, 5)

    def test_restock_not_zero(self):
        restock = Restock.objects.create(restock_PIC="personB")
        with self.assertRaises(ValidationError):
            restock_item = RestockItem(restock=restock, item=self.item_c, restock_item_amount=0, restock_item_total_cost=5000)
            restock_item.full_clean()

    def test_restock_not_negative(self):
        restock = Restock.objects.create(restock_PIC="personC")
        with self.assertRaises(ValidationError):
            restock_item = RestockItem(restock=restock, item=self.item_c, restock_item_amount=-10, restock_item_total_cost=5000)
            restock_item.full_clean()
