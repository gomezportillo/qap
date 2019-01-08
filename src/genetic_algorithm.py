"""
Parent class of the rest of the algorithms holding its variables
"""

from individual import Individual



class GeneticAlgorithm:

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


    def load(datafile):

        if os.path.isfile( datafile ):
            with open( datafile ) as f:
                SIZE  = f.readline()

                f.readline()

                print("Reading the flow matrix")
                for line in range(self.SIZE):
                    print(f.readline())

                f.readline()

                print("Reading the distance matrix")
                for line in range(self.SIZE):
                    print(f.readline())

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
