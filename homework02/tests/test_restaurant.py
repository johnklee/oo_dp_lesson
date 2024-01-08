import unittest
from restaurant import *


class TestMyRestaurant(unittest.TestCase):
  def setUp(self):
    self.rst = Restaurant()


  def test_start_business_with_new_dish(self):
    self.assertEquals(
      self.rst.start_business_with_new_dish(),
      ['beef', 'pork', 'chicken']
    )