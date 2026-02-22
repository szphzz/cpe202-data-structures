import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertFalse(bst.search(20)) # added
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        self.assertEqual(bst.find_max(), (10, 'stuff')) # added
        self.assertEqual(bst.tree_height(), 0) # added
        bst.insert(10, 'other') # should replace root
        self.assertTrue(bst.search(10)) # added
        self.assertFalse(bst.search(20)) # added
        self.assertEqual(bst.find_min(), (10, 'other')) # added
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_yolo(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())

        bst.insert(8)
        bst.insert(3)
        bst.insert(10)
        bst.insert(1)
        bst.insert(6, "haha")
        bst.insert(6, "nono")
        bst.insert(14)
        bst.insert(4)
        bst.insert(7)
        bst.insert(13)

        self.assertFalse(bst.is_empty())  # TEST true is not false
        self.assertTrue(bst.search(8))  # root
        self.assertTrue(bst.search(10))  # level 1
        self.assertTrue(bst.search(6))  # level 2
        self.assertTrue(bst.search(7))  # level 3 and leaf
        self.assertFalse(bst.search(2))

        self.assertEqual(bst.find_min(), (1, None))
        self.assertEqual(bst.find_max(), (14, None))

        self.assertEqual(bst.inorder_list(), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(bst.preorder_list(), [8, 3, 1, 6, 4, 7, 10, 14, 13])
        self.assertEqual(bst.level_order_list(), [8, 3, 10, 1, 6, 14, 4, 7, 13])

        a = Queue(30)
        bst.insert(0, a)
        bst.insert(15, ["hi", 8, (True, False)])
        self.assertEqual(bst.find_min(), (0, a))
        self.assertEqual(bst.find_max(), (15, ["hi", 8, (True, False)]))

if __name__ == '__main__':
    unittest.main()
