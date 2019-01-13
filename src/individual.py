import math
import random


class Individual:

    def __init__(self, size):
        self.INDIVIDUAL_MUTATION_PROBABILITY = 0.8
        self.GENE_MUTATION_PROBABILITY       = 0.2

        self.size    = size
        self.fitness = math.inf
        self.generate_random_chromosome( size )


    def generate_random_chromosome(self, size):
        self.chromosome = list(range(size))
        random.shuffle(self.chromosome)


    def mutate(self):
        if self.INDIVIDUAL_MUTATION_PROBABILITY > random.random():
            for c in self.chromosome:
                if self.GENE_MUTATION_PROBABILITY > random.random():
                    index1, index2 = random.sample(range(0, self.size), 2)
                    self.swap( index1, index2 )


    def swap(self, index1, index2):
        val1 = self.chromosome[index1]
        val2 = self.chromosome[index2]
        self.chromosome[index1] = val2
        self.chromosome[index2] = val1


    def __str__(self):
        return str(self.chromosome)


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


    def __gt__(self, other):
        if not isinstance(other, Individual):
            return False

        return self.fitness > other.fitness
