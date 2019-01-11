import math
from random import shuffle


class Individual:

    def __init__(self, size):
        self.size    = size
        self.fitness = math.inf
        self.generate_random_chromosome( size )


    def generate_random_chromosome(self, size):
        self.chromosome = list(range(size))
        shuffle(self.chromosome)


    def mutate(self):
        pass


    def __eq__(self, other):
        if not isinstance(other, Individual):
            return False

        equal_size = self.size == other.size
        equal_chrom = set(self.chromosome) == set(other.chromosome)

        return equal_size and equal_chrom


    def __lt__(self, other):
        if not isinstance(other, Individual):
            return False

        return self.fitness < other.fitness
