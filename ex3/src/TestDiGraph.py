import unittest
from DiGraph import DiGraph
from DiGraph import Node
from GraphAlgo import GraphAlgo


class TestDiGraph(unittest.TestCase):

    def test_get_all_v(self):
        g = DiGraph()
        d = {}
        for i in range(10):
            g.add_node(i)
            d.setdefault(i,g.nodes.get(i))

        self.assertEqual(g.get_all_v(), d)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(0, 1, 10)
        g.add_edge(2, 1, 58.9)
        g.add_edge(3, 1, 45)
        d = {}
        d.setdefault(0, 10)
        d.setdefault(2, 58.9)
        d.setdefault(3, 45)
        self.assertEqual(d, g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(0, 1, 10)
        g.add_edge(0, 2, 58.9)
        g.add_edge(0, 3, 45)
        d = {}
        d.setdefault(1, 10)
        d.setdefault(2, 58.9)
        d.setdefault(3, 45)
        self.assertEqual(d, g.all_out_edges_of_node(0))

    def test_add_node(self):
        g = DiGraph()
        self.assertEqual(0, g.v_size())
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        self.assertEqual(3, g.v_size())
        g.add_node(1)
        g.add_node(1)
        g.add_node(1)
        self.assertEqual(3, g.v_size())

    def test_add_edge(self):
        g = DiGraph()
        self.assertEqual(0, g.e_size())
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 4)
        g.add_edge(3, 1, 5)
        self.assertEqual(3, g.e_size())

    def test_remove_node(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 4)
        g.add_edge(3, 1, 5)
        self.assertEqual(3, g.v_size())
        self.assertEqual(3, g.e_size())
        g.remove_node(1)
        self.assertEqual(2, g.v_size())
        self.assertEqual(1, g.e_size())

    def test_remove_edge(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 4)
        g.add_edge(3, 1, 5)
        self.assertEqual(3, g.e_size())
        g.remove_edge(3, 2)
        self.assertEqual(3, g.e_size())
        g.remove_edge(1, 2)
        self.assertEqual(2, g.e_size())

    if __name__ == '__main__':
        unittest.main()
