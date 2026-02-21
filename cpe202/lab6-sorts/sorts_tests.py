import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple_selection(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_simple_insertion(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_empty_selection(self):
        nums = []
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

    def test_empty_insertion(self):
        nums = []
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [])

    def test_single_selection(self):
        nums = [10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [10])

    def test_single_insertion(self):
        nums = [10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 0)
        self.assertEqual(nums, [10])
    def test_duplicate_selection(self):
        nums = [10, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 10])

    def test_duplicate_insertion(self):
        nums = [10, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 10])

    def test_selection_01(self):
        nums = [18, 10, 4, 12, 15]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [4, 10, 12, 15, 18])

    def test_insertion_01(self):
        nums = [14, 10, 8, 20, 15]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 8)
        self.assertEqual(nums, [8, 10, 14, 15, 20])

if __name__ == '__main__': 
    unittest.main()
