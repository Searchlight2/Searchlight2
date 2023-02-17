import sys

from misc.is_sample import is_sample
from misc.is_number import is_number


# Validates the ne parameter:
def ne_validation(norm_exp_parameter,sample_list):

    # required inputs
    norm_exp_file_path = None

    # gets the sub-parameters
    sub_params_list = norm_exp_parameter.split(",")

    # checks the sub params
    for sub_param in sub_params_list:

        # Tests if there are two parts to the sub-parameter
        if len(sub_param.split("=")) != 2:
            print("Error: the ne parameter is not in a valid format.", file=sys.stderr)
            sys.exit(1)

        # Tests if the expression threshold is in the correct format
        if sub_param.upper().startswith("expressed=".upper()):
            if not is_number(sub_param.split("=")[1]):
                print("Error: the ne parameter is not in a valid format.", file=sys.stderr)
                sys.exit(1)

        # Tests the file sub-parameter
        if sub_param.upper().startswith("file=".upper()):
            norm_exp_file_path = sub_param.split("=")[1]

            # Tests if the ne file can be opened
            try:
                norm_exp_file = open(norm_exp_file_path).readlines()
            except:
                print("Error: the ne file: \"" + str(norm_exp_file_path) + "\" cannot be opened.", file=sys.stderr)
                sys.exit(1)

            # checks the ne file contents
            line_counter = 1
            for line in norm_exp_file:

                line_split = line.rstrip().split("\t")

                # Validates the header line (samples etc)
                if line_counter == 1:

                    if line_split[0].upper() != "ID":
                        print("Error: the first column in ne file is not called \"ID\".", file=sys.stderr)
                        sys.exit(1)


                    samples = line_split[1:]

                    # Checks the diffexp and ss have the same number of samples:
                    if len(samples) > len(sample_list):
                        print("Error: there are more samples in the ne file than in the sample sheet.", file=sys.stderr)
                        sys.exit(1)
                    if len(samples) < len(sample_list):
                        print("Error: there are fewer samples in the ne file than in the sample sheet.", file=sys.stderr)
                        sys.exit(1)

                    # Checks the samples in the ne are also in the ss
                    for sample in samples:
                        if not is_sample(sample.upper(), sample_list):
                            print("Error: in the ne file the sample " + sample.upper() + " is not in the sample sheet.", file=sys.stderr)
                            sys.exit(1)

                else:
                    cells = line_split[1:]

                    for cell in cells:
                        if not is_number(cell):
                            print("Error: the ne file has a cell that is not a number at line " + str(line_counter) + ".", file=sys.stderr)
                            sys.exit(1)

                line_counter += 1


    # tests if the required inputs have been supplied
    if norm_exp_file_path == None:
        print("Error: the ne parameter is not in a valid format.", file=sys.stderr)
        sys.exit(1)


    print("validated the ne parameter")



