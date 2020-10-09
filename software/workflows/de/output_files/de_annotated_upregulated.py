import os

from misc.get_gene_background import get_gene_background
from misc.get_gene_background_header import get_gene_background_header
from misc.get_gene_de import get_gene_de
from misc.get_gene_de_header import get_gene_de_header
from misc.get_gene_ne import get_gene_ne
from misc.get_gene_ne_header import get_gene_ne_header
from misc.get_gene_ne_stats import get_gene_ne_stats
from misc.get_gene_ne_stats_header import get_gene_ne_stats_header
from misc.get_gene_annotations import get_gene_annotations
from misc.get_gene_annotations_header import get_gene_annotations_header


def de_annotated_upregulated(global_variables, out_path, biotype, de_ID):

    out_file = open(os.path.join(out_path,"data","de_annotated_upregulated.csv"),"w")

    master_gene_table = global_variables["master_gene_table"]

    # gets the header
    header_list = ["ID"]
    header_list += get_gene_background_header(global_variables)
    header_list += get_gene_de_header(global_variables)
    header_list += get_gene_ne_header(global_variables)
    header_list += get_gene_ne_stats_header(global_variables)
    header_list += get_gene_annotations_header(global_variables)
    out_file.write("\t".join(header_list) + "\n")

    # gets the genes
    for gene_ID in master_gene_table:
        gene_dictionary = master_gene_table[gene_ID]

        # tests for a valid gene:
        valid_gene = False
        if gene_dictionary["ne_flag"] and de_ID in gene_dictionary:
            de_Dict = gene_dictionary[de_ID]
            if de_Dict["in_gl"] and de_Dict["log2fold"] > 0:
                if global_variables["GENE_BIOTYPE_FLAG"] and (gene_dictionary["BIOTYPE"] == biotype or biotype == "all_genes") :
                    valid_gene = True
                if global_variables["GENE_BIOTYPE_FLAG"] == False:
                    valid_gene = True

        if valid_gene:
            gene_out_list = [gene_ID]
            gene_out_list += get_gene_background(global_variables,gene_dictionary)
            gene_out_list += get_gene_de(global_variables,de_Dict)
            gene_out_list += get_gene_ne(global_variables,gene_dictionary)
            gene_out_list += get_gene_ne_stats(global_variables,gene_dictionary)
            gene_out_list += get_gene_annotations(global_variables,gene_dictionary)
            out_file.write("\t".join(str(x) for x in gene_out_list) + "\n")

