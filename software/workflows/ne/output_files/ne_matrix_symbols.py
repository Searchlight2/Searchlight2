import os
from misc.get_gene_ne import get_gene_ne
from misc.get_gene_ne_header import get_gene_ne_header

def ne_matrix_symbols(global_variables, out_path, biotype):


    out_file = open(os.path.join(out_path, "data", "ne_matrix_symbols.csv"), "w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the header
    header_list = ["symbol"]
    header_list += get_gene_ne_header(global_variables)
    out_file.write("\t".join(header_list) + "\n")

    # gets the gene expression
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]
        gene_symbol = gene_dictionary["SYMBOL"]

        # tests for a valid gene:
        valid_gene = False
        if gene_dictionary["ne_flag"]:
            if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes"):
                valid_gene = True
            if global_variables["GENE_BIOTYPE_FLAG"] == False:
                valid_gene = True

        if valid_gene:
            gene_out_list = [gene_symbol]
            gene_out_list += get_gene_ne(global_variables, gene_dictionary)
            out_file.write("\t".join(str(x) for x in gene_out_list) + "\n")