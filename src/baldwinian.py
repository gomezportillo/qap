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
        """
        Optimizes the individual but only changes its fitness without letting
        the optimisation, thus not allowing the optimization to be in it
        offspring. Works in the way propposed by the psicologist J. M. Baldwin.
        """
        counter=0
        for individual in generation:
            counter += 1
            print("individual {}/{}".format(counter, len(generation)))
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
                self.calculate_fitness_after_swap( S, T, i, j )

                if T < S:
                    S = deepcopy( T )

        return S


    def calculate_fitness_after_swap(self, S, T, i, j):
        """
        Instead of calculating again the whole fitness, it is only a matter of
        calculing the chromosomes that have been changed, reducing complexity
        from n^2 to 2n
        """
        new_fitness = T.fitness
        chrom_S_i = S.chromosomes[i]
        chrom_S_j = S.chromosomes[j]
        chrom_T_i = T.chromosomes[i]
        chrom_T_j = T.chromosomes[j]

        for k in range(self.problem_size):
            chrom_S_k = S.chromosomes[k]
            chrom_T_k = T.chromosomes[k]

            # recalculate i
            new_fitness -= self.flow_matrix[i][k] * \
                           self.distance_matrix[chrom_S_i][chrom_S_k]

            new_fitness -= self.flow_matrix[i][k] * \
                           self.distance_matrix[chrom_T_i][chrom_T_k]

            # recalculate j
            new_fitness -= self.flow_matrix[j][k] * \
                           self.distance_matrix[chrom_S_j][chrom_S_k]

            new_fitness += self.flow_matrix[j][k] * \
                           self.distance_matrix[chrom_T_j][chrom_T_k]

            # recalculate the rest of the values of the loop
            if k not in [i, j]:
                # recalculate i
                new_fitness -= self.flow_matrix[k][i] * \
                               self.distance_matrix[chrom_S_k][chrom_S_i]

                new_fitness += self.flow_matrix[k][i] * \
                               self.distance_matrix[chrom_T_k][chrom_T_i]

                # recalculate j
                new_fitness -= self.flow_matrix[k][j] * \
                               self.distance_matrix[chrom_S_k][chrom_S_j]

                new_fitness += self.flow_matrix[k][j] * \
                               self.distance_matrix[chrom_T_k][chrom_T_j]
