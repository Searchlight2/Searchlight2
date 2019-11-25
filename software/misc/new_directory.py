import errno
import os

#Generic method to create a new directory. Has error handling for a pre-existing directory.
def new_directory(directory):
    try:
        os.makedirs(directory)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
