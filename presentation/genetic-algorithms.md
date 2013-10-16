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

### Terminology

* **Genes** represent changeable parts of the problem
* **Chromosomes** are a solution, encoded through a data structure of genes.
* **Alleles** are the different variants a gene has.
* **Genotype** is the encoded chromosome.
* **Phenotype** is the real-world value of a chromosome.

--

### Crossover for Ordered Chromosomes

Some problems have genes which cannot be repeated within the chromosome.

"Normal" crossover will produce invalid solutions, so we needs some other
strategies.

--

### Cycle Crossover

![Cycle Crossover](./img/cycle-crossover.png "Cycle Crossover")

--

### Sexual Crossover

* To future imitate real world genetics, some crossover schemes add genders 
  into the chromosomes. 
  * Just a limit on which chromosomes can crossover.
  * Add selection pressures<sup>[[1](#21)]</sup>.

--

### Multi-Objective Genetic Algorithm (MOGA)<sup>[[2](#31)]</sup>

* Normal GAs would combine the fitness function to work out the fitness.
* MOGA uses a weighted some of the fitness functions.
  * The weights are not fixed, but applied randomly at each selection.

--

### References

**[1]** Sexual Selection with Competitive/Co-Operative Operators for Genetic
Algorithms &mdash; *Jos&eacute; S&aacute;nchez-Velazco and John A. Bullinaria*

**[2]** MOGA: Multi-Objective Genetic Algorithms &mdash; *Tadahiko Murata and
Hisao Ishibuchi*.

--
<!-- 8 -->
--
<!-- 9 -->
--
<!-- 10 -->
--

### Cycle Crossover - Detail

* Randomly choose point a `i` within the chromosomes.
* Do:
  * Replace the allele from point `i` in `P1` with the allele from point `i` in
    `P2`.
  * `i` is set to be the index of the current removed allele in `P2`
* While the current removed allele isn't the first removed one.

--

### Cycle Crossover - Detail

* This keeps parts of the tour the same.
* Not as good as preserving parts of the tour as other algorithms
  * Compare Order 1 crossover.

--
<!-- 13 -->
--
<!-- 14 -->
--
<!-- 15 -->
--
<!-- 16 -->
--
<!-- 17 -->
--
<!-- 18 -->
--
<!-- 19 -->
--
<!-- 20 -->
--

### Sexual Crossover and Selection

* Generally sexual crossover is just a limiting factor on crossover.
* Recently, sexual characteristics have been used to enhance selection.

--

### Co-operative Selection

* Males are selected with a normal selection scheme.
* Females are selected based on:
  * Their co-operative fitness with their partner.
  * Their age.
  * The improvement in fitness between their child and its father.

--

### Co-operative Selection

* Shown to have improvements, based on the TSP.
* Parallelisable (assuming the selection scheme used to select males is).

--
<!-- 24 -->
--
<!-- 25 -->
--
<!-- 26 -->
--
<!-- 27 -->
--
<!-- 28 -->
--
<!-- 29 -->
--
<!-- 30 -->
--

### Multi-Objective Genetic Algorithms

* Trying to optimise two or more functions.
* Can't always just weight the functions;
  * Unknown precedence

--

### Multi-Objective Genetic Algorithms

* Randomly weight the fitness functions to get provide more all-encompassing
  results.
