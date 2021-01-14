from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface
import random
import matplotlib.pyplot as plt
import json
from DiGraph import Node
import math
from queue import PriorityQueue


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g = None):
        if g == None:
            self.g = DiGraph()
            self.counter = 0
        else:
            self.g = g
            self.counter = 0

    def get_graph(self) -> GraphInterface:
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        with open(file_name) as f:
            j = json.load(f)
            for n in j["Nodes"]:
                if n.get("pos", -1) == -1:
                    graph.add_node(n["id"])
                else:
                    nd = Node(n["id"], n["pos"])
                    graph.add_node(nd.key, nd.pos.p)
            for e in j["Edges"]:
                graph.add_edge(e["src"], e["dest"], e["w"])
        self.g = graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        node = []
        l = list(self.g.nodes.keys())
        for i in range(len(l)):
            n = self.g.nodes.get(l[i])
            if n.pos == ():
                node.append({"id": n.key})
            else:
                node.append({"pos": n.pos.__str__()})
        edge = []
        l = list(self.g.edges.keys())
        for i in range(len(l)):
            e = self.g.edges.get(l[i])
            edge.append({"src": e.src, "w": e.weight, "dest": e.dst})
        j_graph = json.dumps({"Edges": edge, "Nodes": node})
        with open(file_name, 'w') as f:
            f.write(j_graph)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.g.nodes.get(id1, -1) == -1 or self.g.nodes.get(id2, -1) == -1:
            return None
        s = []
        pq = PriorityQueue()
        if id1 == id2:
            return float("inf"), s
        parent = {}
        visited = {}
        l = list(self.g.nodes.keys())
        self.g.nodes.get(id1).set_weight(0)
        for i in range(len(self.g.nodes)):
            self.g.nodes.get(l[i]).set_weight(float("inf"))
            parent.setdefault(l[i], -1)
            visited.setdefault(l[i], False)
        self.g.nodes.get(id1).set_weight(0)
        pq.put((self.g.nodes.get(id1).weight, self.g.nodes.get(id1)))
        while not pq.empty():
            v = pq.get()[1]
            neigh = list(v.neigh.keys())
            for i in range(len(neigh)):
                e = v.neigh.get(neigh[i])
                u = self.g.nodes.get(e.dst)
                if not visited[e.dst]:
                    weight = v.weight + e.weight
                    if weight < u.weight:
                        self.g.nodes.get(e.dst).set_weight(weight)
                        parent.update({e.dst: v.key})
                        pq.put((self.g.nodes.get(u.key).weight, self.g.nodes.get(u.key)))
            visited.update({v.key: True})
        if self.g.nodes.get(id2).weight == float("inf"):
            return float("inf"), []
        s.append(id2)
        p = id2
        while parent.get(p) != id1:
            s.append(self.g.nodes.get(parent.get(p)).key)
            p = parent.get(p)
        s.append(id1)
        s.reverse()
        return self.g.nodes.get(id2).weight, s

    def connected_component(self, id1: int) -> list:
        if self.g.nodes.get(id1, -1) == -1:
            return []
        lst = self.connected_components()
        for l in lst:
            if l.count(id1) == 1:
                return l
        return list

    def connected_components(self) -> List[list]:
        if self.g.v_size() < 950:
            lst = []
            s = []
            low = {}
            self.counter = 0
            l = list(self.g.nodes.keys())
            for i in range(len(l)):
                low.setdefault(l[i], float("inf"))
            for i in range(len(l)):
                if low.get(l[i]) == float("inf"):
                    self.counter += 1
                    self.DFS(l[i], low, s, lst)
            if len(s) > 0:
                j = []
                while len(s) != 0:
                    j.append(s.pop(len(s) - 1))
                j.sort()
                lst.append(j)
            return lst
        else:
            return self.tarjan()


    def plot_graph(self) -> None:
        l = list(self.g.nodes.keys())
        plt.title("Graph")
        plt.ylabel("y - axis")
        plt.xlabel("x - axis")
        xmax, ymax, xmin, ymin = self.range()
        if xmax == float("-inf") and ymax == float("-inf"):
            xmax, ymax = 400, 400
        elif xmax == float("-inf") and ymax != float("-inf"):
            xmax = ymax
        elif ymax != float("-inf") and ymax == float("-inf"):
            ymax = xmax
        # wid = math.sqrt((xmax-xmin)**2 + (ymax-ymin)**2)
        for i in range(len(l)):
            if self.g.nodes.get(l[i]).pos == ():
                self.g.nodes.get(l[i]).set_pos(random.random()*xmax, random.random()*ymax, 0)
        xmax, ymax, xmin, ymin = self.range()
        if xmax == float("-inf") and ymax == float("-inf"):
            xmax, ymax = 400, 400
        elif xmax == float("-inf") and ymax != float("-inf"):
            xmax = ymax
        elif ymax != float("-inf") and ymax == float("-inf"):
            ymax = xmax
        l = list(self.g.edges.keys())
        for i in range(len(l)):
            e = self.g.edges.get(l[i])
            src = self.g.nodes.get(e.src)
            dst = self.g.nodes.get(e.dst)
            plt.arrow(src.pos.x(), src.pos.y(), src.pos.dx(dst.pos.x()), src.pos.dy(dst.pos.y()), width=(xmax-xmin)/140, color="black")
        l = list(self.g.nodes.keys())
        for i in range(len(l)):
            n = self.g.nodes.get(l[i])
            plt.plot(n.pos.x(), n.pos.y(), 'o', color="red")
            plt.text(n.pos.x() - (xmax-xmin)/150, n.pos.y() + (ymax-ymin)/60, str(n.key), color="orange")
        plt.show()


    def tarjan(self):
        lst = []
        dfs = []
        s = []
        low = {}
        counter = 0
        k = list(self.g.nodes.keys())
        for i in range(len(k)):
            low.setdefault(k[i], float("inf"))
        for i in range(len(k)):
            if len(s) > 0:
                l = []
                while len(s) > 0:
                    l.append(s.pop(len(s)-1))
                lst.append(l)
            if low.get(k[i]) == float("inf"):
                dfs.append(k[i])
                while len(dfs) > 0:
                    root = True
                    v = dfs.pop(len(dfs)-1)
                    if low.get(v) == float("inf"):
                        low.update({v: counter})
                        counter += 1
                        s.append(v)
                    key = list(self.g.nodes.get(v).neigh.keys())
                    check = self.check(key, low)
                    for j in range(len(key)):
                        if low.get(key[j]) == float("inf"):
                            s.append(key[j])
                            dfs.append(v)
                            dfs.append(key[j])
                            low.update({key[j]: counter})
                            counter += 1
                            root = False
                            break
                        if check:
                            if low.get(key[j]) < low.get(v):
                                low.update({v: low.get(key[j])})
                                root = False
                        else:
                            root = False
                    if root:
                       l = []
                       while v != s[len(s)-1]:
                           l.append(s.pop(len(s)-1))
                       l.append(s.pop(len(s)-1))
                       l.sort()
                       lst.append(l)
        return lst

    def DFS(self, v, low, s, lst):
        k = list(self.g.nodes.get(v).neigh.keys())
        root = True
        low.update({v: self.counter})
        s.append(v)
        for i in range(len(k)):
            if low.get(k[i]) == float("inf"):
                self.counter += 1
                self.DFS(k[i], low, s, lst)
            if low.get(k[i]) < low.get(v):
                low.update({v: low.get(k[i])})
                root = False
        if root:
            l = []
            while v != s[len(s)-1]:
                l.append(s.pop(len(s)-1))
            l.append(s.pop(len(s)-1))
            l.sort()
            lst.append(l)

    def range(self):
        xmax, ymax, xmin, ymin = float("-inf"), float("-inf"), float("inf"), float("inf")
        l = list(self.g.nodes.keys())
        for i in range(len(l)):
            p = self.g.nodes.get(i).pos
            if p != ():
                if i == 0:
                    xmin, ymin = p.x(), p.y()
                if p.x() > xmax:
                    xmax = p.x()
                if p.y() > ymax:
                    ymax = p.y()
                if p.x() < xmin:
                    xmin = p.x()
                if p.y() < ymin:
                    ymin = p.y()
        return xmax, ymax, xmin, ymin

    def check(self, keys, low):
        for i in range(len(keys)):
            if low.get(keys[i]) == float("inf"):
                return False
        return True
