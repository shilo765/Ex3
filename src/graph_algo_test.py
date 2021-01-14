import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def test_graph_algo(self):
        """test the methods on graph algo shortestPath and connected_component,connected_components,
         and also save and load"""
        g=DiGraph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        da=GraphAlgo(g)
        assert da.shortest_path(1,2)[0]==-1,"shortestPath not work properly"
        assert da.shortest_path(1,2)[1]==[],"shortestPath not work properly"
        da.graph.add_edge(1,2,7)
        da.graph.add_edge(2,1,1)
        da.graph.add_edge(2,4,1.5)
        da.graph.add_edge(4,3,8)
        da.clear_tags()
        da.save_to_json("test.json")
        da2=GraphAlgo()
        da2.load_from_json("test.json")
        assert da==da2," load or save method not work properly"
        assert da.shortest_path(1, 3)[0] == 16.5, "shortestPath not work properly"
        assert da.shortest_path(1, 3)[1] == [1,2,4,3], "shortestPath not work properly"


if __name__ == '__main__':
    unittest.main()
