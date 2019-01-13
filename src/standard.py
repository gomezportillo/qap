
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
        algorithm on each generation. Finally returns the best of 'em all.
        """
        print("Executing Standard algorithm with file {}".format(datafile))

        super().load( datafile )

        self.current_generation = super().create_generation()
        self.calculate_fitness( self.current_generation )

        for i in range( self.NUMBER_OF_GENERATIONS ):
            print("Executing generation {}/{}...".format(i, self.NUMBER_OF_GENERATIONS), end="\r")

            new_generation = []
            for j in range( 0, int(self.GENERATION_SIZE), 2 ): # step = 2
                parent1 = super().binary_tournament()

                parent2 = None
                while parent1 != parent2:
                    parent2 = super().binary_tournament()

                child1, child2 = super().genetic_crossover(parent1, parent2)

                child1.mutate()
                child2.mutate()

                new_generation.append( child1 )
                new_generation.append( child2 )


            """
            Pops out the worst one of the current generation and inserts in
            its place the best one of the previous generation
            """
            old_best = min( self.current_generation )
            new_worst = max( new_generation )
            new_worst_index = new_generation.index( new_worst )
            new_generation.pop( new_worst_index )
            new_generation.append( old_best )
            self.current_generation = new_generation

            self.calculate_fitness( self.current_generation )

        best_one = min( self.current_generation )
        super().print_result( best_one )
        return best_one


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
