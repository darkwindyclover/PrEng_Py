import unittest
from fact import Factorial

class TestFactorial(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.fact = Factorial()
  #Each test method starts with the keyword test_
  def test_calculate(self):
    self.assertEqual(self.fact.calculate(5), 120)
  def test_calculate_zero(self):
    self.assertEqual(self.fact.calculate(0), 1)
  def test_calculate_exeption(self):
    with self.assertRaises(ValueError):
        self.fact.calculate(-1)
