import unittest
from queue_array import Queue
# from queue_linked import Queue

class TestLab1(unittest.TestCase):

    def test_00(self):
        q = Queue(3)

        # when empty
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)

        # check that an error is raised when try to dequeue
        with self.assertRaises(IndexError):
            q.dequeue()

        # enqueue an item and check changes
        q.enqueue(10)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 1)

        # check that dequeue works (especially with circular array)
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)

    def test_01(self):
        q = Queue(3)

        # fill the queue and check changes
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 3)

        # check that that an error is raised when try to enqueue to full array
        with self.assertRaises(IndexError):
            q.enqueue(40)

        # check that circular array is implemented correctly
        q.dequeue()
        q.enqueue(40)
        self.assertEqual(q.back, 0)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(), 3)
    
if __name__ == '__main__': 
    unittest.main()
