import unittest
from scals import eq_impl

class TestScals(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(eq_impl(5, ({1,2,3}, {4,5})), set())
        self.assertEqual(eq_impl(2, ({1,2,3}, {4,5})), set())
        self.assertEqual(eq_impl(2, ({1,2,3}, {3,4,5})), {3})
        self.assertEqual(eq_impl(2, ({1,2,3}, {3,4,5}, {4,6,7})), {3,4})

if __name__ == '__main__':
    unittest.main()