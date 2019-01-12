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
        self.GENERATION_SIZE        = 50
        self.NUMBER_OF_GENERATIONS  = 200
        self.INDIVIDUAL_MUTATION_PROBABILITY = 0.5
        self.GENE_MUTATION_PROBABILITY       = 0.5

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
        random_num = random.sample(range(0, self.GENERATION_SIZE), 2)

        individ1 = self.current_generation[random_num[0]]
        individ2 = self.current_generation[random_num[1]]

        return min([individ1, individ2])


    def genetic_crossover(self, parent1, parent2):
        slice_index = random.randint(1, self.problem_size-1)
        print(slice_index)
        child1 = parent1.chromosome[:slice_index] + parent2.chromosome[slice_index:]
        child2 = parent2.chromosome[:slice_index] + parent1.chromosome[slice_index:]


        return child1, child2
