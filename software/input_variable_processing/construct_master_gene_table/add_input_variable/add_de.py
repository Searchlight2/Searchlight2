
def add_de(global_variables, master_gene_table):


    parsed_de_parameters = global_variables["de_parameters"]

    for de_parameter_dict in parsed_de_parameters:

        de_dict = de_parameter_dict["de_dict"]
        de_ID = de_parameter_dict["de_ID"]


        for gene_ID in master_gene_table:
            gene_dictionary = master_gene_table[gene_ID]

            if gene_ID in de_dict:

                gene_dictionary[de_ID] = de_dict[gene_ID]
                master_gene_table[gene_ID] = gene_dictionary

        print "de " + de_ID  + " added to master gene table"


    return master_gene_table
