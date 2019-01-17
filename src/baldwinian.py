from genetic_algorithm import GeneticAlgorithm
from individual import Individual


class Baldwinian(GeneticAlgorithm):
    """
    Baldwinian implementation of the genetic algorithm
    """

    def __init__(self):
        super(Baldwinian, self).__init__()


    def execute(self, datafile):
        """
        Loads the data, creates the first generation and executes the genetic
        algorithm on each generation overloading and executing the child
        'calculate_fitness' function. Finally returns the best of 'em all.
        """
        best_one = super().execute( datafile )
        super().print_result( best_one )
        super().save_to_file( best_one )
        return best_one


    def calculate_fitness(self, generation):
        """
        Optimizes the individual but only changes its fitness without letting
        the optimisation, thus not allowing the optimization to be in it
        offspring. Works in the way propposed by the psicologist J. M. Baldwin.
        """
        counter=0
        for individual in generation:
            counter += 1
            print("individual {}/{}".format(counter, len(generation)))
            optimized_individual = super().greedy_optimization( individual )
            individual.fitness = optimized_individual.fitness
