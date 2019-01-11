
from genetic_algorithm import GeneticAlgorithm


class Standard(GeneticAlgorithm):
    """
    Standard implementation of the genetic algorithm
    """

    def __init__(self):
        super(Standard, self).__init__()


    def execute(self, datafile):
        print("Executing standard...")
        super().load( datafile )

        # print("File {}\nSize {}".format(datafile, self.problem_size))
        # for line in self.flow_matrix:
        #     print(line)
        # for line in self.distance_matrix:
        #     print(line)

        generations = []
        for i in range(self.NUMBER_OF_GENERATIONS):
            generation = super().create_population()
            generation.append( generation )


    def calculate_fitness(self):
        fitness = 0

        for i in range(self.problem_size):
            for j in range(self.problem_size):
                fitness += self.flow_matrix[i][j] * self.distance_matrix[i][j]

        return fitness
