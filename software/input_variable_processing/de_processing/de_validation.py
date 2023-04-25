import sys

from misc.is_sample_group import is_sample_group
from misc.is_number import is_number


def de_validation(de_workflow_parameters, sample_groups):

    for de_parameter in de_workflow_parameters:

        # required inputs
        de_file_path = None
        numerator = None
        denominator = None

        # gets the sub-parameters
        sub_params_list = de_parameter.split(",")

        # checks the sub params
        for sub_param in sub_params_list:

            # Tests if there are two parts to the sub-parameter
            if len(sub_param.split("=")) != 2:
                print("Error: the de parameter: " + de_parameter + " is not in the correct format.")
                sys.exit(1)

            # Tests the file sub-parameter
            if sub_param.upper().startswith("file=".upper()):
                de_file_path = sub_param.split("=")[1]

                # Tests if the de file can be opened:
                try:
                    de_file = open(de_file_path).readlines()
                except Exception as e:
                    print(e, "Error: the de file: " + de_file_path + " cannot be opened.")
                    sys.exit(1)

                # Tests if the de file is in the correct format:
                line_counter = 1
                for line in de_file:
                    line_split = line.rstrip().split("\t")

                    if len(line_split) != 4:
                        print("Error: the de file: " + de_file_path + " line " + str(line_counter) + "does not have 4 columns.")
                        sys.exit(1)

                    if line_counter == 1:
                        if line_split[0].upper() != "ID":
                            print("Error: the de file: " + de_file_path + " does not have \"ID\"  as the first column in the header.")
                            sys.exit(1)
                        if line_split[1].upper() != "LOG2FOLD":
                            print("Error: the de file: " + de_file_path + " does not have \"LOG2FOLD\"  as the second column in the header.")
                            sys.exit(1)
                        if line_split[2].upper() != "P":
                            print("Error: the de file: " + de_file_path + " does not have \"P\"  as the third column in the header.")
                            sys.exit(1)
                        if line_split[3].upper() != "P.ADJ":
                            print("Error: the de file: " + de_file_path + " does not have \"P.ADJ\"  as the fourth column in the header.")
                            sys.exit(1)

                    line_counter += 1

            # Tests the numerator sub-parameter
            if sub_param.upper().startswith("numerator=".upper()):
                numerator = sub_param.split("=")[1]
                if not is_sample_group(numerator.upper(), sample_groups):
                    print("Error: the de parameter: " + de_parameter + " \"numerator=\" group is not a valid sample group")
                    sys.exit(1)

            # Tests the numerator sub-parameter
            if sub_param.upper().startswith("denominator=".upper()):
                denominator = sub_param.split("=")[1]
                if not is_sample_group(denominator.upper(), sample_groups):
                    print("Error: the de parameter: " + de_parameter + " \"denominator=\" group is not a valid sample group")
                    sys.exit(1)

            # Tests the p.adj sub-parameter
            if sub_param.upper().startswith("p.adj=".upper()):
                padj = sub_param.split("=")[1]
                if not is_number(padj):
                    print("Error: the de parameter: " + de_parameter + " is not in the correct format.")
                    sys.exit(1)

            # Tests the log2fold sub-parameter
            if sub_param.upper().startswith("p.adj=".upper()):
                log2fold = sub_param.split("=")[1]
                if not is_number(log2fold):
                    print("Error: the de parameter: " + de_parameter + " is not in the correct format.")
                    sys.exit(1)

            # Tests the order sub-parameter
            if sub_param.upper().startswith("order=".upper()):
                order_sample_groups = sub_param.split("=")[1].split("+")

                if len(order_sample_groups) < 2:
                    print("Error: the de parameter: " + de_parameter + " does not have at least 2 sample groups in \" order=\"")
                    sys.exit(1)

                for sample_group in order_sample_groups:
                    if not is_sample_group(sample_group.upper(), sample_groups):
                        print("Error: the de parameter: " + de_parameter + " has a sample group in \"order=\" that is not in the sample sheet")
                        sys.exit(1)

            # Tests the gene list sub-parameter
            if sub_param.upper().startswith("gl=".upper()):
                gl_file_path = sub_param.split("=")[1]
                try:
                    gl_file = open(gl_file_path).readlines()
                except Exception as e:
                    print(e, "Error: the GL file: " + gl_file_path + " cannot be opened.")
                    sys.exit(1)


        # tests if the required inputs have been supplied
        if de_file_path == None or numerator == None or denominator == None:
            print("Error: the de parameter: " + de_parameter + " is not in the correct format.")
            sys.exit(1)


        print("validated the de parameter: " + de_parameter)