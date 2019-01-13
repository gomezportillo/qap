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
        self.NUMBER_OF_GENERATIONS = 100

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
                                                  parent1_chrom.chromosome,
                                                  parent2_chrom.chromosome)
        child2_chrom = self.croosover_chromosomes(slice_index,
                                                  parent2_chrom.chromosome,
                                                  parent1_chrom.chromosome)

        assert(len(child1_chrom) == len(child2_chrom) == self.problem_size)

        child1 = Individual( self.problem_size )
        child1.chromosome = child1_chrom

        child2 = Individual( self.problem_size )
        child2.chromosome = child2_chrom

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
