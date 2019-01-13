from copy import deepcopy

from genetic_algorithm import GeneticAlgorithm
from individual import Individual


class Baldwinian(GeneticAlgorithm):
    """
    Baldwinian implementation of the genetic algorithm
    """

    def __init__(self):
        super(Baldwinian, self).__init__()


    def execute(self, datafile):
        """
        Loads the data, creates the first generation and executes the genetic
        algorithm on each generation overloading and executing the child
        'calculate_fitness' function. Finally returns the best of 'em all.
        """
        best_one = super().execute( datafile )
        super().print_result( best_one )
        return best_one


    def calculate_fitness(self, generation):
        for individual in generation:
            optimized_individual = self.greedy_optimization( individual )
            individual.fitness = optimized_individual.fitness


    def greedy_optimization(self, individual):
        """
        Greedy 2-opt algorithm implementing the pseudocode given on the
        problem statement.
        """
        size = individual.size
        S = deepcopy( individual )
        super().calculate_individual_fitness( S )

        while True:
            best = deepcopy( S )
            for i in range(size):
                for j in range(i + 1, size):
                    T = deepcopy( S )
                    T.chromosomes[i] = S.chromosomes[j]
                    T.chromosomes[j] = S.chromosomes[i]

                    super().calculate_individual_fitness( T )

                    if T < S:
                        S = deepcopy( T )

            if S < best:
                break

        return S
