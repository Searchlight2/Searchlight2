import os

def gene_IDs_significant_upregulated(global_variables, out_path, biotype, de_ID):

    out_file = open(os.path.join(out_path,"data","gene_IDs","gene_IDs_significant_upregulated.txt"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        # tests for a valid gene:
        valid_gene = False
        if gene_dictionary["ne_flag"] and de_ID in gene_dictionary:
            de_Dict = gene_dictionary[de_ID]
            if de_Dict["in_gl"] and de_Dict["log2fold"] > 0 and de_Dict["sig"]:
                if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes") :
                    valid_gene = True
                if global_variables["GENE_BIOTYPE_FLAG"] == False:
                    valid_gene = True

        if valid_gene:
            out_file.write(gene_ID + "\n")
