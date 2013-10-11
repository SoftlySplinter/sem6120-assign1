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

### Representation

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
  * Add selection pressures<sup>[1]</sup>.

--

### Multi-Objective Genetic Algorithm (MOGA)<sup>[2]</sup>

* Normal GAs would combine the fitness function to work out the fitness.
* MOGA uses a weighted some of the fitness functions.
  * The weights are not fixed, but applied randomly at each selection.

--

### References

**[1]** Sexual Selection with Competitive/Co-Operative Operators for Genetic
Algorithms &mdash; *Jos&eacute; S&aacute;nchez-Velazco and John A. Bullinaria*

**[2]** MOGA: Multi-Objective Genetic Algorithms &mdash; *Tadahiko Murata and
Hisao Ishibuchi*.
