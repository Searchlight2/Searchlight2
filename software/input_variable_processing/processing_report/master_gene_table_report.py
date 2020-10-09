import sys

def master_gene_table_report(global_variables):


    master_gene_table = global_variables["master_gene_table"]


    # reports on the background list:
    background_count = len(master_gene_table.keys())
    if global_variables["background_flag"]:

        duplicate_symbols = 0
        for gene_ID in master_gene_table:

            gene_dictionary = master_gene_table[gene_ID]

            if global_variables["GENE_SYMBOL_FLAG"]:
                if gene_dictionary["DUPLICATE_SYMBOL_FLAG"]:
                    duplicate_symbols += 1

        print "there are " + str(len(master_gene_table.keys())) + " genes in the background file."

        if global_variables["GENE_SYMBOL_FLAG"]:
            if duplicate_symbols > 0:
                print "caution: there were " + str(duplicate_symbols) + " genes with duplicated gene symbols. Using IDs for these genes instead."

            print


    # reports on the ne
    if global_variables["ne_flag"]:

        ne_by_gene = global_variables["ne_by_gene"]

        ne_in_background_count = 0
        for gene_ID in master_gene_table:

            gene_dictionary = master_gene_table[gene_ID]
            if gene_dictionary["ne_flag"]:
                ne_in_background_count += 1

        ne_count = len(ne_by_gene.keys())

        print "there are " + str(ne_count) + " genes in the ne file"

        print str(ne_in_background_count) + " / " + str(ne_count) + " of the genes in the ne file are also in the background file."
        print "using " + str(ne_in_background_count) + " genes as the expression set."
        print str(ne_in_background_count) + " / " + str(background_count) + " of the genes in the background file are also in the ne file."

        # cautions
        if ne_count > ne_in_background_count:
            if ne_count - ne_in_background_count == 1:
                print "caution: there is " + str(ne_count - ne_in_background_count) + " gene in the ne file that is not in the background file."
            else:
                print "caution: there are " + str(ne_count - ne_in_background_count) + " genes in the ne file that are not in the background file."
        if background_count > ne_in_background_count:
            if background_count - ne_in_background_count == 1:
                print "caution: there is " + str(background_count - ne_in_background_count) + " gene in the background file that is not in the ne file."
            else:
                print "caution: there are " + str(background_count - ne_in_background_count) + " genes in the background file that are not in the ne file."

        # Tests whether there is at least one valid gene
        if ne_in_background_count == 0:
            print >> sys.stderr, "Error: none of the genes in the ne file match the background file (are you using the same IDs for both)."
            sys.exit(1)

        print



    # reports on the annotations
    if global_variables["annotations_flag"]:

        annotation_by_gene = global_variables["annotation_by_gene"]

        annotations_in_background_count = 0
        for gene_ID in master_gene_table:

            gene_dictionary = master_gene_table[gene_ID]
            if gene_dictionary["annotations_flag"]:
                annotations_in_background_count += 1

        annotations_count = len(annotation_by_gene.keys())

        print "there are " + str(annotations_count) + " genes in the annotations file"

        print str(annotations_in_background_count) + " / " + str(annotations_count) + " of the genes in the annotations file are also in the background file."
        print str(annotations_in_background_count) + " / " + str(background_count) + " of the genes in the background file are also in the annotations file."

        # cautions
        if annotations_count > annotations_in_background_count:
            if annotations_count - annotations_in_background_count == 1:
                print "caution: there is " + str(annotations_count - annotations_in_background_count) + " gene in the annotations file that is not in the background file."
            else:
                print "caution: there are " + str(annotations_count - annotations_in_background_count) + " genes in the annotations file are is not in the background file."
        if background_count > annotations_in_background_count:
            if background_count - annotations_in_background_count == 1:
                print "caution: there is " + str(background_count - annotations_in_background_count) + " gene in the background file that is not in the annotations file."
            else:
                print "caution: there are " + str(background_count - annotations_in_background_count) + " genes in the background file that are not in the annotations file."

        print


    # reports on the des
    if global_variables["de_workflows_flag"]:

        parsed_de_parameters = global_variables["de_parameters"]

        for de_parameter_dict in parsed_de_parameters:
            de_dict = de_parameter_dict["de_dict"]
            de_ID = de_parameter_dict["de_ID"]

            genes_in_de = len(de_dict.keys())
            de_in_expression_set = 0
            de_in_expression_set_with_valid_format = 0
            de_in_expression_set_with_valid_format_in_gl = 0

            for gene_ID in master_gene_table:

                gene_dictionary = master_gene_table[gene_ID]
                if de_ID in gene_dictionary:
                    if gene_dictionary["ne_flag"]:
                        de_in_expression_set += 1
                        if gene_dictionary[de_ID]["valid"]:
                            de_in_expression_set_with_valid_format += 1
                            if gene_dictionary[de_ID]["in_gl"]:
                                de_in_expression_set_with_valid_format_in_gl += 1


            print "there are " + str(genes_in_de) + " genes in the de " + de_ID
            print str(de_in_expression_set) + " / " + str(genes_in_de) + " of the genes in the de " + de_ID  + " are also in the expression set."
            print str(de_in_expression_set) + " / " + str(ne_in_background_count) + " of the genes in the expression set are also in the " + de_ID + "."
            print str(de_in_expression_set_with_valid_format) + " / " + str(de_in_expression_set) + " of the genes in the de " + de_ID  + " that are also in the expression set are in a valid differential expression format."

            if de_parameter_dict["gl_dict"] != None:
                print  str(de_in_expression_set_with_valid_format_in_gl) + " / " + str(de_in_expression_set_with_valid_format) + " of the genes in the de " + de_ID + " that are also in the expression set and are in a valid differential expression format are also in the supplied gene list."
                print "using " + str(de_in_expression_set_with_valid_format_in_gl) + " genes as the differential expression set."
                de_parameter_dict["differential_expression_set_size"] = de_in_expression_set_with_valid_format_in_gl
            else:
                print "using " + str(de_in_expression_set_with_valid_format) + " genes as the differential expression set."
                de_parameter_dict["differential_expression_set_size"] = de_in_expression_set_with_valid_format

            if genes_in_de > de_in_expression_set:
                if genes_in_de - de_in_expression_set == 1:
                    print "caution: there is " + str(genes_in_de - de_in_expression_set) + " gene in the de " + de_ID  + " that is not in the expression set."
                else:
                    print "caution: there are " + str(genes_in_de - de_in_expression_set) + " genes in the de " + de_ID  + " that are not in the expression set."

            if ne_in_background_count > de_in_expression_set:
                if ne_in_background_count - de_in_expression_set == 1:
                    print "caution: there is " + str(ne_in_background_count - de_in_expression_set) + " gene in the expression set that is not in the de " + de_ID + "."
                else:
                    print "caution: there are " + str(ne_in_background_count - de_in_expression_set) + " genes in the expression set that are not in the de " + de_ID + "."

            if de_in_expression_set > de_in_expression_set_with_valid_format:
                if de_in_expression_set - de_in_expression_set_with_valid_format == 1:
                    print "caution: there is " + str(de_in_expression_set - de_in_expression_set_with_valid_format) + " gene in the de " + de_ID + " that is in expression set that is not in a valid differential expression format."
                else:
                    print "caution: there are " + str(de_in_expression_set - de_in_expression_set_with_valid_format) + " genes in the de " + de_ID + " that are in expression set that are not in a valid differential expression format."

            print


    # stores statistics for later use
    global_variables["expression_set_size"] = ne_in_background_count







