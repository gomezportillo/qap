
from genetic_algorithm import GeneticAlgorithm
from individual import Individual

class Standard(GeneticAlgorithm):
    """
    Standard implementation of the genetic algorithm
    """

    def __init__(self):
        super(Standard, self).__init__()


    def execute(self, datafile):
        """
        Loads the data, creates the first generation and executes the genetic algorithm
        """
        print("Executing Standard algorithm with file {}".format(datafile))

        super().load( datafile )

        self.current_generation = super().create_generation()
        self.calculate_fitness( self.current_generation )

        for i in range( self.NUMBER_OF_GENERATIONS ):

            new_generation = []
            for j in range( int(self.GENERATION_SIZE), 2 ): # step = 2
                parent1 = super().binary_tournament()

                parent2 = None
                while parent1 != parent2:
                    parent2 = super().binary_tournament()

                child1, child2 = super().genetic_crossover(parent1, parent2)

                child1.mutate()
                child2.mutate()

                new_generation.append( child1 )
                new_generation.append( child2 )

            # save the best one of the generation?
        # return the best one among all generatoins?


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

            individual.fitness = new_fitness

            # Just ckecking that the fitness is not greater than the possible maximum
            if self.filename == 'tai256c.dat' and new_fitness < 44095032:
                print("Current fitness", new_fitness)
                raise Exception("Fitness cannot be lesser than 44095032 on file tai256c")
