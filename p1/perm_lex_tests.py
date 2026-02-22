import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_00(self): # base case of empty string
        self.assertEqual(perm_lex.perm_gen_lex(''), [])

    def test_perm_gen_lex_01(self): # base case of string with one char
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
        
    def test_perm_gen_lex_02(self): # short string
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_lex_04(self): # longer string
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb',
                                                        'bac', 'bca',
                                                        'cab', 'cba'])

if __name__ == "__main__":
        unittest.main()
