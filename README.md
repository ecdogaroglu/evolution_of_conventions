# The Evolution of Conventions: A Computational Adaptation

## Usage

To get started, create and activate the environment with

```console
$ conda/mamba env create
$ conda activate young_1993
```

To build the project, type

```console
$ pytask
```

See young_1993.pdf for a brief summary of the original paper together with explanations of the code implementation and the related results.

## Project Description

This project is a computational adaptation of the equilibrium selection model in Young (1993).
The paper introduces the concept of "adaptive play", which is similar to fictitous play, although
here players are allowed to make mistakes and have limited information on the history of past play. Theorem 1 of the paper shows that
under certain conditions adaptive play converges to pure strategy Nash equilibria, which are the absorbing
states of the underlying stochastic process. The paper characterizes two distinct processes as Markov chains, 
one where mistakes are allowed and another, where they are not. Theorem 2 is technically interesting in that 
it documents an equivalence relation between certain properties of these two processes, namely, stochastic stability
and minimum stochastic potential by application of graph theory. This explicit characterization, together with 
the availability of efficient algorithms makes this paper an interesting candidate for a computational adaptation.

## Modules

### task_parameters.py

This is where the parametrization takes place and stored temporarily for the global acccess throughout the project.

### game.py

This module handles the creation of the state space from the given parameters and computes best response probabilities
that are fundamental for the characterization of the stochastic processes.

### markov_chain.py

Through best response probabilities, transition matrices of the two Markov chains and their
important properties like recurrent communication classes and the stationary distribution are calculated.

### graph.py

Through utilization of best response probabilities, weights of two directed graphs are calculated. While the first graph takes states of the stochastic process as vertices, the second one takes the recurrent communication classes of the unperturbed process as vertices. The graphs allow for the utilization of the shortest path and the optimum arboresence algorithms.

### plot.py

The stationary distribution, graph of recurrent communication classes and minimum arboresences are plotted for a better visual understanding.

### young_1993.tex

Analyse the research results to be complied into a pdf file.

## References

Young, H. Peyton. "The evolution of conventions." Econometrica: Journal of the Econometric Society (1993): 57-84.

## Credits

This project was created with [cookiecutter](https://github.com/audreyr/cookiecutter)
and the
[econ-project-templates](https://github.com/OpenSourceEconomics/econ-project-templates).
