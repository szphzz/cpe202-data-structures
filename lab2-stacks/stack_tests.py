import unittest

from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    # potentially have to test when capacity is 0

    def test_00(self):
        stack = Stack(3)
        
        # when empty
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

        # push an item and check changes
        stack.push(10)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

        # check that peek works
        self.assertEqual(stack.peek(), 10)
        
        # check that pop works
        stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 0)
        
    def test_01(self):
        stack = Stack(3)

        # fill the stack and check changes
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 3)

        # check that peek works
        self.assertEqual(stack.peek(), 30)

        # check that an error is raised when try to push
        with self.assertRaises(IndexError):
            stack.push(40)
        
if __name__ == '__main__': 
    unittest.main()
