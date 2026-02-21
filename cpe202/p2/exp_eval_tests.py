# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self): # subtraction
        self.assertAlmostEqual(postfix_eval('5 3 -'), 2)

    def test_postfix_eval_05(self): # multiplication
        self.assertAlmostEqual(postfix_eval('5 3 *'), 15)

    def test_postfix_eval_06(self): # division
        self.assertAlmostEqual(postfix_eval('15 5 / '), 3)

    def test_postfix_eval_07(self): # exponent
        self.assertAlmostEqual(postfix_eval('2 3 **'), 8)
        self.assertAlmostEqual(postfix_eval('3 2 **'), 9)

    def test_postfix_eval_08(self): # shift
        self.assertAlmostEqual(postfix_eval('60 2 >>'), 15)
        self.assertAlmostEqual(postfix_eval('15 2 <<'), 60)

    def test_postfix_eval_09(self): # combo
        self.assertAlmostEqual(postfix_eval('5 1 2 + 4 ** + 3 -'), 83)

    def test_postfix_eval_10(self): # single
        self.assertAlmostEqual(postfix_eval('6'), 6)
        
    def test_postfix_eval_11(self): # empty string
        try:
            postfix_eval('')
            self.fail()
        except ValueError as e:
            self.assertEqual(str(e), 'Empty input')

    def test_postfix_eval_12(self): # spaces
        self.assertAlmostEqual(postfix_eval('5     3  -'), 2)
        


            
    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
    
    def test_infix_to_postfix_02(self): # addition
        self.assertEqual(infix_to_postfix('6 + 3'), '6 3 +')
        
    def test_infix_to_postfix_03(self): # multiplication
        self.assertEqual(infix_to_postfix('6 * 3'), '6 3 *')
        
    def test_infix_to_postfix_04(self): # division
        self.assertEqual(infix_to_postfix('6 / 3'), '6 3 /')
        
    def test_infix_to_postfix_05(self): # exponent
        self.assertEqual(infix_to_postfix('6 ** 3'), '6 3 **')
        
    def test_infix_to_postfix_06(self): # shift
        self.assertEqual(infix_to_postfix('60 << 2'), '60 2 <<')
        
    def test_infix_to_postfix_07(self): # combo
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'), '3 4 2 * 1 5 - 2 3 ** ** / +')
        
    def test_infix_to_postfix_08(self): # spaces
        self.assertEqual(infix_to_postfix('5     3  -'), '5 3 -')


        
        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_01(self): # single
        self.assertEqual(prefix_to_postfix('6'), '6')

    def test_prefix_to_postfix_02(self): # addition
        self.assertEqual(prefix_to_postfix('+ 2 2'), '2 2 +')

    def test_prefix_to_postfix_03(self): # subtraction
        self.assertEqual(prefix_to_postfix('- 3 1'), '3 1 -')

    def test_prefix_to_postfix_04(self): # multiplication
        self.assertEqual(prefix_to_postfix('* 2 3'), '2 3 *')

    def test_prefix_to_postfix_05(self): # division
        self.assertEqual(prefix_to_postfix('/ 6 3'), '6 3 /')

    def test_prefix_to_postfix_06(self): # exponent
        self.assertEqual(prefix_to_postfix('** 2 3'), '2 3 **')

    def test_prefix_to_postfix_07(self): # shift
        self.assertEqual(prefix_to_postfix('<< 60 2'), '60 2 <<')

    def test_prefix_to_postfix_08(self): # spaces
        self.assertEqual(prefix_to_postfix('-     5  3'), '5 3 -')

if __name__ == "__main__":
    unittest.main()
