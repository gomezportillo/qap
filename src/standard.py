
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
        Loads the data, creates the first generation and executes the genetic
        algorithm on each generation executing the child 'calculate_fitness' 
        function. Finally returns the best of 'em all.
        """
        return super().execute( datafile )


    def calculate_fitness(self, generation):
        """
        Calculate the fitness of each individual on the generation
        """
        for individual in generation:
            new_fitness = 0
            for i in range(self.problem_size):
                for j in range(self.problem_size):
                    chrom_i = individual.chromosomes[i]
                    chrom_j = individual.chromosomes[j]

                    new_fitness += self.flow_matrix[i][j] * \
                                   self.distance_matrix[chrom_i][chrom_j]

            individual.fitness = new_fitness

            # Just ckecking that the fitness is not greater than the possible maximum
            if self.filename == 'tai256c.dat' and new_fitness < 44095032:
                print("Current fitness", new_fitness)
                raise Exception("Fitness cannot be lesser than 44095032 on file tai256c")
