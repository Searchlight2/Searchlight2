
def add_pde(global_variables, master_gene_table):


    parsed_pde_parameters = global_variables["pde_parameters"]

    for pde_parameter_dict in parsed_pde_parameters:

        pde_dict = pde_parameter_dict["pde_dict"]
        pde_ID = pde_parameter_dict["pde_ID"]


        for gene_ID in master_gene_table:
            gene_dictionary = master_gene_table[gene_ID]

            if gene_ID in pde_dict:

                gene_dictionary[pde_ID] = pde_dict[gene_ID]
                master_gene_table[gene_ID] = gene_dictionary

        print "pde " + pde_ID  + " added to master gene table"


    return master_gene_table
