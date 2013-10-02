import random

class Node:
  def __init__(self, id, graph):
    self.x = int(random.random() * graph.size)
    self.y = int(random.random() * graph.size)
    self.id = id

  def distance(self, other):
    return pow(self.x - other.x, 2) + pow(self.y - other.y, 2)

  def __str__(self):
    return "({}, {})".format(self.x, self.y)

class Graph:
  nodes = None
  def __init__(self, nodes, size, **kwargs):
    if 'seed' in kwargs:
      random.seed(kwargs['seed'])
    self.size = size
    self.nodes = [Node(i, self) for i in xrange(nodes)]

  def distance(self, n1, n2):
    return self.nodes[n1].distance(self.nodes[n2])

  def num_nodes(self):
    return len(self.nodes)

  def __str__(self):
    s = ""
    for x in xrange(0, self.size):
      for y in xrange(0, self.size):
        added = False
        for node in self.nodes:
          if node.x == x and node.y == y:
            s += str(node.id)
            added = True
        if not added:
          s += " "
      s += "\n"
    return s
