import unittest
from counter import *


class TestMyCounter(unittest.TestCase):
  def setUp(self):
    self.cnt = Counter()
    self.cnt_v2 = CounterV2()

  def test_under100(self):
    self.assertEqual(self.cnt.count([99]), 99)

  def test_under100_v2(self):
    self.assertEqual(self.cnt_v2.count([99], CustomerType.NORMAL), 99)
    self.assertEqual(self.cnt_v2.count([99], CustomerType.MEMBER), 89)
    self.assertEqual(self.cnt_v2.count([99], CustomerType.VIP), 99)

  def test_100_to_200(self):
    self.assertEqual(self.cnt.count([200]), 180)

  def test_100_to_200_v2(self):
    self.assertEqual(self.cnt_v2.count([200], CustomerType.NORMAL), 200)
    self.assertEqual(self.cnt_v2.count([200], CustomerType.MEMBER), 180)
    self.assertEqual(self.cnt_v2.count([200], CustomerType.VIP), 180)

  def test_201_to_500(self):
    self.assertEqual(self.cnt.count([500]), 400)

  def test_201_to_500_v2(self):
    self.assertEqual(self.cnt_v2.count([500], CustomerType.NORMAL), 500)
    self.assertEqual(self.cnt_v2.count([500], CustomerType.MEMBER), 450)
    self.assertEqual(self.cnt_v2.count([500], CustomerType.VIP), 400)

  def test_above_500(self):     
    self.assertEqual(self.cnt.count([600]), 400)
    self.assertEqual(self.cnt.count([1000]), 600)

  def test_above_500_v2(self):
    self.assertEqual(self.cnt_v2.count([1000], CustomerType.NORMAL), 1000)
    self.assertEqual(self.cnt_v2.count([1000], CustomerType.MEMBER), 900)
    self.assertEqual(self.cnt_v2.count([1000], CustomerType.VIP), 600)
