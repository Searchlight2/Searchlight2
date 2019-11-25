import os

def MPDE_any_significant_IDs(global_variables, out_path, biotype, pde_IDs):

    out_file = open(os.path.join(out_path,"data","gene_IDs","genes_significant_in_any_PDEs_IDs.txt"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]


        # tests for a valid gene:
        valid_gene = False
        present_in_any_pde = False

        if gene_dictionary["normexp_flag"]:

            if (global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes")) or global_variables["GENE_BIOTYPE_FLAG"] == False:
                valid_gene = True

                for pde_ID in pde_IDs:
                    if pde_ID not in gene_dictionary:
                        valid_gene = False
                    else:
                        pde_Dict = gene_dictionary[pde_ID]
                        if not pde_Dict["in_gl"]:
                            valid_gene = False
                        if pde_Dict["sig"]:
                            present_in_any_pde = True

        if valid_gene and present_in_any_pde:
            out_file.write(gene_ID + "\n")


