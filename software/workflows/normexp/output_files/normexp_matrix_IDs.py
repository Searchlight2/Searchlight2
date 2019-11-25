import os
from misc.get_gene_normexp import get_gene_normexp
from misc.get_gene_normexp_header import get_gene_normexp_header


def normexp_matrix_IDs(global_variables, out_path, biotype):

    out_file = open(os.path.join(out_path,"data","normexp_matrix_IDs.csv"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the header
    header_list = ["ID"]
    header_list += get_gene_normexp_header(global_variables)
    out_file.write("\t".join(header_list) + "\n")

    # gets the gene expression
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        # tests for a valid gene:
        valid_gene = False
        if gene_dictionary["normexp_flag"]:
            if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes") :
                valid_gene = True
            if global_variables["GENE_BIOTYPE_FLAG"] == False:
                valid_gene = True

        if valid_gene:
            gene_out_list = [gene_ID]
            gene_out_list += get_gene_normexp(global_variables,gene_dictionary)
            out_file.write("\t".join(str(x) for x in gene_out_list) + "\n")


