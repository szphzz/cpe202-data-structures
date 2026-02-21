# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_init(self):
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc.name, 'SLO')
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

    def test_eq(self):
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = Location('Paris', 48.9, 2.4)
        loc3 = Location('SLO', 35.3, -120.7)
        loc4 = loc1

        self.assertFalse(loc1 == [])
        self.assertFalse(loc2 == [])
        self.assertFalse(loc3 == [])
        self.assertFalse(loc4 == [])
        
        self.assertNotEqual(loc1, loc2)
        self.assertNotEqual(loc2, loc3)
        self.assertNotEqual(loc2, loc4)
        
        self.assertEqual(loc1, loc3)
        self.assertEqual(loc1, loc4)
        self.assertEqual(loc3, loc4)

        loc4 = Location('San Ramon', 37.835, -122)
        loc5 = Location('San Ramon', 37.836, -122)
        self.assertFalse(loc4 == loc5)

    def test_repr_01(self):
        loc = Location('SLO', 35.3, -120.7)
        str1 = "Location('SLO', 35.3, -120.7)"
        str2 = "Location(SLO, 35.3, -120.7)"
        res = repr(loc)
        # print(res)
        self.assertTrue(res == str1 or res == str2)

    def test_repr_02(self):
        loc = Location('San Ramon', 37.8, -122)
        str1 = "Location('San Ramon', 37.8, -122)"
        str2 = "Location(San Ramon, 37.8, -122)"
        res = repr(loc)
        self.assertTrue(res == str1 or res == str2)

    def test_repr_03(self):
        loc = Location('Tokyo', 35.7, 139.7)
        str1 = "Location('Tokyo', 35.7, 139.7)"
        str2 = "Location(Tokyo, 35.7, 139.7)"
        res = repr(loc)
        self.assertTrue(res == str1 or res == str2)

    def test_repr_04(self):
        loc = Location('Seoul', 37.6, 127)
        str1 = "Location('SLO', 35.3, -120.7)"
        str2 = "Location(SLO, 35.5, -120.7)"
        res = repr(loc)
        self.assertFalse(res == str1 and res == str2)

if __name__ == "__main__":
        unittest.main()
