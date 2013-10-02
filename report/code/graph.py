import random

BOUND=25

class Node:
  def __init__(self, id, graph):
    self.x = int(random.random() * BOUND)
    self.y = int(random.random() * BOUND)
    self.id = id

  def distance(self, other):
    return pow(self.x - other.x, 2) + pow(self.y - other.y, 2)

  def __str__(self):
    return "({}, {})".format(self.x, self.y)

class Graph:
  nodes = None
  def __init__(self, nodes, **kwargs):
    if 'seed' in kwargs:
      random.seed(kwargs['seed'])
    self.nodes = [Node(i, self) for i in xrange(nodes)]

  def distance(self, n1, n2):
    return self.nodes[n1].distance(self.nodes[n2])

  def num_nodes(self):
    return len(self.nodes)

  def __str__(self):
    s = ""
    for x in xrange(0, BOUND):
      for y in xrange(0, BOUND):
        added = False
        for node in self.nodes:
          if node.x == x and node.y == y:
            s += str(node.id)
            added = True
        if not added:
          s += " "
      s += "\n"
    return s

if __name__ == "__main__":
  g = Graph(9)
  print str(g)
