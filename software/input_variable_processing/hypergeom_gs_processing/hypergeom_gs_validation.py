import sys

from misc.is_number import is_number


def hypergeom_gs_validation(hypergeom_gs_parameters):

    gene_set_types_dict = {}

    #iterates for each supplied genesets parameter:
    for gene_set_parameter in hypergeom_gs_parameters:

        # required inputs
        gene_set_file_path = None
        type = None

        # gets the sub-parameters
        sub_params_list = gene_set_parameter.split(",")

        # checks the sub params
        for sub_param in sub_params_list:


            # Tests if there are two parts to the sub-parameter
            if len(sub_param.split("=")) != 2:
                print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (missing =)."
                sys.exit(1)


            # Tests the file sub-parameter
            if sub_param.upper().startswith("file=".upper()):
                gene_set_file_path = sub_param.split("=")[1]

                # Tests if the gene set file can be opened:
                try:
                    gene_set_file = open(gene_set_file_path).readlines()
                except:
                    print >> sys.stderr, "Error: the genesets file: " + gene_set_file_path + " cannot be opened."
                    sys.exit(1)

                # Tests if the gene set file is in the correct format:
                line_counter = 0
                for line in gene_set_file:
                    line_split = line.rstrip().split("\t")

                    if len(line_split) < 3:
                        print >> sys.stderr, "Error: the genesets file: " + gene_set_file_path + " line " + str(line_counter) + "does not have at least 3 columns."
                        sys.exit(1)


            # Tests the type sub-parameter
            if sub_param.upper().startswith("type=".upper()):
                type = sub_param.split("=")[1].upper()

            # Tests the p.adj sub-parameter
            if sub_param.upper().startswith("p.adj=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (p.adj)."
                    sys.exit(1)

            # Tests the log2fold sub-parameter
            if sub_param.upper().startswith("log2fold=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (log2fold)."
                    sys.exit(1)

            # Tests the min sete size sub-parameter
            if sub_param.upper().startswith("min_set_size=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (min_set_size)."
                    sys.exit(1)

            # Tests the max set size sub-parameter
            if sub_param.upper().startswith("max_set_size=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (max_set_size)."
                    sys.exit(1)

            # Tests the overlap ratio sub-parameter
            if sub_param.upper().startswith("network_overlap_ratio=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (network_overlap_ratio)."
                    sys.exit(1)

            # Tests the overlap size sub-parameter
            if sub_param.upper().startswith("network_overlap_size=".upper()):
                if not is_number(sub_param.split("=")[1]):
                    print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (network_overlap_size)."
                    sys.exit(1)


        # Checks for a unique gene sets type:
        if type in gene_set_types_dict:
            print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " has does not have a unique type."
            sys.exit(1)
        else:
            gene_set_types_dict[type] = True

        # tests if the required inputs have been supplied
        if gene_set_file_path == None or type == None:
            print >> sys.stderr, "Error: the hyper_gs parameter: " + gene_set_parameter + " is not in the correct format (missing essential sub-parameters)."
            sys.exit(1)

        print "validated the hyper gs parameter: " + gene_set_parameter
