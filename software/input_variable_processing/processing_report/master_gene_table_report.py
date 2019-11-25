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


    # reports on the normexp
    if global_variables["normexp_flag"]:

        normexp_by_gene = global_variables["normexp_by_gene"]

        normexp_in_background_count = 0
        for gene_ID in master_gene_table:

            gene_dictionary = master_gene_table[gene_ID]
            if gene_dictionary["normexp_flag"]:
                normexp_in_background_count += 1

        normexp_count = len(normexp_by_gene.keys())

        print "there are " + str(normexp_count) + " genes in the normexp file"

        print str(normexp_in_background_count) + " / " + str(normexp_count) + " of the genes in the normexp file are also in the background file."
        print "using " + str(normexp_in_background_count) + " genes as the expression set."
        print str(normexp_in_background_count) + " / " + str(background_count) + " of the genes in the background file are also in the normexp file."

        # cautions
        if normexp_count > normexp_in_background_count:
            if normexp_count - normexp_in_background_count == 1:
                print "caution: there is " + str(normexp_count - normexp_in_background_count) + " gene in the normexp file that is not in the background file."
            else:
                print "caution: there are " + str(normexp_count - normexp_in_background_count) + " genes in the normexp file that are not in the background file."
        if background_count > normexp_in_background_count:
            if background_count - normexp_in_background_count == 1:
                print "caution: there is " + str(background_count - normexp_in_background_count) + " gene in the background file that is not in the normexp file."
            else:
                print "caution: there are " + str(background_count - normexp_in_background_count) + " genes in the background file that are not in the normexp file."

        # Tests whether there is at least one valid gene
        if normexp_in_background_count == 0:
            print >> sys.stderr, "Error: none of the genes in the normexp file match the background file (are you using the same IDs for both)."
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


    # reports on the PDEs
    if global_variables["pde_workflows_flag"]:

        parsed_pde_parameters = global_variables["pde_parameters"]

        for pde_parameter_dict in parsed_pde_parameters:
            pde_dict = pde_parameter_dict["pde_dict"]
            pde_ID = pde_parameter_dict["pde_ID"]

            genes_in_pde = len(pde_dict.keys())
            pde_in_expression_set = 0
            pde_in_expression_set_with_valid_format = 0
            pde_in_expression_set_with_valid_format_in_gl = 0

            for gene_ID in master_gene_table:

                gene_dictionary = master_gene_table[gene_ID]
                if pde_ID in gene_dictionary:
                    if gene_dictionary["normexp_flag"]:
                        pde_in_expression_set += 1
                        if gene_dictionary[pde_ID]["valid"]:
                            pde_in_expression_set_with_valid_format += 1
                            if gene_dictionary[pde_ID]["in_gl"]:
                                pde_in_expression_set_with_valid_format_in_gl += 1


            print "there are " + str(genes_in_pde) + " genes in the pde " + pde_ID
            print str(pde_in_expression_set) + " / " + str(genes_in_pde) + " of the genes in the pde " + pde_ID  + " are also in the expression set."
            print str(pde_in_expression_set) + " / " + str(normexp_in_background_count) + " of the genes in the expression set are also in the " + pde_ID + "."
            print str(pde_in_expression_set_with_valid_format) + " / " + str(pde_in_expression_set) + " of the genes in the pde " + pde_ID  + " that are also in the expression set are in a valid differential expression format."

            if pde_parameter_dict["gl_dict"] != None:
                print  str(pde_in_expression_set_with_valid_format_in_gl) + " / " + str(pde_in_expression_set_with_valid_format) + " of the genes in the pde " + pde_ID + " that are also in the expression set and are in a valid differential expression format are also in the supplied gene list."
                print "using " + str(pde_in_expression_set_with_valid_format_in_gl) + " genes as the differential expression set."
                pde_parameter_dict["differential_expression_set_size"] = pde_in_expression_set_with_valid_format_in_gl
            else:
                print "using " + str(pde_in_expression_set_with_valid_format) + " genes as the differential expression set."
                pde_parameter_dict["differential_expression_set_size"] = pde_in_expression_set_with_valid_format

            if genes_in_pde > pde_in_expression_set:
                if genes_in_pde - pde_in_expression_set == 1:
                    print "caution: there is " + str(genes_in_pde - pde_in_expression_set) + " gene in the pde " + pde_ID  + " that is not in the expression set."
                else:
                    print "caution: there are " + str(genes_in_pde - pde_in_expression_set) + " genes in the pde " + pde_ID  + " that are not in the expression set."

            if normexp_in_background_count > pde_in_expression_set:
                if normexp_in_background_count - pde_in_expression_set == 1:
                    print "caution: there is " + str(normexp_in_background_count - pde_in_expression_set) + " gene in the expression set that is not in the pde " + pde_ID + "."
                else:
                    print "caution: there are " + str(normexp_in_background_count - pde_in_expression_set) + " genes in the expression set that are not in the pde " + pde_ID + "."

            if pde_in_expression_set > pde_in_expression_set_with_valid_format:
                if pde_in_expression_set - pde_in_expression_set_with_valid_format == 1:
                    print "caution: there is " + str(pde_in_expression_set - pde_in_expression_set_with_valid_format) + " gene in the PDE " + pde_ID + " that is in expression set that is not in a valid differential expression format."
                else:
                    print "caution: there are " + str(pde_in_expression_set - pde_in_expression_set_with_valid_format) + " genes in the PDE " + pde_ID + " that are in expression set that are not in a valid differential expression format."

            print


    # stores statistics for later use
    global_variables["expression_set_size"] = normexp_in_background_count







