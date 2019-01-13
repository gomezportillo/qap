"""
Parent class of the rest of the algorithms holding its variables
"""

import os
import random

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
        self.NUMBER_OF_GENERATIONS = 1000

        """
        Changing variables
        """
        self.problem_size    = -1
        self.flow_matrix     = []
        self.distance_matrix = []


    def load(self, filename):
        """
        Parses a file and stores its flow and distance matrices as class variables
        that can be accessed by the class inheriting from it
        """
        self.flow_matrix = []
        self.distance_matrix = []

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
            raise Exception("{} is not a file".format( datafile ))


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
        children, which overload the default 'calculate_fitness' function.
        """
        print("Executing Standard algorithm with file {}".format(datafile))

        self.load( datafile )

        self.current_generation = self.create_generation()
        self.calculate_fitness( self.current_generation )

        for i in range( self.NUMBER_OF_GENERATIONS ):
            print("Executing generation {}/{}...".format(i, self.NUMBER_OF_GENERATIONS), end="\r")

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

        best_one = min( self.current_generation )
        self.print_result( best_one )
        return best_one


    def print_result(self, best_one):
        """
        Prints the final result
        """
        print("________________________________________________")
        print("Recombination operator: Crossover")
        print("Mutation operator: Index swap")
        print("Problem size: ", self.problem_size)
        print("Number of generations: ", self.NUMBER_OF_GENERATIONS)
        print("Generation size: ", self.GENERATION_SIZE)
        print("Fitness of the final best individual: ", best_one.fitness)
        print("Chromosomes:\n", best_one.chromosomes )


    def calculate_fitness(self, generation):
        raise NotImplementedError
