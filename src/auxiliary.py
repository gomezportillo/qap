"""
The aim of this file is to hold the auxiliary functions of the main file to clean it up.
"""

import os
import time

from genetic_algorithm import GeneticAlgorithm


DATA_DIR = os.path.join('src', 'data', 'qap')


def get_data_files( dir ):
    """
    Reference https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    """
    def exists(file):
        return os.path.isfile(os.path.join(dir, file))

    return [file for file in os.listdir(dir) if exists(file)]


def execute_algorithm( algorithm, datafile ):
    """
    Executes an algorithm and returns its computing time
    """
    if issubclass(type(algorithm), GeneticAlgorithm):
        start_time = time.time()
        algorithm.execute( datafile )
        return time.time() - start_time

    else:
        raise Exception('The algorithm is not a subclass of GeneticAlgorithm')
