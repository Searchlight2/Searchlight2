import os
import sys
from subprocess import call

def r_script_validation(r_script_path_parameter, global_variables):

    # required inputs
    r_script_path = None

    # gets the sub-parameters
    sub_params_list = r_script_path_parameter.split(",")

    # checks the sub params
    for sub_param in sub_params_list:

        # Tests if there are two parts to the sub-parameter
        if len(sub_param.split("=")) != 2:
            print("Error: the r script parameter is not in a valid format.")
            sys.exit(1)

        # Tests the path sub-parameter
        if sub_param.upper().startswith("path=".upper()):
            r_script_path = sub_param.split("=")[1]

            # checks the script can be run:
            try:
                r_code = os.path.join(global_variables["SL_path"],"input_variable_processing","r_script_processing","test_script.r")
                with open(os.devnull, "w") as f:
                    call([r_script_path, r_code], stderr=f, stdout=f)
            except Exception as e:
                print(e, "Error: the R-script path is not valid. Does it look right to you?")
                sys.exit(1)

    # tests if the required inputs have been supplied
    if r_script_path == None:
        print("Error: the r script parameter is not in a valid format.")
        sys.exit(1)


    print("validated the r script parameter")

