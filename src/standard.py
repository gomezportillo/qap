
from genetic_algorithm import GeneticAlgorithm


class Standard(GeneticAlgorithm):

    def __init__(self):
        super(Standard, self).__init__()


    def execute(self, datafile):
        print("Executing standard...")
        flow_matrix, distance_matrix = super().load( datafile )

        for line in flow_matrix:
            print(line)

        for line in distance_matrix:
            print(line)

    def calculate_fitness(self):
        fitness = 0

        for i in range(self.SIZE):
            for j in range(self.SIZE):
                fitness += self.flow_matrix[i][j] * self.distance_matrix[i][j]

        return fitness
