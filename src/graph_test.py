import unittest

from src.DiGraph import DiGraph
from src.node import Node


class MyTestCase(unittest.TestCase):
    def test_graph_test(self):
        """test the add and remove methodes of the graph and if the equals method work"""
        g=DiGraph()
        g.add_node(7)
        assert g.Nodes.__len__()==1,"add node method not work properly"
        g.remove_node(7)
        assert g.Nodes.__len__()==0,"remove node method not work properly"
        g.add_edge(5,6,7)
        assert g.Edges.__len__()==1,"add node method not work properly"
        g.remove_edge(5,6)
        assert g.Edges.__len__()==0,"remove node method not work properly"
        g=DiGraph()
        g2=DiGraph()
        assert g==g2, "equal not work"
        g.add_edge(5,6,8)
        assert g!=g2, "equal not work"
        g2.add_edge(5,6,8)
        assert g == g2, "equal not work"

if __name__ == '__main__':
    unittest.main()
