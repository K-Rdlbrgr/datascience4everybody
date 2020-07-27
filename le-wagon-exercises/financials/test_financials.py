import unittest
from financials import forward_price, short_pnl

class TestFinancials(unittest.TestCase):
    def test_forward_price_no_interest_rate(self):
        self.assertEqual(forward_price(100, 0, 1), 100)
        self.assertEqual(forward_price(100, 0, 2), 100)
        self.assertEqual(forward_price(100, 0, 3), 100)
        self.assertEqual(forward_price(100, 0, 4), 100)
        self.assertEqual(forward_price(100, 0, 5), 100)
    
    def test_forward_price_with_interest_date_does_rounding(self):
        self.assertEqual(forward_price(100, 0.02, 1), 102.02)
        self.assertEqual(forward_price(100, 0.02, 2), 104.08)
        self.assertEqual(forward_price(100, 0.02, 3), 106.18)
        self.assertEqual(forward_price(100, 0.02, 4), 108.33)
        self.assertEqual(forward_price(100, 0.02, 5), 110.52)
        
    def test_pnl_is_positive(self):
        self.assertEqual(short_pnl([ 100, 140, 200 ], [ 110, 120, 180 ]), 30)
        
    def test_pnl_is_negative(self):
        self.assertEqual(short_pnl([ 100, 140, 200 ], [ 90, 160, 230 ]), -40)

if __name__ == '__main__':
    unittest.main()
