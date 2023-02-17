import sys

# validates the annotations
def annotations_validation(annotations_parameter):

    # required inputs
    annotations_file_path = None

    # gets the sub-parameters
    sub_params_list = annotations_parameter.split(",")

    # checks the sub params
    for sub_param in sub_params_list:

        # Tests if there are two parts to the sub-parameter
        if len(sub_param.split("=")) != 2:
            print("Error: the annotations parameter is not in a valid format.", file=sys.stderr)
            sys.exit(1)

        # Tests the file sub-parameter
        if sub_param.upper().startswith("file=".upper()):
            annotations_file_path = sub_param.split("=")[1]

            # Tests if the annotations file can be opened:
            try:
                annotations_file = open(annotations_file_path).readlines()
            except:
                print("Error: the annotations file: \"" + str(annotations_file_path) + "\" cannot be opened.", file=sys.stderr)
                sys.exit(1)

            header_line = []

            line_counter = 1
            for line in annotations_file:

                # Validates the header line
                if line_counter == 1:

                    header_line = line.rstrip().split("\t")

                    if header_line[0].upper() != "ID":
                        print("Error: the first column in annotations file is not called \"ID\".", file=sys.stderr)
                        sys.exit(1)

                else:

                    line_split = line.rstrip().split("\t")

                    if len(line_split) != len(header_line):
                        print("Error: line " + str(line_counter) + " of the annotations file has more columns than the header line.", file=sys.stderr)
                        sys.exit(1)


                line_counter += 1


    # tests if the required inputs have been supplied
    if annotations_file_path == None:
        print("Error: the annotations parameter is not in a valid format.", file=sys.stderr)
        sys.exit(1)

    print("validated the annotations parameter")



