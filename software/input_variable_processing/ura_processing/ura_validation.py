import sys
from misc.is_number import is_number


def ura_validation(ura_parameters):


    ureg_types_dict = {}

    # iterates for each supplied ureg parameter:
    for ureg_parameter in ura_parameters:

        # required inputs
        ureg_file_path = None
        type = None

        # gets the sub-parameters
        sub_params_list = ureg_parameter.split(",")

        # checks the sub params
        for sub_param in sub_params_list:


            # Tests if there are two parts to the sub-parameter
            if len(sub_param.split("=")) != 2:
                print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (missing =).")
                sys.exit(1)


            # Tests the file sub-parameter
            if sub_param.upper().startswith("file=".upper()):
                ureg_file_path = sub_param.split("=")[1]

                # Tests if the gene set file can be opened:
                try:
                    ureg_file = open(ureg_file_path).readlines()
                except Exception as e:
                    print(e, "Error: the URA file: " + ureg_file_path + " cannot be opened.")
                    sys.exit(1)

                # Tests if the gene set file is in the correct format:
                line_counter = 0
                for line in ureg_file:
                    line_split = line.rstrip().split("\t")

                    if len(line_split) != 3:
                        print("Error: the URA file: " + ureg_file_path + " line " + str(line_counter) + "does not have exactly 3 columns.")
                        sys.exit(1)


            # Tests the type sub-parameter
            if sub_param.upper().startswith("type=".upper()):
                type = sub_param.split("=")[1].upper()

            # Tests the zscore sub-parameter
            if sub_param.upper().startswith("zscore=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (zscore).")
                    sys.exit(1)

            # Tests the p.adj sub-parameter
            if sub_param.upper().startswith("p.adj=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (p.adj).")
                    sys.exit(1)

            # Tests the log2fold sub-parameter
            if sub_param.upper().startswith("log2fold=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (log2fold).")
                    sys.exit(1)

            # Tests the min set size sub-parameter
            if sub_param.upper().startswith("min_set_size=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (min_set_size).")
                    sys.exit(1)

            # Tests the max set size sub-parameter
            if sub_param.upper().startswith("max_set_size=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (max_set_size).")
                    sys.exit(1)

            # Tests the overlap ratio sub-parameter
            if sub_param.upper().startswith("network_overlap_ratio=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (network_overlap_ratio).")
                    sys.exit(1)

            # Tests the overlap size sub-parameter
            if sub_param.upper().startswith("network_overlap_size=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (network_overlap_size).")
                    sys.exit(1)


        # Checks for a unique gene sets type:
        if type in ureg_types_dict:
            print("Error: the URA parameter: " + ureg_parameter + " has does not have a unique type.")
            sys.exit(1)
        else:
            ureg_types_dict[type] = True

        # tests if the required inputs have been supplied
        if ureg_file_path == None or type == None:
            print("Error: the URA parameter: " + ureg_parameter + " is not in the correct format (missing essential sub-parameters).")
            sys.exit(1)


        print("validated the URA parameter: " + ureg_parameter)
