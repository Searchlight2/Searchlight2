

def add_annotations(global_variables, master_gene_table):

    annotation_by_gene = global_variables["annotation_by_gene"]

    for gene_ID in master_gene_table:

        gene_dictionary = master_gene_table[gene_ID]

        if gene_ID in annotation_by_gene:
            gene_dictionary["annotations"] = annotation_by_gene[gene_ID]
            gene_dictionary["annotations_flag"] = True
        else:
            gene_dictionary["annotations_flag"] = False

        master_gene_table[gene_ID] = gene_dictionary

    print("annotations added to master gene table")

    return master_gene_table

