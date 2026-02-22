import unittest
import sample

class TestLab1(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(sample.factorial(0),1)
        self.assertEqual(sample.factorial(1),1)
        self.assertEqual(sample.factorial(2),2)
        self.assertEqual(sample.factorial(6),720)

    def test_fib(self):
        self.assertEqual(sample.fib(0),0)
        self.assertEqual(sample.fib(1),1)
        self.assertEqual(sample.fib(2),1)
        self.assertEqual(sample.fib(6),8)

    def test_maxlist_rec(self):
        tlist = [10, 9, 8 ,4, 9]
        self.assertEqual(sample.maxlist_rec(tlist),10)
        tlist = [9, 8, 10 ,4, 9]
        self.assertEqual(sample.maxlist_rec(tlist),10)
        tlist = [5, 9, 8 ,4, 10]
        self.assertEqual(sample.maxlist_rec(tlist),10)
        tlist = [-10, -9, -1 ,-4, -9]
        self.assertEqual(sample.maxlist_rec(tlist),-1)
        tlist = []
        with self.assertRaises(ValueError):  # check for correct Exception
            sample.maxlist_rec(tlist)
        self.assertRaises(ValueError, sample.maxlist_rec, tlist)  # another way to check exception

    def test_reverse_iter(self):
        self.assertEqual(sample.reverse_iter(""),"")
        self.assertEqual(sample.reverse_iter("abcd"),"dcba")
            
if __name__ == '__main__': 
    unittest.main()
