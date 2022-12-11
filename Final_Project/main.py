class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def addEdge(self, start, end):
        next(x for x in self.nodes if x is start).edges += [end]

    def hasEdgeTo(self, start, end):
        return end in map(lambda x: x.node, start.edges)

    def getEdgeTo(self, start, end):
        return next(x for x in start.edges if x.node is end)


class Graph2:
    def __init__(self, nodes):
        size = len(nodes)
        self.nodes = nodes
        self.table = [[None for x in range(size)] for y in range(size)]


class Node:
    def __init__(self, name, key):
        self.name = name
        self.edges = []
        self.key = key

    def addEdge(self, edge):
        self.edges += [edge]

    def hasEdgeTo(self, node):
        return node in map(lambda x: x.node, self.edges)

    def getEdgeTo(self, node):
        return next(x for x in self.edges if x.node is node)


class WeightedEdge:
    def __init__(self, node, weight, answer):
        self.node = node
        self.weight = weight
        self.answer = answer

