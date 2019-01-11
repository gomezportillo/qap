"""
The aim of this file is to hold the auxiliary functions of the main file to clean it up.
"""

import os
import time

from genetic_algorithm import GeneticAlgorithm
from standard import Standard

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
    Executes a genetic algorithm and returns its computing time
    """
    if issubclass(type(algorithm), GeneticAlgorithm):
        start_time = time.time()
        algorithm.execute( datafile )
        return time.time() - start_time

    else:
        raise Exception('The algorithm is not a subclass of GeneticAlgorithm')


def check_files( ):
    """
    Runs the Standar genetic algorithm with all the files and checks for
    AssertionErrors, that happens when the files are not well-structured
    Corret structure: Problem size, flow matrix and distance matrix with
    size equal to the problem size
    Current erros: 19
    """
    n_assertion_err = 0
    for file in get_data_files( DATA_DIR ):
        try:
            execute_algorithm( Standard(), file )
        except AssertionError:
            print("=========== AssertionError exception on file", file)
            n_assertion_err += 1
    print(n_assertion_err)
