import unittest
from order import *
from restaurant import *


class TestMyRestaurant(unittest.TestCase):
  def setUp(self):
    self.rst = Restaurant()


  def test_start_business_with_new_dish(self):
    self.assertEqual(
      self.rst.start_business_with_new_dish(['beef', 'pork', 'chicken']),
      ['beef', 'pork', 'chicken']
    )
