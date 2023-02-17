
def add_ne(global_variables, master_gene_table):


    ne_by_gene = global_variables["ne_by_gene"]
    sample_list = global_variables["sample_list"]

    for gene_ID in master_gene_table:

        gene_dictionary = master_gene_table[gene_ID]

        # Tests if the gene is in the ne
        if gene_ID in ne_by_gene:

            gene_dictionary["ne_flag"] = True

            gene_ne = ne_by_gene[gene_ID]
            for sample in sample_list:
                gene_dictionary[sample] = gene_ne[sample]

        else:
            gene_dictionary["ne_flag"] = False

        master_gene_table[gene_ID] = gene_dictionary


    print("ne added to master gene table")


    return master_gene_table
