import random, math, time
from graph import Graph

MUTATION = 0.06
CROSSOVER = 0.2

class Chromosome:
  @classmethod
  def create(cls, graph):
    genes = [i for i in xrange(graph.num_nodes())]
    random.shuffle(genes)
    return Chromosome(genes, graph)

  def __init__(self, genes, graph):
    self.genes = genes
    self.graph = graph

  def __str__(self):
    return "{} - {}".format(self.genes, Chromosome.fitness(self))

  def __repr__(self):
    return self.__str__()

  @classmethod
  def fitness(cls, c):
    return sum([graph.distance(n1, n2) for (n1, n2) in zip(c.genes, c.genes[1:])])
      

class GA:
  def __init__(self, graph, pop_size):
    self.graph = graph
    self.pop_size = pop_size
    self.mutants_rate = int(math.ceil(pop_size * MUTATION))
    self.crossover_rate = int(math.ceil(pop_size * CROSSOVER))

  def run(self, secs):
    self.gen_pop()
    original_pop = self.population
    start_time = time.time()
    end_time = start_time + secs
    while time.time() < end_time:
      ranked = self.rank()
      best = self.select(ranked)
      offspring = self.crossover(best)
      mutants = self.mutate(best)
      self.population = best + offspring + mutants
    best = next(iter(self.rank()))
    print "Best solution is: {}".format(best)
    if best in original_pop:
      print "Best was already in original population"
    
    

  def gen_pop(self):
    self.population = [Chromosome.create(self.graph) for i in xrange(self.pop_size)]

  def rank(self):
    return sorted(self.population, key=Chromosome.fitness)

  def select(self, ranked):
    return self.population[0:self.pop_size - self.mutants_rate - self.crossover_rate]

  def crossover(self, population):
    return [self.perform_crossover(population) for i in xrange(self.crossover_rate)]

  def perform_crossover(self, population):
    point = int(random.random() * self.graph.num_nodes())
    p1 = random.choice(population)
    p2 = random.choice(population)
    return Chromosome(p1.genes[:point] + p2.genes[point:], graph)

  def mutate(self, population):
    return [population[i] for i in xrange(self.mutants_rate)]
graph = Graph(7, seed="genetic-algorithm")
random.seed()
ga = GA(graph, 100)
ga.run(10)
