# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):
            
    def test_max_list_01(self): # returns max of list
        tlist = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_02(self): # when the list is None, raises ValueError
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)
            
    def test_max_list_03(self): # when the list is empty
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max_list_04(self): # when the list only has one element
        tlist = [1]
        self.assertEqual(max_list_iter(tlist), 1)

    def test_max_list_05(self): # when all numbers are equal
        tlist = [1, 1, 1]
        self.assertEqual(max_list_iter(tlist), 1)

    def test_max_list_06(self): # when the list is in descending order
        tlist = [3, 2, 1]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_07(self): # when the max is a repeat
        tlist = [1, 2, 2]
        self.assertEqual(max_list_iter(tlist), 2)

    def test_max_list_08(self): # when there is a repeat besides the max
        tlist = [1, 1, 2]
        self.assertEqual(max_list_iter(tlist), 2)

    def test_reverse_01(self): # reverses list without mutating
        tlist = [1, 2, 3]
        revlist = reverse_list(tlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(tlist, [1, 2, 3])

    def test_reverse_02(self): # when the list is None, raises ValueError
        tlist = None
        with self.assertRaises(ValueError):
            reverse_list(tlist)

    def test_reverse_03(self): # when the list is empty, returns empty list
        tlist = []
        revlist = reverse_list(tlist)
        self.assertEqual(revlist, [])
        self.assertEqual(tlist, [])

    def test_reverse_04(self): # when the list only has one element
        tlist = [1]
        revlist = reverse_list(tlist)
        self.assertEqual(revlist, [1])
        self.assertEqual(tlist, [1])

    def test_reverse_mutate_01(self): # reverses list 
        tlist = [1, 2, 3]
        reverse_list_mutate(tlist)
        self.assertEqual(tlist, [3, 2, 1])

    def test_reverse_mutate_02(self): # when the list is None, raises ValueError
        tlist = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(tlist)

    def test_reverse_mutate_03(self): # when the list is empty, returns empty list
        tlist = []
        reverse_list_mutate(tlist)
        self.assertEqual(tlist, [])

    def test_reverse_mutate_04(self): # when the list only has one element
        tlist = [1]
        reverse_list_mutate(tlist)
        self.assertEqual(tlist, [1])
        
    def test_reverse_rec_01(self): # reverses list using recursion
        tlist = [1, 2, 3]
        self.assertEqual(reverse_rec(tlist),[3, 2, 1])
        self.assertEqual(tlist,[1, 2, 3])

    def test_reverse_rec_02(self): # when the list is None, raises ValueError
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_reverse_rec_03(self): # when the list only has one element
        tlist = [1]
        self.assertEqual(reverse_rec(tlist), [1])
        self.assertEqual(tlist, [1])

    def test_reverse_rec_04(self): # when the list is empty
        tlist = []
        self.assertEqual(reverse_rec(tlist), [])
        self.assertEqual(tlist, [])
    

if __name__ == "__main__":
        unittest.main()
