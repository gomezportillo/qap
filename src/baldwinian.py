
from genetic_algorithm import GeneticAlgorithm


class Baldwinian(GeneticAlgorithm):

    def __init__(self):
        super(Baldwinian, self).__init__()


    def execute(self, datafile):
        print("Executing baldwinian...{}".format( self.SIZE ))
