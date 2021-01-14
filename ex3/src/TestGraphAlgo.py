import unittest
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph


class TestGraphAlgo(unittest.TestCase):
    def test_get_graph(self):
        g = DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1, 2, 3)
        ga = GraphAlgo(g)
        self.assertEqual(g, ga.get_graph())

    def test_save_to_json(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(0, 1, 10)
        g.add_edge(1, 2, 45)
        g.add_edge(2, 3, 25)
        g.add_edge(3, 4, 28.12)
        g.add_edge(4, 5, 101.1)
        ga = GraphAlgo(g)
        self.assertTrue(ga.save_to_json("j.json"))

    def test_load_from_json(self):
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json("j.json"))

    def test_shortest_path(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(0, 1, 13)
        g.add_edge(1, 2, 15)
        g.add_edge(2, 3, 20)
        g.add_edge(3, 4, 35)
        g.add_edge(4, 5, 12)
        g.add_edge(0, 5, 100)
        ga = GraphAlgo(g)
        arr = [0, 1, 2, 3, 4, 5]
        self.assertEqual(ga.shortest_path(0, 5), (95, arr))

    def test_connected_component(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_node(7)
        g.add_edge(0, 1, 10)
        g.add_edge(1, 0, 11)
        g.add_edge(2, 3, 4)
        g.add_edge(3, 4, 5)
        g.add_edge(4, 5, 45)
        g.add_edge(5, 2, 8)
        g.add_edge(6, 7, 42)
        ga = GraphAlgo(g)
        l = [[0, 1], [2, 3, 4, 5], [7], [6]]
        self.assertEqual(ga.connected_components(), l)
        self.assertEqual(ga.connected_component(0), l[0])
        self.assertEqual(ga.connected_component(1), l[0])
        self.assertEqual(ga.connected_component(3), l[1])
        self.assertEqual(ga.connected_component(6), l[3])
        self.assertEqual(ga.connected_component(7), l[2])

    def test_plot_graph(self):
        ga = GraphAlgo()
        ga.load_from_json("j.json")
        ga.plot_graph()

    if __name__ == '__main__':
        unittest.main()
