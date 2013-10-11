title: Genetic Algorithms
author:
  name: "Alexander D Brown (adb9)"
output: genetic-algorithms.html
controls: true
layout: template/layout.mustache
style: template/ga.css

--

# Genetic Algorithms
## SEM6120 Assignment 1

--

### What is a genetic algorithm?

* [Example](http://boxcar2d.com/)
* More formally:
  * A form of evolutionary algorithm.
  * Focus on search optimisation.
  * Biologically inspired.

--

### Recap

* Solutions are represented as **chromosomes**.
* An initial population of chromosomes is produced and evaluated
* The "best" chromosomes are selected and used as parents for the next
  generation.
* New children are produced.
* Children are mutated.
* Evaluate the children
* Discard members of the population.
* Repeat until termination criteria reached.

--

### Selection

* Select the fittest members of the population.
* Many simple types:
  * Roulette Wheels
  * Rank-based
  * Tournament

--

### Crossover

* The artificial process of reproduction.
* Usually involves splicing two parent chromosomes into a new offspring
  chromosome. 
* Simplistic methods:
  * Crossover at a single point
  * Crossover at two points


--

### Crossover Point

![Crossover](./img/crossover.png "Crossover")

--

### Crossover Mask

![Crossover Mask](./img/mask-crossover.png "Crossover Mask")

--

### Mutation

* Adds variety into the new populations.
* Simple form is to flip or swap genes.
* Rate of mutation must be kept low to encourage improvement.

--

### Termination

* As with most AI approaches, overfitting may be a problem.
* GAs provide a good approximation, not an absolute solution.
