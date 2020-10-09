
import os

def Mde_all_significant_IDs(global_variables, out_path, biotype, de_IDs):

    out_file = open(os.path.join(out_path,"data","gene_IDs","genes_significant_in_all_des_IDs.txt"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        # tests for a valid gene:
        valid_gene = False

        if gene_dictionary["ne_flag"]:
            if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes"):
                valid_gene = True
            if global_variables["GENE_BIOTYPE_FLAG"] == False:
                valid_gene = True

            # determines if the gene is present in all des of the Mde:
            for de_ID in de_IDs:
                if de_ID not in gene_dictionary:
                    valid_gene = False
                else:
                    de_Dict = gene_dictionary[de_ID]

                    if not de_Dict["in_gl"] or not de_Dict["sig"]:
                        valid_gene = False

        if valid_gene:
            out_file.write(gene_ID + "\n")







