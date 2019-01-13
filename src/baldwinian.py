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
        # print("greedy")

        result_fount = False
        # counter = 1
        while not result_fount:
            best = deepcopy( S )
            # print("pre-for ", counter)

            for i in range(size):
                # print("post-for {}/{}".format(i+1, size))

                for j in range(i + 1, size):
                    T = deepcopy( S )
                    T.chromosomes[i] = S.chromosomes[j]
                    T.chromosomes[j] = S.chromosomes[i]

                    self.calculate_fitness_after_swap( S, T, i, j )

                    if T < S:
                        S = deepcopy( T )

            if S < best:
                result_fount = True
            # counter+= 1
        return S


    def calculate_fitness_after_swap(self, S, T, i, j):
        """
        Instead of calculating again the whole fitness, it is only a matter of
        calculing the chromosomes that have been changed, decreasing the
        complexity of the function from quadratic to lineal
        Fitness(T) = Fitness(S) - Fitness(S)(ij) + Fitness(F)(ij)
        """
        fitnessSij = self.flow_matrix[i][j] * self.distance_matrix[S.chromosomes[i]][S.chromosomes[j]]
        fitnessTij = self.flow_matrix[i][j] * self.distance_matrix[T.chromosomes[i]][T.chromosomes[j]]

        new_fitness = S.fitness - fitnessSij + fitnessTij
        T.fitness = new_fitness
