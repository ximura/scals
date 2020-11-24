import unittest
from scals import Scals

class TestScals(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Scals.eq_impl(5, ({1,2,3}, {4,5})), set())
        self.assertEqual(Scals.eq_impl(2, ({1,2,3}, {4,5})), set())
        self.assertEqual(Scals.eq_impl(2, ({1,2,3}, {3,4,5})), {3})
        self.assertEqual(Scals.eq_impl(2, ({1,2,3}, {3,4,5}, {4,6,7})), {3,4})

    def test_le(self):
        self.assertEqual(Scals.le_impl(5, ({1,2}, {4,5})), {1,2,4,5})
        self.assertEqual(Scals.le_impl(2, ({1,2}, {4,5})), {1,2,4,5})
        self.assertEqual(Scals.le_impl(2, ({1,2,3}, {3,4})), {1,2,4})
        self.assertEqual(Scals.le_impl(2, ({1,2,3}, {3,4}, {4,6})), {1,2,6})

    def test_gr(self):
        self.assertEqual(Scals.gr_impl(5, ({1,2,3}, {4,5})), set())
        self.assertEqual(Scals.gr_impl(2, ({1,2,3}, {3,4,5})), set())
        self.assertEqual(Scals.gr_impl(2, ({1,2,3}, {2,3,4}, {3,4,5}, {4,5,6})), {3,4})

if __name__ == '__main__':
    unittest.main()