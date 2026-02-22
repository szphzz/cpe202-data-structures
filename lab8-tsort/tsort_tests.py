import unittest
from tsort import *

class TestTsort(unittest.TestCase):
        
    def test_01(self):
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = "141\n101\n102\n225\n103\n315\n357"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_02(self):
        input = ['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        expect = "red\ngreen\npurple\nblue\nblack"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_03(self):
        input = ['1', '2', '1', '9', '1', '8', '9', '8', '9', '10', '8', '11', '10', '11', '2', '3', '3', '11', '3', '4', '4', '7', '4', '5', '7', '5', '7', '13', '7', '6', '6', '14', '6', '12']
        expect = "1\n9\n10\n8\n2\n3\n4\n7\n6\n12\n14\n13\n5\n11"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_04(self):
        input = ['3', '8', '3', '10', '5', '11', '7', '8', '7', '11', '8', '9', '11', '2', '11', '9', '11', '10']
        expect = "7\n5\n11\n2\n3\n10\n8\n9"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_05(self):
        input = ['v1', 'v2', 'v1', 'v3', 'v2', 'v4', 'v2', 'v5', 'v1', 'v4', 'v3', 'v6', 'v5', 'v4', 'v4', 'v3', 'v4', 'v6', 'v7', 'v6', 'v4', 'v7', 'v5', 'v7']
        expect = 'v1\nv2\nv5\nv4\nv7\nv3\nv6'
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_empty(self):
        input = []
        with self.assertRaises(ValueError):
            tsort(input)
            
    def test_single(self):
        input = ['3']
        with self.assertRaises(ValueError):
            tsort(input)
            
    def test_odd(self):
        input = ['3', '8', '3']
        with self.assertRaises(ValueError):
            tsort(input)
            
    def test_cycle_01(self):
        input = ['3', '3']
        with self.assertRaises(ValueError):
            tsort(input)

    def test_cycle_02(self):
        input = ['1', '2', '2', '1']
        with self.assertRaises(ValueError):
            tsort(input)

    def test_cycle_03(self):
        input = ['1', '2', '2', '3', '3', '1']
        with self.assertRaises(ValueError):
            tsort(input)

    def test_cycle_04(self):
        input = ['1', '2', '2', '3', '3', '4', '4', '2']
        with self.assertRaises(ValueError):
            tsort(input)

    def test_simple(self):
        input = ['v1', 'v2', 'v3', 'v4']
        expect = 'v3\nv4\nv1\nv2'
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_duplicates(self):
        input = ['v1', 'v2', 'v1', 'v2']
        expect = 'v1\nv2'
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

if __name__ == "__main__":
    unittest.main()
