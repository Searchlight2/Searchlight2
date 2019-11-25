import os
import sys
from misc.new_directory import new_directory


def out_validation(out_path_parameter, global_variables):

    # required inputs
    out_path = None

    # gets the sub-parameters
    sub_params_list = out_path_parameter.split(",")

    # checks the sub params
    for sub_param in sub_params_list:

        # Tests if there are two parts to the sub-parameter
        if len(sub_param.split("=")) != 2:
            print >> sys.stderr, "Error: the out parameter is not in a valid format."
            sys.exit(1)

        # Tests the path sub-parameter
        if sub_param.upper().startswith("path=".upper()):
            out_path = sub_param.split("=")[1]

            # makes the outpath and checks if its valid:
            try:
                new_directory(out_path)
            except:
                print >> sys.stderr, "Error: the outpath is not valid. Does it look right to you?"
                sys.exit(1)

    # tests if the required inputs have been supplied
    if out_path == None:
        print >> sys.stderr, "Error: the out parameter is not in a valid format."
        sys.exit(1)


    print "validated the out parameter"

