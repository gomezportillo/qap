"""
Parent class of the rest of the algorithms holding its variables
"""

import os

from individual import Individual
from random import shuffle


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
                # Read the problem size
                self.problem_size = int(f.readline())

                # Reading the flow matrix
                line_str = f.readline().split()
                while line_str == []:
                    line_str = f.readline().split()

                line = 0
                while line < self.problem_size and line_str != []:
                    list_int = list(map(int, line_str))
                    self.flow_matrix.append(list_int)

                    line_str = f.readline().split()
                    line += 1

                assert( len(self.flow_matrix) == self.problem_size)

                # Reading the distance matrix
                while line_str == []:
                    line_str = f.readline().split()

                line = 0
                while line < self.problem_size and line_str != []:
                    list_int = list(map(int, line_str))
                    self.distance_matrix.append(list_int)

                    line_str = f.readline().split()
                    line += 1

                assert( len(self.distance_matrix) == self.problem_size)

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
        # tournament = []
        # shuffle( self.current_generation )
        # return min(tournament)
        pass



    def select(self):
        tournament = []
        pass


    def crossover(self, indiv1, indiv2):
        pass


    def mutate(self, indiv):
        pass
