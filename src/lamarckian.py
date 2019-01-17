from genetic_algorithm import GeneticAlgorithm
from individual import Individual


class Lamarckian(GeneticAlgorithm):
    """
    Lamarckian implementation of the genetic algorithm
    """

    def __init__(self):
        super(Lamarckian, self).__init__()


    def execute(self, datafile):
        """
        Loads the data, creates the first generation and executes the genetic
        algorithm on each generation overloading and executing the child
        'calculate_fitness' function. Finally returns the best of 'em all.
        """
        best_one = super().execute( datafile )
        super().print_result( best_one )
        return best_one


    def calculate_fitness(self, generation):
        """
        Optimizes the individual and saves the changes for them to be inherited
        by its offspring so next generation have it. Works in the say proposed
        by the biologist J. B. Lamark.
        """
        counter=0
        for individual in generation:
            counter += 1
            print("individual {}/{}".format(counter, len(generation)))
            individual = super().greedy_optimization( individual )
