import os

def Mde_any_significant_symbols(global_variables, out_path, biotype, de_IDs):

    out_file = open(os.path.join(out_path,"data","gene_symbols","genes_significant_in_any_des_symbols.txt"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]


        # tests for a valid gene:
        valid_gene = False
        present_in_any_de = False

        if gene_dictionary["ne_flag"]:

            if (global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes")) or global_variables["GENE_BIOTYPE_FLAG"] == False:
                valid_gene = True

                for de_ID in de_IDs:
                    if de_ID not in gene_dictionary:
                        valid_gene = False
                    else:
                        de_Dict = gene_dictionary[de_ID]
                        if not de_Dict["in_gl"]:
                            valid_gene = False
                        if de_Dict["sig"]:
                            present_in_any_de = True

        if valid_gene and present_in_any_de:
            out_file.write(gene_dictionary["SYMBOL"] + "\n")
