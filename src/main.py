from auxiliary import *

from standard import Standard
from baldwinian import Baldwinian
from lamarckian import Lamarckian


standard   = Standard()
baldwinian = Baldwinian()
lamarckian = Lamarckian()


if __name__ == '__main__':

    # elapsed_time = execute_algorithm( standard, 'tai256c.dat' ) # bur26a
    # print("Standard executing time: {:.3f}s\n".format(elapsed_time))

    elapsed_time = execute_algorithm( baldwinian, 'tai256c.dat' )
    print("Baldwinian executing time: {:.3f}s\n".format(elapsed_time))

    # elapsed_time = execute_algorithm( lamarckian )
    # print("Lamarckian executing time: {:.3f}s\n".format(elapsed_time))
