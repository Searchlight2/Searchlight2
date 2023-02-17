# Parses the background file:
def background_parsing(bg_parameter, global_variables):


    # gets the sub-parameters
    sub_params_list = bg_parameter.split(",")

    for sub_param in sub_params_list:
        if sub_param.upper().startswith("file=".upper()):
            background_file_path = sub_param.split("=")[1]
            background_file = open(background_file_path).readlines()
            background_by_gene = {}
            biotypes_dict = {}

            line_counter = 1
            for line in background_file:

                line_split = line.rstrip().split("\t")

                # Processes the header line
                if line_counter == 1:
                    header_dict = {}

                    #Gets the column index for each header type
                    for index in range(0, len(line_split)):
                        header_dict[line_split[index].upper()] = index

                # Processes each gene
                else:

                    gene_background = {}

                    if global_variables["GENE_SYMBOL_FLAG"]:
                        gene_background["SYMBOL"] = line_split[header_dict["SYMBOL"]].upper()
                    if global_variables["GENE_BIOTYPE_FLAG"]:
                        gene_background["BIOTYPE"] = line_split[header_dict["BIOTYPE"]]
                    if global_variables["GENE_CHROMOSOME_FLAG"]:
                        gene_background["CHROMOSOME"] = line_split[header_dict["CHROMOSOME"]]
                    if global_variables["GENE_START_FLAG"]:
                        gene_background["START"] = line_split[header_dict["START"]]
                    if global_variables["GENE_STOP_FLAG"]:
                        gene_background["STOP"] = line_split[header_dict["STOP"]]

                    background_by_gene[line_split[0].upper()] = gene_background

                    if global_variables["GENE_BIOTYPE_FLAG"]:
                        biotypes_dict[gene_background["BIOTYPE"]] = True

                line_counter += 1


            global_variables["background_by_gene"] = background_by_gene
            global_variables["background_file_path"] = background_file_path


            if len(list(biotypes_dict.keys())) > 1:
                global_variables["biotypes_dict"] = biotypes_dict
                global_variables["biotypes_flag"] = True
            else:
                global_variables["biotypes_flag"] = False


            print("parsed the background parameter")

    return global_variables

