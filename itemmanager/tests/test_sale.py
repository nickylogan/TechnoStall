from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from itemmanager.models import Sale, SaleItem, Item


class SaleTestCase(TestCase):
    def setUp(self):
        self.item_d = Item.objects.create(
            item_name="Item D", item_price=1_000, item_stock=100)
        self.user = User.objects.create_user('test','test@email.com','justpass')
        self.sale = Sale.objects.create(user_on_duty=self.user)

    def test_sale(self):
        sale_item = SaleItem.objects.create(sale=self.sale, item=self.item_d, sale_amount=5, sale_price=10000)
        self.assertEqual(self.item_d.item_stock, 95)

    def test_sale_not_zero(self):
        with self.assertRaises(ValidationError):
            sale_item = SaleItem.objects.create(sale=self.sale, item=self.item_d, sale_amount=0, sale_price=10000)
            sale_item.full_clean()

    def test_sale_not_negative(self):
        with self.assertRaises(ValidationError):
            sale_item = SaleItem.objects.create(sale=self.sale, item=self.item_d, sale_amount=-5, sale_price=10000)
            sale_item.full_clean()

    def test_sale_under_stock(self):
        with self.assertRaises(ValidationError):
            sale_item = SaleItem.objects.create(sale=self.sale, item=self.item_d, sale_amount=1000, sale_price=10000)
            sale_item.full_clean()