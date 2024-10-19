import unittest
from src.gas_tracker import get_current_gas_price

class TestGasTracker(unittest.TestCase):

    def test_get_current_gas_price(self):
        price = get_current_gas_price()
        self.assertIsNotNone(price)
        self.assertIsInstance(price, int)
    
if __name__ == '__main__':
    unittest.main()
