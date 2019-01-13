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
        counter=0
        for individual in generation:
            counter += 1
            print("individual ", counter)
            optimized_individual = self.greedy_optimization( individual )
            individual.fitness = optimized_individual.fitness


    def greedy_optimization(self, individual):
        """
        Greedy 2-opt algorithm implementing the pseudocode given on the
        problem statement.
        The do/while loop has been ommited from the algorithm as it is virtually
        impossible that after all the permutations S == best, and even though if
        that was the case it would not change for executing for loops again.
        """
        S = deepcopy( individual )
        super().calculate_individual_fitness( S )

        best = deepcopy( S )

        for i in range( S.size ):
            for j in range(i + 1, S.size):
                T = deepcopy( S )
                T.chromosomes[i] = S.chromosomes[j]
                T.chromosomes[j] = S.chromosomes[i]

                # super().calculate_individual_fitness( T )
                self.calculate_fitness_after_swap( T, i, j )

                if T < S:
                    S = deepcopy( T )

        return S


    def calculate_fitness_after_swap(self, T, i, j):
        """
        Instead of calculating again the whole fitness, it is only a matter of
        calculing the chromosomes that have been changed.
        Complexity reduced from n^2 to 2n
        """
        new_fitness = T.fitness

        # recalculate i
        chrom_new_i = T.chromosomes[i]
        chrom_old_i = T.chromosomes[j]
        for aux_j in range(self.problem_size):
            chrom_j = T.chromosomes[aux_j]

            new_fitness -= self.flow_matrix[j][i] * \
                           self.distance_matrix[chrom_old_i][chrom_j]

            new_fitness += self.flow_matrix[i][j] * \
                           self.distance_matrix[chrom_new_i][chrom_j]

        # recalculate j
        chrom_new_j = T.chromosomes[j]
        chrom_old_j = T.chromosomes[i]
        for aux_i in range(self.problem_size):
            chrom_i = T.chromosomes[aux_i]

            new_fitness -= self.flow_matrix[j][i] * \
                           self.distance_matrix[chrom_i][chrom_old_j]

            new_fitness += self.flow_matrix[i][j] * \
                           self.distance_matrix[chrom_i][chrom_new_j]

        T.fitness = new_fitness
