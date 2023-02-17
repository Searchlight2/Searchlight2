import sys
import re

# Validates the sample sheet:
def ss_validation(ss_parameter):


    # required inputs
    ss_file_path = None

    # gets the sub-parameters
    sub_params_list = ss_parameter.split(",")

    # checks the sub params
    for sub_param in sub_params_list:

        # Tests if there are two parts to the sub-parameter
        if len(sub_param.split("=")) != 2:
            print("Error: the sample sheet parameter is not in a valid format.", file=sys.stderr)
            sys.exit(1)

        # Tests the file sub-parameter
        if sub_param.upper().startswith("file=".upper()):
            ss_file_path = sub_param.split("=")[1]

            # Tests if the ss file can be opened:
            try:
                ss_file = open(ss_file_path).readlines()
            except:
                print("Error: the sample sheet file: " + ss_file_path + " cannot be opened.", file=sys.stderr)
                sys.exit(1)


            samples = {}
            sample_groups_by_column = []
            header_column_count = None

            # Reads the sample sheet:
            line_counter = 1
            for line in ss_file:
                line_split = line.rstrip().split("\t")

                # Tests the header line:
                if line_counter == 1:

                    header_column_count = len(line_split)

                    # Tests that the first column is SAMPLE - forces users to be good.
                    if line_split[0].upper() != "SAMPLE":

                        print("Error: The sample sheet first column header is not \"SAMPLE\".", file=sys.stderr)
                        sys.exit(1)

                    # Sets up the sample_groups_by_column list
                    for column in line_split[1:]:
                        sample_groups_column = {}
                        sample_groups_by_column.append(sample_groups_column)


                else:

                    # Tests if the current line has the same culumn count as the header line:
                    if len(line_split) != header_column_count:
                        print("Error: line " + str(line_counter) + " in the sample sheet is not in the correct format.", file=sys.stderr)
                        sys.exit(1)

                    # Tests for a valid sample name:
                    if not line_split[0][0].upper().isalpha():
                        print("Error: The sample sheet sample: " + line_split[0].upper() + ", starts with an invalid character. Sample names may only start with a letter (i.e. a-z or A-Z).", file=sys.stderr)
                        sys.exit(1)

                    if not re.match("^[A-Za-z0-9_]*$",line_split[0].upper()):
                        print("Error: The sample sheet sample: " + line_split[0].upper() + ", contains an invalid character. Sample names may only include the characters: a-z, A-Z, 1-9, or underscore (_).", file=sys.stderr)
                        sys.exit(1)


                    # Tests for a non-unique sample name:
                    if  line_split[0].upper() in samples:
                        print("Error: the sample " + line_split[0].upper() + " appears more than once in the sample sheet.", file=sys.stderr)
                        sys.exit(1)

                    else:
                        samples[line_split[0].upper()] = True

                    for sample_group in line_split[1:]:

                        sample_group = sample_group.upper()

                        # Tests for a valid sample group name:
                        if not sample_group[0].isalpha():
                            print("Error: The sample sheet sample group: " + sample_group + ", starts with an invalid character. Sample group names may only start with a letter (i.e. a-z or A-Z).", file=sys.stderr)
                            sys.exit(1)

                        if not re.match("^[A-Za-z0-9_]*$", sample_group):
                            print("Error: The sample sheet sample group: " + sample_group + ", contains an invalid character. Sample group names may only include the characters: a-z, A-Z, 1-9, or underscore (_).", file=sys.stderr)
                            sys.exit(1)

                        # Tests for non-unique sample group name (e.g. "high" used as a group in more than one column of the ss)
                        matches = 0
                        for sample_groups_column in sample_groups_by_column:
                            if sample_group in sample_groups_column:
                                matches += 1

                        if matches > 1:
                            print("The sample group \"" + sample_group + "\" appears in more than one column in the sample sheet.", file=sys.stderr)
                            sys.exit(1)


                line_counter += 1

    # tests if the required inputs have been supplied
    if ss_file_path == None:
        print("Error: the sample sheet parameter is not in a valid format.", file=sys.stderr)
        sys.exit(1)


    print("validated the ss parameter")