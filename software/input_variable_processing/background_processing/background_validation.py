import sys

from misc.is_number import is_number


# Validates the background file:
def background_validation(bg_parameter, global_variables):


    # required inputs
    background_file_path = None

    # gets the sub-parameters
    sub_params_list = bg_parameter.split(",")

    # checks the sub params
    for sub_param in sub_params_list:

        # Tests if there are two parts to the sub-parameter
        if len(sub_param.split("=")) != 2:
            print("Error: the background parameter is not in a valid format.")
            sys.exit(1)

        # Tests the file sub-parameter
        if sub_param.upper().startswith("file=".upper()):
            background_file_path = sub_param.split("=")[1]

            # Tests if the background file can be opened:
            try:
                background_file = open(background_file_path).readlines()
            except Exception as e:
                print(e, "Error: the background file: \"" + str(background_file_path) + "\" cannot be opened.")
                sys.exit(1)

            line_counter = 1
            gene_IDs_dict = {}
            for line in background_file:

                line_split = line.rstrip().split("\t")

                # Validates the header line
                if line_counter == 1:
                    accepted_col_headers = {"ID":True, "SYMBOL":True, "BIOTYPE":True, "CHROMOSOME":True, "START":True, "STOP":True}
                    header_dict = {}

                    for index in range(0,len(line_split)):

                        header_dict[line_split[index].upper()] = index

                        if line_split[index].upper() not in accepted_col_headers:
                            print("Error: the background file column header: " + line_split[index].upper() + " is not an accepted column header, e.g. " + "\t\t".join(accepted_col_headers.keys()))
                            sys.exit(1)

                    if "ID" not in header_dict:
                        print("Error: there must be a column called \"ID\" in the background file.")
                        sys.exit(1)


                    #Sets up the types of background information in the global variables
                    if "SYMBOL" in header_dict:
                        global_variables["GENE_SYMBOL_FLAG"] = True
                    if "BIOTYPE" in header_dict:
                        global_variables["GENE_BIOTYPE_FLAG"] = True
                    if "CHROMOSOME" in header_dict:
                        global_variables["GENE_CHROMOSOME_FLAG"] = True
                    if "START" in header_dict:
                        global_variables["GENE_START_FLAG"] = True
                    if "STOP" in header_dict:
                        global_variables["GENE_STOP_FLAG"] = True
                    if global_variables["GENE_CHROMOSOME_FLAG"] and global_variables["GENE_START_FLAG"] and global_variables["GENE_STOP_FLAG"]:
                        global_variables["GENE_COORDINATES_FLAG"] = True


                # Validates the genes
                else:
                    if line_split[header_dict["ID"]] in gene_IDs_dict:
                        print("Error: line " + str(line_counter) + " of the background file has a duplicate gene ID. Gene IDs MUST be unique.")
                        sys.exit(1)

                    gene_IDs_dict[line_split[header_dict["ID"]]] =True

                    if len(line_split) != len(header_dict):
                        print("Error: line " + str(line_counter) + " of the background file has more columns than the header line.")
                        sys.exit(1)

                    if global_variables["GENE_START_FLAG"]:
                        if not is_number(line_split[header_dict["START"]]):
                            print("Error: line " + str(line_counter) + " of the background file has a start coordinate that is not a number.")
                            sys.exit(1)

                    if global_variables["GENE_STOP_FLAG"]:
                        if not is_number(line_split[header_dict["STOP"]]):
                            print("Error: line " + str(line_counter) + " of the background file has a stop coordinate that is not a number.")
                            sys.exit(1)


                line_counter += 1


    # tests if the required inputs have been supplied
    if background_file_path == None:
        print("Error: the background parameter is not in a valid format. No file-path.")
        sys.exit(1)


    print("validated the background parameter")

    return global_variables



