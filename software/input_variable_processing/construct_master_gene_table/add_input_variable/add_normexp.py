
def add_normexp(global_variables, master_gene_table):


    normexp_by_gene = global_variables["normexp_by_gene"]
    sample_list = global_variables["sample_list"]

    for gene_ID in master_gene_table:

        gene_dictionary = master_gene_table[gene_ID]

        # Tests if the gene is in the normexp
        if gene_ID in normexp_by_gene:

            gene_dictionary["normexp_flag"] = True

            gene_normexp = normexp_by_gene[gene_ID]
            for sample in sample_list:
                gene_dictionary[sample] = gene_normexp[sample]

        else:
            gene_dictionary["normexp_flag"] = False

        master_gene_table[gene_ID] = gene_dictionary


    print "normexp added to master gene table"


    return master_gene_table
