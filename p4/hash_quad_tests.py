import math
import unittest
from hash_quad import *


class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)

        self.assertListEqual(ht.get_all_keys(), ['h', 'o', 'a'])   # added
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_table_size(), 7)

        ht.insert("v", 0) # Causes rehash
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

        self.assertFalse(ht.in_table('s'))  # added
        self.assertEqual(ht.get_index('s'), None)
        self.assertEqual(ht.get_value('a'), 0)
        self.assertEqual(ht.get_value('h'), 0)
        self.assertEqual(ht.get_value('o'), 0)
        self.assertEqual(ht.get_value('v'), 0)
        self.assertEqual(ht.get_value('s'), None)
        self.assertListEqual(ht.get_all_keys(), ['h', 'o', 'a', 'v'])
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 17)
        self.assertAlmostEqual(ht.get_load_factor(), 4/17)

    def test_03(self):
        ht = HashTable(7)
        ht.insert('a', 0)
        self.assertEqual(ht.get_index('a'), 6)
        self.assertEqual(ht.get_value('a'), 0)
        ht.insert('a', 1)  # bc key in table, replace old value with new value
        self.assertEqual(ht.get_index('a'), 6)
        self.assertEqual(ht.get_value('a'), 1)
        self.assertListEqual(ht.get_all_keys(), ['a'])

    def test_change(self):
        ht = HashTable(6)
        ht.insert('cat', 5)
        self.assertEqual(ht.get_value('cat'), 5)
        self.assertEqual(ht.get_index('cat'), 3)
        ht.insert('cat', 7)
        self.assertEqual(ht.get_value('cat'), 7)
        self.assertEqual(ht.get_index('cat'), 3)
        ht.insert('cat', 9)
        self.assertEqual(ht.get_value('cat'), 9)
        self.assertEqual(ht.get_index('cat'), 3)
        self.assertListEqual(ht.get_all_keys(), ['cat'])
        self.assertEqual(ht.get_num_items(), 1)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.get_load_factor(), 1/7)

    def test_empty(self):
        ht = HashTable(7)
        self.assertFalse(ht.in_table('a'))
        self.assertEqual(ht.get_index('a'), None)
        self.assertEqual(ht.get_num_items(), 0)
        self.assertEqual(ht.get_all_keys(), [])
        self.assertEqual(ht.get_value('a'), None)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_primes(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(25))
        ht = HashTable(1)
        self.assertEqual(ht.length, 2)


if __name__ == '__main__':
   unittest.main()
