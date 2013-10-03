import random, math, time
from graph import Graph

MUTATION = 0.1
CROSSOVER = 0.3

class Chromosome:
  @classmethod
  def create(cls, graph):
    genes = [i for i in xrange(graph.num_nodes())]
    random.shuffle(genes)
    return Chromosome(genes, graph)

  def __init__(self, genes, graph):
    while not self.valid(genes):
      genes = self.make_valid(genes)
    self.genes = genes
    self.graph = graph

  def valid(self, genes):
    for i in xrange(len(genes)):
      if i not in genes:
        return False
    return True

  def make_valid(self, genes):
    missing = [i for i in xrange(len(genes)) if i not in genes]
    double = [i for i in xrange(len(genes)) if genes.count(i) > 1]

    random.shuffle(missing)
    random.shuffle(double)

    for i in double:
      genes[genes.index(i)] = missing.pop()
    return genes
    

  def __str__(self):
    return "{} - {}".format(self.genes, Chromosome.fitness(self))

  def __repr__(self):
    return self.__str__()

  @classmethod
  def fitness(cls, c):
    return sum([graph.distance(n1, n2) 
                for (n1, n2) in zip(c.genes, c.genes[1:])])
      

class BasicGA(object):
  def __init__(self, graph, pop_size):
    self.graph = graph
    self.pop_size = pop_size
    self.mutants_rate = int(math.ceil(pop_size * MUTATION))
    self.crossover_rate = int(math.ceil(pop_size * CROSSOVER))
    self.gen_pop()

  def run(self):
    """Runs the GA once."""
    best = self.select()
    offspring = self.crossover(best)
    mutants = self.mutate(best)
    cur_best = self.population[0]
    self.population = best + offspring + mutants
    return cur_best

  def gen_pop(self):
    """Generates a new population."""
    self.population = [Chromosome.create(self.graph) 
                       for i in xrange(self.pop_size)]

  def select(self):
    """Selects the best individuals from a population."""
    retained_pop = self.pop_size - self.mutants_rate - self.crossover_rate
    return sorted(self.population, key=Chromosome.fitness)[0:retained_pop]

  def crossover(self, population):
    """Performs crossover on a certain amount of the population."""
    return [self.perform_crossover(population) 
            for i in xrange(self.crossover_rate)]

  def perform_crossover(self, population):
    """
    Perform crossover by:
    - Choosing a crossover point randomly.
    - Choosing two parents.
    - Slicing the genes of both parents together at the crossover point.
    """
    point = int(random.random() * self.graph.num_nodes())
    p1 = random.choice(population)
    p2 = random.choice(population)
    return Chromosome(p1.genes[:point] + p2.genes[point:], self.graph)

  def mutate(self, population):
    """Performs mutation of a certain number of the population."""
    return [self.perform_mutation(population) 
            for i in xrange(self.mutants_rate)]

  def perform_mutation(self, population):
   """Randomly swap two genes to mutate the chromosome."""
   target = random.choice(population)
   genes = [i for i in target.genes]
   pos1 = int(random.random() * len(genes))
   pos2 = int(random.random() * len(genes))
   temp = genes[pos1]
   genes[pos1] = genes[pos2]
   genes[pos2] = temp
   return Chromosome(genes, self.graph)

class TournamentGA(BasicGA):
  def __init__(self, graph, num, tournament_size):
    super(TournamentGA, self).__init__(graph, num)
    self.tournament_size = tournament_size

  def select(self):
    """
    Selects the best members of the population using a tournament-based 
    algorithm.
    """
    retained_pop = self.pop_size - self.mutants_rate - self.crossover_rate
    temp = self.population
    best = []
    while len(best) != retained_pop:
      tournament = random.sample(temp, min(self.tournament_size, len(temp)))
      b = min(tournament, key=Chromosome.fitness)
      best.append(b)
    return best
    

if __name__ == "__main__":
  graph = Graph(15, 25, seed="ga")

  # Reset the random seed from graph creation.
  random.seed()
  gas = [BasicGA(graph, 10), TournamentGA(graph, 10, 2)]

  for ga in gas:
    avg = []
    improving = True
    runs = 0
    while improving:
      runs += 1
      best = ga.run()
      avg.append(Chromosome.fitness(best))
      if len(avg) > 1000:
        median = avg[len(avg)/2]
        improving = Chromosome.fitness(best) != median
    print "{} found best: {} in {} runs".format(ga.__class__.__name__, 
                                                str(best),
                                                runs)
 
