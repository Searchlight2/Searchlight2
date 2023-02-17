
def ora_parsing(ora_parameters,global_variables):


    parsed_gene_sets_parameters = []
    for gene_sets_parameter in ora_parameters:

        # default sub-parameters
        gene_sets_file_path = None
        type = None
        p_threshold = 0.05
        fold_threshold = 0.0
        min_set_size = 5.0
        max_set_size = 250.0
        network_overlap_ratio = 0.5
        network_overlap_size = 5.0


        # gets the sub-parameters
        sub_params_list = gene_sets_parameter.split(",")
        for sub_param in sub_params_list:
            if sub_param.upper().startswith("file=".upper()):
                gene_sets_file_path = sub_param.split("=")[1]
            if sub_param.upper().startswith("type=".upper()):
                type = sub_param.split("=")[1].upper()
            if sub_param.upper().startswith("p.adj=".upper()):
                p_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("log2fold=".upper()):
                fold_threshold = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("min_set_size=".upper()):
                min_set_size = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("max_set_size=".upper()):
                max_set_size = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("network_overlap_ratio=".upper()):
                network_overlap_ratio = float(sub_param.split("=")[1])
            if sub_param.upper().startswith("network_overlap_size=".upper()):
                network_overlap_size = float(sub_param.split("=")[1])


        # parses the gene sets file:
        gene_sets_dict = {}
        gene_sets_file = open(gene_sets_file_path).readlines()

        for line in gene_sets_file:
            line_split = line.rstrip().split("\t")
            gene_set_name = line_split[0]
            gene_set = line_split[2:]
            gene_sets_dict[gene_set_name] = gene_set


        # updates the information
        gene_set_parameter_dict = {}
        gene_set_parameter_dict["type"] = type
        gene_set_parameter_dict["gene_sets"] = gene_sets_dict
        gene_set_parameter_dict["p_threshold"] = p_threshold
        gene_set_parameter_dict["fold_threshold"] = fold_threshold
        gene_set_parameter_dict["min_set_size"] = min_set_size
        gene_set_parameter_dict["max_set_size"] = max_set_size
        gene_set_parameter_dict["network_overlap_ratio"] = network_overlap_ratio
        gene_set_parameter_dict["network_overlap_size"] = network_overlap_size

        parsed_gene_sets_parameters.append(gene_set_parameter_dict)
        print("parsed the hypergeom gs parameter: " + gene_sets_parameter)

    global_variables["ora_parameters"] = parsed_gene_sets_parameters


    return global_variables