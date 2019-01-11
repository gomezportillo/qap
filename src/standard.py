
from genetic_algorithm import GeneticAlgorithm


class Standard(GeneticAlgorithm):
    """
    Standard implementation of the genetic algorithm
    """

    def __init__(self):
        super(Standard, self).__init__()


    def execute(self, datafile):
        """
        Executes standard genetic algorithm
        """
        print("Executing standard with file {}".format(datafile))

        super().load( datafile )
        generation = super().create_population()
        self.calculate_fitness( generation )


    def calculate_fitness(self, generation):
        """
        Calculate the fitness of each individual on the generation
        """
        for individual in generation:
            new_fitness = 0
            for i in range(self.problem_size):
                for j in range(self.problem_size):
                    chrom_i = individual.chromosome[i]
                    chrom_j = individual.chromosome[j]

                    new_fitness += self.flow_matrix[i][j] * \
                                   self.distance_matrix[chrom_i][chrom_j]


            # Just ckecking that the fitness is not greater than the possible maximum
            if self.filename == 'tai256c.dat':
                if new_fitness < 44095032:
                    print(new_fitness)
                    raise Exception("Fitness cannot be lesser than 44095032 on file tai256c")

            individual.fitness = new_fitness
