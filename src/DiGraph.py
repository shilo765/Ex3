from abc import ABC

from src.edge import Edge
from GraphInterface import GraphInterface
from src.node import Node


class DiGraph(GraphInterface, ABC):
    def __eq__(self, other):
        return self.Nodes==other.Nodes and self.Edges==other.Edges
    def __init__(self):
        self.Nodes = {}
        self.Edges = {}
        self.modeCount = 0

    def v_size(self) -> int:
        return self.Nodes.__sizeof__()

    def e_size(self) -> int:
        return self.Nodes.__sizeof__()

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        thisEdges = {}
        if self.Edges == {}:
            return {}
        for key in self.Edges:
            if self.Edges.get(key).dest == id1:
                thisEdges[key] = self.Edges.get(key)
        return thisEdges

    def all_out_edges_of_node(self, id1: int) -> dict:
        thisEdges = {}
        if self.Edges == {}:
            return {}
        for key in self.Edges:
            if self.Edges.get(key).src == id1:
                thisEdges[key] = self.Edges.get(key)
        return thisEdges

    def get_mc(self) -> int:
        return self.modeCount

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        e1 = Edge(id1,id2, weight)
        self.Edges[str(id1) + "," + str(id2)] = e1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        n1 = Node(node_id)
        if not pos==None:
            n1.pos=str(pos[0])+","+str(pos[1])
        self.Nodes[node_id] = n1
        self.modeCount+=1

    def remove_node(self, node_id: int) -> bool:
       try:
            del self.Nodes[node_id]
            for key in self.all_out_edges_of_node(node_id):
                self.remove_edge(int(key.split(",")[0]),int(key.split(",")[1]))
            for key in self.all_in_edges_of_node(node_id):
                self.remove_edge(int(key.split(",")[0]),int(key.split(",")[1]))
            self.modeCount+=1
       except:
           pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
       try:
           del self.Edges[str(node_id1) + "," + str(node_id2)]
           self.modeCount+=1
       except:
           pass