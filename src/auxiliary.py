import os
import time


def get_data_files( dir ):
    """
    Reference https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    """
    def exists(file):
        return os.path.isfile(file)

    return [file for file in os.listdir(dir) if exists(os.path.join(dir, file))]


def execute_algorithm( algorithm, datafile ):
    start_time = time.time()
    algorithm.execute( datafile )
    return time.time() - start_time
