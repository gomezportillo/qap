from auxiliary import *

from standard import Standard
from baldwinian import Baldwinian
from lamarckian import Lamarckian


DATA_DIR = os.path.join('src', 'data', 'qap')

standard = Standard()
baldwinian = Baldwinian()
lamarckian = Lamarckian()


if __name__ == '__main__':

    files = get_data_files( DATA_DIR )

    elapsed_time = execute_algorithm( standard, files[0] )
    print("Standard executing time: {:.3f}s\n".format(elapsed_time))

    # elapsed_time = execute_algorithm( baldwinian )
    # print("Baldwinian executing time: {:.3f}s\n".format(elapsed_time))
    #
    # elapsed_time = execute_algorithm( lamarckian )
    # print("Lamarckian executing time: {:.3f}s\n".format(elapsed_time))
