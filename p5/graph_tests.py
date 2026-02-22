import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_one_edge(self):
        g = Graph('one_edge.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2'])
        self.assertTrue(g.get_vertex('v1') is not None)
        self.assertFalse(g.get_vertex('v2') is None)
        self.assertEqual(g.get_vertex('v3'), None)

    def test_simple(self):
        g = Graph('simple.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['1', '2', '3', '4'])
        self.assertTrue(g.get_vertex('1') is not None)
        self.assertFalse(g.get_vertex('2') is None)
        self.assertEqual(g.get_vertex('5'), None)

    def test_complex(self):
        g = Graph('complex.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '8', 'a', 'b', 'c'], ['4', '6', '9', 'd', 'e']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['1', '2', '4', '6', '8', '9', 'a', 'b', 'c', 'd', 'e'])
        self.assertTrue(g.get_vertex('a') is not None)
        self.assertFalse(g.get_vertex('b') is None)
        self.assertEqual(g.get_vertex('f'), None)

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        self.assertTrue(g.get_vertex('v1') is not None)
        self.assertFalse(g.get_vertex('v2') is None)
        self.assertEqual(g.get_vertex('v10'), None)

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8'])
        self.assertTrue(g.get_vertex('v3') is not None)
        self.assertFalse(g.get_vertex('v4') is None)
        self.assertEqual(g.get_vertex('v5'), None)

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4', '5'], ['6', '7', '8']])
        self.assertFalse(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['1', '2', '3', '4', '5', '6', '7', '8'])
        self.assertTrue(g.get_vertex('1') is not None)
        self.assertFalse(g.get_vertex('2') is None)
        self.assertEqual(g.get_vertex('10'), None)


if __name__ == '__main__':
   unittest.main()
