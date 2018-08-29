from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from itemmanager.models import Restock, RestockItem, Item


class RestockTestCase(TestCase):
    def setUp(self):
        self.item_c = Item.objects.create(
            item_name="Item C", item_price=1_000)
        self.user = User.objects.create_user('test','test@email.com','justpass')

    def test_restock_PIC(self):
        restock = Restock.objects.create(restock_PIC=self.user)
        self.assertEqual(restock.restock_PIC, self.user)

    def test_restock_stock(self):
        restock = Restock.objects.create(restock_PIC=self.user)
        restock_item = RestockItem.objects.create(restock=restock, item=self.item_c, restock_item_amount=5, restock_item_total_cost=5000)
        self.assertEqual(self.item_c.item_stock, 5)

    def test_restock_not_zero(self):
        restock = Restock.objects.create(restock_PIC=self.user)
        with self.assertRaises(ValidationError):
            restock_item = RestockItem(restock=restock, item=self.item_c, restock_item_amount=0, restock_item_total_cost=5000)
            restock_item.full_clean()

    def test_restock_not_negative(self):
        restock = Restock.objects.create(restock_PIC=self.user)
        with self.assertRaises(ValidationError):
            restock_item = RestockItem(restock=restock, item=self.item_c, restock_item_amount=-10, restock_item_total_cost=5000)
            restock_item.full_clean()

    def test_restock_unique_item(self):
        restock = Restock.objects.create(restock_PIC=self.user)
        restock_item1 = RestockItem.objects.create(restock=restock, item=self.item_c, restock_item_amount=5, restock_item_total_cost=5000)
        with self.assertRaises(IntegrityError):
            restock_item2 = RestockItem.objects.create(restock=restock, item=self.item_c, restock_item_amount=5, restock_item_total_cost=5000)