"""
Parent class of the rest of the algorithms holding its variables
"""

import os
import sys
import random
from copy import deepcopy

from individual import Individual


class GeneticAlgorithm:
    """
    Parent class of the rest of algorithms, holding their common functions and variables
    """

    def __init__(self):
        """
        Fixed variables
        """
        self.GENERATION_SIZE       = 50
        self.NUMBER_OF_GENERATIONS = 250
        self.MAX_NUMBER_REPETITION_BEST_ONE = 30
        """
        Changing variables
        """
        self.problem_size    = -1
        self.flow_matrix     = []
        self.distance_matrix = []

        self.last_best_one = Individual(0)
        self.repetition_best_one = 0

    def load(self, filename):
        """
        Parses a file and stores its flow and distance matrices as class variables
        that can be accessed by the class inheriting from it
        """
        self.filename = filename
        datafile = os.path.join('src', 'data', 'qap', self.filename)

        if os.path.isfile( datafile ):
            with open( datafile, 'r' ) as f:
                lines = f.readlines()
                lines = [line.split() for line in lines]
                lines = [list(map(int, line)) for line in lines if line != []] # avoids empty lines

                self.problem_size = int(lines[0][0])

                assert(len(lines) == self.problem_size*2+1) # checks the file has a correct structure

                self.flow_matrix = lines[1:self.problem_size+1]
                self.distance_matrix = lines[self.problem_size+1:]

        else:
            raise FileNotFoundError("Cannot find file {}".format( datafile ))


    def create_generation(self):
        """
        Creates a generation with the size of the problem initialised
        with random individuals
        """
        generation = []
        for i in range(self.GENERATION_SIZE):
            generation.append( Individual( self.problem_size ) )

        return generation


    def binary_tournament(self):
        """
        Randomly selects two different individuals from the current generation
        and returns the optimal one
        """
        rand_numb1, rand_numb2 = random.sample(range(0, self.GENERATION_SIZE), 2)

        individ1 = self.current_generation[rand_numb1]
        individ2 = self.current_generation[rand_numb2]

        return min([individ1, individ2])


    def genetic_crossover(self, parent1_chrom, parent2_chrom):
        """
        Mixes the two parent individuals into two children slicing them by a
        random index and avoiding repeating chromosomes in eahc child
        """
        slice_index = random.randint(1, self.problem_size-1)

        child1_chrom = self.croosover_chromosomes(slice_index,
                                                  parent1_chrom.chromosomes,
                                                  parent2_chrom.chromosomes)
        child2_chrom = self.croosover_chromosomes(slice_index,
                                                  parent2_chrom.chromosomes,
                                                  parent1_chrom.chromosomes)

        assert(len(child1_chrom) == len(child2_chrom) == self.problem_size)

        child1 = Individual( self.problem_size )
        child1.chromosomes = child1_chrom

        child2 = Individual( self.problem_size )
        child2.chromosomes = child2_chrom

        return child1, child2


    def croosover_chromosomes(self, slice_index, parent1, parent2):
        numbers_left = self.problem_size - slice_index
        child = parent1[:slice_index]

        index = slice_index
        while len(child) < self.problem_size:
            if parent2[index] not in child:
                child.append(parent2[index])

            index += 1
            if index >= self.problem_size:
                index = 0

        return child


    def execute(self, datafile):
        """
        Genetic algorithm's execution function. It is inherited by all its
        children, which will overload the default 'calculate_fitness' function.
        """
        print("Executing algorithm with file {}".format(datafile))

        self.load( datafile )

        self.current_generation = self.create_generation()
        self.calculate_fitness( self.current_generation )

        for i in range( self.NUMBER_OF_GENERATIONS ):
            print("Executing generation {}/{}... Best {}".format(i+1, self.NUMBER_OF_GENERATIONS, self.last_best_one.fitness), end="\r")

            new_generation = []
            for j in range( 0, int(self.GENERATION_SIZE), 2 ): # step = 2
                parent1 = self.binary_tournament()

                parent2 = None
                while parent1 != parent2:
                    parent2 = self.binary_tournament()

                child1, child2 = self.genetic_crossover(parent1, parent2)

                child1.mutate()
                child2.mutate()

                new_generation.append( child1 )
                new_generation.append( child2 )


            """
            Pops out the worst one of the current generation and inserts in
            its place the best one of the previous generation
            """
            old_best = min( self.current_generation )
            new_worst = max( new_generation )
            new_worst_index = new_generation.index( new_worst )
            new_generation.pop( new_worst_index )
            new_generation.append( old_best )
            self.current_generation = new_generation

            self.calculate_fitness( self.current_generation )

            """
            Check the best one is not stuck being repeated over generations.
            Otherwise, reinitialise the population keeping the best one
            """
            best_one = min( self.current_generation )
            self.check_best_one_from_generation( best_one )

        best_one = min( self.current_generation )
        return best_one


    def calculate_fitness(self, generation):
        """
        All the child classes inheriting from this one shall override this
        function.
        """
        raise NotImplementedError


    def calculate_individual_fitness(self, individual):
        """
        Calculates the fitness of a single individual and checks that it is not
        greater than the possible maximum.
        """
        new_fitness = 0
        for i in range(self.problem_size):
            for j in range(self.problem_size):
                chrom_i = individual.chromosomes[i]
                chrom_j = individual.chromosomes[j]

                new_fitness += self.flow_matrix[i][j] * \
                               self.distance_matrix[chrom_i][chrom_j]

        self.check_fitness( new_fitness )
        return new_fitness


    def greedy_optimization(self, individual):
        """
        Greedy 2-opt algorithm implementing the pseudocode given on the
        problem statement.
        The do/while loop has been ommited from the algorithm as it is virtually
        impossible that after all the permutations S == best, and even though if
        that was the case it would not change for executing for loops again.
        """
        S = deepcopy( individual )
        S.fitness = self.calculate_individual_fitness( S )

        best = deepcopy( S )

        for i in range( S.size ):
            for j in range(i + 1, S.size):
                T = deepcopy( S )
                T.chromosomes[i] = S.chromosomes[j]
                T.chromosomes[j] = S.chromosomes[i]

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


    def check_best_one_from_generation(self, best_one):
        """
        Check the best one is not stuck being repeated over generations.
        Otherwise, reinitialise the population keeping the best one
        """
        if best_one == self.last_best_one:
            self.repetition_best_one += 1
            if self.repetition_best_one > self.MAX_NUMBER_REPETITION_BEST_ONE:
                print("\nStuck population! Best one {}. Reinitialising...".format(best_one.fitness))
                self.reinitialise_population( best_one )
                self.repetition_best_one = 0

        else:
            self.repetition_best_one = 0

        self.last_best_one = best_one


    def reinitialise_population(self, best_one):
        """
        Generates another random generation, pops one individual at random and
        inserts the best one from the previous generation
        """
        self.current_generation = self.create_generation()
        self.calculate_fitness( self.current_generation )
        self.current_generation.pop()
        self.current_generation.append(best_one)


    def print_result(self, best_one):
        """
        Prints the final result.
        """
        print("________________________________________________")
        print("Recombination operator: Crossover")
        print("Mutation operator: Index swap")
        print("Problem size: ", self.problem_size)
        print("Number of generations: ", self.NUMBER_OF_GENERATIONS)
        print("Generation size: ", self.GENERATION_SIZE)
        print("Fitness of the final best individual: ", best_one.fitness)
        print("Chromosomes:\n", best_one.chromosomes )


    def save_to_file(self, best_one, i):
        """
        Redirects the stdout to a file and saves the results
        """
        filename = 'result-{}.txt'.format(i)
        filename = os.path.join('results', filename)
        f = open( filename, 'w')

        orig_stdout = sys.stdout
        sys.stdout = f

        self.print_result( best_one )

        sys.stdout = orig_stdout
        f.close()


    def check_fitness(self, fitness):
        """
        Check the fitness is not lesser than the possible value
        """
        if self.filename == 'tai256c.dat' and fitness < 44095032:
            raise Exception("Fitness cannot be lesser than 44095032 on file \
                             tai256c, current ", fitness)
