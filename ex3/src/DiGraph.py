from GraphInterface import GraphInterface
import math

class Node:
    def __init__(self, key, pos=None):
        if pos == None:
            self.key = key
            self.neigh = {}
            self.weight = 0
            self.pos = ()
        else:
            self.key = key
            self.neigh = {}
            self.weight = 0
            p = pos.split(',')
            self.pos = Pos(float(p[0]), float(p[1]), float(p[2]))

    def __str__(self):
        return str(self.key)

    def set_weight(self, w):
        self.weight = w

    def set_pos(self, x, y, z):
        self.pos = Pos(x, y, z)


class Edge:
    def __init__(self, src, dst, w):
        self.src = src
        self.dst = dst
        self.weight = w

    def __str__(self):
        return "(src:" + str(self.src) + ", dst:" + str(self.dst) + ", w:" + str(self.weight) + ")"


class Pos:
    def __init__(self, x, y, z):
        self.p = (x, y, z)

    def x(self):
        return self.p[0]

    def y(self):
        return self.p[1]

    def z(self):
        return self.p[2]

    def dx(self, x):
        return x - self.x()

    def dy(self, y):
        return y - self.y()

    def dis(self, x, y):
        return math.sqrt(self.dx(x)**2 + self.dy(y)**2)

    def __str__(self):
        return str(self.x()) + "," + str(self.y()) + "," + str(self.z())

    def get_tuple(self):
        t = (self.x(), self.y(), self.z())
        return t


class DiGraph(GraphInterface):
    def __init__(self):
        self.mc = 0
        self.edges = {}
        self.nodes = {}

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        return self.mc

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        d = {}
        l = list(self.nodes.keys())
        for i in range(len(l)):
            e = self.nodes.get(l[i]).neigh.get(id1, -1)
            if e != -1:
                d.setdefault(l[i], e.weight)
        return d

    def all_out_edges_of_node(self, id1: int) -> dict:
        d = {}
        l = list(self.nodes.get(id1).neigh.keys())
        for i in range(len(l)):
            d.setdefault(l[i], self.nodes.get(id1).neigh.get(l[i]).weight)
        return d

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        if self.nodes.get(id1, -1) == -1 or self.nodes.get(id2, -1) == -1:
            return False
        e = Edge(id1, id2, weight)
        self.nodes.get(id1).neigh.setdefault(id2, e)
        self.edges.setdefault(self.edge_key(e), e)
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.nodes.get(node_id, -1) != -1:
            return False
        if pos == None:
            n = Node(node_id)
            self.nodes.setdefault(node_id, n)
        else:
            n = Node(node_id)
            n.pos = Pos(pos[0], pos[1], pos[2])
            self.nodes.setdefault(node_id, n)
        self.mc += 1
        return True


    def remove_node(self, node_id: int) -> bool:
        if self.nodes.get(node_id, -1) == -1:
            return False
        self.nodes.pop(node_id)
        l = list(self.nodes.keys())
        print(l)
        for i in range(len(l)):
            if self.nodes.get(l[i]).neigh.get(node_id) != None:
                self.nodes.get(l[i]).neigh.pop(node_id)
        l = list(self.edges.keys())
        for i in range(len(l)):
            e = self.edges.get(l[i])
            if e.src == node_id or e.dst == node_id:
                self.edges.pop(l[i])
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 == node_id2:
            return False
        if self.nodes.get(node_id1,-1) == -1 or self.nodes.get(node_id2,-1) == -1:
            return False
        e = self.nodes.get(node_id1).neigh.get(node_id2)
        if e == None:
            return False
        self.nodes.get(node_id1).neigh.pop(node_id2)
        self.edges.pop(self.edge_key(e))
        self.mc += 1
        return True

    def edge_key(self, e):
        return e.src*17.17 + e.dst*19.19 + e.weight*23.23
