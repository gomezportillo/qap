
from genetic_algorithm import GeneticAlgorithm


class Lamarckian(GeneticAlgorithm):

    def __init__(self):
        super(Lamarckian, self).__init__()


    def execute(self, datafile):
        print("Executing lamarckian...{}".format( self.SIZE ))
