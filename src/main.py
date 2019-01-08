import os
import time

from standard import Standard
from baldwinian import Baldwinian
from lamarckian import Lamarckian


DATA_DIR = os.path.join('data', 'qap')

standard = Standard()
baldwinian = Baldwinian()
lamarckian = Lamarckian()


def execute_algorithm( algorithm ):
    print ("[MAIN] Executing standard")
    start_time = time.time()
    algorithm.execute()
    return time.time() - start_time


if __name__ == '__main__':

    elapsed_time = execute_algorithm( standard )
    print("Standard executing time: {:.3f}s\n".format(elapsed_time))

    elapsed_time = execute_algorithm( baldwinian )
    print("Baldwinian executing time: {:.3f}s\n".format(elapsed_time))

    elapsed_time = execute_algorithm( lamarckian )
    print("Lamarckian executing time: {:.3f}s\n".format(elapsed_time))
