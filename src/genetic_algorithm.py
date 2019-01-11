"""
Parent class of the rest of the algorithms holding its variables
"""

import os

from individual import Individual


class GeneticAlgorithm:
    """
    Parent class of the rest of algorithms, holding their common functions and variables
    """

    def __init__(self):
        self.SIZE                   = 1
        self.POPULATION_SIZE        = 0
        self.NUMBER_OF_GENERATIONS  = 200
        self.TOURNAMENT_SIZE        = 4
        self.INDIVIDUAL_MUTATION_PROBABILITY = 0.5
        self.GENE_MUTATION_PROBABILITY       = 0.5

        self.flow_matrix     = []
        self.distance_matrix = []


    def create_population(self):
        population = []
        for i in self.POPULATION_SIZE:
            population.append( Individual() )

        return population


    def calculate_fitness(self, population):
        for i in population:
            i.calculate_fitness()


    def load(self, filename):
        """
        Reads a file and returns it flow and distance matrices
        """
        self.flow_matrix = []
        self.distance_matrix = []

        datafile = os.path.join('src', 'data', 'qap', filename)

        if os.path.isfile( datafile ):
            with open( datafile ) as f:
                self.SIZE = int(f.readline())

                # Avoids an empty line before the size
                f.readline()

                # Reading the flow matrix
                for line in range(self.SIZE):
                    list_str = f.readline().split()
                    list_int = list(map(int, list_str))
                    self.flow_matrix.append( list_int)

                # Avoids an empty line on the middle of the file
                f.readline()

                # Reading the distance matrix
                for line in range(self.SIZE):
                    list_str = f.readline().split()
                    list_int = list(map(int, list_str))
                    self.distance_matrix.append( list_int)


        else:
            raise Exception("{} is not a file".format( datafile ))


    def execute(self):
        pass


    def select(self):
        tournamet = []
        pass


    def crossover(self, indiv1, indiv2):
        pass


    def mutate(self, indiv):
        pass
