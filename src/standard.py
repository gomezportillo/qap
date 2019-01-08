
from genetic_algorithm import GeneticAlgorithm


class Standard(GeneticAlgorithm):

    def __init__(self):
        super(Standard, self).__init__()


    def execute(self, datafile):
        print("Executing standard...{}".format( self.SIZE ))
