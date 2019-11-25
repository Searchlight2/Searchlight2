import os

def gene_IDs_upregulated(global_variables, out_path, biotype, pde_ID):

    out_file = open(os.path.join(out_path,"data","gene_IDs","gene_IDs_upregulated.txt"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        # tests for a valid gene:
        valid_gene = False
        if gene_dictionary["normexp_flag"] and pde_ID in gene_dictionary:
            pde_Dict = gene_dictionary[pde_ID]
            if pde_Dict["in_gl"] and pde_Dict["log2fold"] > 0:
                if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes") :
                    valid_gene = True
                if global_variables["GENE_BIOTYPE_FLAG"] == False:
                    valid_gene = True

        if valid_gene:
            out_file.write(gene_ID + "\n")
