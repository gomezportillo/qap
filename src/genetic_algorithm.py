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
        self.TOURNAMENT_SIZE        = 2 # binary tournament
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
            with open( datafile ) as f:
                self.problem_size = int(f.readline())

                # Avoids an empty line before the size
                f.readline()

                # Reading the flow matrix
                for line in range(self.problem_size):
                    if line != '':
                        list_str = f.readline().split()
                        list_int = list(map(int, list_str))
                        self.flow_matrix.append( list_int)

                # Reading the distance matrix
                for line in range(self.problem_size):
                    if line != '':
                        list_str = f.readline().split()
                        list_int = list(map(int, list_str))
                        self.distance_matrix.append( list_int )

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


    def tournament(self):
        tournament = []
        shuffle( self.current_generation )

        for i in range( self.TOURNAMENT_SIZE )
            tournament.append( self.current_generation[i] )

        return min(tournament)


    def select(self):
        tournament = []
        pass


    def crossover(self, indiv1, indiv2):
        pass


    def mutate(self, indiv):
        pass
