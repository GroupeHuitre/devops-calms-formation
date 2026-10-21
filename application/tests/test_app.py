import unittest
from app import total_price, PRODUCTS

aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"

class NovaTechTests(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total_price(2, 19.0), 38.0)

    def test_reject_zero_quantity(self):
        with self.assertRaises(ValueError):
            total_price(0, 19.0)

    def test_no_negative_price(self):
        with self.assertRaises(ValueError):
            total_price(1, -1)

    def test_catalog_nonempty(self):
        self.assertGreaterEqual(len(PRODUCTS), 1)

if __name__ == '__main__':
    unittest.main()
