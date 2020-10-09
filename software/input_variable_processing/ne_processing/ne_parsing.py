# Parses the ne parameter:
def ne_parsing(norm_exp_parameter, global_variables):

    # default sub-parameters
    norm_exp_file_path = None
    expressed_threshold = 1.0
    expression_type = "normalised read counts"

    # gets the sub-parameters
    sub_params_list = norm_exp_parameter.split(",")

    for sub_param in sub_params_list:
        if sub_param.upper().startswith("file=".upper()):
            norm_exp_file_path = sub_param.split("=")[1]
        if sub_param.upper().startswith("expressed=".upper()):
            expressed_threshold = float(sub_param.split("=")[1])
        if sub_param.upper().startswith("type=".upper()):
            expression_type = sub_param.split("=")[1]

    global_variables["ne_threshold"] = expressed_threshold
    global_variables["ne_type"] = expression_type

    sample_order = []
    ne_by_gene = {}

    norm_exp_file = open(norm_exp_file_path).readlines()

    line_counter = 1
    for line in norm_exp_file:

        line_split = line.rstrip().split("\t")

        # Gets the header info
        if line_counter == 1:
            sample_order = line_split[1:]
            sample_order = map(str.upper, sample_order)

        # Gets the expression info for each gene
        else:
            gene_ID = line_split[0].upper()
            gene_norm_exp_list = line_split[1:]
            gene_norm_exp_dict = {}

            for index in range(0,len(sample_order)):
                gene_norm_exp_dict[sample_order[index]] = float(gene_norm_exp_list[index])
            ne_by_gene[gene_ID] = gene_norm_exp_dict

        line_counter += 1

    global_variables["ne_by_gene"] = ne_by_gene
    global_variables["ne_file_path"] = norm_exp_file_path

    print "parsed the ne parameter"

    return global_variables