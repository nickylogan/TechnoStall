from django.test import TestCase
from tsmanager.models import Restock, Item

class RestockTestCase(TestCase):
  def setUp(self):
    self.item_init=Item.objects.create(item_name="Item C", item_price=1_000)
    self.item_stocked=Item.objects.create(
      item_name="Item D", item_price=1_000, item_stock=5)

  def test_restock_init(self):
    self.assertEqual(self.item_init.item_stock, 0,
                     "Wrong initial stock amount!")
    r=Restock.objects.create(item=self.item_init,
                     restock_amount=10, restock_cost=5000)
    self.assertEqual(self.item_init.item_stock, 10,
                     "Wrong amount after stock!")

  def test_restock_stocked(self):
    self.assertEqual(self.item_stocked.item_stock, 5,
                     "Wrong initial stock amount!")
    r=Restock.objects.create(item=self.item_stocked,
                     restock_amount=10, restock_cost=5000)
    self.assertEqual(self.item_stocked.item_stock,
                     15, "Wrong amount after stock!")
