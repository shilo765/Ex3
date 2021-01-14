import json
import queue
import timeit
from abc import ABC
from random import random
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from src.GraphInterface import GraphInterface

from src.DiGraph import DiGraph
from src.graph_algo_interface import GraphAlgoInterface
from src.node import Node


class GraphAlgo(GraphAlgoInterface):
    def __eq__(self, other):
        return self.graph == other.graph

    def __init__(self, graph=DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        dict_graph = {}
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                g = DiGraph()
                for x in my_dict["Nodes"]:
                    n1 = Node()
                    if str(x).__len__() == 1:
                        v = my_dict["Nodes"][x]
                    else:
                        v = x
                    try:
                        n1.key = v["id"]
                    except:
                        n1.key = v["key"]
                    try:
                        n1.pos = v["pos"]
                    except:
                        v["pos"]=""
                    if v["pos"] == "":
                        x = np.random.uniform(35.186, 35.214)
                        y = np.random.uniform(32.0989, 32.10990)
                        n1.pos = str(x) + "," + str(y)
                    g.add_node(n1.key)
                    g.Nodes[n1.key].pos = n1.pos
                for x in my_dict["Edges"]:
                    if str(x).__len__() == 3:
                        v = my_dict["Edges"][x]
                    else:
                        v = x
                    try:

                        g.add_edge(v["src"], v["dest"], v["weight"])
                    except:
                        g.add_edge(v["src"], v["dest"], v["w"])

                self.__init__(g)
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump(self.graph, default=lambda m: m.__dict__, indent=4, fp=file)
        except IOError as e:
            print(e)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        l1 = list()
        self.clear_tags()
        pq = queue.PriorityQueue()
        if not self.graph.get_all_v().__contains__(id1) or not self.graph.get_all_v().__contains__(id2):
            return -1, l1
        node_count = 1
        if id1 == id2:
            l1.append(id1)
            return 0, l1
        self.graph.Nodes[id1].tag = 0
        pq.put((self.graph.Nodes[id1].tag, self.graph.Nodes[id1]))
        while not pq.empty():
            temp = pq.get()
            for e in self.graph.all_out_edges_of_node(temp[1].key):
                if self.graph.Nodes[self.graph.Edges[e].dest].tag == -1 or self.graph.Nodes[
                    self.graph.Edges[e].dest].tag > temp[0] + self.graph.Edges[e].weight:
                    self.graph.Nodes[self.graph.Edges[e].dest].lastNei = temp[1].key
                    if self.graph.Nodes[self.graph.Edges[e].dest].tag == -1:
                        node_count += 1

                    self.graph.Nodes[self.graph.Edges[e].dest].tag = temp[0] + self.graph.Edges[e].weight
                    ed = self.graph.Nodes[self.graph.Edges[e].dest].tag
                    ef = self.graph.Nodes[self.graph.Edges[e].dest]
                    pq.put((ed, ef))

        if self.graph.Nodes[id2].tag != -1:
            temp = self.graph.Nodes[id2].lastNei
            l1.append(id2)
            while temp != self.graph.Nodes[id1].key:
                l1.append(temp)
                temp = self.graph.Nodes[temp].lastNei
            l1.append(id1)
            l1.reverse()
        return self.graph.Nodes[id2].tag, l1

    def helpSCC (self,id1):
        "return list of all the point that connected to id1"
        l1= list()
        l2=[]
        l1.append(id1)
        while l1!=[]:
            temp=int(l1.pop())
            l2.append(temp)
            for x in self.graph.all_out_edges_of_node(temp):
                if not l2.__contains__(int(x.split(",")[1])) and not l1.__contains__(x.split(",")[1]):
                    l1.append(x.split(",")[1])


        return l2

    def connected_component(self, id1: int) -> list:

        l1 = list()
        l1= self.helpSCC(id1)
        l1.sort()
        g = DiGraph()
        for e in self.graph.Edges.items():
            g.add_edge(e[1].dest, e[1].src, e[1].weight)
        da = GraphAlgo(g)
        l2 = list()
        da.graph.Nodes = self.graph.Nodes
        l2=self.helpSCC(id1)
        l2.sort()
        l3=list()
        for x in l1:
            if l2.__contains__(x)and x not in l3:
                l3.append(x)
        return l3

    def connected_components(self) -> List[list]:
        l1 = list()
        l2 = list()
        list_used = list()
        for n in self.graph.Nodes:
            if n in list_used:
                continue
            l1=self.connected_component(n)
            if l1 not in l2:
                l2.append(l1)
            list_used += l1
        return l2

    def plot_graph(self) -> None:
        for n in self.graph.Nodes.items():
            if n[1].pos == "":
                x = np.random.uniform(35.186, 35.214)
                y = np.random.uniform(32.0989, 32.10990)
                n[1].pos = str(x) + "," + str(y)

        x = list()
        y = list()
        fig = plt.figure()
        axes = fig.add_axes([0, 0, 1, 1])
        for n in self.graph.Nodes.items():
            x.append(float(n[1].pos.split(",")[0]))
            y.append(float(n[1].pos.split(",")[1]))
            axes.text(float(n[1].pos.split(",")[0]), float(n[1].pos.split(",")[1]), n[0])
        xn = np.array(x)
        yn = np.array(y)

        for e in self.graph.Edges.items():
            axes.annotate("", xy=(
                float(self.graph.Nodes[e[1].dest].pos.split(",")[0]),
                float(self.graph.Nodes[e[1].dest].pos.split(",")[1])), xytext=(
            float(self.graph.Nodes[e[1].src].pos.split(",")[0]), float(self.graph.Nodes[e[1].src].pos.split(",")[1])),
                          arrowprops=dict(arrowstyle="->"))
            axes.plot(xn, yn, 'o')
        plt.show()

    def clear_tags(self):
        "clear all the tags from the nodes"
        for n in self.graph.Nodes.items():
            n[1].tag = -1
        pass
