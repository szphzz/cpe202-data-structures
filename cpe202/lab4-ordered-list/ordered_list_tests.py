import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_00(self): # another simple test with integers
        i_list = OrderedList()
        i_list.add(1)
        i_list.add(3)
        i_list.add(2)
        self.assertEqual(i_list.python_list(), [1, 2, 3]) # check list is ordered
        self.assertEqual(i_list.python_list_reversed(), [3, 2, 1]) # check reversed list

    def test_01(self): # strings
        s_list = OrderedList()
        # skipped pop(0) test
        with self.assertRaises(IndexError): # error when negative pop
            s_list.pop(-1)
        self.assertEqual(s_list.size(), 0) # check size of empty list
        self.assertFalse(s_list.remove(1)) # can't remove a value that isn't in the list
        s_list.add('A')
        self.assertEqual(s_list.size(), 1)
        self.assertEqual(s_list.pop(0), 'A') # check pop
        # skipped pop(0) test 
        s_list.add('A')
        s_list.add('C')
        self.assertTrue(s_list.add('B')) # check add returns True
        self.assertEqual(s_list.size(), 3) 
        self.assertFalse(s_list.add('B')) # no duplicates
        self.assertEqual(s_list.python_list(), ['A', 'B', 'C'])
        self.assertEqual(s_list.python_list_reversed(), ['C', 'B', 'A'])
        self.assertFalse(s_list.search('a')) # check difference between capitalization
        self.assertTrue(s_list.search('B')) # check search returns True
        self.assertTrue(s_list.index('C'), 2) # check index
        self.assertTrue(s_list.remove('C'))
        self.assertFalse(s_list.remove('C'))
        self.assertTrue(s_list.remove('A'))
        self.assertEqual(s_list.python_list_reversed(), ['B']) # check list with one value
        self.assertFalse(s_list.add('B')) 
        self.assertIsNone(s_list.index('C')) # check index returns None when value not found

    def test_02(self): # floats (and negatives)
        f_list = OrderedList()
        self.assertTrue(f_list.add(-0.00001))
        self.assertFalse(f_list.add(-0.00001))
        self.assertTrue(f_list.search(-0.00001))
        self.assertFalse(f_list.remove(-0.00002))
        self.assertEqual(f_list.size(), 1)
        self.assertTrue(f_list.remove(-0.00001))

    def test_03(self): # empty
        e_list = OrderedList()
        self.assertEqual(e_list.python_list(), [])
        self.assertEqual(e_list.python_list_reversed(), []) # should be the same
        self.assertEqual(e_list.size(), 0) 
        self.assertEqual(e_list.index(-1), None)
        self.assertEqual(e_list.index(0), None)
        self.assertFalse(e_list.search([None])) # doesn't even contain None value
        self.assertTrue(e_list.is_empty())
        self.assertFalse(e_list.remove(None)) # can't even remove None value
        # skipped pop(0) test
        
if __name__ == '__main__': 
    unittest.main()
