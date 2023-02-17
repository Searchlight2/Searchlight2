# parses the annotations file
def annotations_parsing(annotations_parameter, global_variables):


    # gets the sub-parameters
    sub_params_list = annotations_parameter.split(",")

    for sub_param in sub_params_list:
        if sub_param.upper().startswith("file=".upper()):
            annotations_file_path = sub_param.split("=")[1]
            annotations_file = open(annotations_file_path).readlines()
            annotations_headers = []
            annotations_by_gene = {}

            line_counter = 1
            for line in annotations_file:

                # gets the header line
                if line_counter == 1:
                    annotations_headers = line.rstrip().split("\t")[1:]

                else:
                    line_split = line.rstrip().split("\t")

                    gene_ID = line_split[0].upper()
                    annotations = line_split[1:]
                    annotations_by_gene[gene_ID] = annotations

                line_counter += 1


            global_variables["annotation_headers"] = annotations_headers
            global_variables["annotation_by_gene"] = annotations_by_gene

    print("parsed the annotations paremeter")

    return global_variables




