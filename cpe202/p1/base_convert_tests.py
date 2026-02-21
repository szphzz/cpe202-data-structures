import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base00(self): # 0 is always 0 no matter what base
        self.assertEqual(convert(0,10), '0')

    def test_base01(self): # num must be nonnegative
        with self.assertRaises(ValueError):
            convert(-1, 10)
            
    def test_base02(self): # num must be an int
        with self.assertRaises(ValueError):
            convert(1.1, 10)

    def test_base03(self): # b must be between 2 and 16
        with self.assertRaises(ValueError):
            convert(36, 17)

    def test_base04(self): # b must be between 2 and 16
        with self.assertRaises(ValueError):
            convert(36, 1)

    def test_base05(self): # b must be an int
        with self.assertRaises(ValueError):
            convert(36, 10.1)

    def test_base06(self): 
        self.assertEqual(convert(8, 16), '8')

    def test_base2(self):
        self.assertEqual(convert(45, 2),'101101')

    def test_base4(self):
        self.assertEqual(convert(30, 4),'132')

    def test_base16(self):
        self.assertEqual(convert(316, 16),'13C')

    def test_base6(self):
        self.assertEqual(convert(345, 6), '1333')

    def test_base8(self):
        self.assertEqual(convert(548, 8), '1044')

    def test_base10(self):
        self.assertEqual(convert(36, 10), '36')

    def test_base12(self):
        self.assertEqual(convert(76, 12), '64')

    def test_base14(self):
        self.assertEqual(convert(101,14), '73')

if __name__ == "__main__":
        unittest.main()
