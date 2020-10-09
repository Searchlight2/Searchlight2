import os

def ne_gene_symbols(global_variables, out_path, biotype):

    out_file = open(os.path.join(out_path,"data","gene_symbols","gene_symbols.txt"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        # tests for a valid gene:
        valid_gene = False
        if gene_dictionary["ne_flag"]:
            if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes") :
                valid_gene = True
            if global_variables["GENE_BIOTYPE_FLAG"] == False:
                valid_gene = True

        if valid_gene:
            out_file.write(gene_dictionary["SYMBOL"] + "\n")


