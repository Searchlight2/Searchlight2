import os
from misc.get_gene_background import get_gene_background
from misc.get_gene_background_header import get_gene_background_header
from misc.get_gene_mpde import get_gene_mpde
from misc.get_gene_mpde_header import get_gene_mpde_header
from misc.get_gene_normexp import get_gene_normexp
from misc.get_gene_normexp_header import get_gene_normexp_header
from misc.get_gene_normexp_stats import get_gene_normexp_stats
from misc.get_gene_normexp_stats_header import get_gene_normexp_stats_header
from misc.get_gene_annotations import get_gene_annotations
from misc.get_gene_annotations_header import get_gene_annotations_header


def MPDE_any_significant_annotated(global_variables, out_path, biotype, pde_IDs):

    out_file = open(os.path.join(out_path,"data","genes_significant_in_any_PDEs_annotated.csv"),"w")

    master_gene_table = global_variables["master_gene_table"]


    # gets the header
    header_list = ["ID"]
    header_list += get_gene_background_header(global_variables)
    header_list += get_gene_mpde_header(pde_IDs)
    header_list += get_gene_normexp_header(global_variables)
    header_list += get_gene_normexp_stats_header(global_variables)
    header_list += get_gene_annotations_header(global_variables)
    out_file.write("\t".join(header_list) + "\n")


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
            gene_out_list = [gene_ID]
            gene_out_list += get_gene_background(global_variables,gene_dictionary)
            gene_out_list += get_gene_mpde(global_variables,gene_dictionary,pde_IDs)
            gene_out_list += get_gene_normexp(global_variables,gene_dictionary)
            gene_out_list += get_gene_normexp_stats(global_variables,gene_dictionary)
            gene_out_list += get_gene_annotations(global_variables,gene_dictionary)
            out_file.write("\t".join(str(x) for x in gene_out_list) + "\n")


